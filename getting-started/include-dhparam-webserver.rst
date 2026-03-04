.. hint::

   **🤓 Don't have a dhparam.pem file yet?**

   You can easily adapt below example to generate this file.
   It will improve HTTPs security and thus should be used.

   You can find the path by looking at your webserver configuration by
   looking for:

      * ``ssl_dhparam`` directive (Nginx)
      * ``SSLOpenSSLConfCmd DHParameters`` directive (Apache2)

   .. code-block:: console

      $ openssl dhparam -out <path>/dhparam.pem 4096
