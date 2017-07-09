Twitter
*******

It is possible to create a quick login for your helpdesk via Twitter To do so, you need to follow these steps:

Register Twitter app
====================

.. image:: images/apps.twitter.com_start.png
   :alt: inital page
   
   Click on "Create App"
   
   
   .. image:: images/apps.twitter.com_new_app_screen.png
   :alt: new app page
   
   Enter app settings. As "Callback URL" you need to enter "https://zammad_host/api/v1/external_credentials/twitter/callback"
   
   After the app has been created, update the application icon and organization attributes.

.. image:: images/apps.twitter.com_set_permissions.png
   :alt: set permissions to receive and send direct messages

Next we need to set _read, write and access direct messages permissions_ for the app.

.. image:: images/apps.twitter.com_get_credentials.png
   :alt: click on Keys & Access Token, note them

Go to "Keys and Access Token" tab and note the "Consumer Key" and "Consumer Secret".

Configure Zammad as Twitter app
===============================

Go to "Admin -> Security -> Twitter -> Third Party Applications -> Twitter Section"

.. image:: images/zammad_connect_twitter_thirdparty1.png
   :alt: Admin -> Security -> Third Party Applications
   
Fill in the "Twitter Key" and the "Twitter Secret" and click the "Submit" button.
