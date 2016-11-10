Group
*****

List
====

Required permission:

* admin.group (can read all groups)

Request::

 GET /api/v1/groups

Response::

 Status: 200 Ok
 
 [
   {
     "id": 123,
     "name": "Group 1",
     "signature_id": 123,
     "email_address_id": 123,
     "assignment_timeout": 180,
     "follow_up_possible": "yes",
     "follow_up_assignment": true,
     "active": true,
     "note": "some note",
     "updated_at": "2016-08-16T07:55:42.119Z",
     "created_at": "2016-08-16T07:55:42.119Z"
   },
   {
     "id": 124,
     "name": "Group 2",
     "signature_id": 123,
     "email_address_id": 123,
     "assignment_timeout": 180,
     "follow_up_possible": "no",
     "follow_up_assignment": false,
     "active": true,
     "note": "some note",
     "updated_at": "2016-08-16T07:55:42.119Z",
     "created_at": "2016-08-16T07:55:42.119Z"
   },
 ]



Show
====

Required permission:

* admin.group (can read all groups)

Request::

 GET /api/v1/groups/{id}


Response::

 Status: 200 Ok
 
 {
  "id": 123,
  "name": "Group 1",
  "signature_id": 123,
  "email_address_id": 123,
  "assignment_timeout": 180,
  "follow_up_possible": "yes",
  "follow_up_assignment": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }

Create
======

Required permission:

* admin.group

Request::

 POST /api/v1/groups


 {
  "name": "Group 1",
  "signature_id": 123,
  "email_address_id": 123,
  "assignment_timeout": 180,
  "follow_up_possible": "yes",
  "follow_up_assignment": true,
  "active": true,
  "note": "some note"
 }



Response::

 Status: 201 Created

 {
  "id": 123,
  "name": "Group 1",
  "signature_id": 123,
  "email_address_id": 123,
  "assignment_timeout": 180,
  "follow_up_possible": "yes",
  "follow_up_assignment": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Update
======

Required permission:

* admin.group

Request::

 PUT /api/v1/groups/{id}

 {
  "id": 123,
  "name": "Group 1",
  "signature_id": 123,
  "email_address_id": 123,
  "assignment_timeout": 180,
  "follow_up_possible": "yes",
  "follow_up_assignment": true,
  "active": true,
  "note": "some note"
 }


Response::

 Status: 200 Ok

 {
  "id": 123,
  "name": "Group 1",
  "signature_id": 123,
  "email_address_id": 123,
  "assignment_timeout": 180,
  "follow_up_possible": "yes",
  "follow_up_assignment": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Delete
======

Required permission:

* admin.group (only if no references in history tables and tickets exists)

Request::

 DELETE /api/v1/groups/{id}


Response::

 Status: 200 Ok

 {}
