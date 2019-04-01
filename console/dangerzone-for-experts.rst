Working with ticket information
*******************************

.. DANGER:: Please note that the commands on this page cause **DATA LOSS**! Only proceed if you know what you're doing and you **have a backup**!

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.


Delete a certain ticket
-----------------------

::

 Ticket.find(4).destroy

Delete some tickets
------------------

::

 tickets_to_keep = [1, 2, 3] # enter the ids of all tickets you want to keep
 (Ticket.all.pluck(:id) - tickets_to_keep).each { |id| Ticket.find(id).destroy }


Delete all tickets
------------------

::

 Ticket.destroy_all


Destroy stuff
-------------

::

 OnlineNotification.destroy_all
 ActivityStream.destroy_all
 RecentView.destroy_all
 History.destroy_all

