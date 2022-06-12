roles
====

.. note:: **🤓 To see or not to see**

   Please note that below samples were provided with ``admin`` and
   ``ticket.agent`` permissions. Some attributes / information may not be
   available in specific situations.

   Please see our `Permission Guide`_ to get better insights.

.. _Permission Guide:
   https://admin-docs.zammad.org/en/latest/manage/roles/index.html#reference-guide-permissions


roles
======

Required permission: ``ticket.agent`` **or** ``admin.user``

**All roles**

``GET`` -Request sent: ``https://endpointdocu.zammad.com/api/v1/roles/?full=true&_={userid}``

Response: 

.. code-block:: json 

	# HTTP-Code 200 OK

	{
	{"record_ids":[1,2,3,4],
	"assets":{"Role":{"1":{"id":1,
	"name":"Admin",
	"default_at_signup":false,
	"active":true,
	"note":"To configure your system.",
	"updated_by_id":3,"preferences":{},
	"created_by_id":1,
	"created_at":"2022-05-18T17:40:55.190Z",
	"updated_at":"2022-05-19T00:26:27.303Z",
	"permission_ids":[1,41,61,51],
	"knowledge_base_permission_ids":[],
	"group_ids":{}},
	"2":{"id":2,
	"name":"Agent",
	"preferences":{},
	"default_at_signup":false,
	"active":true,
	"note":"To work on Tickets.",
	"updated_by_id":1,
	"created_by_id":1,
	"created_at":"2022-05-18T17:40:55.212Z",
	"updated_at":"2022-05-18T17:40:55.212Z",
	"permission_ids":[41,53,56,58,62],
	"knowledge_base_permission_ids":[],
	"group_ids":{}},
	"3":{"id":3,
	"name":"Customer",
	"preferences":{},
	"default_at_signup":true,
	"active":true,
	"note":"People who create Tickets ask for help.",
	"updated_by_id":1,"created_by_id":1,
	"created_at":"2022-05-18T17:40:55.219Z",
	"updated_at":"2022-05-18T17:40:55.219Z",
	"permission_ids":[42,45,46,48,54],
	"knowledge_base_permission_ids":[],
	"group_ids":{}},
	"4":{"id":4,"name":"Mathew",
	"preferences":{},
	"default_at_signup":false,
	"active":true,
	"note":"New User",
	"updated_by_id":3,
	"created_by_id":3,
	"created_at":"2022-05-19T01:02:58.007Z",
	"updated_at":"2022-05-19T01:02:58.007Z",
	"permission_ids":[1],
	"knowledge_base_permission_ids":[],
	"group_ids":{}}},
	"User":{"1":{"id":1,
	"organization_id":null,
	"login":"-",
	"firstname":"-",
	"lastname":"",
	"email":"",
	"image":null,
	"image_source":null,
	"web":"",
	"phone":"",
	"fax":"",
	"mobile":"",
	"department":"",
	"street":"",
	"zip":"",
	"city":"",
	"country":"",
	"address":"",
	"vip":false,
	"verified":false,
	"active":false,
	"note":"",
	"last_login":null,
	"source":null,
	"login_failed":0,
	"out_of_office":false,
	"out_of_office_start_at":null,
	"out_of_office_end_at":null,
	"out_of_office_replacement_id":null,
	"preferences":{},
	"updated_by_id":1,
	"created_by_id":1,
	"created_at":"2022-05-18T17:40:55.144Z",
	"updated_at":"2022-05-18T17:40:55.144Z",
	"role_ids":[],
	"organization_ids":[],
	"authorization_ids":[],
	"karma_user_ids":[],
	"group_ids":{},
	"accounts":{}},
	"3":{"active":true,"login_failed":0,
	"verified":false,
	"source":null,
	"id":3,
	"updated_by_id":1,
	"organization_id":2,
	"login":"matmccabe@gmail.com",
	"firstname":"Mathew",
	"lastname":"McCabe",
	"email":"matmccabe@gmail.com",
	"image":null,
	"image_source":null,
	"web":"",
	"phone":"",
	"fax":"",
	"mobile":"",
	"department":null,
	"street":"","zip":"",
	"city":"",
	"country":"",
	"address":null,
	"vip":false,
	"note":"",
	"last_login":"2022-05-19T00:36:11.231Z",
	"out_of_office":false,
	"out_of_office_start_at":null,
	"out_of_office_end_at":null,
	"out_of_office_replacement_id":null,
	"preferences":{"notification_config":{"matrix":{"create":{"criteria":{"owned_by_me":true,
	"owned_by_nobody":true,"subscribed":true,"no":false},
	"channel":{"email":true,"online":true}},
	"update":{"criteria":{"owned_by_me":true,
	"owned_by_nobody":true,
	"subscribed":true,"no":false},
	"channel":{"email":true,"online":true}},
	"reminder_reached":{"criteria":{"owned_by_me":true,
	"owned_by_nobody":false,"subscribed":false,"no":false},
	"channel":{"email":true,"online":true}},
	"escalation":{"criteria":{"owned_by_me":true,
	"owned_by_nobody":false,
	"subscribed":false,
	"no":false},
	"channel":{"email":true,"online":true}}}},
	"locale":"en-us","intro":true},
	"created_by_id":1,
	"created_at":"2022-05-19T00:06:31.281Z",
	"updated_at":"2022-05-19T00:36:11.233Z",
	"role_ids":[1,2],
	"organization_ids":[],"authorization_ids":[],
	"karma_user_ids":[],
	"group_ids":{"1":["full"]},
	"accounts":{}}},"Group":{"1":{"id":1,
	"signature_id":1,
	"email_address_id":1,
	"name":"Users",
	"assignment_timeout":null,
	"follow_up_possible":"yes",
	"follow_up_assignment":true,
	"active":true,
	"shared_drafts":true,
	"note":"Standard Group/Pool for Tickets.",
	"updated_by_id":3,
	"created_by_id":1,
	"created_at":"2022-05-18T17:40:55.690Z",
	"updated_at":"2022-05-19T00:06:31.383Z",
	"user_ids":[3]}},
	"Organization":{"2":{"id":2,
	"name":"Docu",
	"shared":true,
	"domain":"",
	"domain_assignment":false,
	"active":true,
	"note":"",
	"updated_by_id":1,
	"created_by_id":1,
	"created_at":"2022-05-19T00:06:31.249Z",
	"updated_at":"2022-05-19T00:06:31.325Z",
	"member_ids":[3]}}},"total_count":4}
	}



