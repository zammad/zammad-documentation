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


Destroy stuff
-------------

These commands will destroy historical information within Zammad.
::

 OnlineNotification.destroy_all	# Remove all online notifications
 ActivityStream.destroy_all	# Remove all entries from the Activity Stream (Dashboard)
 RecentView.destroy_all		# Removes the entries for all recently viewed Objects (Tickets, Users, Organizations)
 History.destroy_all		# This removes all history information from Tickets, Users and Organizations (dangeorus!)

