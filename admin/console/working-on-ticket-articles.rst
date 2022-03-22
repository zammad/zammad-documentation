Working with ticket articles
****************************

.. include:: /admin/console/missing-commands-ask-community.include.rst

Count Public “Notes” toward SLAs
--------------------------------

Normally, `notes <https://user-docs.zammad.org/en/latest/basics/service-ticket/follow-up.html#adding-new-messages-notes>`_ don't count toward `service-level agreements <https://admin-docs.zammad.org/en/latest/manage-slas.html>`_.
Use the following command to include publicly-visible notes when tracking SLA compliance.
(Internal notes cannot be made to apply toward SLAs.)

.. note:: By default, customers are not notified when public notes are added to a ticket. Set up a `trigger <https://admin-docs.zammad.org/en/latest/manage-trigger.html>`_ if you wish to change this behavior. 

.. warning:: Changing this setting will disable the option to delete public notes.

.. code-block:: ruby

   >> Ticket::Article::Type.find_by(name:'note').update!(communication: true)    # Enable SLA to count notes as communication
   >> Ticket::Article::Type.find_by(name:'note').update!(communication: false)   # Enable SLA to ignore notes as communication
