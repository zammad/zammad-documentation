Firewall & SELinux
------------------

Some parts of these steps may not apply to you, feel free to skip them!

SELinux
^^^^^^^
.. note::
   The commands below only work on Ubuntu, Debian and CentOS. If you use a
   different distribution, please have a look at their documentation.

Allow nginx or apache to access public files of Zammad and communicate:

.. code-block:: console

   $ sudo chcon -Rv --type=httpd_sys_content_t /opt/zammad/public/

.. code-block:: console

   $ sudo setsebool httpd_can_network_connect on -P

.. code-block:: console

   $ sudo semanage fcontext -a -t httpd_sys_content_t /opt/zammad/public/

.. code-block:: console

   $ sudo restorecon -Rv /opt/zammad/public/

.. code-block:: console

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

      Open Port 80 and 443 on your Firewall:

      .. code-block:: console

         $ sudo ufw allow 80

      .. code-block:: console

         $ sudo ufw allow 443

      .. code-block:: console

         $ sudo ufw reload

   .. tab:: Debian

      .. warning::

         We're covering ``nftables`` in this part - iptables is discouraged
         starting from Debian 10 (Buster).
         Our example uses the ``input`` chain, yours may be a different one!

      Add the following lines to ``/etc/nftables.conf`` or your specific rule
      file. Ensure to add these lines to your input-chain.

      Open Port 80 and 443 for Zammad:

      .. code-block::

         sudo tcp dport { http, https } accept

      .. code-block::

         sudo udp dport { http, https } accept

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

      To load your new rules, simply run ``sudo systemctl reload nftables``.

   .. tab:: CentOS, RHEL, openSUSE, SLES

      Open Port 80 and 443 on your Firewall:

      .. code-block:: console

         $ sudo firewall-cmd --zone=public --add-service=http --permanent

      .. code-block:: console

         $ sudo firewall-cmd --zone=public --add-service=https --permanent

      .. code-block:: console

         $ sudo firewall-cmd --reload



