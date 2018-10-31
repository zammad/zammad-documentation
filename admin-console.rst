Console
*******

Zammad uses Ruby on Rails so you can make use of the rails console: http://guides.rubyonrails.org/command_line.html


To open the rails console on the shell you have to enter the following commands.

Start Zammad's Rails console
============================

If you used a Zammad DEB or RPM package:
----------------------------------------

::

 shell> zammad run rails c

If you installed Zammad from source use:
----------------------------------------

::

 shell> rails c


Example commands
================

Find user
---------

::

 rails> User.find(4)
 rails> User.find_by(email: 'your@email')


Find group
----------

::

 rails> Group.find_by(name: 'Users').follow_up_possible
 

Change / Update E-Mail-Adress of User
-------------------------------------

::

 rails> u=User.find(**USERID**)
 rails> u.email = 'user@exmaple.com'
 rails> u.save!
  
  
You need to find the User-ID of the user first for this.
  
  
Change / Update Login name of User
----------------------------------

::

 rails> u=User.find(**USERID**)
 rails> u.login = 'user@exmaple.com'
 rails> u.save!
  
  
You need to find the User-ID of the user first for this.


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


Get ticket_hook setting
-----------------------

::

 rails> Setting.get('ticket_hook')


Get fqdn setting
----------------

::

 rails> Setting.get('fqdn')


Find storage_provide setting
----------------------------

::

 rails> Setting.find_by(name: 'storage_provider')


Set storage_rpovider Setting
----------------------------

::

 rails> Setting.set('storage_provider', 'DB')


Fetch mails
-----------

::

 rails> Channel.fetch


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

Delete a certain ticket
-----------------------

::

 rails> Ticket.find(4).destroy

Delete some tickets
------------------

::

 rails> tickets_to_keep = [1, 2, 3] # enter the ids of all tickets you want to keep
 rails> (Ticket.all.pluck(:id) - tickets_to_keep).each { |id| Ticket.find(id).destroy }


Delete all tickets
------------------

::

 rails> Ticket.destroy_all


Add translation
---------------

::

 rails> Translation.create_if_not_exists( :locale => 'de-de', :source => "New", :target => "Neu", format: 'string', created_by_id: 1, updated_by_id: 1 )


Set admin rights for user
-------------------------

::

 rails> u = User.find_by(email: 'you@example.com')
 rails> u.roles = Role.where(name: ['Agent', 'Admin'])
 rails> u.save!


Set password for user
---------------------

::

 rails> User.find_by(email: 'you@example.com').update!(password: 'your_new_password')


Configuring Elasticsearch
-------------------------

::

 rails> Setting.set('es_url', 'http://127.0.0.1:9200')
 rails> Setting.set('es_user', 'elasticsearch')
 rails> Setting.set('es_password', 'zammad')
 rails> Setting.set('es_index', Socket.gethostname + '_zammad')
 rails> Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )
 rails> Setting.set('es_attachment_max_size_in_mb', 50)


Use the OTRS importer from the shell
------------------------------------

::

 rails> Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 rails> Setting.set('import_otrs_endpoint_key', 'xxx')
 rails> Setting.set('import_mode', true)
 rails> Import::OTRS.start


Enable proxy
------------

::

 rails> Setting.set('proxy', 'proxy.example.com:3128')
 rails> Setting.set('proxy_username', 'some user')
 rails> Setting.set('proxy_password', 'some pass')


Destroy stuff
-------------

::

 rails> OnlineNotification.destroy_all
 rails> ActivityStream.destroy_all
 rails> RecentView.destroy_all
 rails> History.destroy_all


Fill a testsystem with testdata (don´t do this on your production system!)
-------------

::

 rails> FillDB.load(agents: 50,customers: 1000,groups: 20,organizations: 40,overviews: 5,tickets: 100,)

