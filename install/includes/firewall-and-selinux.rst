Firewall & SELinux
==================

Some parts of these steps may not apply to you, feel free to skip them!

SELinux
-------

.. tabs::

   .. tab:: Ubuntu / Debian / CentOS

      .. code-block:: sh

         $ # Allow nginx or apache to access public files of Zammad and communicate
         $ chcon -Rv --type=httpd_sys_content_t /opt/zammad/public/
         $ setsebool httpd_can_network_connect on -P
         $ semanage fcontext -a -t httpd_sys_content_t /opt/zammad/public/
         $ restorecon -Rv /opt/zammad/public/
         $ chmod -R a+r /opt/zammad/public/

   .. tab:: OpenSUSE

      See `the documentation <https://doc.opensuse.org/documentation/leap/security/html/book-security/cha-selinux.html>`_
      for more input if you wish to continue.

Firewall
--------

   .. note::

      Below only covers the distribution's default firewall.
      It may not cover your case.

.. tabs::

   .. tab:: Ubuntu

      .. code-block:: sh

         $ # Open Port 80 and 443 on your Firewall
         $ ufw allow 80
         $ ufw allow 443
         $ ufw reload

   .. tab:: Debian

      .. warning::

         We're covering ``nftables`` in this part - iptables is discouraged
         starting from Debian 10 (Buster).
         Our example uses the ``input`` chain, yours may be a different one!

      Add the following lines to ``/etc/nftables.conf`` or your specific rule
      file. Ensure to add these lines to your input-chain.

      .. code-block::

         # Open Port 80 and 443 for Zammad
         tcp dport { http, https } accept
         udp dport { http, https } accept

      The result should look like the following. Keep in mind that your
      enviroment could require different / more rules.

      .. code-block::

         #!/usr/local/sbin/nft -f
         flush ruleset

         table inet filter {
            chain input {
               type filter hook input priority 0; policy drop;
               ct state established,related accept
               tcp dport ssh log accept
               tcp dport { http, https } accept
               udp dport { http, https } accept
            }

            chain forward {
               type filter hook forward priority 0; policy accept;
            }

            chain output {
               type filter hook output priority 0; policy accept;
            }
         }

      To load your new rules, simply run ``systemctl reload nftables``.

   .. tab:: CentOS

      .. code-block:: sh

         $ # Open Port 80 and 443 on your Firewall
         $ firewall-cmd --zone=public --add-service=http --permanent
         $ firewall-cmd --zone=public --add-service=https --permanent
         $ firewall-cmd --reload

   .. tab:: OpenSUSE

      If your system does not yet know webserver rules, you can add a new one
      for your firewall by creating the file
      ``/etc/sysconfig/SuSEfirewall2.d/services/webserver`` with this content:

      .. code-block::

         ## Name: Webserver
         ## Description: Open ports for HTTP and HTTPs

         # space separated list of allowed TCP ports
         TCP="http https"
         # space separated list of allowed UDP ports
         UDP="http https"

      After that locate ``FW_CONFIGURATIONS_EXT`` within
      ``/etc/sysconfig/SuSEfirewall2`` and add the option ``webserver`` to the
      list. The list is seperated by spaces.
      You may require a different zone, above covers the external zone.

      Now ensure to restart the firewall service.

      .. code-block:: sh

         systemctl restart SuSEfirewall2

   .. tab:: other

      If we didn't cover your distribution or firewall in question, ensure to
      open ports ``80`` and ``443`` (TCP & UDP) beside of the ports you need.
