Working with Ticket Information
===============================

.. include:: /admin/console/missing-commands-ask-community.include.rst

Get the RAW Email That Zammad Fetched
-------------------------------------

The following command will help you to check on received EML-files Zammad
fetched. This comes in handy if you delete Mails upon fetching and you need to
check the EML-file itself.

To get the first articles EML-file, you can use the following command.
In our example the ticket number in question is ``101234``.

.. code-block:: irb

   >> Ticket.find_by(number:'101234').articles.first.as_raw.content

If needed, you can also get the raw content of later articles (you'll need to
find the correct article though). Again, we expect ``101234`` to be our ticket
number. In the first step we get all article IDs of the ticket, from the list
we get, we can then get the articles content.

Get article IDs:

.. code-block:: irb

   >> Ticket.find_by(number:'101234').article_ids

Example output:

.. code-block:: irb

   => [4, 3, 2]

Get raw content of specific article ID:

.. code-block:: irb

  >> Ticket::Article.find(3).as_raw.content

.. note::

   If you just use ``Ticket::Article.find(3)`` you can see further information
   (like who sent the mail, when we fetched it, ...).

Update All Tickets of a Specific Customer
-----------------------------------------

.. warning::

   Please note that this action can be expensive resource wise, if you have many
   tickets, this might slow down Zammad.

.. code-block:: irb

   >> Ticket.where(customer_id: 4).update_all(customer_id: 1)

.. _state_types:

Get Ticket State Types
----------------------
.. Not removed because it is still referenced in API state creation.

This will show all state types needed for creating new ticket states.

.. tip:: **What are state types?**

   Zammad uses state types to know what it should do with your state.
   This allows you to have different types like *pending actions*,
   *pending reminders* or *closed* states.

   State types also indicate the color scheme to be used.
   You can learn more about that
   :user-docs:`in our user documentation </basics/service-ticket/settings/state.html>`.

   If you want to add custom states, have a look in our
   :admin-docs:`admin documentation section </system/objects.html#system-attributes>`.

.. code-block:: irb

   >> Ticket::StateType.pluck(:id, :name)

Above will return both, the type ID and name - e.g.:
``[[1, "new"], [2, "open"], ...``.
