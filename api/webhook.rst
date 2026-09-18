Webhook
=======

.. note::

   Webhooks are referenced by :doc:`Triggers </api/trigger>` via the
   ``notification.webhook`` perform action
   (``{"notification.webhook": {"webhook_id": <id>}}``), create the
   webhook first, then point one or more triggers at its ``id``.

List
----

Required permission: ``admin.webhook``

``GET``-Request sent: ``/api/v1/webhooks``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 1,
         "name": "Local Operaton ticket lifecycle",
         "endpoint": "https://example.com/webhooks/incoming",
         "http_method": "post",
         "signature_token": "**********",
         "ssl_verify": true,
         "basic_auth_username": null,
         "basic_auth_password": null,
         "bearer_token": null,
         "note": "Correlates local Zammad lifecycle events to one Operaton process instance per ticket.",
         "pre_defined_webhook_type": null,
         "customized_payload": false,
         "custom_payload": null,
         "preferences": {},
         "active": true,
         "updated_by_id": 3,
         "created_by_id": 3,
         "created_at": "2026-09-07T07:31:30.066Z",
         "updated_at": "2026-09-07T07:51:40.855Z"
      }
   ]

.. note::

   🤓 ``signature_token`` is always masked as ``**********`` on read once
   it's set, the API never returns the real secret back to you after
   creation. An empty/unset token is returned as an empty string instead.

Show
----

Required permission: ``admin.webhook``

``GET``-Request sent: ``/api/v1/webhooks/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 1,
      "name": "Local Operaton ticket lifecycle",
      "endpoint": "https://example.com/webhooks/incoming",
      "http_method": "post",
      "signature_token": "**********",
      "ssl_verify": true,
      "basic_auth_username": null,
      "basic_auth_password": null,
      "bearer_token": null,
      "note": "Correlates local Zammad lifecycle events to one Operaton process instance per ticket.",
      "pre_defined_webhook_type": null,
      "customized_payload": false,
      "custom_payload": null,
      "preferences": {},
      "active": true,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2026-09-07T07:31:30.066Z",
      "updated_at": "2026-09-07T07:51:40.855Z"
   }

Create
------

Required permission: ``admin.webhook``

``POST``-Request sent: ``/api/v1/webhooks``

.. code-block:: json

   {
      "name": "Local Operaton ticket lifecycle",
      "endpoint": "https://example.com/webhooks/incoming",
      "http_method": "post",
      "signature_token": "your-signature-token",
      "ssl_verify": true,
      "customized_payload": false,
      "note": "Correlates local Zammad lifecycle events to one Operaton process instance per ticket.",
      "active": true
   }

.. note::

   ``ssl_verify`` matters for ``https://`` endpoints, set it ``true``
   to actually validate the endpoint's TLS certificate. It only makes
   sense to set it ``false`` for a plain ``http://`` endpoint, which has
   no certificate to verify in the first place.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 1,
      "name": "Local Operaton ticket lifecycle",
      "endpoint": "https://example.com/webhooks/incoming",
      "http_method": "post",
      "signature_token": "**********",
      "ssl_verify": true,
      "basic_auth_username": null,
      "basic_auth_password": null,
      "bearer_token": null,
      "note": "Correlates local Zammad lifecycle events to one Operaton process instance per ticket.",
      "pre_defined_webhook_type": null,
      "customized_payload": false,
      "custom_payload": null,
      "preferences": {},
      "active": true,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2026-09-07T07:31:30.066Z",
      "updated_at": "2026-09-07T07:31:30.066Z"
   }

Update
------

Required permission: ``admin.webhook``

``PUT``-Request sent: ``/api/v1/webhooks/{id}``

Same payload shape as Create above. Response is the updated record, same
shape as Show/Create with ``updated_at`` refreshed.
