Checklist Items
===============

Show
----

Required permission: ``ticket.agent``

``GET``-Request sent: ``/api/v1/checklist_items/{checklist item id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "text": "Hand over the goods to the shipping company",
      "checked": false,
      "updated_by_id": 3,
      "ticket_id": null,
      "created_by_id": 3,
      "checklist_id": 6,
      "id": 20,
      "created_at": "2024-10-15T08:48:14.216Z",
      "updated_at": "2024-10-15T08:49:10.467Z"
   }

Create
------


Update
------

Required permission: ``ticket.agent``

``PATCH``-Request sent: ``/api/v1/checklist_items/{checklist item id}``

Request:

.. code-block:: json
   :force:

   {
      "text": "Changed checklist item text",
      "checked": true
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "text": "Changed checklist item text",
      "checked": true,
      "updated_by_id": 3,
      "ticket_id": null,
      "created_by_id": 3,
      "checklist_id": 6,
      "id": 20,
      "created_at": "2024-10-15T08:48:14.216Z",
      "updated_at": "2024-10-15T12:19:35.235Z"
   }

Delete
------

Required permission: ``ticket.agent``

``DELETE``-Request sent: ``/api/v1/checklist_items/{checklist item id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK