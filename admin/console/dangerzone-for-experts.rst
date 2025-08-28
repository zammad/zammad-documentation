Deleting Records
================

.. danger::

   ☠️ The commands listed here cause **irrecoverable data loss**!
   Only proceed if you know what you're doing and you
   :doc:`have a backup </appendix/backup-and-restore/index>`!

.. include:: /admin/console/missing-commands-ask-community.include.rst

Removing Tickets (And Their Articles)
-------------------------------------

Delete a ticket (specified by database ID):

.. code-block:: irb

   >> Ticket.find(4).destroy

Delete all tickets:

.. code-block:: irb

   >> Ticket.destroy_all

Keep some tickets (specified by database ID) and delete the rest:

.. code-block:: irb

   >> tickets_to_keep = [1, 2, 3]

.. code-block:: irb

   >> Ticket.where.not(id: tickets_to_keep).destroy_all

Removing Users
--------------

.. warning::

   - Deletion via console is not recommended. Use Zammad's
     :admin-docs:`data privacy </system/data-privacy.html>` UI feature to delete
     users and organizations.
   - Customers **cannot** be deleted while they have tickets remaining in the
     system. The examples below will delete **all tickets associated with them**
     as well.
   - The commands below remove data without requiring a confirmation.

Removing users is possible in 2 ways: A single user and in bulk.

.. tabs::

   .. tab:: Remove a single user

      .. code-block:: irb

         >> User.find_by(email: '<email address>').destroy

   .. tab:: Remove several users

      .. code-block:: irb

         >> User.where(
               email: ['<email address 1>', '<email address 2>']
            ).destroy_all

Removing Organizations
----------------------

.. note:: Removing an organization does **not** delete associated customers.

Step 1: Select organizations
   By "active" status:

   .. code-block:: irb

      >> organizations = Organization.where(active: false)

   By name:

   .. code-block:: irb

      >> organizations = Organization.where(name: 'Acme')

   By partial match of the notes field:

   .. code-block:: irb

      >> organizations = Organization.where('note LIKE ?', '%foo%')

Step 2: Preview affected organizations
   .. code-block:: irb

      >> puts organizations.map { |org| "ORGANIZATION #{org.name}" }.join("\n")

Step 3: Proceed with deletion
   .. code-block:: irb

      >> organizations.each do |org|
           puts %{Preparing deletion of organization "#{org.name}"...}

           org.members.each do |member|
              puts "  Removing #{member.fullname} from organization..."
              member.update!(organization_id: nil)
           end

           puts "  Deleting #{org.name}..."
           org.destroy
         end

Removing System Records
-----------------------

Remove all online notifications:

.. code-block:: irb

   >> OnlineNotification.destroy_all

Remove all entries from the Activity Stream (dashboard):

.. code-block:: irb

   >> ActivityStream.destroy_all

Remove entries for all recently viewed objects (tickets, users, organizations):

.. code-block:: irb

   >> RecentView.destroy_all

Remove all history information from tickets, users and organizations (dangerous!):

.. code-block:: irb

   >> History.destroy_all

.. _dangerzone_reset_zammad:

Reset Zammad Installation
-------------------------

.. hint::

   Below commands are incomplete intentionally, error outputs will hint you
   through! The following operations will cause data loss and are for
   development / testing only.

   Don't forget to stop Zammad before trying to drop the database!

.. code-block:: console

   $ rake db:drop

.. code-block:: console

   $ rake db:create

.. code-block:: console

   $ rake db:migrate

.. code-block:: console

   $ rake db:seed
