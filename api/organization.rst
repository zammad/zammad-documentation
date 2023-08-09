Organization
************

List
====

Required permission: ``ticket.agent`` **or** ``admin.organization``

   .. note:: 

      Technically, customers can only see their own organization
      if applicable.

``GET``-Request sent: ``/api/v1/organizations``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
	   {
	      "id": 1,
	      "name": "Zammad Foundation",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "",
	      "updated_by_id": 1,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:39.608Z",
	      "updated_at": "2023-08-04T12:02:00.018Z",
	      "vip": false,
	      "member_ids": [
	         2
	      ],
	      "secondary_member_ids": []
	   },
	   {
	      "name": "Chrispresso Inc.",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "Manufacturer of individual coffee products.",
	      "vip": false,
	      "updated_by_id": 3,
	      "id": 2,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:48.617Z",
	      "updated_at": "2023-08-04T12:01:44.370Z",
	      "member_ids": [
	         3,
	         5,
	         4
	      ],
	      "secondary_member_ids": []
	   },
	   {
	      "name": "Awesome Customer Inc.",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "Global distributor of communication and security products, electrical and electronic wire &amp; cable.",
	      "vip": true,
	      "updated_by_id": 3,
	      "id": 3,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:48.632Z",
	      "updated_at": "2023-08-04T12:54:30.974Z",
	      "member_ids": [
	         8,
	         7,
	         6
	      ],
	      "secondary_member_ids": []
	   },
	   {
	      "id": 4,
	      "name": "Good Customer Inc.",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "Search the world's information, including webpages, images, videos and more. Good Customer has many special features to help you find exactly what you're looking for.",
	      "updated_by_id": 1,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:48.645Z",
	      "updated_at": "2023-07-26T08:44:48.645Z",
	      "member_ids": [
	      	9
	      ],
	      "secondary_member_ids": []
	   }
   ]

Search
======

Required permission: ``ticket.agent`` **or** ``admin.organization``

``GET``-Request sent:
``/api/v1/organizations/search?query=inc&limit=10``

.. include:: /api/includes/sort_and_order.rst

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
	   {
	      "name": "Awesome Customer Inc.",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "Global distributor of communication and security products, electrical and electronic wire &amp; cable.",
	      "vip": true,
	      "updated_by_id": 3,
	      "id": 3,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:48.632Z",
	      "updated_at": "2023-08-04T12:54:30.974Z",
	      "member_ids": [
	         8,
	         7,
	         6
	      ],
	      "secondary_member_ids": []
	   },
	   {
	      "name": "Chrispresso Inc.",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "Manufacturer of individual coffee products.",
	      "vip": false,
	      "updated_by_id": 3,
	      "id": 2,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:48.617Z",
	      "updated_at": "2023-08-04T12:01:44.370Z",
	      "member_ids": [
	         3,
	         5,
	         4
	      ],
	      "secondary_member_ids": []
	   },
	   {
	      "id": 4,
	      "name": "Good Customer Inc.",
	      "shared": true,
	      "domain": "",
	      "domain_assignment": false,
	      "active": true,
	      "note": "Search the world's information, including webpages, images, videos and more. Good Customer has many special features to help you find exactly what you're looking for.",
	      "updated_by_id": 1,
	      "created_by_id": 1,
	      "created_at": "2023-07-26T08:44:48.645Z",
	      "updated_at": "2023-07-26T08:44:48.645Z",
	      "member_ids": [
	         9
	      ],
	      "secondary_member_ids": []
	   }
   ]

Show
====

Required permission: ``ticket.agent`` **or** ``admin.organization``

   .. note:: 

      Technically any users in question can only see their own organization.

``GET``-Request sent: ``/api/v1/organizations/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 2,
         "name": "Chrispresso Inc.",
         "shared": true,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "Manufacturer of individual coffee products.",
         "vip": false,
         "updated_by_id": 3,
         "created_by_id": 1,
         "created_at": "2023-07-26T08:44:48.617Z",
         "updated_at": "2023-08-04T12:01:44.370Z",
         "member_ids": [
            3,
            5,
            4
	      ],
	      "secondary_member_ids": []
      }
   ]

Create
======

Required permission: ``admin.organization``

``POST``-Request sent: ``/api/v1/organizations``

.. code-block:: json

   [
      {
         "name": "Sample Corp.",
         "shared": false,
         "domain": "example.com",
         "domain_assignment": true,
         "active": true,
         "vip": true,
         "note": "Just a sample, aint that nice?",
         "members": [
            "olivia@example.com",
            "david@example.com"
         ]
      }
   ]

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   [
      {
	      "id": 5,
	      "name": "Sample Corp.",
	      "shared": false,
	      "domain": "example.com",
	      "domain_assignment": true,
	      "active": true,
	      "note": "Just a sample, aint that nice?",
	      "updated_by_id": 3,
	      "created_by_id": 3,
	      "created_at": "2023-08-08T09:12:42.023Z",
	      "updated_at": "2023-08-08T09:12:42.602Z",
	      "vip": true,
	      "member_ids": [
	         10,
	         11
	      ],
	      "secondary_member_ids": []
      }
   ]

Update
======

Required permission: ``admin.organization``

``PUT``-Request sent: ``/api/v1/organizations/{id}``

.. code-block:: json

   [  
      {
         "name": "Sample Corp.",
         "shared": false,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "This was a triumph - I'm making a note here - H-U-G-E success!",
         "members": [
            "olivia@example.com",
            "david@example.com"
         ]
      }
   ]

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [   
      {
         "id": 5,
         "name": "Sample Corp.",
         "shared": false,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "This was a triumph - I'm making a note here - H-U-G-E success!",
         "updated_by_id": 3,
         "created_by_id": 3,
         "created_at": "2023-08-08T09:12:42.023Z",
         "updated_at": "2023-08-08T09:16:58.922Z",
         "vip": true,
         "member_ids": [
            10,
            11
         ],
         "secondary_member_ids": []
      }
   ]

Delete
======

Required permission: ``admin.organization``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing organizations cannot be undone.

   Removing organizations with references in e.g. activity streams or users
   is not possible via API - this will be indicated by
   ``"error": "Can't delete, object has references."``. This is *not* a bug.

   Consider using `Data Privacy`_ via UI for more control instead.

.. _Data Privacy:
   https://admin-docs.zammad.org/en/latest/system/data-privacy.html

``DELETE``-Request sent: ``/api/v1/organizations/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
