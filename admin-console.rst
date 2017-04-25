Console
*******

Zammad uses Ruby on Rails so you can make use of the rails console: http://guides.rubyonrails.org/command_line.html


To open the rails console on the shell you have enter the following commands.

Start Zammad's Rails console
============================

If you used a Zammad DEB or RPM package:
----------------------------------------

::

 shell> zammad run rails c

If you compiled Zammad by yoursef just use:
-------------------------------------------

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


Update the customer of a bundle of tickets
------------------------------------------

::

 rails> Ticket.where(customer_id: 4).update_all(customer_id: 1)


Change priority
---------------

::

  rails> priority2 = Priority.find(2)
  rails> priority2.name = '2-high'
  rails> priority2.default_create = true
  rails> priority2.save!


Get ticket_hook setting------
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

::

 rails> Ticket::State.create_or_update(
          name: 'customer feedback',
          state_type_id: Ticket::StateType.find_by(name: 'open').id,
          ignore_escalation: true,
          created_by_id: 1,
          updated_by_id: 1,
        )


Delete a certain ticket
-----------------------

::

 rails> Ticket.find(4).destroy

Delte some tickets
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

 rails> Translation.create!(source: 'Username / email', target: 'My Username / My Email', locale: 'en-us', format: 'string', created_by_id: 1, updated_by_id: 1)
 rails> Translation.create_if_not_exists( :locale => 'de', :source => "New", :target => "Neu" )


Set admin rights for user
-------------------------

::

 rails> u = User.find_by(email: 'you@example.com')
 rails> u.roles = Role.where(name: ['Agent', 'Admin'])
 rails> u.save!


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
