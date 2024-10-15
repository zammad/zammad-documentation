Checklist Templates
===================

Show
----

Required permission: ``admin.checklists`` or ``ticket.agent``

``GET``-Request sent: ``/api/v1/checklist_templates/{checklist template id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
        "name": "Return order",
        "active": true,
        "updated_by_id": 3,
        "created_by_id": 3,
        "id": 28,
        "sorted_item_ids": [
            "18",
            "19",
            "20",
            "21"
        ],
        "created_at": "2024-10-15T12:43:14.642Z",
        "updated_at": "2024-10-15T12:43:34.242Z",
        "item_ids": [
            18,
            19,
            20,
            21
        ]
    }

Create
------

Required permission: ``admin.checklists``

``POST``-Request sent: ``/api/v1/checklist_templates``

Request:

.. code-block:: json
   :force:

   {
      "name": "My checklist template",
      "active": true,
      "items": [
         "Item 1",
         "Item 2",
         "Item 3"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "id": 30,
      "name": "Test API II",
      "active": true,
      "sorted_item_ids": [
         "22",
         "23",
         "24"
      ],
      "created_by_id": 3,
      "updated_by_id": 3,
      "created_at": "2024-10-15T12:46:31.927Z",
      "updated_at": "2024-10-15T12:46:31.982Z",
      "item_ids": [
         22,
         23,
         24
      ]
   }


Update
------

Required permission: ``admin.checklists``

``PATCH``-Request sent: ``/api/v1/checklist_templates/{checklist template id}``

Request:

.. code-block:: json
   :force:

   {
      "name": "My changed checklist template name",
      "active": true,
      "items": [
         "Item 7",
         "Item 8",
         "Item 9"
         ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "name": "My changed checklist template name",
      "active": true,
      "updated_by_id": 3,
      "created_by_id": 3,
      "id": 30,
      "sorted_item_ids": [
         "25",
         "26",
         "27"
      ],
      "created_at": "2024-10-15T12:46:31.927Z",
      "updated_at": "2024-10-15T12:51:22.245Z",
      "item_ids": [
         25,
         26,
         27
      ]
   }

Delete
------

Required permission: ``admin.checklists``

``DELETE``-Request sent: ``/api/v1/checklist_templates/{checklist template id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK