Ticket State
************

List
====

Required permission:

* admin.object (can read all ticket states)
* ticket.agent (can read all ticket states)
* ticket.customer (can read all ticket states)

Request::

 GET /api/v1/ticket_states

Response::

 Status: 200 Ok
 
 [
  {
    "id": 123,
    "name": "Ticket State 1",
    "state_type_id": 1,
    "next_state_id": null,
    "ignore_escalation": true,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "name": "Ticket State 2",
    "state_type_id": 2,
    "next_state_id": 4,
    "ignore_escalation": false,
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

 GET /api/v1/ticket_states/{id}


Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "name": "Ticket State 1",
  "state_type_id": 1,
  "next_state_id": null,
  "ignore_escalation": true,
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

 POST /api/v1/ticket_states
 
 {
  "name": "Ticket State 1",
  "state_type_id": 1,
  "next_state_id": null,
  "ignore_escalation": true,
  "active": true,
  "note": "some note"
 }
 

Response::

 Status: 201 Created
 
 {
  "id": 123,
  "name": "Ticket State 1",
  "state_type_id": 1,
  "next_state_id": null,
  "ignore_escalation": true,
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

 PUT /api/v1/ticket_states/{id}
 
 {
  "id": 123,
  "name": "Ticket State 1",
  "state_type_id": 1,
  "next_state_id": null,
  "ignore_escalation": true,
  "active": true,
  "note": "some note"
 }

Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "name": "Ticket State 1",
  "state_type_id": 1,
  "next_state_id": null,
  "ignore_escalation": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Delete
======

Required permission:

* admin.object (only if no references in history tables and tickets exists)

Request::

 DELETE /api/v1/ticket_states/{id}


Response::

 Status: 200 Ok
 
 {}
