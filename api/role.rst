Roles
=====

List
----

Required permission: ``admin.role``

``GET`` -Request sent: ``/api/v1/roles``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   [
      {
         "id": 1,
         "name": "Admin",
         "preferences": {},
         "default_at_signup": false,
         "active": true,
         "note": "To configure your system.",
         "updated_by_id": 3,
         "created_by_id": 1,
         "created_at": "2023-07-26T08:44:37.326Z",
         "updated_at": "2023-08-08T09:45:15.315Z",
         "permission_ids": [
            1,
            43,
            55,
            57,
            65
         ],
         "knowledge_base_permission_ids": [],
         "group_ids": {
            "1": [
               "full"
            ],
            "2": [
               "full"
            ],
            "3": [
               "full"
            ]
         }
      },
      {
         "id": 2,
         "name": "Agent",
         "preferences": {},
         "default_at_signup": false,
         "active": true,
         "note": "To work on Tickets!",
         "updated_by_id": 3,
         "created_by_id": 1,
         "created_at": "2023-07-26T08:44:37.362Z",
         "updated_at": "2023-08-22T11:07:16.532Z",
         "permission_ids": [
            43,
            57,
            60,
            62,
            66
         ],
         "knowledge_base_permission_ids": [],
         "group_ids": {
            "1": [
               "full"
            ],
            "2": [
               "full"
            ],
            "3": [
               "full"
            ]
         }
      },
      {
         "id": 3,
         "name": "Service",
         "preferences": {},
         "default_at_signup": false,
         "active": true,
         "note": "Changed text",
         "updated_by_id": 3,
         "created_by_id": 1,
         "created_at": "2023-07-26T08:44:37.379Z",
         "updated_at": "2023-08-22T11:36:49.504Z",
         "permission_ids": [
            57,
            58
         ],
         "knowledge_base_permission_ids": [],
         "group_ids": {
            "1": [
               "full"
            ],
            "2": [
               "full"
            ],
            "3": [
               "full"
            ]
         }
      }
   ]

Show
----

Required permission: ``admin.role``

``GET`` -Request sent: ``/api/v1/roles/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "id": 2,
      "name": "Agent",
      "preferences": {},
      "default_at_signup": false,
      "active": true,
      "note": "To work on Tickets.",
      "updated_by_id": 3,
      "created_by_id": 1,
      "created_at": "2023-07-26T08:44:37.362Z",
      "updated_at": "2023-08-08T09:59:48.202Z",
      "permission_ids": [
         43,
         57,
         60,
         62,
         66
      ],
      "knowledge_base_permission_ids": [],
      "group_ids": {
         "1": [
            "full"
         ],
         "2": [
            "full"
         ],
         "3": [
            "full"
         ]
      }
   }

Create
------

Required permission: ``admin.role``

``POST`` -Request sent: ``/api/v1/roles``

Request:

.. code-block:: json
   :force:

   {
      "active": true,
      "default_at_signup": false,
      "group_ids": {
         "1": "full",
         "2": "full",
         "3": "full"
      },
      "id": "c-12",
      "name": "VIP service",
      "note": "Handling of VIP customers!",
      "permission_ids": [
         "57",
         "58"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 4,
      "name": "VIP service",
      "preferences": {},
      "default_at_signup": false,
      "active": true,
      "note": "Handling of VIP customers!",
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2023-08-22T11:24:02.114Z",
      "updated_at": "2023-08-22T11:24:02.111Z",
      "permission_ids": [
         57,
         58
      ],
      "knowledge_base_permission_ids": [],
      "group_ids": {
         "1": [
            "full"
         ],
         "2": [
            "full"
         ],
         "3": [
            "full"
         ]
      }
   }

Update
------

Required permission: ``admin.role``

``PUT`` -Request sent: ``/api/v1/roles/{id}``

Request:

.. code-block:: json
   :force:

   {
      "active": true,
      "default_at_signup": false,
      "group_ids": {
         "1": "full",
         "2": "full",
         "3": "full"
      },
      "name": "Service",
      "note": "Changed text",
      "permission_ids": [
         "57",
         "58"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "updated_at": "2023-08-22T11:36:49.136Z",
      "name": "Service",
      "default_at_signup": false,
      "active": true,
      "note": "Changed text",
      "updated_by_id": 3,
      "id": 3,
      "preferences": {},
      "created_by_id": 1,
      "created_at": "2023-07-26T08:44:37.379Z",
      "permission_ids": [
         57,
         58
      ],
      "knowledge_base_permission_ids": [],
      "group_ids": {
         "1": [
            "full"
         ],
         "2": [
            "full"
         ],
         "3": [
            "full"
         ]
      }
   }
