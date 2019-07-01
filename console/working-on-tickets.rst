Working with ticket information
*******************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Get the RAW mail that Zammad fetched
------------------------------------

The following command will help you to check on received emls Zamamd fetched. This comes in handy if you delete Mails upon fetching and you need to check the eml itself.

To get the first articles eml, you can use the following command. In our example the ticket number in question is ``101234``
::
  
  Ticket.find_by(number:'101234').articles.first.as_raw.content

If needed, you can also get the raw content of later articles (you'll need to find the correct article though). Again, we expect ``101234`` to be our ticket number.
In the first step we get all article IDs of the ticket, from the list we get, we can then get the articles content.
::
  
  > Ticket.find_by(number:'101234').articles_ids
  => [4, 3, 2]
  > Ticket::Article.find(3).as_raw.content

.. Note:: If you just use ``Ticket::Article.find(3)`` you can see further information (like who sent the mail, when we fetched it, ...).


Update all tickets of a specific customer
-----------------------------------------

.. Warning:: Please note that this action can be expensive in ressource terms, if you have many tickets, this might slow down Zammad.

::

 Ticket.where(customer_id: 4).update_all(customer_id: 1)


Change priority
---------------

The following commands will enable you to change the naming of priorities. If you set ``.default_create`` to ``true`` you can manipulate what Zammad will use as default priority.
::

 priority2 = Ticket::Priority.find(2)
 priority2.name = '2-high'
 priority2.default_create = true
 priority2.save!


Get ticket state types
----------------------

This will show all Ticket States needed for creating new states.

.. Note:: Missing States you just created? You might want to use ``Ticket.State.all``  to display all states for Tickets.

::

 Ticket::StateType.all


Add new ticket state
--------------------

.. Note:: You can use ``ignore_escalation: true,`` to ignore possible SLA escalations (pending reminder and pending close use that by default).

Non-Pending states
^^^^^^^^^^^^^

A state that's not a pending state (e.g. open, closed). Just replace ``'open'`` by whatever you need (like closed).
::

    Ticket::State.create_or_update(
      name: 'Developing',
      state_type: Ticket::StateType.find_by(name: 'open'),
      created_by_id: 1,
      updated_by_id: 1,
    )

Pending reminders
^^^^^^^^^^^^^^^^^^

A pending reminder state that will send a reminder notification to the agent if the time has been reached.
::

    Ticket::State.create_or_update(
      name: 'pending customer feedback',
      state_type: Ticket::StateType.find_by(name: 'pending reminder'),
      ignore_escalation: true,
      created_by_id: 1,
      updated_by_id: 1,
    )

Pending Action
^^^^^^^^^^^^^^
	
A pending action that will change to another state if "pending till" has been reached.
::

    Ticket::State.create_or_update(
      name: 'pending and reopen',
      state_type: Ticket::StateType.find_by(name: 'pending action'),
      ignore_escalation: true,
      next_state: Ticket::State.find_by(name: 'open'),
      created_by_id: 1,
      updated_by_id: 1,
    )

Add a date and time picker (pending till) for pending states
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to pick a date and time for a pending state (which usually makes sense), you'll need to run the following code.
To do this state specific, just use ``state_id: {UD}`` while ``{ID}`` is the ID of the state you created before.
If you want to apply this to all pending states, you can use ``state_id: Ticket::State.by_category(:pending).pluck(:id)`` instead of ``state_id: {UD}``
::
  ObjectManager::Attribute.add(
  force: true,
  object: 'Ticket',
  name: 'pending_time',
  display: 'Pending till',
  data_type: 'datetime',
  data_option: {
  future: true,
  past: false,
  diff: 24,
  null: true,
  translate: true,
  required_if: {
  state_id: {ID},
  },
  shown_if: {
  state_id: {ID},
  },
  },
  editable: false,
  active: true,
  screens: {
  create_middle: {
  '-all-' => {
  null: false,
  item_class: 'column',
  },
  },
  edit: {
  '-all-' => {
  null: false,
  },
  },
  },
  to_create: false,
  to_migrate: false,
  to_delete: false,
  position: 41,
  )


Make new states available to UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before being able to use the new states within the WebApp, you need to run the following commands to make them available.
::

    attribute = ObjectManager::Attribute.get(
      object: 'Ticket',
      name: 'state_id',
    )
    attribute.data_option[:filter] = Ticket::State.by_category(:viewable).pluck(:id)
    attribute.screens[:create_middle]['ticket.agent'][:filter] = Ticket::State.by_category(:viewable_agent_new).pluck(:id)
    attribute.screens[:create_middle]['ticket.customer'][:filter] = Ticket::State.by_category(:viewable_customer_new).pluck(:id)
    attribute.screens[:edit]['ticket.agent'][:filter] = Ticket::State.by_category(:viewable_agent_new).pluck(:id)
    attribute.screens[:edit]['ticket.customer'][:filter] = Ticket::State.by_category(:viewable_customer_edit).pluck(:id)
    attribute.save!

