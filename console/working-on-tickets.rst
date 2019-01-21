Working with ticket information
*******************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Update the customer of a bundle of tickets
------------------------------------------

::

 rails> Ticket.where(customer_id: 4).update_all(customer_id: 1)


Change priority
---------------

::

 rails> priority2 = Ticket::Priority.find(2)
 rails> priority2.name = '2-high'
 rails> priority2.default_create = true
 rails> priority2.save!


Get ticket state types
----------------------

::

 rails> Ticket::StateType.all


Add new ticket state
--------------------

option a) a pending remidner state (send reminder notification to agent if time has reached)
::

 rails> 
    Ticket::State.create_or_update(
      name: 'pending customer feedback',
      state_type: Ticket::StateType.find_by(name: 'pending reminder'),
      ignore_escalation: true,
      created_by_id: 1,
      updated_by_id: 1,
    )

option b) a pending action state (convert ticket into next state if time has reached)
::

 rails> 
    Ticket::State.create_or_update(
      name: 'pending and reopen',
      state_type: Ticket::StateType.find_by(name: 'pending action'),
      ignore_escalation: true,
      next_state: Ticket::StateType.find_by(name: 'open'),
      created_by_id: 1,
      updated_by_id: 1,
    )

to make them available in UI you need to execute the following:

::

 rails> 
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

