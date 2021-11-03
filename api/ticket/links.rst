Linking Tickets
*******************

Required permission: ``ticket.agent`` **or** ``admin``

Available endpoints:

``GET      /api/v1/links``

``POST     /api/v1/links/add``

``DELETE   /api/v1/links/remove``

Get
===

Request::

   GET /api/v1/links

with following parameters:

   {
      "link_object": "Ticket", 
      "link_object_value": "147469"
   }

Response::

   Status: 200 Ok

   {
      "links": [
         {
            "link_type": "normal",
            "link_object": "Ticket",
            "link_object_value": 147470
         },
         {
            "link_type": "normal",
            "link_object": "Ticket",
            "link_object_value": 147471
         }
      ],
      "assets": {
         "Ticket": {
            "147470": {
            "id": 147470,
            "group_id": 1,
            "priority_id": 2,
            "state_id": 2,
            "organization_id": null,
            "number": "34147470",
            "title": "Test Ticket #2",
            "owner_id": 1,
            "customer_id": 3,
            "note": null,
            "first_response_at": null,
            "first_response_escalation_at": null,
            "first_response_in_min": null,
            "first_response_diff_in_min": null,
            "close_at": null,
            "close_escalation_at": null,
            "close_in_min": null,
            "close_diff_in_min": null,
            "update_escalation_at": null,
            "update_in_min": null,
            "update_diff_in_min": null,
            "last_contact_at": "2021-11-03T10:16:45.266Z",
            "last_contact_agent_at": null,
            "last_contact_customer_at": "2021-11-03T10:16:45.266Z",
            "last_owner_update_at": null,
            "create_article_type_id": 5,
            "create_article_sender_id": 2,
            "article_count": 1,
            "escalation_at": null,
            "pending_time": null,
            "type": null,
            "time_unit": null,
            "preferences": {},
            "updated_by_id": 3,
            "created_by_id": 3,
            "created_at": "2021-11-03T10:16:45.092Z",
            "updated_at": "2021-11-03T10:17:01.428Z",
            "remote_access_permission_by": null,
            "remote_access": "",
            "affected_area": "",
            "service_number": "",
            "article_ids": [
               464964
            ],
            "ticket_time_accounting_ids": []
            },
            "147471": {
            "id": 147471,
            "group_id": 1,
            "priority_id": 2,
            "state_id": 2,
            "organization_id": null,
            "number": "34147471",
            "title": "Test Ticket #3",
            "owner_id": 1,
            "customer_id": 3,
            "note": null,
            "first_response_at": null,
            "first_response_escalation_at": null,
            "first_response_in_min": null,
            "first_response_diff_in_min": null,
            "close_at": null,
            "close_escalation_at": null,
            "close_in_min": null,
            "close_diff_in_min": null,
            "update_escalation_at": null,
            "update_in_min": null,
            "update_diff_in_min": null,
            "last_contact_at": "2021-11-03T10:16:51.995Z",
            "last_contact_agent_at": null,
            "last_contact_customer_at": "2021-11-03T10:16:51.995Z",
            "last_owner_update_at": null,
            "create_article_type_id": 5,
            "create_article_sender_id": 2,
            "article_count": 1,
            "escalation_at": null,
            "pending_time": null,
            "type": null,
            "time_unit": null,
            "preferences": {},
            "updated_by_id": 3,
            "created_by_id": 3,
            "created_at": "2021-11-03T10:16:51.824Z",
            "updated_at": "2021-11-03T10:16:57.862Z",
            "remote_access_permission_by": null,
            "remote_access": "",
            "affected_area": "",
            "service_number": "",
            "article_ids": [
               464965
            ],
            "ticket_time_accounting_ids": []
            }
         },
         "User": {
            "3": {
            "id": 3,
            "organization_id": null,
            "login": "test@test.de",
            "firstname": "Max",
            "lastname": "Mustermann",
            "email": "test@test.de",
            "image": null,
            "image_source": null,
            "web": "",
            "phone": "",
            "fax": "",
            "mobile": "",
            "department": null,
            "street": "",
            "zip": "",
            "city": "",
            "country": "",
            "address": null,
            "vip": false,
            "verified": false,
            "active": true,
            "note": "",
            "last_login": "2021-11-01T05:03:23.328Z",
            "source": null,
            "login_failed": 0,
            "out_of_office": false,
            "out_of_office_start_at": null,
            "out_of_office_end_at": null,
            "out_of_office_replacement_id": null,
            "preferences": {
               "notification_config": {
                  "matrix": {
                  "create": {
                     "criteria": {
                        "owned_by_me": true,
                        "owned_by_nobody": true,
                        "subscribed": true,
                        "no": false
                     },
                     "channel": {
                        "email": true,
                        "online": true
                     }
                  },
                  "update": {
                     "criteria": {
                        "owned_by_me": true,
                        "owned_by_nobody": true,
                        "subscribed": true,
                        "no": false
                     },
                     "channel": {
                        "email": true,
                        "online": true
                     }
                  },
                  "reminder_reached": {
                     "criteria": {
                        "owned_by_me": true,
                        "owned_by_nobody": false,
                        "subscribed": false,
                        "no": false
                     },
                     "channel": {
                        "email": true,
                        "online": true
                     }
                  },
                  "escalation": {
                     "criteria": {
                        "owned_by_me": true,
                        "owned_by_nobody": false,
                        "subscribed": false,
                        "no": false
                     },
                     "channel": {
                        "email": true,
                        "online": true
                     }
                  }
                  }
               },
               "locale": "de-de",
               "intro": true
            },
            "updated_by_id": 1,
            "created_by_id": 1,
            "created_at": "2021-10-29T13:25:59.261Z",
            "updated_at": "2021-11-01T05:03:23.334Z",
            "salutation": null,
            "wawi_number": 0,
            "guid": null,
            "notification_optin": false,
            "zr_number": null,
            "role_ids": [
               1,
               2
            ],
            "organization_ids": [],
            "authorization_ids": [],
            "karma_user_ids": [],
            "group_ids": {
               "1": [
                  "full"
               ]
            },
            "accounts": {}
            },
            "1": {
            "id": 1,
            "organization_id": null,
            "login": "-",
            "firstname": "-",
            "lastname": "",
            "email": "",
            "image": null,
            "image_source": null,
            "web": "",
            "phone": "",
            "fax": "",
            "mobile": "",
            "department": "",
            "street": "",
            "zip": "",
            "city": "",
            "country": "",
            "address": "",
            "vip": false,
            "verified": false,
            "active": false,
            "note": "",
            "last_login": null,
            "source": null,
            "login_failed": 0,
            "out_of_office": false,
            "out_of_office_start_at": null,
            "out_of_office_end_at": null,
            "out_of_office_replacement_id": null,
            "preferences": {},
            "updated_by_id": 1,
            "created_by_id": 1,
            "created_at": "2021-10-29T13:11:53.378Z",
            "updated_at": "2021-10-29T13:11:53.378Z",
            "salutation": null,
            "wawi_number": 0,
            "guid": null,
            "notification_optin": false,
            "zr_number": null,
            "role_ids": [],
            "organization_ids": [],
            "authorization_ids": [],
            "karma_user_ids": [],
            "group_ids": {},
            "accounts": {}
            }
         },
         "Role": {
            "1": {
            "id": 1,
            "name": "Admin",
            "preferences": {},
            "default_at_signup": false,
            "active": true,
            "note": "To configure your system.",
            "updated_by_id": 3,
            "created_by_id": 1,
            "created_at": "2021-10-29T13:11:53.503Z",
            "updated_at": "2021-10-30T21:44:00.923Z",
            "permission_ids": [
               1,
               41,
               51,
               61
            ],
            "group_ids": {}
            },
            "2": {
            "id": 2,
            "name": "Agent",
            "preferences": {},
            "default_at_signup": false,
            "active": true,
            "note": "To work on Tickets.",
            "updated_by_id": 3,
            "created_by_id": 1,
            "created_at": "2021-10-29T13:11:53.542Z",
            "updated_at": "2021-10-30T18:26:29.027Z",
            "permission_ids": [
               41,
               53,
               56,
               58,
               62
            ],
            "group_ids": {}
            }
         },
         "Group": {
            "1": {
            "id": 1,
            "signature_id": 1,
            "email_address_id": null,
            "name": "Users",
            "assignment_timeout": null,
            "follow_up_possible": "yes",
            "follow_up_assignment": true,
            "active": true,
            "note": "Standard Group/Pool for Tickets.",
            "updated_by_id": 1,
            "created_by_id": 1,
            "created_at": "2021-10-29T13:11:54.863Z",
            "updated_at": "2021-10-30T18:53:24.803Z",
            "user_ids": [
               3,
               2,
               5,
               55,
               65,
               83,
               90,
               101,
               105,
               112,
               118,
               132,
               153,
               168,
               203,
               295,
               493,
               515,
               528,
               535,
               565,
               618,
               730,
               755,
               839,
               859,
               912,
               914,
               983,
               1106,
               1138,
               1229,
               1287,
               1405,
               1410,
               1482,
               1486,
               1490,
               1543,
               1573
            ]
            }
         }
      }
   }


Add
===

Required permission: ``ticket.agent`` **or** ``admin``

Request::

   POST /api/v1/links/add

Response::

   Status: 200 Ok

   {

   }

Delete
======

Required permission: ``ticket.agent`` **or** ``admin``

Request::

   DELETE /api/v1/links/remove

Response::

   Status: 200 Ok

   {
   
   }

