Online Notification
*******************

List
====

Required permission:

* authenticated user (content of notitifcations depends on user permissions)

Request::

   GET /api/v1/online_notifications

Response::

   Status: 200 Ok

   [
     {
       "id": 123,
       "o_id": 628,
       "object": "Ticket",
       "type": "escalation",
       "seen": true,
       "updated_at": "2016-08-16T07:55:42.119Z",
       "updated_by_id": 123,
       "created_at": "2016-08-16T07:55:42.119Z",
       "created_at_id": 123
     },
     {
       "id": 124,
       "o_id": 629,
       "object": "Ticket",
       "type": "update",
       "seen": false,
       "updated_at": "2016-08-16T07:55:47.119Z",
       "updated_by_id": 123,
       "created_at": "2016-08-16T07:55:47.119Z",
       "created_at_id": 123
     },
     {
       "id": 125,
       "o_id": 630,
       "object": "Ticket",
       "type": "create",
       "seen": false,
       "updated_at": "2016-08-16T07:57:49.119Z",
       "updated_by_id": 123,
       "created_at": "2016-08-16T07:57:49.119Z",
       "created_at_id": 123
     },
   ]


Show
====

Required permission:

* authenticated user (content of notifications depends on user permissions)

Request::

   GET /api/v1/online_notifications/{id}

Response::

   Status: 200 Ok

   {
     "id": 123,
     "o_id": 628,
     "object": "Ticket",
     "type": "escalation",
     "seen": true,
     "updated_at": "2016-08-16T07:55:42.119Z",
     "updated_by_id": 123,
     "created_at": "2016-08-16T07:55:42.119Z",
     "created_at_id": 123
   }

Update
======

Required permission:

* admin.object

Request::

   PUT /api/v1/online_notifications/{id}

   {
     "seen": true,
   }

Response::

   Status: 200 Ok

   {
     "id": 123,
     "o_id": 628,
     "object": "Ticket",
     "type": "escalation",
     "seen": true,
     "updated_at": "2016-08-16T07:55:42.119Z",
     "updated_by_id": 123,
     "created_at": "2016-08-16T07:55:42.119Z",
     "created_at_id": 123
   }


Delete
======

Required permission:

* authenticated user (content of notifications depends on user permissions)

Request::

   DELETE /api/v1/online_notifications/{id}

Response::

   Status: 200 Ok

   {}

Mark all as read
================

Required permission:

* authenticated user (content of notifications depends on user permissions)

Request::

   POST /api/v1/online_notifications/mark_all_as_read

Response::

   Status: 200 Ok

   {}
