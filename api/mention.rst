Mention
******

List
====

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

   GET /api/v1/mentions

Response::

   Status: 200 Ok

   {
     mentions: [
       {
         "id":2,
         "mentionable_type":"Ticket",
         "mentionable_id":1,
         "user_id":3,
         "updated_by_id":3,
         "created_by_id":3,
         "created_at":"2021-03-16T08:51:08.985Z",
         "updated_at":"2021-03-16T08:51:08.985Z"
       },
       {
         "id":3,
         "mentionable_type":"Ticket",
         "mentionable_id":1,
         "user_id":4,
         "updated_by_id":4,
         "created_by_id":4,
         "created_at":"2021-03-16T08:51:08.986Z",
         "updated_at":"2021-03-16T08:51:08.986Z"
       },
     ]
   }

Create
======

Required permission:

* ticket.agent (create in all allocated groups)

Request::

   POST /api/v1/mentions

   {
     "mentionable_type": "Ticket",
     "mentionable_id": 12,
   }

Response::

   Status: 201 Created

   {
     "id":2,
     "mentionable_type":"Ticket",
     "mentionable_id":1,
     "user_id":3,
     "updated_by_id":3,
     "created_by_id":3,
     "created_at":"2021-03-16T08:51:08.985Z",
     "updated_at":"2021-03-16T08:51:08.985Z"
   }

The mention will be created for the user of the current session.

Delete
======

Required permission:

* ticket.agent (access to all ticket in allocated groups)

Request::

   DELETE /api/v1/mentions/{id}

Response::

   Status: 200 Ok

   {
     "id":2,
     "mentionable_type":"Ticket",
     "mentionable_id":1,
     "user_id":3,
     "updated_by_id":3,
     "created_by_id":3,
     "created_at":"2021-03-16T08:51:08.985Z",
     "updated_at":"2021-03-16T08:51:08.985Z"
   }
