Organization
************

List
====

Required permission:

* ticket.agent or admin.organization (can read all organizations)
* any (can only read it's own organization if exists)

Request::

 GET /api/v1/organizations

Response::

 Status: 200 Ok
 
 [
  {
    "id": 123,
    "name": "Org 1",
    "shared": true,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "name": "Org 2",
    "shared": false,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
 ]


Search
======

Required permission:

* ticket.agent or admin.organization (can read all organization)

Request::

 GET /api/v1/organizations/search?query=what&limit=10

Response::

 Status: 200 Ok
 
 [
  {
    "id": 123,
    "name": "Org 1",
    "shared": true,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "name": "Org 2",
    "shared": false,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
 ]



Show
====

Required permission:

* ticket.agent or admin.organization (can read all organizations)
* any (can only read it's own user if exists)

Request::

 GET /api/v1/organizations/{id}

Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }

Create
======

Required permission:

* admin.organization

Request::

 POST /api/v1/organizations
 
 {
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note"
 }

Response::

 Status: 201 Created
 
 {
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Update
======

Required permission:

* admin.organization

Request::

 PUT /api/v1/organizations/{id}
 
 {
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note"
 }

Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }

Delete
======

Required permission:

* admin.organization (only if no references in history tables and tickets exists)

Request::

 DELETE /api/v1/organization/{id}


Response::

 Status: 200 Ok
 
 {}

