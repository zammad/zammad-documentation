Audit Log
=========

The audit log records security-relevant changes to your Zammad system:
who changed what, and when. The audit log is read-only.

List
----

Required permission: ``admin.audit_log``

``GET``-Request sent: ``/api/v1/audit_logs``

The endpoint supports pagination. The default page size is ``500``.
Entries are returned ordered by ``id`` (ascending). Pass ``?sort_by=id``
and ``?order_by=DESC`` to return the newest entries first.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
     {
       "id": 1,
       "user_id": 3,
       "user_fullname": "Christopher Miller",
       "action_type": "create",
       "auditable_type": "ChecklistTemplate",
       "auditable_id": 1,
       "auditable_name": "Onboarding",
       "value_from": {},
       "value_to": {
         "name": "Onboarding",
         "active": true,
         "sorted_item_names": [
           "Buy chair",
           "Coffee briefing",
           "Create accounts"
         ]
       },
       "source_ip": "172.19.0.1",
       "preferences": {},
       "created_at": "2026-07-23T09:14:51.650Z",
       "updated_at": "2026-07-23T09:14:51.650Z"
     },
     {
       "id": 2,
       "user_id": 3,
       "user_fullname": "Christopher Miller",
       "action_type": "update",
       "auditable_type": "Setting",
       "auditable_id": 280,
       "auditable_name": "ai_provider",
       "value_from": {
         "area": "AI::Provider",
         "name": "ai_provider",
         "title": "AI provider",
         "options": {},
         "frontend": true,
         "description": "Defines if the AI provider is configured.",
         "state_current": {
           "value": true
         },
         "state_initial": {
           "value": false
         }
       },
       "value_to": {
         "area": "AI::Provider",
         "name": "ai_provider",
         "title": "AI provider",
         "options": {},
         "frontend": true,
         "description": "Defines if the AI provider is configured.",
         "state_current": {
           "value": false
         },
         "state_initial": {
           "value": false
         }
       },
       "source_ip": "172.19.0.1",
       "preferences": {
         "changed_attributes": [
           "state_current"
         ]
       },
       "created_at": "2026-07-23T09:14:59.501Z",
       "updated_at": "2026-07-23T09:14:59.501Z"
     },
     {
       "id": 3,
       "user_id": 3,
       "user_fullname": "Christopher Miller",
       "action_type": "update",
       "auditable_type": "Role",
       "auditable_id": 2,
       "auditable_name": "Agent",
       "value_from": {},
       "value_to": {
         "permissions": [
           "admin.text_module"
         ],
         "group_permissions": {
           "2nd Level": [
             "full"
           ],
           "Service Desk": [
             "full"
           ]
         }
       },
       "source_ip": "172.19.0.1",
       "preferences": {},
       "created_at": "2026-07-23T09:16:30.188Z",
       "updated_at": "2026-07-23T09:16:30.188Z"
     },
     {
       "id": 4,
       "user_id": 3,
       "user_fullname": "Christopher Miller",
       "action_type": "update",
       "auditable_type": "Setting",
       "auditable_id": 265,
       "auditable_name": "pgp_integration",
       "value_from": {
         "area": "Integration::Switch",
         "name": "pgp_integration",
         "title": "PGP integration",
         "options": {
           "form": [
             {
               "tag": "boolean",
               "name": "pgp_integration",
               "null": true,
               "display": "",
               "options": {
                 "true": "yes",
                 "false": "no"
               }
             }
           ]
         },
         "frontend": true,
         "description": "Defines if PGP encryption is enabled or not.",
         "state_current": {
           "value": false
         },
         "state_initial": {
           "value": false
         }
       },
       "value_to": {
         "area": "Integration::Switch",
         "name": "pgp_integration",
         "title": "PGP integration",
         "options": {
           "form": [
             {
               "tag": "boolean",
               "name": "pgp_integration",
               "null": true,
               "display": "",
               "options": {
                 "true": "yes",
                 "false": "no"
               }
             }
           ]
         },
         "frontend": true,
         "description": "Defines if PGP encryption is enabled or not.",
         "state_current": {
           "value": true
         },
         "state_initial": {
           "value": false
         }
       },
       "source_ip": "172.19.0.1",
       "preferences": {
         "changed_attributes": [
           "state_current"
         ]
       },
       "created_at": "2026-07-23T09:17:20.469Z",
       "updated_at": "2026-07-23T09:17:20.469Z"
     }
   ]


Show
----

Required permission: ``admin.audit_log``

