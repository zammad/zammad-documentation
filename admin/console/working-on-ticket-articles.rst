Working with Ticket Articles
============================

.. include:: /admin/console/missing-commands-ask-community.include.rst

Count Public “Notes” Toward SLAs
--------------------------------

Normally, :user-docs:`notes </basics/service-ticket/follow-up.html#adding-new-messages-notes>`
don't count toward :admin-docs:`service-level agreements </manage/slas/index.html>`.
Use the following command to include publicly-visible notes when tracking SLA
compliance. (Internal notes *will never* affect SLA calculations.)

.. note::

   By default, customers are not notified when public notes are added to a
   ticket. Set up a :admin-docs:`trigger </manage/trigger.html>` if you wish to
   change this behavior.

.. warning::

   Changing this setting will disable the option to delete public notes.

Enable SLA to count notes as communication:

.. code-block:: irb

   >> Ticket::Article::Type.find_by(name:'note').update!(communication: true)

Enable SLA to ignore notes as communication:

.. code-block:: irb

   >> Ticket::Article::Type.find_by(name:'note').update!(communication: false)
