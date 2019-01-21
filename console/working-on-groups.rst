Working with groups
*******************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.


To open the rails console on the shell you have to enter the following commands.

Find group
----------

::

 rails> Group.find_by(name: 'Users').follow_up_possible 

