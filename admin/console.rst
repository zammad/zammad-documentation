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
