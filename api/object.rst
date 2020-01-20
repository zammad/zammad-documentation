Object
******

List
====

Required permission:

* admin (access to admin interface)

Request::

   GET /api/v1/object_manager_attributes

Response::

   Status: 200 Ok

   [
     {
       "id":49,
       "name":"anrede",
       "display":"Anrede",
       "data_type":"select",
       "data_option":{
         "options":{
           "Mr":"Mr",
           "Ms":"Ms",
           "Company":"Company"
         },
         "default":"Mr",
         "null":true,
         "maxlength":255,
         "nulloption":true
       },
       "data_option_new":{

       },
       "editable":true,
       "active":true,
       "screens":{
         "create":{
           "Customer":{
             "shown":true,
             "required":true
           }
         },
         "edit":{
           "Customer":{
             "shown":true
           },
           "Agent":{
             "shown":true
           }
         },
         "create_middle":{
           "Agent":{
             "shown":true
           }
         }
       },
       "to_create":false,
       "to_migrate":false,
       "to_delete":false,
       "to_config":false,
       "position":1550,
       "created_by_id":3,
       "updated_by_id":3,
       "created_at":"2017-01-13T16:19:23.116Z",
       "updated_at":"2017-01-17T11:16:13.298Z",
       "object":"Ticket"
     },
     ...
   ]

Show
====

Required permission:

* admin (access to admin interface)

Request::

   GET /api/v1/object_manager_attributes/:id

Response::

   Status: 200 Ok

   {
     "id":49,
     "name":"anrede",
     "display":"Anrede",
     "data_type":"select",
     "data_option":{
       "options":{
         "Mr":"Mr",
         "Ms":"Ms",
         "Company":"Company"
       },
       "default":"Mr",
       "null":true,
       "maxlength":255,
       "nulloption":true
     },
     "data_option_new":{

     },
     "editable":true,
     "active":true,
     "screens":{
       "create":{
         "Customer":{
           "shown":true,
           "required":true
         }
       },
       "edit":{
         "Customer":{
           "shown":true
         },
         "Agent":{
           "shown":true
         }
       },
       "create_middle":{
         "Agent":{
           "shown":true
         }
       }
     },
     "to_create":false,
     "to_migrate":false,
     "to_delete":false,
     "to_config":false,
     "position":1550,
     "created_by_id":3,
     "updated_by_id":3,
     "created_at":"2017-01-13T16:19:23.116Z",
     "updated_at":"2017-01-17T11:16:13.298Z",
     "object":"Ticket"
   }

Create
======

Required permission:

* admin (access to admin interface)

Request::

   POST /api/v1/object_manager_attributes

Response::

   Status: 200 Ok

   {
     "name":"product",
     "object":"Ticket",
     "display":"Produkt",
     "active":true,
     "data_type":"select",
     "data_option":{
       "options":{
         "wert1":"anzeige1",
         "wert2":"anzeige12"
       }
     },
     "screens":{
       "create_middle":{
         "Customer":{
           "shown":true,
           "item_class":"column"
         },
         "Agent":{
           "shown":true,
           "item_class":"column"
         }
       },
       "edit":{
         "Customer":{
           "shown":true
         },
         "Agent":{
           "shown":true
         }
       }
     }
   }

Update
======

Required permission:

* admin (access to admin interface)

Request::

   PUT /api/v1/object_manager_attributes/:id

Response::

   Status: 200 Ok

   {
     "id":49,
     "name":"anrede",
     "display":"Anrede",
     "data_type":"select",
     "data_option":{
       "options":{
         "Mr":"Mr",
         "Ms":"Ms",
         "Company":"Company"
       },
       "default":"Mr",
       "null":true,
       "maxlength":255,
       "nulloption":true
     },
     "data_option_new":{

     },
     "editable":true,
     "active":true,
     "screens":{
       "create":{
         "Customer":{
           "shown":true,
           "required":true
         }
       },
       "edit":{
         "Customer":{
           "shown":true
         },
         "Agent":{
           "shown":true
         }
       },
       "create_middle":{
         "Agent":{
           "shown":true
         }
       }
     },
     "to_create":false,
     "to_migrate":false,
     "to_delete":false,
     "to_config":false,
     "position":1550,
     "created_by_id":3,
     "updated_by_id":3,
     "created_at":"2017-01-13T16:19:23.116Z",
     "updated_at":"2017-01-17T11:16:13.298Z",
     "object":"Ticket"
   }

Execute Database Migrations
===========================

Required permission:

* admin (access to admin interface)

Request::

   POST /api/v1/object_manager_attributes_execute_migrations

Response::

   Status: 200 Ok

   {}
