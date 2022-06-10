Migrating to Zammad
*******************

Zammad will migrate the following information:

   * Tickets and their Articles
   * Groups / Queues
   * Organizations
   * Agents and Customers (if applicable)

After migrating to Zammad you'll want to continue with the 
:doc:`/getting-started/first-steps` to configure Zammad. This has to be 
done *after migration*.

.. _migration_limitations:

Limitations
===========

There might be source dependent limitations which we will be covering on the direct migration pages. 

However, these limitations count for all migrations:

   * Migrations are only possible on new instances.
   * Migrations are only possible from **one sources**.
     Several migration sources on one instance are *not* supported.
   * Zammad can't migrate object types it doesn't know, migrations will fail.
   * Zammad migrates **all or nothing**. This means that you can't deselect
     specific information specific groups, tickets or users.

Available Migration Options
===========================

.. toctree::
   :maxdepth: 1

   Freshdesk </migration/freshdesk>
   Kayako </migration/kayako>
   OTRS </migration/otrs>
   Zendesk </migration/zendesk>

.. note::

   **😖 Missing a migration source?**

   If we don't cover your favorite source yet, you'll have two options. 
   You can either fiddle around by using Zammads powerful :doc:`API </api/intro>` 
   or drop our `sales team <https://zammad.com/en/company/contact>`_ a message 
   for a custom development or even migrator sponsoring.

   **🤓 Migrations are available for hosted setups too, contact support for 
   further information!**
