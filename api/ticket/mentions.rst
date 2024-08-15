Mentions
========

.. warning::

    The mention endpoint depends on the group permissions and if the user you're
    using is an **agent**. Because of this tickets may or may not be available.

List
----

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/mentions``

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
     mentions: [
       {
         "id":2,
         "mentionable_type":"Ticket",
         "mentionable_id":1,
         "user_id":3,
         "updated_by_id":3,
         "created_by_id":3,
         "created_at":"2021-03-16T08:51:08.985Z",
         "updated_at":"2021-03-16T08:51:08.985Z"
       },
       {
         "id":3,
         "mentionable_type":"Ticket",
         "mentionable_id":1,
         "user_id":4,
         "updated_by_id":4,
         "created_by_id":4,
         "created_at":"2021-03-16T08:51:08.986Z",
         "updated_at":"2021-03-16T08:51:08.986Z"
       },
     ]
   }

Create
------

Required permission: ``ticket.agent``

``POST``-Request sent: ``/api/v1/mentions``

.. code-block:: json

   {
     "mentionable_type": "Ticket",
     "mentionable_id": 12,
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
     "id":2,
     "mentionable_type":"Ticket",
     "mentionable_id":1,
     "user_id":3,
     "updated_by_id":3,
     "created_by_id":3,
     "created_at":"2021-03-16T08:51:08.985Z",
     "updated_at":"2021-03-16T08:51:08.985Z"
   }

The mention will be created for the user of the current session.

Delete
------

Required permission: ``ticket.agent``

``DELETE``-Request sent: ``/api/v1/mentions/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
     "id":2,
     "mentionable_type":"Ticket",
     "mentionable_id":1,
     "user_id":3,
     "updated_by_id":3,
     "created_by_id":3,
     "created_at":"2021-03-16T08:51:08.985Z",
     "updated_at":"2021-03-16T08:51:08.985Z"
   }
