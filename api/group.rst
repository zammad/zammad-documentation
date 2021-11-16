Group
*****

.. note:: **🤓 Confusing setting for endpoint**

   Please note that ``follow_up_possible`` may not work as expected.
   The possible values are ``yes`` or ``new_ticket``!

List
====

Required permission: ``admin.group``

``GET``-Request sent: ``/api/v1/groups``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 1,
         "signature_id": 1,
         "email_address_id": null,
         "name": "Sales",
         "assignment_timeout": null,
         "follow_up_possible": "yes",
         "follow_up_assignment": true,
         "active": true,
         "note": "Standard Group/Pool for Tickets.",
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:51:13.449Z",
         "updated_at": "2021-11-03T11:57:16.357Z",
         "user_ids": [
            3,
            4,
            5
         ]
      },
      {
         "id": 2,
         "signature_id": null,
         "email_address_id": null,
         "name": "2nd Level",
         "assignment_timeout": null,
         "follow_up_possible": "yes",
         "follow_up_assignment": true,
         "active": true,
         "note": null,
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.802Z",
         "updated_at": "2021-11-03T11:57:16.361Z",
         "user_ids": [
            3,
            4,
            5
         ]
      },
      {
         "id": 3,
         "signature_id": null,
         "email_address_id": null,
         "name": "Service Desk",
         "assignment_timeout": null,
         "follow_up_possible": "yes",
         "follow_up_assignment": true,
         "active": true,
         "note": null,
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.807Z",
         "updated_at": "2021-11-03T11:57:16.365Z",
         "user_ids": [
            3,
            4,
            5
         ]
      }
   ]


Show
====

Required permission: ``admin.group``

``GET``-Request sent: ``/api/v1/groups/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 2,
      "signature_id": null,
      "email_address_id": null,
      "name": "2nd Level",
      "assignment_timeout": null,
      "follow_up_possible": "yes",
      "follow_up_assignment": true,
      "active": true,
      "note": null,
      "updated_by_id": 1,
      "created_by_id": 1,
      "created_at": "2021-11-03T11:57:15.802Z",
      "updated_at": "2021-11-03T11:57:16.361Z",
      "user_ids": [
         3,
         4,
         5
      ]
   }

Create
======

Required permission: ``admin.group``

``POST``-Request sent: ``/api/v1/groups``

.. code-block:: json

   {
     "name": "Amazing Group",
     "signature_id": 1,
     "email_address_id": 1,
     "assignment_timeout": 180,
     "follow_up_possible": "new_ticket",
     "follow_up_assignment": false,
     "active": true,
     "note": "Look at my group, my group is amazing!"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 7,
      "signature_id": 1,
      "email_address_id": 3,
      "name": "Amazing Group",
      "assignment_timeout": 180,
      "follow_up_possible": "new_ticket",
      "follow_up_assignment": false,
      "active": true,
      "note": "Look at my group, my group is amazing!",
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T13:09:41.526Z",
      "updated_at": "2021-11-08T13:09:41.526Z",
      "user_ids": []
   }


Update
======

Required permission: ``admin.group``

``PUT``-Request sent: ``/api/v1/groups/{id}``

.. code-block:: json

   {
     "name": "Amazing Group",
     "signature_id": 1,
     "email_address_id": 3,
     "assignment_timeout": 0,
     "follow_up_possible": "new_ticket",
     "follow_up_assignment": true,
     "active": true,
     "note": "Look at my group, my group is amazing!"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 7,
      "signature_id": 1,
      "email_address_id": 3,
      "name": "Amazing Group",
      "assignment_timeout": 0,
      "follow_up_possible": "new_ticket",
      "follow_up_assignment": true,
      "active": true,
      "note": "Look at my group, my group is amazing!",
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T13:09:41.526Z",
      "updated_at": "2021-11-08T13:36:24.571Z",
      "user_ids": []
   }


Delete
======

Required permission: ``admin.group``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing groups cannot be undone.

   Removing organizations with references in e.g. activity streams or tickets
   is not possible via API - this will be indicated by
   ``"error": "Can't delete, object has references."``. This is *not* a bug.

   Consider setting affected groups to inactive instead or ensure to move all
   existing tickets to new groups.

``DELETE``-Request sent: ``/api/v1/groups/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
