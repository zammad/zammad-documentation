Sla
*****

List
====

Required permission:

* admin.sla (can read all slas)

Request::

   GET /api/v1/slas

Response::

   Status: 200 Ok

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

Required permission:

* admin.sla (can read all slas)

Request::

   GET /api/v1/slas/{id}

Response::

   Status: 200 Ok

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

Required permission:

* admin.sla

Request::

   POST /api/v1/slas


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

Response::

   Status: 201 Created

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

Required permission:

* admin.sla

Request::

   PUT /api/v1/slas/{id}

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

Response::

   Status: 200 Ok

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

Required permission:

* admin.sla

Request::

   DELETE /api/v1/slas/{id}

Response::

   Status: 200 Ok

   {}
