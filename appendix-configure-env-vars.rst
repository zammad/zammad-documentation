Configure environment variables
*******************************

If you're using the DEB or RPM packages you can change Zammads environment variables by the following commands.

Configure IP
============

::

 zammad config:set ZAMMAD_BIND_IP=0.0.0.0
 systemctl restart zammad


Configure ports
===============

Please note that you also have to reconfigure Nginx when changing the ports!

::

 zammad config:set ZAMMAD_RAILS_PORT=3000
 zammad config:set ZAMMAD_WEBSOCKET_PORT=6042
 systemctl restart zammad

Application Servers
===================

Per default one application server will get started. If you have more http requests (user sessions) you need to increase the amount of your application server. The typical problem is long waiting times in the web interface for opening or editing tickets. 

::

 zammad config:set WEB_CONCURRENCY=3
 systemctl restart zammad

Configure Restart Command
=========================
If you need to make changes (creating objects) to Zammad, it can be necessary to restart the service. 
This can be done manually or automatic. For use the automatic solution you need to set an special ENV Var

Note: you might need to adjust the value for APP_RESTART_CMD if you have / need a different command to restart your Zammad on your installation.

::

 zammad config:set APP_RESTART_CMD="systemctl restart zammad"




