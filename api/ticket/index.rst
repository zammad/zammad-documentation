Tickets
*******

   .. warning::

      Ticket endpoints depend on on group permissions if the user you're 
      using is an agent. Because of this tickets may or may not be available.

List
====

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets``

Response:

.. code-block:: json
   
   # HTTP-Code 200 Ok
   [
      {
         "id": 123,
         "title": "Help me!",
         "group_id": 1,
         "state_id": 1,
         "priority_id": 2,
         "customer_id": 2,
         "note": "some note",
         "updated_at": "2016-08-16T07:55:42.119Z",
         "created_at": "2016-08-16T07:55:42.119Z",
         ...
      },
      {
         "id": 124,
         "title": "Just want to ask for support",
         "state_id": 2,
         "priority_id": 2,
         "customer_id": 2,
         "note": "some note",
         "updated_at": "2016-08-16T07:55:42.119Z",
         "created_at": "2016-08-16T07:55:42.119Z",
         ...
      },
   ]

Search
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets/search?query={search-term}&limit=10``

.. 
   TODO: Introduce sort-area to reference to

.. note:: **Sorting ↕**

   As of Zammad 2.6 parameters (sort_by=some_row and order_by=asc or desc) 
   can also be used.

Response:

.. code-block:: json

   # HTTP-Code 200 Ok
   [
      {
         "id": 123,
         "title": "Help me!",
         "group_id": 1,
         "state_id": 1,
         "priority_id": 2,
         "customer_id": 2,
         "note": "some note",
         "updated_at": "2016-08-16T07:55:42.119Z",
         "created_at": "2016-08-16T07:55:42.119Z",
         ...
      },
      {
         "id": 124,
         "title": "Just want to ask for support",
         "state_id": 2,
         "priority_id": 2,
         "customer_id": 2,
         "note": "some note",
         "updated_at": "2016-08-16T07:55:42.119Z",
         "created_at": "2016-08-16T07:55:42.119Z",
         ...
      },
   ]


Show
====

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets/{ticket-id}``

Response:

.. code-block:: json

   # HTTP-Code 200 Ok
   {
      "id": 123,
      "title": "Help me!",
      "group_id": 1,
      "state_id": 1,
      "priority_id": 2,
      "customer_id": 2,
      "note": "some note",
      "updated_at": "2016-08-16T07:55:42.119Z",
      "created_at": "2016-08-16T07:55:42.119Z",
      ...
   }

Create
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

   .. tip:: 

      **🐱‍👤 On behalf of users**

      If you want to create tickets on behalf other users, use 
      the ``customer_id`` attribute. ``ticket.agent`` is mandatory for this. 
      Use ``guess:{email-address}`` to save an API call if you don't know the 
      users ID or want to create the user in question.

      **📣 Add mention subscription right away**

      Add the ``mentions`` attribute to your ticket payload and provide 
      an array of user ids to directly subscribe them during ticket creation. 

      *E.g.:* ``"mentions": [1, 5, 7, 8],``

``POST``-Request sent: ``/api/v1/tickets``

   {
      "title": "Help me!",
      "group": "Users",
      "customer": "email_of_existing_customer@example.com",
      "article": {
         "subject": "some subject",
         "body": "some message",
         "type": "note",
         "internal": false
      },
      "note": "some note",
      ...
   }

Response:

.. code-block:: json

   # HTTP-Code 201 Created
   {
      "id": 123,
      "title": "Help me!",
      "group_id": 1,
      "state_id": 1,
      "priority_id": 2,
      "customer_id": 2,
      ...
      "note": "some note",
      "updated_at": "2016-08-16T07:55:42.119Z",
      "created_at": "2016-08-16T07:55:42.119Z"
   }

For more article attributes have a look into :doc:`articles`.

If you want to include attachments of the first article, the payload looks like:

``POST``-Request sent: ``/api/v1/tickets``

.. code-block:: json

   {
      "title": "Help me!",
      "group": "Users",
      "article": {
         "subject": "some subject",
         "body": "some message",
         "attachments": [
            {
               "filename": "some_file1.txt",
               "data": "content in base64",
               "mime-type": "text/plain"
            },
            {
               "filename": "some_file2.txt",
               "data": "content in base64",
               "mime-type": "text/plain"
            }
         ]
      },
      "note": "some note",
      ...
   }

Zammad supports inline images in article bodies, use data URIs in your HTML 
markup like so:

``POST``-Request sent: ``/api/v1/tickets``

.. code-block:: json

   {
      "title": "Help me!",
      "group": "Users",
      "article": {
         "content_type": "text/html",
         "subject": "some subject",
         "body": "<b>some</b> message witn inline image <img src=\"data:image/jpeg;base64,ABCDEFG==\">"
      },
      "note": "some note",
      ...
   }

Update
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``PUT``-Request sent: ``/api/v1/tickets/{ticket-id}``

   {
      "id": 123,
      "title": "Help me!",
      "group": "Users",
      "state": "open",
      "priority": "3 high",
      "article": {
         "subject": "some subject of update",
         "body": "some message of update"
      },
      ...
   }

Response:

.. code-block:: json

   # HTTP-Code 200 Ok
   {
      "id": 123,
      "title": "Help me!",
      "group_id": 1,
      "state_id": 1,
      "priority_id": 2,
      ...
      "note": "some note",
      "updated_at": "2016-08-16T07:55:42.119Z",
      "created_at": "2016-08-16T07:55:42.119Z"
   }

.. tip:: **Adding attachments**

   Attachment payloads are identical to the ``POST`` method, just use ``PUT`` 
   instead if you.

Delete
======

.. 

   TODO: Needs verification

Required permission: ``admin``

``DELETE``-Request sent: ``/api/v1/tickets/{ticket-id}``

Response:

.. code-block:: json

   # HTTP-Code 200 Ok
   {}
