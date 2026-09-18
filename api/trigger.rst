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

   🤓 ``recipient: "article_last_sender"`` emails whoever wrote the
   triggering article, correct here since the condition requires
   ``article.sender_id`` to be ``2`` (Customer). If an *agent* wrote the
   article instead, this would wrongly email the agent; use
   ``recipient: "ticket_customer"`` (see Create below) to always target
   the customer regardless of who performed the action.

Show
----

Required permission: ``admin.trigger``

``GET``-Request sent: ``/api/v1/triggers/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 13,
      "name": "Notify customer on public note",
      "condition": {
         "operator": "AND",
         "conditions": [
            {"name": "ticket.action", "operator": "is", "value": "update"},
            {"name": "article.type_id", "operator": "is", "value": 10},
            {"name": "article.internal", "operator": "is", "value": false}
         ]
      },
      "perform": {
         "notification.email": {
            "recipient": "ticket_customer",
            "subject": "Update on your ticket (#{ticket.title})",
            "body": "<div>There has been a follow-up on your ticket <b>(#{config.ticket_hook}#{ticket.number})</b>.</div><br/><div>To view the details, click the following link:<a href=\"#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}\">#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}</a></div><br/><div>Your #{config.product_name} Team</div>"
         }
      },
      "disable_notification": false,
      "localization": null,
      "timezone": null,
      "note": "Notifies the customer by email whenever an agent adds a public note.",
      "activator": "action",
      "execution_condition_mode": "selective",
      "active": false,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2026-09-18T00:00:00.000Z",
      "updated_at": "2026-09-18T00:00:00.000Z"
   }

Create
------

Required permission: ``admin.trigger``

``POST``-Request sent: ``/api/v1/triggers``

.. code-block:: json

   {
      "name": "Notify customer on public note",
      "condition": {
         "operator": "AND",
         "conditions": [
            {"name": "ticket.action", "operator": "is", "value": "update"},
            {"name": "article.type_id", "operator": "is", "value": 10},
            {"name": "article.internal", "operator": "is", "value": false}
         ]
      },
      "perform": {
         "notification.email": {
            "recipient": "ticket_customer",
            "subject": "Update on your ticket (#{ticket.title})",
            "body": "<div>There has been a follow-up on your ticket <b>(#{config.ticket_hook}#{ticket.number})</b>.</div><br/><div>To view the details, click the following link:<a href=\"#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}\">#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}</a></div><br/><div>Your #{config.product_name} Team</div>"
         }
      },
      "disable_notification": false,
      "activator": "action",
      "execution_condition_mode": "selective",
      "active": false,
      "note": "Notifies the customer by email whenever an agent adds a public note."
   }

.. note::

   Two ``condition`` shapes both work when creating a trigger through
   this API: a flat dict keyed by field name (as shown in the List
   example above, matching Zammad's own stock triggers) and the explicit
   ``{"operator": "AND", "conditions": [...]}`` array form used above.
   Both were directly confirmed to be accepted and to function correctly
   when the trigger fires.

.. note::

   ``article.type_id: 10`` is Zammad's internal id for the "note"
   article type.

In this example, an agent adding a public note to a ticket results in
the ticket's actual customer receiving the email, not the agent who
wrote the note, because ``recipient: "ticket_customer"`` always
resolves to the customer regardless of who performed the triggering
action.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 13,
      "name": "Notify customer on public note",
      "condition": {
         "operator": "AND",
         "conditions": [
            {"name": "ticket.action", "operator": "is", "value": "update"},
            {"name": "article.type_id", "operator": "is", "value": 10},
            {"name": "article.internal", "operator": "is", "value": false}
         ]
      },
      "perform": {
         "notification.email": {
            "recipient": "ticket_customer",
            "subject": "Update on your ticket (#{ticket.title})",
            "body": "<div>There has been a follow-up on your ticket <b>(#{config.ticket_hook}#{ticket.number})</b>.</div><br/><div>To view the details, click the following link:<a href=\"#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}\">#{config.http_type}://#{config.fqdn}/#ticket/zoom/#{ticket.id}</a></div><br/><div>Your #{config.product_name} Team</div>"
         }
      },
      "disable_notification": false,
      "localization": null,
      "timezone": null,
      "note": "Notifies the customer by email whenever an agent adds a public note.",
      "activator": "action",
      "execution_condition_mode": "selective",
      "active": false,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2026-09-18T00:00:00.000Z",
      "updated_at": "2026-09-18T00:00:00.000Z"
   }

Update
------

Required permission: ``admin.trigger``

``PUT``-Request sent: ``/api/v1/triggers/{id}``

Same payload shape as Create above. Response is the updated record, same
shape as Show/Create with ``updated_at`` refreshed.

.. note::

   A partial payload works too, e.g. ``{"active": false}`` to toggle
   just that field. Re-sending the same full Create payload updates the
   existing record in place rather than creating a duplicate, locate the
   trigger's id first via ``GET /api/v1/triggers`` (list and filter by
   ``name``), then ``PUT`` to ``/api/v1/triggers/{id}`` with that id.
