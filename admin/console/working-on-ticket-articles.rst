Working with ticket articles
****************************

.. note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at the `Community <https://community.zammad.org>`_.

Count Public “Notes” toward SLAs
--------------------------------

In some cases you might want to count note articles to your `service level agreements <https://admin-docs.zammad.org/en/latest/manage-slas.html>`_. 
By default, Zammad ignores notes with SLA activated. You might also want to ensure that public notes will be sent to the customer by a `Trigger <https://admin-docs.zammad.org/en/latest/manage-trigger.html>`_, because Zammad does not check for this!

.. note:: By default, customers are not notified when public notes are added to a ticket. Set up a `trigger <https://admin-docs.zammad.org/en/latest/manage-trigger.html>`_ if you wish to change this behavior. 

.. warning:: Changing this setting will disable the option to delete public notes.

.. code-block:: ruby

   >> Ticket::Article::Type.find_by(name:'note').update!(communication: true)    # Enable SLA to count notes as communication
   >> Ticket::Article::Type.find_by(name:'note').update!(communication: false)   # Enable SLA to ignore notes as communication
