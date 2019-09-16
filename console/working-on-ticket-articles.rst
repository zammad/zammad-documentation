Working with ticket articles
****************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at the `Community <https://community.zammad.org>`_.

Change notes to communication articles for SLA calculation
----------------------------------------------------------

In some cases you might want to count note articles to your `service level agreements <https://admin-docs.zammad.org/en/latest/manage-slas.html>`_. 
By default, Zammad ignores notes with SLA activated. You might also want to ensure that public notes will be sent to the customer by a `Trigger <https://admin-docs.zammad.org/en/latest/manage-trigger.html>`_, because Zammad does not check for this!

.. Note:: The command below will only affect public notes, Zammad will still ignore private notes for SLA calculation!

::
  
  Ticket::Article::Type.find_by(name:'note').update!(communication: true)   # Enable SLA to count notes as communication
  Ticket::Article::Type.find_by(name:'note').update!(communication: false)   # Enable SLA to ignore notes as communication

