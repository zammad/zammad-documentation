User
****

me - current user
=================

Required permission:

* any (only valid authentication)

Request::

 GET /api/v1/users/me


Response::

 Status: 200 Ok

 {
  "id": 123,
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 },


List
====

Required permission:

* ticket.agent or admin.user (can read all users)
* any (can only read its own user if exists)

Request::

 GET /api/v1/users

Response::

 Status: 200 Ok

 [
  {
    "id": 123,
    "firstname": "Bob",
    "lastname": "Smith",
    "email": "bob@smith.example.com",
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "firstname": "Martha",
    "lastname": "Braun",
    "email": "marta@braun.example.com",
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
 ]


Search
======

Required permission:

* ticket.agent or admin.user (can read all users)

Request::

 GET /api/v1/users/search?query=what&limit=10

Note: As of Zammad 2.6 parameters (sort_by=some_row and order_by=asc or desc) can also be used for sorting.

Response::

 Status: 200 Ok

 [
  {
    "id": 123,
    "firstname": "Bob",
    "lastname": "Smith",
    "email": "bob@smith.example.com",
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "firstname": "Martha",
    "lastname": "Braun",
    "email": "marta@braun.example.com",
    ...
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
 ]

Show
====

Required permission:

* ticket.agent or admin.user (can read all users)
* customer with same organization (can read all users of same organization)
* any (can only read it's own user if exists)

Request::

 GET /api/v1/users/{id}

Response::

 Status: 200 Ok

 {
  "id": 123,
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }

Create
======

Required permission:

* admin.user
* ticket.agent (can not set roles/role_ids and not set groups/group_ids - roles.default_at_signup roles will get assigned automatically)
* any - until user_create_account is disabled (can not set roles/role_ids and not set groups/group_ids - roles.default_at_signup roles will get assigned automatically)

Request::

 POST /api/v1/users

 {
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization": "Some Organization Name",
  ...
 }


Response::

 Status: 201 Created

 {
  "id": 123,
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization_id": 123,
  "organization": "Some Organization Name",
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }

Update
======

Required permission:

* admin.user
* ticket.agent (can only update customer accounts and not set roles/role_ids and not set groups/group_ids - already assigned attributes will not changed)

Request::

 PUT /api/v1/users/{id}

 {
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization": "Some Other Organization Name",
  ...
 }


Response::

 Status: 200 Ok

 {
  "id": 123,
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization_id": 124,
  "organization": "Some Other Organization Name",
  ...
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }

Delete
======

Required permission:

* admin.user (only if no references in history tables and tickets exist)

Request::

 DELETE /api/v1/users/{id}


Response::

 Status: 200 Ok

 {}

