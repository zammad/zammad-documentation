.. tip::

   **😖 Can't login because of CSRF token errors?**

   This usually affects systems with more than one proxy server only. 
   For this to function you may have to tell your web server directly 
   which connection type was used.

   .. warning::

      **Do not** use below options if you're unsure, they may technically 
      be a security issue!

   The following options expect HTTPs connections which should be your goal.

   .. tabs::

      .. tab:: nginx

         Within your virtual host configuration, locate both directives 
         ``proxy_set_header X-Forwarded-Proto`` and replace ``$scheme`` by 
         ``https``.

      .. tab:: apache2

         Within your virtual host configuration just above the first 
         ``ProxyPass`` directive insert:

         .. code-block::

            RequestHeader set X_FORWARDED_PROTO 'https' 
            RequestHeader set X-Forwarded-Ssl on
