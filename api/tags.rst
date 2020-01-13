Tags
****

List
====

Required permission:

* ticket.agent or admin.tag

Request::

 GET /api/v1/tags?object=Ticket&o_id=10

Response::

 Status: 200 Ok

 {
     "tags": [
         "tag 1",
         "tag 2",
         "tag 3"
     ]
 }


Search
======

Required permission:

* ticket.agent or admin.tag

Request::

 GET /api/v1/tag_search?term=tag

Response::

 Status: 200 Ok

 [
     {
         "id": 7,
         "value": "tag 1"
     },
     {
         "id": 8,
         "value": "tag 2"
     },
     {
         "id": 9,
         "value": "tag 3"
     }
 ]

Add
===

Required permission:

* ticket.agent or admin.tag

Request::

 GET /api/v1/tags/add?object=Ticket&o_id=10&item=tag+4

Response::

 Status: 200 Ok

 true

Remove
======

Required permission:

* ticket.agent or admin.tag

Request::

 GET /api/v1/tags/remove?object=Ticket&o_id=10&item=tag+4

Response::

 Status: 200 Ok

 true

Admin - List
============

Required permission:

* admin.tag

Request::

 GET /api/v1/tag_list

Response::

 Status: 200 Ok

 [
     {
         "id": 7,
         "name": "tag 1",
         "count": 1
     },
     {
         "id": 8,
         "name": "tag 2",
         "count": 1
     },
     {
         "id": 9,
         "name": "tag 3",
         "count": 1
     },
     {
         "id": 11,
         "name": "tag 4",
         "count": 0
     },
     {
         "id": 6,
         "name": "test",
         "count": 0
     }
 ]

Admin - Create
==============

Required permission:

* admin.tag

Request::

 POST /api/v1/tag_list

 {
   name: "tag 5"
 }

Response::

 Status: 200 Ok

 {}

Admin - Rename
==============

Required permission:

* admin.tag

Request::

 PUT /api/v1/tag_list/{id}

 {
   id: 6,
   name: "tag 5"
 }

Response::

 Status: 200 Ok

 {}

Admin - Delete
==============

Required permission:

* admin.tag

Request::

 DELETE /api/v1/tag_list/{id}

Response::

 Status: 200 Ok

 {}
