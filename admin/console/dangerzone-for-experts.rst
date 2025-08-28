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

.. code-block:: ruby

   Ticket.find(4).destroy

Delete all tickets:

.. code-block:: ruby

   Ticket.destroy_all

Keep some tickets (specified by database ID); delete the rest:

.. code-block:: ruby

   tickets_to_keep = [1, 2, 3]

.. code-block:: ruby

   Ticket.where.not(id: tickets_to_keep).destroy_all

Removing Users
--------------

.. hint::

   Console based deletion is not recommended. Instead, use Zammad's
   :admin-docs:`data privacy </system/data-privacy.html>` feature.

.. warning::

   Customers **can't be** deleted while they have tickets remaining in the
   system. Because of that, the examples below delete **all tickets associated
   with them**, as well. The commands don't require a confirmation, be careful.

Removing users is possible in 2 ways: A single user and in bulk.

.. tabs::

   .. tab:: Remove a single user

      .. code-block:: ruby

         User.find_by(email: '<email address>').destroy

   .. tab:: Remove several users

      .. code-block:: ruby

         User.where(
            email: ['<email address 1>', '<email address 2>']
         ).destroy_all

Removing Organizations
----------------------

.. note:: Removing an organization does **not** delete associated customers.

Step 1: Select organizations
   By "active" status:

   .. code-block:: ruby

      organizations = Organization.where(active: false)

   By name:

   .. code-block:: ruby

      organizations = Organization.where(name: 'Acme')

   By partial match on notes content:

   .. code-block:: ruby

      organizations = Organization.where('note LIKE ?', '%foo%')

Step 2: Preview affected organizations
   .. code-block:: ruby

      puts organizations.map { |org| "ORGANIZATION #{org.name}" }.join("\n")

Step 3: Proceed with deletion
   .. code-block:: ruby

      organizations.each do |org|
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

.. code-block:: ruby

   OnlineNotification.destroy_all

Remove all entries from the Activity Stream (dashboard):

.. code-block:: ruby

   ActivityStream.destroy_all

Remove entries for all recently viewed objects (tickets, users, organizations):

.. code-block:: ruby

   RecentView.destroy_all

Remove all history information from tickets, users and organizations
(dangerous!):

.. code-block:: ruby

   History.destroy_all

.. _dangerzone_reset_zammad:

Reset Zammad Installation
-------------------------

.. hint::

   Below commands are incomplete intentionally, error outputs will hint you
   through! The following operations will cause data loss and are for
   development / testing only.

   Don't forget to stop Zammad before trying to drop the database!

.. code-block:: sh

   rake db:drop

.. code-block:: sh

   rake db:create

.. code-block:: sh

   rake db:migrate

.. code-block:: sh

   rake db:seed
