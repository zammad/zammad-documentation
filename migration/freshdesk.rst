from Freshdesk
**************

Limitations
===========

Please note below Freshdesk specific limitations. 
These are additional limitations to the
:ref:`general ones listed <migration_limitations>`.

   * | Differential migrations are **not** supported!
     | The general suggestion is to run a test import before to learn
       how long the migration is going to take.
   * **Important:** Please note that migration speed highly depends on your
     Freshdesk plan (API rate limits apply)

   .. note::

      Your Freshdesk plan has to provide API support.
      This may not apply to all available plans.

Prerequisites
=============

Step 1: Install Znuny4OTRS-Repo
--------------------------------

This is a dependency of the OTRS migration plugin.

Importing Freshdesk data
===================

After installing Zammad and configuring your 
:doc:`webserver </getting-started/configure-webserver>`, navigate to your 
Zammads FQDN in your Browser and follow the migration wizard.

Depending on the size of your OTRS installation this may take a while. 

You can get an idea of this process in the 
`migrator video on vimeo <https://vimeo.com/187752786>`_ .

After successfully migrating your OTRS installation, continue with :doc:`/getting-started/first-steps`.

Restarting from scratch
=======================

Turned wrong at some point? 
You can find the required commands to reset Zammad in our 
:ref:`Dangerzone <dangerzone_reset_zammad>`.
