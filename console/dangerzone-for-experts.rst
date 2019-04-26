Working with ticket information
*******************************

.. DANGER:: Please note that the commands on this page cause **DATA LOSS**! Only proceed if you know what you're doing and you **have a backup**!

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.


Delete a certain ticket
-----------------------

The following command removes a specific ticket and all of it's articles from Zammad.
::

 Ticket.find(4).destroy

Delete some tickets
------------------

This will remove all existing tickets, except for those you specified within `tickets_to_keep`-variable before.
::

 tickets_to_keep = [1, 2, 3] # enter the ids of all tickets you want to keep
 (Ticket.all.pluck(:id) - tickets_to_keep).each { |id| Ticket.find(id).destroy }


Delete all tickets
------------------

This removes all existing tickets within Zammad.
::

 Ticket.destroy_all


Delete one or more users with all their related information
-----------------------------------------------------------

.. Warning:: You can't remove users without removing tickets of them!

.. Note:: This is meant for deleting customers, agents differ a bit and might have different results - user with caution!

yes
::

 target_user_emails = ['customer@example.com']
 # This will generate an overview what Zammad will remove
 list = ''
 target_user_emails.each {|email|
   User.where(email: email.downcase).each {|user|
     next if user.id == 1
     next if !user.permissions?('ticket.customer')
     list += "Customer #{user.login}/#{user.email}/#{user.id} has #{Ticket.where(customer_id: user.id).count} tickets #{Ticket.where(customer_id: user.id).pluck(:number)}\n"
   }
 }
 puts list


blah
::
 # Actual deletion, requires overview run before
 User.joins(roles: :permissions).where(email: target_user_emails.map(&:downcase), roles: { active: true }, permissions: { name: 'ticket.customer', active: true }).where.not(id: 1).find_each do |user|
  puts "Customer #{user.login}/#{user.email} has #{Ticket.where(customer_id: user.id).count} tickets"

  Ticket.where(customer: user).find_each do |ticket|
    puts "  Deleting ticket #{ticket.number}..."
    ticket.destroy
  end

  puts "  Removing references for user with E-Mail #{user.email}..."
  ActivityStream.where(created_by_id: user.id).update_all(created_by_id: 1)
  History.where(created_by_id: user.id).update_all(created_by_id: 1)
  Ticket::Article.where(created_by_id: user.id).update_all(created_by_id: 1)
  Ticket::Article.where(updated_by_id: user.id).update_all(updated_by_id: 1)
  Store.where(created_by_id: user.id).update_all(created_by_id: 1)
  StatsStore.where(created_by_id: user.id).update_all(created_by_id: 1)
  Tag.where(created_by_id: user.id).update_all(created_by_id: 1)
  if OnlineNotification.find_by(user_id: user.id)==""
   OnlineNotification.find_by(user_id: user.id).destroy!
  end

  puts "  Deleting user #{user.login}/#{user.email}..."
  user.destroy
 end


Destroy stuff
-------------

These commands will destroy historical information within Zammad.
::

 OnlineNotification.destroy_all	# Remove all online notifications
 ActivityStream.destroy_all	# Remove all entries from the Activity Stream (Dashboard)
 RecentView.destroy_all		# Removes the entries for all recently viewed Objects (Tickets, Users, Organizations)
 History.destroy_all		# This removes all history information from Tickets, Users and Organizations (dangeorus!)

