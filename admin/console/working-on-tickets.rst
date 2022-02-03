Working with ticket information
*******************************

.. note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at the `Community <https://community.zammad.org>`_.

Get the RAW mail that Zammad fetched
------------------------------------

The following command will help you to check on received emls Zamamd fetched. This comes in handy if you delete Mails upon fetching and you need to check the eml itself.

To get the first articles eml, you can use the following command. In our example the ticket number in question is ``101234``

.. code-block:: ruby

  >> Ticket.find_by(number:'101234').articles.first.as_raw.content

If needed, you can also get the raw content of later articles (you'll need to find the correct article though). Again, we expect ``101234`` to be our ticket number.
In the first step we get all article IDs of the ticket, from the list we get, we can then get the articles content.

.. code-block:: ruby

  >> Ticket.find_by(number:'101234').article_ids
  => [4, 3, 2]
  >> Ticket::Article.find(3).as_raw.content

.. note:: If you just use ``Ticket::Article.find(3)`` you can see further information (like who sent the mail, when we fetched it, ...).


Update all tickets of a specific customer
-----------------------------------------

.. warning:: Please note that this action can be expensive in ressource terms, if you have many tickets, this might slow down Zammad.

.. code-block:: ruby

   >> Ticket.where(customer_id: 4).update_all(customer_id: 1)


Change priority
---------------

The following commands will enable you to change the naming of priorities. If you set ``.default_create`` to ``true`` you can manipulate what Zammad will use as default priority.

.. code-block:: ruby

   >> priority2 = Ticket::Priority.find(2)
   >> priority2.name = '2-high'
   >> priority2.default_create = true
   >> priority2.save!

.. _state_types:

Get ticket state types
----------------------


This will show all state types needed for creating new ticket states.

.. tip:: **😖 What are state types?**

   Zammad uses state types to know what it should do with your state.
   This allows you to have different types like *pending actions*,
   *pending reminders* or *closed* states.

   State types also indicate the color scheme to be used.
   You can learn more about that `in our user documentation`_.

.. _in our user documentation:
   https://user-docs.zammad.org/en/latest/basics/service-ticket/settings/state.html

.. code-block:: ruby

   >> Ticket::StateType.pluck(:id, :name)

Above will return both, the type ID and name - e.g.:
``[[1, "new"], [2, "open"], ...``.


Add new ticket state
--------------------

   .. note:: **🤓 Missing States you just created?**

      You might want to use ``Ticket::State.pluck(:id, :name)``
      to get a listing of all available ticket states.

   .. tip:: **🙈 ignoring escalations**

      You can use ``ignore_escalation: true,`` to ignore possible SLA
      calculations (pending reminder and pending close do this by default).

Non-Pending states
^^^^^^^^^^^^^^^^^^

A state that's not a pending state (e.g. open, closed). Just replace ``'open'`` by whatever you need (like closed).

.. code-block:: ruby

   >> Ticket::State.create_or_update(
        name: 'Developing',
        state_type: Ticket::StateType.find_by(name: 'open'),
        created_by_id: 1,
        updated_by_id: 1,
      )

Pending reminders
^^^^^^^^^^^^^^^^^^

A pending reminder state that will send a reminder notification to the agent if the time has been reached.

.. code-block:: ruby

   >> Ticket::State.create_or_update(
        name: 'pending customer feedback',
        state_type: Ticket::StateType.find_by(name: 'pending reminder'),
        ignore_escalation: true,
        created_by_id: 1,
        updated_by_id: 1,
      )

Pending Action
^^^^^^^^^^^^^^

A pending action that will change to another state if "pending till" has been reached.

.. code-block:: ruby

   >> Ticket::State.create_or_update(
        name: 'pending and reopen',
        state_type: Ticket::StateType.find_by(name: 'pending action'),
        ignore_escalation: true,
        next_state: Ticket::State.find_by(name: 'open'),
        created_by_id: 1,
        updated_by_id: 1,
      )

(optional) Disable date and time picker (pending till) for pending states
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting with Zammad 5.0, `Core Workflows`_ automatically handles displaying the
"pending till" field for pending states. Below snippet *is not required* and is
only relevant if you don't want to create a workflow within the UI of Zammad.

Replace ``pending customer feedback`` with the pending state of your choice.

.. code-block:: ruby

   >> CoreWorkflow.create_if_not_exists(
         name:               'remove pending till on state "pending customer feedback"',
         object:             'Ticket',
         condition_selected: { 'ticket.state_id'=>{ 'operator' => 'is', 'value' => Ticket::State.find_by(name: 'pending customer feedback').id.to_s } },
         perform:            { 'ticket.pending_time'=> { 'operator' => 'remove', 'remove' => 'true' } },
         created_by_id:      1,
         updated_by_id:      1,
      )

.. _states_to_ui:

Make new states available to UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before being able to use the new states within the WebApp, you need to run the following commands to make them available.

.. warning:: Please **do not replace** anything below, state_id is a named attribute which is correct and shall not be replaced!

.. code-block:: ruby

   >> attribute = ObjectManager::Attribute.get(
        object: 'Ticket',
        name: 'state_id',
      )
   >> attribute.data_option[:filter] = Ticket::State.by_category(:viewable).pluck(:id)
   >> attribute.screens[:create_middle]['ticket.agent'][:filter] = Ticket::State.by_category(:viewable_agent_new).pluck(:id)
   >> attribute.screens[:create_middle]['ticket.customer'][:filter] = Ticket::State.by_category(:viewable_customer_new).pluck(:id)
   >> attribute.screens[:edit]['ticket.agent'][:filter] = Ticket::State.by_category(:viewable_agent_edit).pluck(:id)
   >> attribute.screens[:edit]['ticket.customer'][:filter] = Ticket::State.by_category(:viewable_customer_edit).pluck(:id)
   >> attribute.save!


Limit available states for customers
------------------------------------

.. tip::

   `Core Workflows`_ allows you to achieve below described behavior any time
   without any issues. No need to use the console if you don't want to!

By default Zammad allows customers to change Ticket states to ``open`` and ``closed``.
If this does not meet your requirenments, you can adjust this at anytime.
The below example shows how to restrict your customer to only close tickets if needed:

.. code-block:: ruby

   >> attribute = ObjectManager::Attribute.get(
        object: 'Ticket',
        name: 'state_id',
      )
   >> attribute.screens['edit']['ticket.customer']['filter'] = Ticket::State.where(name: ['closed']).pluck(:id)
   >> attribute.save!


.. hint:: If you want to allow several different states for customers, you need to provide the state names as array - like so: ``['closed', 'open', 'my-amazing-state']`` (instead of ``['closed']``).

You can check the current active states that customers can set like so:

.. code-block:: ruby

   >> ObjectManager::Attribute.get(
        object: 'Ticket',
        name: 'state_id',
      ).screens['edit']['ticket.customer']['filter']

The above will return one or more IDs - if you're not sure which state they belong to, you can check the state name with the following command. (Ensure to replace ``{ID}`` with your returned ID(s))

.. code-block:: ruby

   >> Ticket::State.find({ID}).name

.. _Core Workflows: https://admin-docs.zammad.org/en/latest/system/core-workflows.html
