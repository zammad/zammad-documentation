Service-Level Agreements (SLA)
******************************

.. note::

   🤓 SLAs depend on Zammads :doc:`Calendars </api/calendar>`.

List
====

Required permission: ``admin.sla``

``GET``-Request sent: ``/api/v1/slas``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id":2,
         "calendar_id":1,
         "name":"new sla",
         "first_response_time":120,
         "response_time":null,
         "update_time":120,
         "solution_time":120,
         "condition":{
            "ticket.state_id":{
               "operator":"is",
               "value":"2"
            }
         },
         "updated_by_id":3,
         "created_by_id":3,
         "created_at":"2021-11-10T12:54:39.368Z",
         "updated_at":"2021-11-10T12:54:39.368Z"
      }
   ]


Show
====

Required permission: ``admin.sla``

``GET``-Request sent: ``/api/v1/slas/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id":2,
      "calendar_id":1,
      "name":"new sla",
      "first_response_time":120,
      "response_time":null,
      "update_time":120,
      "solution_time":120,
      "condition":{
         "ticket.state_id":{
            "operator":"is",
            "value":"2"
         }
      },
      "updated_by_id":3,
      "created_by_id":3,
      "created_at":"2021-11-10T12:54:39.368Z",
      "updated_at":"2021-11-10T12:54:39.368Z"
   }

Create
======

Required permission: ``admin.sla``

``POST``-Request sent: ``/api/v1/slas``

.. code-block:: json

   {
      "name":"new sla",
      "first_response_time":"120",
      "response_time":"",
      "update_time":"120",
      "solution_time":"120",
      "condition":{
         "ticket.state_id":{
            "operator":"is",
            "value":"2"
         }
      },
      "calendar_id":"1",
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id":2,
      "calendar_id":1,
      "name":"new sla",
      "first_response_time":120,
      "response_time":null,
      "update_time":120,
      "solution_time":120,
      "condition":{
         "ticket.state_id":{
            "operator":"is",
            "value":"2"
         }
      },
      "updated_by_id":3,
      "created_by_id":3,
      "created_at":"2021-11-10T12:54:39.368Z",
      "updated_at":"2021-11-10T12:54:39.368Z"
   }


Update
======

Required permission: ``admin.sla``

``PUT``-Request sent: ``/api/v1/slas/{id}``

.. code-block:: json

   {
      "name":"update sla",
      "first_response_time":"120",
      "response_time":"",
      "update_time":"120",
      "solution_time":"120",
      "condition":{
         "ticket.state_id":{
            "operator":"is",
            "value":"2"
         }
      },
      "calendar_id":"1",
      "id":2
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id":2,
      "calendar_id":1,
      "name":"update sla",
      "first_response_time":120,
      "response_time":null,
      "update_time":120,
      "solution_time":120,
      "condition":{
         "ticket.state_id":{
            "operator":"is",
            "value":"2"
         }
      },
      "updated_by_id":3,
      "created_by_id":3,
      "created_at":"2021-11-10T12:54:39.368Z",
      "updated_at":"2021-11-10T13:02:52.053Z"
   }


Delete
======

Required permission: ``admin.sla``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing SLA configurations cannot be undone.

``DELETE``-Request sent: ``/api/v1/slas/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