``GET``-Request sent: ``/api/v1/audit_logs/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
       "id": 3,
       "user_id": 3,
       "user_fullname": "Christopher Miller",
       "action_type": "update",
       "auditable_type": "Role",
       "auditable_id": 2,
       "auditable_name": "Agent",
       "value_from": {},
       "value_to": {
         "permissions": [
           "admin.text_module"
         ],
         "group_permissions": {
           "2nd Level": [
             "full"
           ],
           "Service Desk": [
             "full"
           ]
         }
       },
       "source_ip": "172.19.0.1",
       "preferences": {},
       "created_at": "2026-07-23T09:16:30.188Z",
       "updated_at": "2026-07-23T09:16:30.188Z"
   }

Search
------

Required permission: ``admin.audit_log``

The search endpoint accepts the Zammad search-backend ``query``
syntax. The simplest case is a literal substring on a single
indexed field such as ``auditable_name``, ``auditable_type`` or
``user_fullname``:

``GET``-Request sent: ``/api/v1/audit_logs/search?query={search-string}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
     {
       "id": 3,
       "user_id": 3,
       "user_fullname": "Christopher Miller",
       "action_type": "update",
       "auditable_type": "Role",
       "auditable_id": 2,
       "auditable_name": "Agent",
       "value_from": {},
       "value_to": {
         "permissions": [
           "admin.text_module"
         ],
         "group_permissions": {
           "2nd Level": [
             "full"
           ],
           "Service Desk": [
             "full"
           ]
         }
       },
       "source_ip": "172.19.0.1",
       "preferences": {},
       "created_at": "2026-07-23T09:16:30.188Z",
       "updated_at": "2026-07-23T09:16:30.188Z"
     }
   ]

To filter on a specific attribute rather than substring-match the
whole record, prefix the attribute name. You can even use the logical ``AND``
connector to narrow down the results:

``GET``-Request sent:
``/api/v1/audit_logs/search?query=auditable_type:Setting AND user_id:3``

.. note::

   Search matches are case-sensitive and search only the indexed
   attribute fields (``auditable_name``, ``auditable_type``,
   ``user_fullname`` and so on). The ``value_from`` and ``value_to``
   payloads are not searchable.

.. note::

   By default the response is a bare JSON array of matching entries.
   Pass ``with_total_count=true`` on the URL (or ``with_total_count:
   true`` in the body of a ``POST`` request) to wrap the response in
   an object that also contains the ``total_count``. Send a ``POST``
   request when the query is too long or complex for a URL.

Field Reference
---------------

``id``
   Integer primary key of the audit log entry.

``user_id``
   ID of the user that triggered the change. ``null`` when the entry
   was written by a background job without a current user.

``user_fullname``
   Full name of the user at the time the entry was written. Stored
   separately so it remains readable after the user account is
   removed. When the action was performed via ``View from user's
   perspective``, the format is ``Original User -> Acting User``.

``action_type``
   Type of the recorded change. One of:

   - ``create`` - a record was added.
   - ``update`` - an existing record was modified.
   - ``destroy`` - a record was removed.
   - ``switch_to`` - a user took over another user's session via
     ``View from user's perspective``
   - ``switch_back_to`` - the original session was resumed.

``auditable_id``
   ID of the record that was changed.

``auditable_type``
   Class name of the record that was changed (e.g. ``Role``,
   ``User``, ``Setting``, ``KnowledgeBase``, ``ChecklistTemplate``).

``auditable_name``
   Display name of the changed record at the time the entry was
   written. Stored separately so it remains readable after the record
   itself is gone.

``value_from``
   Object (JSON) holding the previous state of the audited
   attributes. Empty (``{}``) on ``create`` entries.

``value_to``
   Object (JSON) holding the new state of the audited attributes.
   Empty (``{}``) on ``destroy`` entries.

``source_ip``
   IP address that issued the underlying request. ``Rails console``
   or ``Rails runner`` is stored when the entry was written from a
   maintenance script.

``preferences``
   Object (JSON) holding additional per-entry metadata. For
   ``update`` entries this contains a ``changed_attributes`` array
   listing the attributes that actually changed. For entries created
   while a user session was taken over via ``View from user's
   perspective``, this also contains ``switched_from_user_id`` and
   ``switched_from_user_fullname`` identifying the original user.

``created_at``
   Timestamp at which the entry was written. Audit log entries are
   append-only.

``updated_at``
   Same as ``created_at`` for audit log entries. Audit log entries
   are append-only.

Lifecycle
---------

A scheduled task removes entries older than ``12 months`` every day.
Use the ``AuditLog.cleanup`` in the Rails console to trigger a cleanup manually.
