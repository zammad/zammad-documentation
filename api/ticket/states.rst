States
******

   .. warning::

      Creating, changing or removing states via below endpoints require further
      steps via console. See :doc:`/admin/console/working-on-tickets`

List
====

Required permission:
``admin.object`` **or** ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: /api/v1/ticket_states

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
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
``admin.object`` **or** ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_states/{id}``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
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

Required permission: ``admin.object``

``POST``-Request sent: ``/api/v1/ticket_states``

.. code-block:: json

   {
     "name": "Ticket State 1",
     "state_type_id": 1,
     "next_state_id": null,
     "ignore_escalation": true,
     "active": true,
     "note": "some note"
   }


Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 201 Created
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

Required permission: ``admin.object``

``PUT``-Request sent: ``/api/v1/ticket_states/{id}``

.. code-block:: json
   
   {
     "id": 123,
     "name": "Ticket State 1",
     "state_type_id": 1,
     "next_state_id": null,
     "ignore_escalation": true,
     "active": true,
     "note": "some note"
   }

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
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

Required permission: ``admin.object``

``DELETE``-Request sent: ``/api/v1/ticket_states/{id}``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok
   {}
