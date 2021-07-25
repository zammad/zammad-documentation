Priorities
**********

List
====

Required permission:
``admin.object`` **or** ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_priorities``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
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
``admin.object`` **or** ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_priorities/{id}``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
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

Required permission: ``admin.object``

``POST``-Request sent: ``/api/v1/ticket_priorities``

.. code-block:: json
   
   {
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note"
   }

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 201 Created
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

Required permission: ``admin.object``

``PUT``-Request sent: ``/api/v1/ticket_priorities/{id}``

.. code-block:: json
   
   {
     "id": 123,
     "name": "Ticket Priority 1",
     "active": true,
     "note": "some note"
   }

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
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

Required permission: ``admin.object``

``DELETE``-Request sent: ``/api/v1/ticket_priorities/{id}``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
   {}