**Specific role**

``GET`` -Request sent: ``https://endpointdocu.zammad.com/api/v1/roles/:id``

Response: 

.. code-block:: json 

	# HTTP-Code 200 OK

	{"id":4,"name":"Mathew",
	"preferences":{},
	"default_at_signup":false,
	"active":true,
	"note":"New User",
	"updated_by_id":3,
	"created_by_id":3,
	"created_at":"2022-05-19T01:02:58.007Z",
	"updated_at":"2022-05-19T01:02:58.007Z",
	"permission_ids":[1],"knowledge_base_permission_ids":[],
	"group_ids":{}}


**Create role**

``POST`` -Request sent: ``https://endpointdocu.zammad.com/api/v1/roles``

Response: 

.. code-block:: json
	 
	# HTTP-Code 201 OK

	{
		{"id":4,
		"name":"Mathew",
		"preferences":{},
		"default_at_signup":false,
		"active":true,
		"note":"New User",
		"updated_by_id":3,
		"created_by_id":3,
		"created_at":"2022-05-19T01:02:58.007Z",
		"updated_at":"2022-05-19T01:02:58.007Z",
		"permission_ids":[1],"knowledge_base_permission_ids":[],
		"group_ids":{}}

	}

.. code-block:: json
	
	# HTTP-Code 422 ERROR
	{
		{"error":"Cannot set default at signup when role has admin.branding, admin.group permissions.",
		"error_human":"Cannot set default at signup when role has admin.branding, admin.group permissions."}
	}


**Update role**

``PUT`` -Request sent: ``https://endpointdocu.zammad.com/api/v1/roles/:id``

.. code-block:: json
	
	# HTTP-Code 422 ERROR
	{
		{"id":5,"name":"User 2",
		"default_at_signup":false,
		"active":true,
		"note":"To configure your system.",
		"updated_by_id":3,"preferences":{},
		"created_by_id":3,"created_at":"2022-05-19T01:46:44.175Z",
		"updated_at":"2022-05-19T01:47:28.349Z",
		"permission_ids":[],"knowledge_base_permission_ids":[],
		"group_ids":{}}
	}