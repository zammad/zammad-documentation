Checklists
==========

.. note:: To add checklist items, use the
   :doc:`checklist items endpoint <checklist-items>`.

Show
----

Required permission: ``ticket.agent``

``GET``-Request sent: ``/api/v1/checklists/{checklist id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "name": "Return order",
      "sorted_item_ids": [
         "18",
         "19",
         "20",
         "21"
      ],
      "updated_by_id": 3,
      "created_by_id": 3,
      "ticket_id": 4,
      "id": 6,
      "created_at": "2024-10-15T08:47:50.860Z",
      "updated_at": "2024-10-15T08:50:52.698Z",
      "item_ids": [
         18,
         19,
         20,
         21
      ]
   }

Show By Ticket
--------------

Required permission: ``ticket.agent``

``GET``-Request sent: ``/api/v1/checklists/by_ticket/{ticket id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "id": 6,
      "assets": {
         "Checklist": {
            "6": {
               "name": "Return order",
               "sorted_item_ids": [
                  "18",
                  "19",
                  "20",
                  "21"
               ],
               "updated_by_id": 3,
               "created_by_id": 3,
               "ticket_id": 4,
               "id": 6,
               "created_at": "2024-10-15T08:47:50.860Z",
               "updated_at": "2024-10-15T08:50:52.698Z",
               "item_ids": [
                  18,
                  19,
                  20,
                  21
               ]
            }
         },
         "ChecklistItem": {
            "18": {
               "text": "Prepare shipment",
               "checked": false,
               "updated_by_id": 3,
               "ticket_id": null,
               "created_by_id": 3,
               "checklist_id": 6,
               "id": 18,
               "created_at": "2024-10-15T08:47:51.036Z",
               "updated_at": "2024-10-15T08:47:59.717Z"
            },
            "19": {
               "text": "Inform customer",
               "checked": false,
               "updated_by_id": 3,
               "ticket_id": null,
               "created_by_id": 3,
               "checklist_id": 6,
               "id": 19,
               "created_at": "2024-10-15T08:48:02.042Z",
               "updated_at": "2024-10-15T08:48:12.726Z"
            },
            "20": {
               "text": "Hand over the goods to the shipping company",
               "checked": false,
               "updated_by_id": 3,
               "ticket_id": null,
               "created_by_id": 3,
               "checklist_id": 6,
               "id": 20,
               "created_at": "2024-10-15T08:48:14.216Z",
               "updated_at": "2024-10-15T08:49:10.467Z"
            },
            "21": {
               "text": "Check whether return has arrived",
               "checked": false,
               "updated_by_id": 3,
               "ticket_id": null,
               "created_by_id": 3,
               "checklist_id": 6,
               "id": 21,
               "created_at": "2024-10-15T08:49:12.388Z",
               "updated_at": "2024-10-15T08:49:40.746Z"
            }
         }
      }
   }


Create
------

Required permission: ``ticket.agent``

``POST``-Request sent: ``/api/v1/checklists``

Request:

.. code-block:: json
   :force:

   {
      "name": "My new checklist",
      "ticket_id": 7
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "id": 12,
      "assets": {
         "Checklist": {
            "12": {
               "id": 12,
               "name": "",
               "sorted_item_ids": [
                  "32"
               ],
               "created_by_id": 3,
               "updated_by_id": 3,
               "ticket_id": 7,
               "created_at": "2024-10-16T06:57:51.474Z",
               "updated_at": "2024-10-16T06:57:51.512Z",
               "item_ids": [
                  32
               ]
            }
         },
         "ChecklistItem": {
            "32": {
               "id": 32,
               "text": "",
               "checked": false,
               "checklist_id": 12,
               "created_by_id": 3,
               "updated_by_id": 3,
               "created_at": "2024-10-16T06:57:51.505Z",
               "updated_at": "2024-10-16T06:57:51.505Z",
               "ticket_id": null
            }
         }
      }
   }

Update
------

Required permission: ``ticket.agent``

``PATCH``-Request sent: ``/api/v1/checklists/{checklist id}``

Request:

.. code-block:: json
   :force:

   {
      "name": "New checklist name",
      "sorted_item_ids": [
         "34",
         "33",
         "32"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "name": "New checklist name",
      "sorted_item_ids": [
         "34",
         "33",
         "32"
      ],
      "updated_by_id": 3,
      "created_by_id": 3,
      "ticket_id": 7,
      "id": 12,
      "created_at": "2024-10-16T06:57:51.474Z",
      "updated_at": "2024-10-16T07:49:06.923Z",
      "item_ids": [
         32,
         33,
         34
      ]
   }

Delete
------

Required permission: ``ticket.agent``

``DELETE``-Request sent: ``/api/v1/checklists/{checklist id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK