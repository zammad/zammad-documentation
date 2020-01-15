Installation on Univention Corporate Server via App Center
**********************************************************

.. Note:: As Zammad is using Docker Compose for Univention Corporate Server, the minimum requirement is UCS 4.3-2 errata 345.

Univention Corporate Server (UCS) is an enterprise server with focus on identity and infrastructure management. With its marketplace called App Center it can easily extended by solutions like Zammad that benefit from integrations with the LDAP directory service and the mail infrastructure.

`Click here to learn more about Univention and what it can do for you <https://www.univention.de/>`_.


Prerequisites
=============

To install the Zammad app on UCS, please ensure that you're using at least UCS 4.3-2 errata 345.
The basic installation will already meet our requirement. You'll need the following additional things:

* An email server (no matter if handled via UCS or with an external system) for notifications, as you can't use sendmail in our Docker setup!
* You should at least have **2 CPU-Cores and 4GB of free RAM**.


.. Note:: Running the Zammad app with less than 4GB free RAM will lead to unexpected errors!

You see, that's not much - so go a head with the installation.


Installing Zammad
=================

The app installation itself is quite easy: Just open the App Center within UCS management system and search for ``Zammad``.
Press ``Install``, accept our license agreement and wait for the installation to finish.

.. image:: /images/univention/zammad-in-store.png

The installation will take about 5-15 minutes, depending on your hardware
speed. Please give the installation the needed time and don't abort. During the
automated setup there are some waits for services to come up. Please be
patient!

If it's finished, you can press ``open`` - you'll get to our Zammad Wizard. It helps you with the minimum of information we need. ( See ``First steps you should consider`` )

.. image:: /images/univention/installed-zammad.png


Values we automatically change during the UCS-Setup
---------------------------------------------------

In order to make the installation as complete and convenient as possible, we're changing the following default values to the following:

.. csv-table:: Changes values during installation
	:header: "value", "default value", "new value"
	:widths: 10,20,20

	"notification sender", "Notification Master <noreply@#{config.fqdn}>", "Zammad <noreply@{FQDN-of-UCS}> ³"
	"maximum email size", "10 MB", "35 MB"
	"FQDN", "{FQDN-of-UCS}", "{FQDN-of-UCS}:10412 ³"
	"HTTP-Type", "<empty>", "https"
	"Allow customer registration", "true", "false"
	"LDAP configuration", "<empty>", "Full LDAP-Configuration prepared ²"
	"LDAP activated", "<empty>", "false"


.. Note:: ² Please note that the Zammad-LDAP integration is pre filled with authentication data and the group mapping ``Zammad-Admin`` to the Admin-Role and ``Zammad-Agent`` to the Agent-Role. You can use those security groups.
  LDAP synchronization is disabled during installation, as activating it would disable the installation wizard of Zammad, which is needed to setup your Zammad instance properly.


.. Note:: ³ Please note that these settings are updated automatically, if you update FQDN and Port settings within the :doc:`/install/univention/app-settings` .

First steps you should consider
===============================

The most important part is obvious: Run the wizard and insert the information for your admin account.

.. Warning:: If the email address is used within UCS, you need to ensure that your user account within UCS has the needed Admin-Group, as otherwise a LDAP synchronization will downgrade your user account to the setup role!

You can now enter your company name and upload a company logo, if you want to. (the company name is mandatory).
The system URL has been set by our installation routine already, you should be good to continue without changing it.

.. Note:: Changing the system URL might lead to broken links within notification mails.

For the notification sender, you should use SMTP, as the Docker container does not come with any sendmail or local MTA.
If you choose local MTA, Zammad will not be able to send you any notifications.

The last step offers you to add your first email accounts to Zammad.
You're free to skip this step, you can configure your accounts later, as well.

Zammad is now ready to go.

The identity management integration with UCS LDAP directory allows the system administrator to maintain the users at one single point.
If you want to take advantage of UCS identity management integration, you need to do the following before hand:

* Add your desired Zammad admin users to the user group ``Zammad-Admin``.
* Add your desired Zammad agents to the user group ``Zammad-Agent``.
* All user accounts that are not covered by the default group mapping, will be added in the Zammad customer role.

You can now go to Admin-Settings -> Integration -> LDAP and simply activate LDAP.
The first LDAP synchronization will start shortly thereafter - Zammad will then synchronize user account data with the UCS LDAP directory hourly.

.. Note:: You're free to change the group-role mapping at any time. See `Configuring LDAP integration <https://admin-docs.zammad.org/en/latest/integrations/ldap.html>`_ for more information.

.. image:: /images/univention/initial-setup-ucs.gif


Further configuration
---------------------

The rest of the configuration is pretty straight forward and applies to our default.
We split our documentation into two further parts that will be of your interest:

 * `Admin-Documentation <https://admin-docs.zammad.org/>`_: this documentation holds any information about how to configure Zammad via WebApp.
 * `User-Documentation <https://user-docs.zammad.org/>`_: this documentation holds a complete user documentation (how to work with Zammad).

Further information
===================

The following sub pages might come in handy and help you to understand how the app works or on how to solve an issue.

.. toctree::
   :maxdepth: 1

   univention/app-settings
   univention/running-console-commands-on-univention
   univention/issues-you-might-encounter

.. Warning:: **Never** change any configurations the Zammad-App scripts create and work with! This will lead to unexpected issues and loss of configurations upon update!
