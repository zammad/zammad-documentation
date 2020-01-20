User Access Token
*****************

List
====

Required permission:

* user_preferences.access_token

Request::

   GET /api/v1/user_access_token

Response::

   Status: 200 Ok

   {
     "tokens": [
       {
         "id": 1,
         "label": "some user access token",
         "preferences": {
           "permission": ["cti.agent","ticket.agent"]
         },
         "last_used_at": null,
         "expires_at": null,
         "created_at": "2018-07-11T08:18:56.947Z"
       },
       {
         "id": 2,
         "label": "some user access token 2",
         "preferences": {
           "permission": ["ticket.agent"]
         },
         "last_used_at": null,
         "expires_at": null,
         "created_at": "2018-07-11T08:18:56.947Z"
       }
     ],
     "permissions": [
       {
         id: 1,
         name: "admin",
         note: "Admin Interface",
         preferences: {},
         active: true,
         ...
       },
       {
         id: 2,
         name: "admin.user",
         note: "Manage Users",
         preferences: {},
         active: true,
         ...
       },
       ...
     ]
   }

Create
======

Required permission:

* user_preferences.access_token

Request::

   POST /api/v1/user_access_token

   {
     "label": "some test",
     "permission": ["cti.agent","ticket.agent"],
     "expires_at": null
   }

Response::

   Status: 200 Ok

   {
     "name": "new_token_only_shown_once"
   }

Delete
======

Required permission:

* user_preferences.access_token

Request::

   PUT /api/v1/user_access_token/:id

Response::

   Status: 200 Ok

   {}
