Running console commands on an Univention-Host
==============================================

.. include:: /install/univention/deprecation-warning.rst

In some cases you might need to access Zammads rails console on the
Univention-Host. For this, you'll need to get the correct container ID first.

Univention will hold this information for you, you can get it like that:

.. code-block:: sh

   $ ucr get appcenter/apps/zammad/container

Now where we have our ID, you can run any command from the :doc:`/admin/console`
section with either:

.. code-block:: sh

   $ docker exec -i "{Container-ID}" rails r "{COMMAND}"

or -if you need a console for more commands- by:

.. code-block:: sh

   $ docker exec -i "{Container-ID}" rails c

.. note::

   Please replace ``{Container-ID}`` in the above commands by the ID the first
   command returns. Replace ``{COMMAND}`` by any rails command Zammad supports.

That's it!
