Other usefull commands
**********************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Fetch mails
-----------

::

 rails> Channel.fetch


Add translation
---------------

::

 rails> Translation.create_if_not_exists( :locale => 'de-de', :source => "New", :target => "Neu", format: 'string', created_by_id: 1, updated_by_id: 1 )


Fill a testsystem with testdata (don´t do this on your production system!)
-------------

::

 rails> FillDB.load(agents: 50,customers: 1000,groups: 20,organizations: 40,overviews: 5,tickets: 100,)

