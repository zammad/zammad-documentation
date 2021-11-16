Priorities
**********

List
====

Required permission:
``admin.object`` **or** ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_priorities``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
   
   [
      {
         "id": 1,
         "name": "1 low",
         "default_create": false,
         "ui_icon": "low-priority",
         "ui_color": "low-priority",
         "note": null,
         "active": true,
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:51:13.559Z",
         "updated_at": "2021-11-03T11:51:13.572Z"
      },
      {
         "id": 2,
         "name": "2 normal",
         "default_create": true,
         "ui_icon": null,
         "ui_color": null,
         "note": null,
         "active": true,
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:51:13.570Z",
         "updated_at": "2021-11-03T11:51:13.570Z"
      },
      {
         "id": 3,
         "name": "3 high",
         "default_create": false,
         "ui_icon": "important",
         "ui_color": "high-priority",
         "note": null,
         "active": true,
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:51:13.579Z",
         "updated_at": "2021-11-03T11:51:13.579Z"
      }
   ]


Show
====

Required permission:
``admin.object`` **or** ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_priorities/{id}``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
   
   {
      "id": 3,
      "name": "3 high",
      "default_create": false,
      "ui_icon": "important",
      "ui_color": "high-priority",
      "note": null,
      "active": true,
      "updated_by_id": 1,
      "created_by_id": 1,
      "created_at": "2021-11-03T11:51:13.579Z",
      "updated_at": "2021-11-03T11:51:13.579Z"
   }


Create
======

Required permission: ``admin.object``

``POST``-Request sent: ``/api/v1/ticket_priorities``

.. code-block:: json
   
   {
      "name": "4 disaster",
      "default_create": false,
      "ui_icon": "important",
      "ui_color": "high-priority",
      "note": "Added via API for disasterious situations."
   }

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 201 Created
   
   {
      "id": 4,
      "name": "4 disaster",
      "default_create": false,
      "ui_icon": "important",
      "ui_color": "high-priority",
      "note": "Added via API for disasterious situations.",
      "active": true,
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T15:31:57.704Z",
      "updated_at": "2021-11-08T15:31:57.704Z"
   }

Update
======

Required permission: ``admin.object``

``PUT``-Request sent: ``/api/v1/ticket_priorities/{id}``

.. code-block:: json
   
   {
      "ui_icon": "",
      "ui_color": "",
      "note": "Adjusted via API - not so important"
   }

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
   
   {
      "id": 3,
      "ui_icon": "",
      "ui_color": "",
      "note": "Adjusted via API - not so important",
      "updated_by_id": 3,
      "name": "3 high",
      "default_create": false,
      "active": true,
      "created_by_id": 1,
      "created_at": "2021-11-03T11:51:13.579Z",
      "updated_at": "2021-11-08T15:33:12.181Z"
   }


Delete
======

Required permission: ``admin.object``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing priorities cannot be undone.

   Removing ticket priorities with references in tickets is not possible via
   API - this will be indicated by
   ``"error": "Can't delete, object has references."``. This is *not* a bug.

   Consider either setting said priority to ``active: false`` or adjust all
   tickets with the to remove priority to another priority.

``DELETE``-Request sent: ``/api/v1/ticket_priorities/{id}``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
   
   {}
