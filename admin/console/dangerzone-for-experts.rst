Deleting records
****************

.. danger::

   ☠️ The commands listed here cause **irrecoverable data loss**!
   Only proceed if you know what you're doing and you
   :doc:`have a backup </appendix/backup-and-restore/index>`!

.. include:: /admin/console/missing-commands-ask-community.include.rst

Removing tickets (and their articles)
-------------------------------------

.. code-block:: ruby

   # Delete a ticket (specified by database ID)
   >> Ticket.find(4).destroy

   # Delete all tickets
   >> Ticket.destroy_all

   # Keep some tickets (specified by database ID); delete the rest
   >> tickets_to_keep = [1, 2, 3]
   >> Ticket.where.not(id: tickets_to_keep).destroy_all

Removing users
--------------

.. warning::

   Customers **may not** be deleted while they have tickets remaining in the
   system.

   As such, the examples below will delete not only the specified customers,
   but **all tickets associated with them**, as well. Below commands remove
   upon executing without any further warnings.

.. hint::

   If you're not sure what to do and need to learn more about what Zammad does
   upon removing users, please consider using Zammad's UI options in stead.

   Our documentation for the :admin-docs:`data privacy </system/data-privacy.html>`
   function will help you a lot!

Removing users is possible in 2 ways: A single user and in bulk.

.. tabs::

   .. tab:: Remove a single user

      .. code-block:: ruby

         >> User.find_by(email: '<email address>').destroy

   .. tab:: Remove several users

      .. code-block:: ruby

         >> User.where(
               email: ['<email address 1>', '<email address 2>']
            ).destroy_all

Removing organizations
----------------------

.. note:: Removing an organization does **not** delete associated customers.

Step 1: Select organizations
   .. code-block:: ruby

      # by "active" status
      >> organizations = Organization.where(active: false)

      # by name
      >> organizations = Organization.where(name: 'Acme')

      # by partial match on notes
      >> organizations = Organization.where('note LIKE ?', '%foo%')

Step 2: Preview affected organizations
   .. code-block:: ruby

      >> puts organizations.map { |org| "ORGANIZATION #{org.name}" }.join("\n")

Step 3: Proceed with deletion
   .. code-block:: ruby

      >> organizations.each do |org|
           puts %{Preparing deletion of organization "#{org.name}"...}

           org.members.each do |member|
              puts "  Removing #{member.fullname} from organization..."
              member.update!(organization_id: nil)
           end

           puts "  Deleting #{org.name}..."
           org.destroy
         end

Removing system records
-----------------------

.. code-block:: ruby

   # Remove all online notifications
   >> OnlineNotification.destroy_all

   # Remove all entries from the Activity Stream (dashboard)
   >> ActivityStream.destroy_all

   # Remove entries for all recently viewed objects
   # (tickets, users, organizations)
   >> RecentView.destroy_all

   # Remove all history information from tickets, users and organizations
   # (dangerous!)
   >> History.destroy_all

.. _dangerzone_reset_zammad:

Reset Zammad installation
-------------------------

.. hint:: 

   Below commands are incomplete intentionally, error outputs will hint you
   through! The following operations will cause data loss and are for
   development / testing only.

   Don't forget to stop Zammad before trying to drop the database!

.. code-block:: sh

   $ rake db:drop
   $ rake db:create
   $ rake db:migrate
   $ rake db:seed
