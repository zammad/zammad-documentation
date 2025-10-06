.. tip::

   **Can't login because of CSRF token errors?**

   This usually affects systems with more than one proxy server only.
   For this to function you may have to tell your web server directly
   which connection type was used. Only use the options described below if you're sure. They may cause security issues.

   The following options expect HTTPS connections which should be your goal.

   Nginx
      Within your virtual host configuration, locate both directives
      ``proxy_set_header X-Forwarded-Proto`` and replace ``$scheme`` by
      ``https``.

   Apache2
      Within your virtual host configuration just above the first
      ``ProxyPass`` directive insert:

      .. code-block:: text

         RequestHeader set X_FORWARDED_PROTO 'https'
         RequestHeader set X-Forwarded-Ssl on
