Checklists
==========

.. note:: To create a checklist, you can add checklist items via
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



Update
------

Delete
------

Required permission: ``ticket.agent``

``DELETE``-Request sent: ``/api/v1/checklists/{checklist id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK