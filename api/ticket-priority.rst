Ticket Priority
***************

List
====

Required permission:

* admin.object (can read all ticket states)
* ticket.agent (can read all ticket states)
* ticket.customer (can read all ticket states)

Request::

   GET /api/v1/ticket_priorities

Response::

   Status: 200 Ok

   [
     {
       "id": 123,
       "name": "Ticket Priority 1",
       "active": true,
       "note": "some note",
       "updated_at": "2016-08-16T07:55:42.119Z",
       "created_at": "2016-08-16T07:55:42.119Z"
     },
     {
       "id": 124,
       "name": "Ticket Priority 2",
       "active": true,
       "note": "some note",
       "updated_at": "2016-08-16T07:55:42.119Z",
       "created_at": "2016-08-16T07:55:42.119Z"
     },
   ]


Show
====

Required permission:

* admin.object (can read all ticket states)
* ticket.agent (can read all ticket states)
* ticket.customer (can read all ticket states)

Request::

   GET /api/v1/ticket_priorities/{id}

Response::

   Status: 200 Ok

   {
     "id": 123,
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note",
     "updated_at": "2016-08-16T07:55:42.119Z",
     "created_at": "2016-08-16T07:55:42.119Z"
   }


Create
======

Required permission:

* admin.object

Request::

   POST /api/v1/ticket_priorities

   {
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note"
   }

Response::

   Status: 201 Created

   {
     "id": 123,
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note",
     "updated_at": "2016-08-16T07:55:42.119Z",
     "created_at": "2016-08-16T07:55:42.119Z"
   }

Update
======

Required permission:

* admin.object

Request::

   PUT /api/v1/ticket_priorities/{id}

   {
     "id": 123,
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note"
   }

Response::

   Status: 200 Ok

   {
     "id": 123,
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note",
     "updated_at": "2016-08-16T07:55:42.119Z",
     "created_at": "2016-08-16T07:55:42.119Z"
   }


Delete
======

Required permission:

* admin.object (only if no references in history tables and tickets exist)

Request::

   DELETE /api/v1/ticket_priorities/{id}

Response::

   Status: 200 Ok

   {}
