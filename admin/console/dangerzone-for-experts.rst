Deleting Records
****************

.. danger:: ☠️ The commands listed here cause **irrecoverable data loss**! Only proceed if you know what you're doing **and you have a backup**!

.. note:: The list of commands below is not exhaustive. If you can't find what you're looking for here, you are encouraged to `ask the community <https://community.zammad.org>`_.


Deleting Tickets (and their articles)
-------------------------------------

.. code-block:: ruby

   # Delete a ticket (specified by database ID)
   >> Ticket.find(4).destroy

   # Delete all tickets
   >> Ticket.destroy_all

   # Keep some tickets (specified by database ID); delete the rest
   >> tickets_to_keep = [1, 2, 3]
   >> Ticket.where.not(id: tickets_to_keep).destroy_all


Deleting Customers
------------------

.. warning:: Customers **may not** be deleted while they have tickets remaining in the system.

   As such, the examples below will delete not only the specified customers, but **all tickets associated with them**, as well.

Step 1: Select customers by email address
   .. code-block:: ruby

      >> customer_emails = %w[customer@example.com customer@example.org]

      >> customers = User.joins(roles: :permissions).where(email: customer_emails, roles: { active: true }, permissions: { name: 'ticket.customer', active: true }).where.not(id: 1)

Step 2: Preview affected users & tickets
   .. code-block:: ruby

      >> puts customers.map { |user| <<~PREVIEW }.join("\n")
           Customer #{user.fullname}/#{user.id}/#{user.email} has #{Ticket.where(customer_id: user.id).count} tickets #{Ticket.where(customer_id: user.id).pluck(:number)}
         PREVIEW

Step 3: Proceed with deletion
   .. code-block:: ruby

      >> customers.find_each do |user|
           puts %{Preparing deletion of customer "#{user.fullname}" (and #{Ticket.where(customer_id: user.id).count} associated tickets)}

           Ticket.where(customer: user).find_each do |ticket|
             puts "  Deleting ticket ##{ticket.number}..."
             ticket.destroy
           end

           puts "  Removing references for user with email #{user.email}..."
           ActivityStream.where(created_by_id: user.id).update_all(created_by_id: 1)
           History.where(created_by_id: user.id).update_all(created_by_id: 1)
           Ticket::Article.where(created_by_id: user.id).update_all(created_by_id: 1)
           Ticket::Article.where(updated_by_id: user.id).update_all(updated_by_id: 1)
           Store.where(created_by_id: user.id).update_all(created_by_id: 1)
           StatsStore.where(created_by_id: user.id).update_all(created_by_id: 1)
           Tag.where(created_by_id: user.id).update_all(created_by_id: 1)
           OnlineNotification.find_by(user_id: user.id)&.destroy!

           puts "  Deleting #{user.fullname}..."
           user.destroy
         end


Deleting Organizations
----------------------

.. note:: Deleting an organization does **not** delete associated customers.

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


Deleting System Records
-----------------------

.. code-block:: ruby

   # Remove all online notifications
   >> OnlineNotification.destroy_all

   # Remove all entries from the Activity Stream (dashboard)
   >> ActivityStream.destroy_all

   # Remove entries for all recently viewed objects (tickets, users, organizations)
   >> RecentView.destroy_all

   # Remove all history information from tickets, users and organizations (dangerous!)
   >> History.destroy_all

.. _dangerzone_reset_zammad:

Reset Zammad installation
-------------------------

.. hint:: 

   Below commands are incomplete intentionally, error outputs will hint you through! 
   The following operations will cause data loss and for development / testing only.

   Package installations will require you to add ``zammad run`` before the command itself.

   Don't forget to stop Zammad before trying to drop the database!

.. code-block:: sh

   $ rake db:drop
   $ rake db:create
   $ rake db:migrate
   $ rake db:seed
