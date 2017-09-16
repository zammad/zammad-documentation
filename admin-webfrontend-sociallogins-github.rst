Social Logins - GitHub
**********************

It is possible to create a quick login for your helpdesk via GitHub.
To activate the quick login you need to enable OAuth for GitHub.

Register GitHub App
===================

Visit https://www.github.com/settings/applications/new and enter the app settings.
As callback URL enter "https://zammad_host/auth/github/callback"
where zammad_host has to be replaced with your Zammad FQDN

.. image:: images/zammad_connect_github_thirdparty_github.png
   :alt: Register OAuth app on www.github.com


Configure Zammad as GitHub app
==============================

Enter the "APP ID" and the "APP SECRET" from the GitHub OAUTH Applications Dashboard

.. image:: images/zammad_connect_github_thirdparty_zammad.png
   :alt: GitHub config in Zammad admin interface


After you configured the GitHub credentials and activated
the login method, you should see a new icon on the login page.

.. image:: images/zammad_connect_github_thirdparty_login.png
   :alt: GitHub logo on login page

If you click on the icon you will be redirected to GitHub and see something
similar to this:

.. image:: images/zammad_connect_github_thirdparty_github_authorize.png
   :alt: GitHub oauth page

When you grant the access you will be redirected to your Zammad instance
and logged in as a customer.
