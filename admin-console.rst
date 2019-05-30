Console
*******

Zammad uses Ruby on Rails so you can make use of the `rails console <http://guides.rubyonrails.org/command_line.html>`_.

.. Warning:: Please double check your commands before running, as some of those commands might cause data loss or damaged tickets! If you're unsure, **use a test system first**!

To open the rails console on the shell you have to enter the following commands.

Start Zammad's Rails console
============================

Running a single command
------------------------

The following command will allow you to run a single command, without running a shell (e.g. for automation).

.. Note:: Replace ``{COMMAND}`` with your command you want to run.

.. Tip:: If you enter a ``p`` in front of your command (e.g. like ``rails r 'p Delayed::Job.count'``), you'll actually receive a printed output (without you won't!).

when you've installed Zammad from a package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

 shell> zammad run rails r '{COMMAND}'

 
when you've installed Zammad from source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

 shell> rails r '{COMMAND}'


Running several commands in a shell
-----------------------------------

The following command will provide you a rails console, you can run several commands inside it.

when you've installed Zammad from a package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

 shell> zammad run rails c

 
when you've installed Zammad from source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

 shell> rails c


Working on the console
======================

Here's a topic list for quick jumping and better overview.

.. toctree::
   :maxdepth: 2

   console/zammad-settings
   console/hidden-settings
   console/working-on-users
   console/working-on-tickets
   console/working-on-groups
   console/other-usefull-commands
   console/dangerzone-for-experts

