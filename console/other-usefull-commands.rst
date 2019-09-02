Other useful commands
**********************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Fetch mails
-----------

The below command will do a manual fetch of mail channels. This will also show erors that might appear within that process.
::

 Channel.fetch


Add translation
---------------

This comes in handy if you e.g. added a new state that you need to translate for several languages.
::

 Translation.create_if_not_exists( :locale => 'de-de', :source => "New", :target => "Neu", format: 'string', created_by_id: 1, updated_by_id: 1 )


Translating attributes
~~~~~~~~~~~~~~~~~~~~~~

By default Zammad will not translate custom attributes.
With the following code you can enable translation. 
This will translate the attribute display name and the display names of values (if it's a value field).
For this to work, just replace ``{attribute-name}`` against the name of your attribute. 
::
  
  attribute = ObjectManager::Attribute.find_by(name: '{attribute-name}')
  attribute.data_option[:translate] = true		# set this to false to disable translation again
  attribute.save!

.. Note:: Translating value display names works for the following attribute types:
  
  * Boolean
  * Select
  * Tree Select
  
  If you're translating the display name of e.g. an Integer-attribute, this works as well!


Fill a test system with test data
---------------------------------

.. Warning:: Don't run this in a productive environment! This can slow down Zammad and is hard to revert if you create much!

The below command will add 50 agents, 1000 customers, 20 groups, 40 organizations, 5 new overviews and 100 tickets. 
You can always use ``0`` to not create specific items. Zammad will create random "fill data". 
::

 FillDB.load(agents: 50,customers: 1000,groups: 20,organizations: 40,overviews: 5,tickets: 100,)

