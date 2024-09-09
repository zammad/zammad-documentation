Firewall & SELinux
------------------

Some parts of these steps may not apply to you, feel free to skip them!

SELinux
^^^^^^^
.. note::
   The commands below only work on Ubuntu, Debian and CentOS. If you use a
   different distribution, please have a look at their documentation.

.. code-block:: sh

   $ # Allow nginx or apache to access public files of Zammad and communicate
   $ sudo chcon -Rv --type=httpd_sys_content_t /opt/zammad/public/
   $ sudo setsebool httpd_can_network_connect on -P
   $ sudo semanage fcontext -a -t httpd_sys_content_t /opt/zammad/public/
   $ sudo restorecon -Rv /opt/zammad/public/
   $ sudo chmod -R a+r /opt/zammad/public/


Firewall
^^^^^^^^

Ensure to open ports ``80`` and ``443`` (TCP & UDP) beside of the ports you
need. Below you can find a few examples for different distributions.
If you are using a different distribution, please have a look at their
documentation.

Please note that the examples below only cover the distribution's default
firewall. It may not cover your case.

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
      environment could require different / more rules.

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

   .. tab:: CentOS, RHEL, openSUSE, SLES

      .. code-block:: sh

         $ # Open Port 80 and 443 on your Firewall
         $ firewall-cmd --zone=public --add-service=http --permanent
         $ firewall-cmd --zone=public --add-service=https --permanent
         $ firewall-cmd --reload

