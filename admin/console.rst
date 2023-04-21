Console
*******

Zammad uses Ruby on Rails so you can make use of the `rails console`_.

.. _rails console:
   http://guides.rubyonrails.org/command_line.html

.. warning:: 

   Please double check your commands before running, as some of those commands
   might cause data loss or damaged tickets! If you're unsure,
   **use a test system first**!

To open the rails console on the shell you have to enter the following commands.

Start Zammad's Rails console
============================

Running a single command
------------------------

The following command will allow you to run a single command, without running
a shell (e.g. for automation).

.. note:: Replace ``{COMMAND}`` with your command you want to run.

.. tip::

   If you enter a ``p`` in front of your command
   (e.g. like ``rails r 'p Delayed::Job.count'``),
   you'll actually receive a printed output (without you won't!).

.. code-block:: sh

   # package installation
   $ zammad run rails r '{COMMAND}'

   # source installation
   $ rails r '{COMMAND}'

.. _rails_shell:

Running several commands in a shell
-----------------------------------

The following command will provide you a rails console.
It allows you to run several commands inside it.

This reduces loading times greatly.

.. include:: /admin/console-rails-shell.include.rst

.. warning:: **Safe Mode**

   Normally, starting rails console requires certain `third-party services`_ to
   be up and running. You may receive errors and console will refuse to start
   in case they are not available.

   However, it's possible to start rails console in safe mode by setting a
   special environment variable. With ``ZAMMAD_SAFE_MODE=1`` set, availability
   of these services will be ignored:

   .. code-block:: console

      $ ZAMMAD_SAFE_MODE=1 rails c
      Zammad app is running in safe mode. Any third-party service is ignored.

      There was an error trying to connect to Redis via redis://localhost:6379.
      Please provide a Redis instance at localhost:6379 or set REDIS_URL to point to a different location.
      ＃<Redis::CannotConnectError: Error connecting to Redis on localhost:6379 (Errno::ECONNREFUSED)>
      Loading production environment (Rails 6.1.7.3)
      3.1.3 :001 >

.. _`third-party services`: Server requirements

Working on the console
======================

Here's a topic list for quick jumping and better overview.

.. toctree::
   :maxdepth: 2

   console/zammad-settings
   console/hidden-settings
   console/working-on-users
   console/working-on-tickets
   console/working-on-ticket-articles
   console/working-on-groups
   console/working-on-chat
   console/other-useful-commands
   console/dangerzone-for-experts
