Organization
************

List
====

Required permission: ``ticket.agent`` **or** ``admin.organization``

   .. note:: 

      Technically any, customers can only see their own organization
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
         "created_at": "2021-11-03T11:51:13.683Z",
         "updated_at": "2021-11-03T11:51:13.822Z",
         "member_ids": [
            2
         ]
      },
      {
         "id": 2,
         "name": "Chrispresso Inc.",
         "shared": true,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "Manufacturer of individual coffee products.",
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.817Z",
         "updated_at": "2021-11-03T11:57:15.817Z",
         "member_ids": [
            5,
            4,
            3
         ]
      },
      {
         "id": 3,
         "name": "Awesome Customer Inc.",
         "shared": true,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "Global distributor of communication and security products, electrical and electronic wire &amp; cable.",
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.825Z",
         "updated_at": "2021-11-03T11:57:15.825Z",
         "member_ids": [
            8,
            7,
            6
         ]
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
         "created_at": "2021-11-03T11:57:15.839Z",
         "updated_at": "2021-11-03T11:57:15.839Z",
         "member_ids": [
            9
         ]
      },
      {
         "id": 5,
         "name": "Test",
         "shared": true,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "",
         "updated_by_id": 3,
         "created_by_id": 3,
         "created_at": "2021-11-03T14:42:28.555Z",
         "updated_at": "2021-11-03T15:04:03.149Z",
         "member_ids": []
      }
   ]

Search
======

Required permission: ``ticket.agent`` **or** ``admin.organization``

``GET``-Request sent:
``/api/v1/organizations/search?query=inc&limit=10``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
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
         "created_at": "2021-11-03T11:57:15.839Z",
         "updated_at": "2021-11-03T11:57:15.839Z",
         "member_ids": [
            9
         ]
      },
      {
         "id": 3,
         "name": "Awesome Customer Inc.",
         "shared": true,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "Global distributor of communication and security products, electrical and electronic wire &amp; cable.",
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.825Z",
         "updated_at": "2021-11-03T11:57:15.825Z",
         "member_ids": [
            8,
            7,
            6
         ]
      },
      {
         "id": 2,
         "name": "Chrispresso Inc.",
         "shared": true,
         "domain": "",
         "domain_assignment": false,
         "active": true,
         "note": "Manufacturer of individual coffee products.",
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.817Z",
         "updated_at": "2021-11-03T11:57:15.817Z",
         "member_ids": [
            5,
            4,
            3
         ]
      }
   ]

Show
====

Required permission: ``ticket.agent`` **or** ``admin.organization``

   .. note:: 

      Technically any - users in question can only see their own organization.

``GET``-Request sent: ``/api/v1/organizations/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 2,
      "name": "Chrispresso Inc.",
      "shared": true,
      "domain": "",
      "domain_assignment": false,
      "active": true,
      "note": "Manufacturer of individual coffee products.",
      "updated_by_id": 1,
      "created_by_id": 1,
      "created_at": "2021-11-03T11:57:15.817Z",
      "updated_at": "2021-11-03T11:57:15.817Z",
      "member_ids": [
         5,
         4,
         3
      ]
   }

Create
======

Required permission: ``admin.organization``

``POST``-Request sent: ``/api/v1/organizations``

.. code-block:: json

   {
      "name": "Sample Corp.",
      "shared": false,
      "domain": "example.com",
      "domain_assignment": true,
      "active": true,
      "note": "Just a sample, aint that nice?",
      "members": [
         "olivia@example.com",
         "jdoe",
         "david@example.com"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 6,
      "name": "Sample Corp.",
      "shared": false,
      "domain": "example.com",
      "domain_assignment": true,
      "active": true,
      "note": "Just a sample, aint that nice?",
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-03T17:38:39.527Z",
      "updated_at": "2021-11-03T17:38:39.768Z",
      "member_ids": [
         10,
         16,
         11
      ]
   }

Update
======

Required permission: ``admin.organization``

``PUT``-Request sent: ``/api/v1/organizations/{id}``

.. code-block:: json

   {
      "name": "Sample Corp.",
      "shared": false,
      "domain": "",
      "domain_assignment": false,
      "active": true,
      "note": "This was a triump - I'm making a note here - H-U-G-E success!",
      "members": [
         "olivia@example.com",
         "david@example.com"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 6,
      "name": "Sample Corp.",
      "shared": false,
      "domain": "",
      "domain_assignment": false,
      "active": true,
      "note": "This was a triump - I'm making a note here - H-U-G-E success!",
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-03T17:38:39.527Z",
      "updated_at": "2021-11-03T17:40:59.740Z",
      "member_ids": [
         11,
         10
      ]
   }

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

``DELETE``-Request sent: ``/api/v1/organization/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
