Tags
====

Ticket Scope
------------

List
^^^^

Required permission: ``ticket.agent`` **or** ``admin.tag``

``GET``-Request sent: ``/api/v1/tags?object=Ticket&o_id={ticket id}``

Sample response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
       "tags": [
           "americano",
           "complaint"
       ]
   }

Add
^^^

Required permission: ``ticket.agent`` **or** ``admin.tag``

``POST``-Request sent: ``/api/v1/tags/add``

.. code-block:: json
   :force:

   {
       "item": "{tag name}",
       "object": "Ticket",
       "o_id": {ticket id}
   }

.. hint::

   This will create the tag if it doesn't exist and
   the user has permission to do so.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   true

Remove
^^^^^^

Required permission: ``ticket.agent`` **or** ``admin.tag``

``DELETE``-Request sent: ``/api/v1/tags/remove``

.. code-block:: json

   {
       "item": "{tag name}",
       "object": "Ticket",
       "o_id": "{ticket id}"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   true

Administration Scope
--------------------

Admin - List
^^^^^^^^^^^^

Required permission: ``admin.tag``

``GET``-Request sent: ``/api/v1/tag_list``

Sample response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   [
       {
           "id": 1,
           "name": "americano",
           "count": 0
       },
       {
           "id": 2,
           "name": "complaint",
           "count": 0
       },
       {
           "id": 3,
           "name": "viennese melange",
           "count": 0
       }
   ]

Admin - Create
^^^^^^^^^^^^^^

Required permission: ``admin.tag``

``POST``-Request sent: ``/api/v1/tag_list``

.. code-block:: json

   {
     "name": "tag 5"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {}

Admin - Rename
^^^^^^^^^^^^^^

Required permission: ``admin.tag``

``PUT``-Request sent: ``/api/v1/tag_list/{tag id}``

.. code-block:: json

   {
     "name": "order"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {}

Admin - Delete
^^^^^^^^^^^^^^

Required permission: ``admin.tag``

``DELETE``-Request sent: ``/api/v1/tag_list/{tag id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {}
