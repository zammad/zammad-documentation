Ticket
******

List
====

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 GET /api/v1/tickets

Response::

 Status: 200 Ok

 [
  {
    "id": 123,
    "title": "Help me!",
    "state_id": 1,
    "priority_id": 2,
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "title": "Just want to ask for support",
    "state_id": 2,
    "priority_id": 2,
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
 ]

Search
======

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 GET /api/v1/tickets/search?query=what&limit=10

Response::

 Status: 200 Ok
 
 [
  {
    "id": 123,
    "title": "Help me!",
    "state_id": 1,
    "priority_id": 2,
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "title": "Just want to ask for support",
    "state_id": 2,
    "priority_id": 2,
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
 ]


Show
====

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 GET /api/v1/tickets/{id}


Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "title": "Help me!",
  "state_id": 1,
  "priority_id": 2,
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Create
======

Required permission:

* ticket.agent (create in all allocated groups)
* ticket.customer

Request::

 POST /api/v1/tickets
 
 {
  "title": "Help me!",
  "state_id": 1,
  "priority_id": 2,
  "article": {
    "subject": "some subject",
    "body": "some message"
  },
  ...
  "note": "some note",
 }

Response::

 Status: 201 Created
 
 {
  "id": 123,
  "title": "Help me!",
  "state_id": 1,
  "priority_id": 2,
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Update
======

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 PUT /api/v1/tickets/{id}
 
 {
  "id": 123,
  "title": "Help me!",
  "state_id": 1,
  "priority_id": 2,
  "article": {
    "subject": "some subject of update",
    "body": "some message of update"
  },
  ...
 }


Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "title": "Help me!",
  "state_id": 1,
  "priority_id": 2,
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Delete
======

Required permission:

* admin

Request::

 DELETE /api/v1/tickets/{id}

Response::

 Status: 200 Ok
 
 {}
