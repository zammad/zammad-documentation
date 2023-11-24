Working with ticket information
*******************************

.. include:: /admin/console/missing-commands-ask-community.include.rst

Get the RAW mail that Zammad fetched
------------------------------------

The following command will help you to check on received EML-files Zammad
fetched. This comes in handy if you delete Mails upon fetching and you need to
check the EML-file itself.

To get the first articles EML-file, you can use the following command.
In our example the ticket number in question is ``101234``.

.. code-block:: ruby

  >> Ticket.find_by(number:'101234').articles.first.as_raw.content

If needed, you can also get the raw content of later articles (you'll need to
find the correct article though). Again, we expect ``101234`` to be our ticket
number. In the first step we get all article IDs of the ticket, from the list
we get, we can then get the articles content.

.. code-block:: ruby

  >> Ticket.find_by(number:'101234').article_ids
  => [4, 3, 2]
  >> Ticket::Article.find(3).as_raw.content

.. note::

   If you just use ``Ticket::Article.find(3)`` you can see further information
   (like who sent the mail, when we fetched it, ...).

Update all tickets of a specific customer
-----------------------------------------

.. warning::

   Please note that this action can be expensive resource wise, if you have many
   tickets, this might slow down Zammad.

.. code-block:: ruby

   >> Ticket.where(customer_id: 4).update_all(customer_id: 1)

Priorities
----------

Ticket priorities help your agent to see how important a customer request is.
Priorities are not available to customers and, Core wise, have no impact
on how Zammad handles a ticket. You can however adjust Zammad's behavior
with e.g. triggers, SLAs and schedulers.

Not sure what priorities are available in the system? Either have a look
in any ticket or run the following command.

.. code-block:: ruby

   >> Ticket::Priority.pluck(:name)

Adding priorities for tickets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ticket priorities come with several attributes, however, the most relevant
as of now are: ``name``, ``default_create`` and ``ui_color``.

   .. warning::

      ``default_create`` allows you to define the default priority Zammad should
      use during ticket creation. **However** - on default installations this is
      the priority ``2 normal``.

      *You cannot have more than one priority as the default_create priority!*

   .. note::

      ``ui_color`` defines the CSS class to use. On default installations
      you can either use ``low-priority`` (light blue) or ``high-priority``
      (red). This affects how Zammad displays the ticket titles
      *in overviews*.

.. code-block:: ruby

   >> Ticket::Priority.create(
         name: '4 super high',
         default_create: false,
         ui_color: 'high-priority',
         created_by_id: 1,
         updated_by_id: 1
      )

Change priority
~~~~~~~~~~~~~~~

If needed you can also set priorities to inactive or rename them if they
don't fit your desired scheme. Renaming would look like so:

.. code-block:: ruby

   >> Ticket::Priority.update(name: '1 high')

.. _state_types:

Get ticket state types
----------------------


This will show all state types needed for creating new ticket states.

.. tip:: **😖 What are state types?**

   Zammad uses state types to know what it should do with your state.
   This allows you to have different types like *pending actions*,
   *pending reminders* or *closed* states.

   State types also indicate the color scheme to be used.
   You can learn more about that
   :user-docs:`in our user documentation </basics/service-ticket/settings/state.html>`.

.. code-block:: ruby

   >> Ticket::StateType.pluck(:id, :name)

Above will return both, the type ID and name - e.g.:
``[[1, "new"], [2, "open"], ...``.
