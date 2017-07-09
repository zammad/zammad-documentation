Github
******

It is possible to create a quick login for your helpdesk via Twitter To do so, you need to follow these steps:

Register Github App
===================

Visit https://github.com/settings/applications/new and enter the app settings as callback URL you need to enter "https://zammad_host/api/v1/external_credentials/twitter/callback"

.. image:: images/github.com-create-app.png
   :alt: Create App
   
   
Configure Zammad as Github app
==============================

Enter the "APP ID" and the "APP SECRET" from the Github OAUTH Applications Dashboard

.. image:: images/zammad_connect_github_thirdparty1.png
   :alt: Github
   
NOTICE: Don't forget to enable the function
======

