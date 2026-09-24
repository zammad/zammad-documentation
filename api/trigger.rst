Trigger
=======

.. note::

   Triggers can ``perform`` a ``notification.webhook`` action that
   references a :doc:`Webhook </api/webhook>` by id
   (``{"notification.webhook": {"webhook_id": <id>}}``) instead of, or
   alongside, ``notification.email``, create the webhook first, then
   point the trigger's ``perform`` at its ``id``.

List
----

Required permission: ``admin.trigger``

``GET``-Request sent: ``/api/v1/triggers``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 2,
         "name": "auto reply (on follow-up of tickets)",
         "condition": {
            "ticket.action": {"operator": "is", "value": "update"},
            "article.sender_id": {"operator": "is", "value": 2},
            "article.type_id": {"operator": "is", "value": [1, 5, 11]}
         },
         "perform": {
            "notification.email": {
               "body": "<div>Your follow-up for <b>(#{config.ticket_hook}#{ticket.number})</b> has been received and will be reviewed by our support staff.</div>\n<br/>\n<div>To provide additional information, please reply to this email or click on the following link:\n<a href=\"#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}\">#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}</a>\n</div>\n<br/>\n<div>Your #{config.product_name} Team</div>\n<br/>\n<div><i><a href=\"https://zammad.com\">Zammad</a>, your customer support system</i></div>",
               "recipient": "article_last_sender",
               "subject": "Thanks for your follow-up (#{ticket.title})"
            }
         },
         "disable_notification": true,
         "localization": null,
         "timezone": null,
         "note": null,
         "activator": "action",
         "execution_condition_mode": "selective",
         "active": false,
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2026-09-07T06:40:27.193Z",
         "updated_at": "2026-09-07T06:40:27.193Z"
      }
   ]

.. note::

   ``recipient: "article_last_sender"`` emails whoever wrote the
   triggering article. In this example that is always the customer,
   because the condition requires ``article.sender_id`` to be ``2``
   (Customer). If an agent wrote the article, the agent would receive the
   email instead. Use ``recipient: "ticket_customer"`` (see Create below)
   to always target the customer regardless of who performed the action.

Show
----

Required permission: ``admin.trigger``

``GET``-Request sent: ``/api/v1/triggers/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 4,
      "name": "Notify customer on auto-close",
      "condition": {
         "operator": "AND",
         "conditions": [
            {"name": "ticket.state_id", "operator": "is", "value": [4]}
         ]
      },
      "perform": {
         "notification.email": {
            "recipient": "ticket_customer",
            "subject": "Your ticket #{ticket.number} has been closed",
            "body": "<div>Your ticket <b>#{ticket.number}</b> has been closed. Thank you for contacting us.</div>"
         }
      },
      "disable_notification": false,
      "localization": null,
      "timezone": null,
      "note": "Sends a confirmation email when a ticket is closed.",
      "activator": "action",
      "execution_condition_mode": "selective",
      "active": true,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2026-09-24T12:31:52.822Z",
      "updated_at": "2026-09-24T12:31:52.822Z"
   }

Create
------

Required permission: ``admin.trigger``

``POST``-Request sent: ``/api/v1/triggers``

.. code-block:: json

   {
      "name": "Notify customer on auto-close",
      "condition": {
         "operator": "AND",
         "conditions": [
            {"name": "ticket.state_id", "operator": "is", "value": [4]}
         ]
      },
      "perform": {
         "notification.email": {
            "recipient": "ticket_customer",
            "subject": "Your ticket #{ticket.number} has been closed",
            "body": "<div>Your ticket <b>#{ticket.number}</b> has been closed. Thank you for contacting us.</div>"
         }
      },
      "disable_notification": false,
      "activator": "action",
      "execution_condition_mode": "selective",
      "active": true,
      "note": "Sends a confirmation email when a ticket is closed."
   }

.. note::

   ``condition`` accepts two shapes: a flat object keyed by field name
   (as shown in the List example above, matching Zammad's stock
   triggers) and the explicit
   ``{"operator": "AND", "conditions": [...]}`` form used above.

In this example, closing a ticket results in the ticket's customer
receiving a confirmation email, because ``recipient:
"ticket_customer"`` always resolves to the customer regardless of who
performed the closing action.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 4,
      "name": "Notify customer on auto-close",
      "condition": {
         "operator": "AND",
         "conditions": [
            {"name": "ticket.state_id", "operator": "is", "value": [4]}
         ]
      },
      "perform": {
         "notification.email": {
            "recipient": "ticket_customer",
            "subject": "Your ticket #{ticket.number} has been closed",
            "body": "<div>Your ticket <b>#{ticket.number}</b> has been closed. Thank you for contacting us.</div>"
         }
      },
      "disable_notification": false,
      "localization": null,
      "timezone": null,
      "note": "Sends a confirmation email when a ticket is closed.",
      "activator": "action",
      "execution_condition_mode": "selective",
      "active": true,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2026-09-24T12:31:52.822Z",
      "updated_at": "2026-09-24T12:31:52.822Z"
   }

Update
------

Required permission: ``admin.trigger``

``PUT``-Request sent: ``/api/v1/triggers/{id}``

Same payload shape as Create above. Response is the updated record, same
shape as Show/Create with ``updated_at`` refreshed.

.. note::

   A partial payload works too, e.g. ``{"active": false}`` to toggle
   just that field. To update a trigger by name, look up its ``id`` via
   ``GET /api/v1/triggers`` first, then send the ``PUT`` request to
   ``/api/v1/triggers/{id}``.

Delete
------

Required permission: ``admin.trigger``

.. danger:: **This is a permanent removal**

   Please note that removing triggers cannot be undone.

``DELETE``-Request sent: ``/api/v1/triggers/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
