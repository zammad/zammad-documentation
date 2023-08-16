Timeaccounting
**************

List
====

Required permission: ``ticket.agent`` **or** ``admin.time_accounting``

``GET``-Request sent: ``/api/v1/tickets/{ticket id}/time_accountings``

Sample response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   [
      {
         "id": 6,
         "ticket_id": 50,
         "ticket_article_id": 87,
         "time_unit": "15.0",
         "type_id": 3,
         "created_by_id": 3,
         "created_at": "2023-08-16T08:11:49.315Z",
         "updated_at": "2023-08-16T08:11:49.315Z"
      },
      {
         "id": 7,
         "ticket_id": 50,
         "ticket_article_id": 88,
         "time_unit": "30.0",
         "type_id": 2,
         "created_by_id": 3,
         "created_at": "2023-08-16T08:12:02.249Z",
         "updated_at": "2023-08-16T08:12:02.249Z"
      },
      {
         "id": 8,
         "ticket_id": 50,
         "ticket_article_id": 89,
         "time_unit": "35.0",
         "type_id": 4,
         "created_by_id": 3,
         "created_at": "2023-08-16T08:12:29.910Z",
         "updated_at": "2023-08-16T08:12:29.910Z"
      }
   ]


Show
====

Required permission: ``ticket.agent`` **or** ``admin.time_accounting``

``GET``-Request sent: ``/api/v1/tickets/{ticket id}/time_accountings/{timeaccounting id}``

Sample response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "id": 7,
      "ticket_id": 50,
      "ticket_article_id": 88,
      "time_unit": "30.0",
      "type_id": 2,
      "created_by_id": 3,
      "created_at": "2023-08-16T08:12:02.249Z",
      "updated_at": "2023-08-16T08:12:02.249Z"
   }

Create
======

Required permission: ``ticket.agent`` **or** ``admin.time_accounting``

``POST``-Request sent: ``/api/v1/tickets/{ticket id}/time_accountings``

.. code-block:: json
   :force:

   {
      "time_unit": "60.0",
      "type_id": 4
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 9,
      "ticket_id": 50,
      "ticket_article_id": null,
      "time_unit": "60.0",
      "type_id": 4,
      "created_by_id": 3,
      "created_at": "2023-08-16T08:30:36.138Z",
      "updated_at": "2023-08-16T08:30:36.138Z"
   }

Update
======

Required permission: ``admin.time_accounting``

``PUT``-Request sent: ``/api/v1/tickets/{ticket id}/time_accounting/{timeaccounting id}``


.. code-block:: json
   :force:

   {
      "id": 7,
      "time_unit": "15.0",
      "type_id": 4
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "ticket_id": 50,
      "time_unit": "15.0",
      "type_id": 4,
      "id": 7,
      "ticket_article_id": 88,
      "created_by_id": 3,
      "created_at": "2023-08-16T08:12:02.249Z",
      "updated_at": "2023-08-16T08:24:00.788Z"
   }

Remove
======

Required permission: ``admin.time_accounting``

``DELETE``-Request sent: ``/api/v1/tickets/{ticket id}/time_accountings/{timeaccounting id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK
