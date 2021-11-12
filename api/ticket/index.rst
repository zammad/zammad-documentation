Tickets
*******

   .. warning::

      Ticket endpoints depend on on group permissions if the user you're 
      using is an agent. Because of this tickets may or may not be available.

List
====

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets``

Response:

.. code-block:: json
   :force:
   
   # HTTP-Code 200 Ok

   [
      {
         "id": 1,
         "group_id": 1,
         "priority_id": 2,
         "state_id": 1,
         "organization_id": 1,
         "number": "22001",
         "title": "Welcome to Zammad!",
         "owner_id": 1,
         "customer_id": 2,
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
         "last_contact_at": "2021-11-03T11:51:13.790Z",
         "last_contact_agent_at": null,
         "last_contact_customer_at": "2021-11-03T11:51:13.790Z",
         "last_owner_update_at": null,
         "create_article_type_id": 5,
         "create_article_sender_id": 2,
         "article_count": 1,
         "escalation_at": null,
         "pending_time": null,
         "type": null,
         "time_unit": null,
         "preferences": {},
         "updated_by_id": 2,
         "created_by_id": 2,
         "created_at": "2021-11-03T11:51:13.759Z",
         "updated_at": "2021-11-03T11:51:13.809Z"
      },
      {
         "id": 2,
         "group_id": 1,
         "priority_id": 2,
         "state_id": 4,
         "organization_id": 3,
         "number": "22002",
         "title": "Order 777555",
         "owner_id": 3,
         "customer_id": 6,
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
         "last_contact_at": "2021-05-04T16:57:17.920Z",
         "last_contact_agent_at": "2021-05-03T10:57:17.904Z",
         "last_contact_customer_at": "2021-05-04T16:57:17.920Z",
         "last_owner_update_at": null,
         "create_article_type_id": 1,
         "create_article_sender_id": 2,
         "article_count": 3,
         "escalation_at": null,
         "pending_time": null,
         "type": null,
         "time_unit": null,
         "preferences": {},
         "updated_by_id": 6,
         "created_by_id": 6,
         "created_at": "2021-05-03T09:57:17.837Z",
         "updated_at": "2021-11-03T11:57:17.927Z"
      },

      ...
   ]

Search
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets/search?query={search string}&limit=10``

.. include:: /api/includes/sort_and_order.rst

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok
   
   {
      "tickets": [
         9,
         10,
         11
      ],
      "tickets_count": 3,
      "assets": {
         "Ticket": {
            "9": {
               "id": 9,
               "group_id": 1,
               "priority_id": 3,
               "state_id": 2,
               "organization_id": 7,
               "number": "22009",
               "title": "Need more information!",
               "owner_id": 5,
               "customer_id": 10,
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
               "last_contact_at": "2021-11-03T05:42:19.141Z",
               "last_contact_agent_at": "2021-11-03T05:42:19.141Z",
               "last_contact_customer_at": "2021-11-03T02:57:19.141Z",
               "last_owner_update_at": null,
               "create_article_type_id": 1,
               "create_article_sender_id": 2,
               "article_count": 4,
               "escalation_at": null,
               "pending_time": null,
               "type": null,
               "time_unit": null,
               "preferences": {},
               "updated_by_id": 3,
               "created_by_id": 10,
               "created_at": "2021-11-03T02:57:19.141Z",
               "updated_at": "2021-11-03T17:48:52.849Z",
               "article_ids": [
                  19,
                  18,
                  17,
                  16
               ],
               "ticket_time_accounting_ids": []
            },
            "10": {
               "id": 10,
               "group_id": 1,
               "priority_id": 3,
               "state_id": 1,
               "organization_id": 7,
               "number": "22010",
               "title": "Heads up 🕹!",
               "owner_id": 1,
               "customer_id": 11,
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
               "last_contact_at": "2021-11-03T11:57:19.227Z",
               "last_contact_agent_at": null,
               "last_contact_customer_at": "2021-11-03T11:57:19.227Z",
               "last_owner_update_at": null,
               "create_article_type_id": 1,
               "create_article_sender_id": 2,
               "article_count": 1,
               "escalation_at": null,
               "pending_time": null,
               "type": null,
               "time_unit": null,
               "preferences": {},
               "updated_by_id": 3,
               "created_by_id": 11,
               "created_at": "2021-11-03T02:57:19.216Z",
               "updated_at": "2021-11-03T17:48:52.730Z",
               "article_ids": [
                  20
               ],
               "ticket_time_accounting_ids": []
            },
            "11": {
               "id": 11,
               "group_id": 1,
               "priority_id": 3,
               "state_id": 1,
               "organization_id": 3,
               "number": "22011",
               "title": "Surprise - well done",
               "owner_id": 1,
               "customer_id": 6,
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
               "last_contact_at": "2021-11-03T02:57:19.243Z",
               "last_contact_agent_at": null,
               "last_contact_customer_at": "2021-11-03T02:57:19.243Z",
               "last_owner_update_at": null,
               "create_article_type_id": 11,
               "create_article_sender_id": 2,
               "article_count": 1,
               "escalation_at": null,
               "pending_time": null,
               "type": null,
               "time_unit": null,
               "preferences": {},
               "updated_by_id": 6,
               "created_by_id": 6,
               "created_at": "2021-11-03T02:57:19.243Z",
               "updated_at": "2021-11-03T11:57:19.263Z",
               "article_ids": [
                  21
               ],
               "ticket_time_accounting_ids": []
            }
         },
         "User": {
            "10": {
               "id": 10,
               "organization_id": null,
               "login": "david@example.com",
               "firstname": "David",
               "lastname": "Bell",
               "email": "david@example.com",
               "image": "d829d234f377f231534802df6d5500a7",
               "image_source": null,
               "web": "",
               "phone": "0033 892 12 34 56",
               "fax": "",
               "mobile": "",
               "department": "",
               "street": "",
               "zip": "",
               "city": "",
               "country": "",
               "address": "Eiffel Tower\r\n5 Avenue Anatole France\r\n75007 Paris",
               "vip": false,
               "verified": false,
               "active": true,
               "note": "did order viennese melange, ask next time if the flavor was as expected",
               "last_login": null,
               "source": null,
               "login_failed": 0,
               "out_of_office": false,
               "out_of_office_start_at": null,
               "out_of_office_end_at": null,
               "out_of_office_replacement_id": null,
               "preferences": {
                  "tickets_closed": 1,
                  "tickets_open": 3,
                  "mail_delivery_failed": true,
                  "mail_delivery_failed_data": "2021-11-08T13:38:32.059Z"
               },
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:17.495Z",
               "updated_at": "2021-11-08T13:45:04.107Z",
               "role_ids": [
                  3
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
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
               "created_at": "2021-11-03T11:51:12.786Z",
               "updated_at": "2021-11-03T11:51:12.786Z",
               "role_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
               "accounts": {}
            },
            "3": {
               "id": 3,
               "organization_id": 2,
               "login": "chris@chrispresso.com",
               "firstname": "Christopher",
               "lastname": "Miller",
               "email": "chris@chrispresso.com",
               "image": "7a6a0d1d94ad2037153cf3a6c1b49a53",
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
               "active": true,
               "note": "",
               "last_login": "2021-11-03T12:26:53.410Z",
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
                  "locale": "en-us",
                  "intro": true,
                  "chat": {
                     "active": {
                        "1": "on"
                     }
                  }
               },
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:15.975Z",
               "updated_at": "2021-11-08T13:45:07.798Z",
               "role_ids": [
                  1,
                  2
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [
                  1
               ],
               "group_ids": {
                  "1": [
                     "full"
                  ],
                  "2": [
                     "full"
                  ],
                  "3": [
                     "full"
                  ]
               },
               "accounts": {}
            },
            "4": {
               "id": 4,
               "organization_id": 2,
               "login": "jacob@chrispresso.com",
               "firstname": "Jacob",
               "lastname": "Smith",
               "email": "jacob@chrispresso.com",
               "image": "95afc1244af5cb8b77edcd7224c5d5f8",
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
               "last_login": null,
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
                  "locale": "en-us"
               },
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:16.160Z",
               "updated_at": "2021-11-03T11:57:16.214Z",
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
                  ],
                  "2": [
                     "full"
                  ],
                  "3": [
                     "full"
                  ]
               },
               "accounts": {}
            },
            "5": {
               "id": 5,
               "organization_id": 7,
               "login": "emma@chrispresso.com",
               "firstname": "Emma",
               "lastname": "Taylor",
               "email": "emma@chrispresso.com",
               "image": "b64fef91c29105b4a08a2a69be08eda3",
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
               "last_login": null,
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
                  "locale": "en-us"
               },
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:16.349Z",
               "updated_at": "2021-11-08T13:22:38.130Z",
               "role_ids": [
                  2
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {
                  "1": [
                     "full"
                  ],
                  "2": [
                     "full"
                  ],
                  "3": [
                     "full"
                  ]
               },
               "accounts": {}
            },
            "11": {
               "id": 11,
               "organization_id": 7,
               "login": "olivia@example.com",
               "firstname": "Olivia",
               "lastname": "Ross",
               "email": "olivia@example.com",
               "image": "b6f7a2d56544bb471eb3a3c238c7d964",
               "image_source": null,
               "web": "",
               "phone": "0044 20 1234 5678",
               "fax": "",
               "mobile": "",
               "department": "",
               "street": "",
               "zip": "",
               "city": "",
               "country": "",
               "address": "Westminster\r\nLondon SW1A 0AA",
               "vip": false,
               "verified": false,
               "active": true,
               "note": "",
               "last_login": null,
               "source": null,
               "login_failed": 0,
               "out_of_office": false,
               "out_of_office_start_at": null,
               "out_of_office_end_at": null,
               "out_of_office_replacement_id": null,
               "preferences": {
                  "tickets_closed": 0,
                  "tickets_open": 1
               },
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:17.741Z",
               "updated_at": "2021-11-03T17:48:52.739Z",
               "role_ids": [
                  3
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
               "accounts": {}
            },
            "16": {
               "id": 16,
               "organization_id": 7,
               "login": "jdoe",
               "firstname": "Jane",
               "lastname": "Doe",
               "email": "jdoe@example.com",
               "image": null,
               "image_source": null,
               "web": "",
               "phone": "+49 30 55 57 160 00",
               "fax": "",
               "mobile": "",
               "department": "Sales",
               "street": "",
               "zip": "",
               "city": "",
               "country": "",
               "address": "Marienstr. 18\r\n10117 Berlin",
               "vip": false,
               "verified": false,
               "active": true,
               "note": "",
               "last_login": null,
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
                  "locale": "en-us"
               },
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2021-11-03T14:42:36.855Z",
               "updated_at": "2021-11-08T13:20:18.500Z",
               "role_ids": [
                  2,
                  3
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
               "accounts": {}
            },
            "6": {
               "id": 6,
               "organization_id": 3,
               "login": "anna@example.com",
               "firstname": "Anna",
               "lastname": "Lopez",
               "email": "anna@example.com",
               "image": "4b1cb1fae2e608ffa72099774e1f57ad",
               "image_source": null,
               "web": "",
               "phone": "415-123-5858",
               "fax": "",
               "mobile": "",
               "department": null,
               "street": "",
               "zip": "",
               "city": "",
               "country": "",
               "address": "Golden Gate Bridge\nSan Francisco, CA 94129",
               "vip": false,
               "verified": false,
               "active": true,
               "note": "likes espresso romano - recommended espresso con panna",
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
               "created_at": "2021-11-03T11:57:16.526Z",
               "updated_at": "2021-11-03T11:57:16.611Z",
               "role_ids": [
                  3
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
               "accounts": {}
            },
            "7": {
               "id": 7,
               "organization_id": 3,
               "login": "samuel@example.com",
               "firstname": "Samuel",
               "lastname": "Lee",
               "email": "samuel@example.com",
               "image": "5911d228f3588c36a72d80eb0c1e4d08",
               "image_source": null,
               "web": "",
               "phone": "855-666-7777",
               "fax": "",
               "mobile": "",
               "department": null,
               "street": "",
               "zip": "",
               "city": "",
               "country": "",
               "address": "5201 Blue Lagoon Drive\n8th Floor & 9th Floor\nMiami, FL 33126",
               "vip": false,
               "verified": false,
               "active": true,
               "note": "likes americano, did order two units",
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
               "created_at": "2021-11-03T11:57:16.748Z",
               "updated_at": "2021-11-03T11:57:16.861Z",
               "role_ids": [
                  3
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
               "accounts": {}
            },
            "8": {
               "id": 8,
               "organization_id": 3,
               "login": "emily@example.com",
               "firstname": "Emily",
               "lastname": "Adams",
               "email": "emily@example.com",
               "image": "99ba64a89f7783c099c304c9b00ff9e8",
               "image_source": null,
               "web": "",
               "phone": "0061 2 1234 7777",
               "fax": "",
               "mobile": "",
               "department": null,
               "street": "",
               "zip": "",
               "city": "",
               "country": "",
               "address": "Bennelong Point\nSydney NSW 2000",
               "vip": false,
               "verified": false,
               "active": true,
               "note": "did order café au lait, ask next time if the flavor was as expected",
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
               "created_at": "2021-11-03T11:57:17.000Z",
               "updated_at": "2021-11-03T11:57:17.060Z",
               "role_ids": [
                  3
               ],
               "organization_ids": [],
               "authorization_ids": [],
               "karma_user_ids": [],
               "group_ids": {},
               "accounts": {}
            }
         },
         "Role": {
            "3": {
               "id": 3,
               "name": "Customer",
               "preferences": {},
               "default_at_signup": true,
               "active": true,
               "note": "People who create Tickets ask for help.",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:51:12.856Z",
               "updated_at": "2021-11-08T13:38:31.573Z",
               "permission_ids": [
                  42,
                  45,
                  46,
                  48,
                  54
               ],
               "group_ids": {}
            },
            "1": {
               "id": 1,
               "name": "Admin",
               "preferences": {},
               "default_at_signup": false,
               "active": true,
               "note": "To configure your system.",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:51:12.831Z",
               "updated_at": "2021-11-03T11:51:12.831Z",
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
               "created_at": "2021-11-03T11:51:12.848Z",
               "updated_at": "2021-11-03T14:42:36.875Z",
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
               "name": "Sales",
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "follow_up_assignment": true,
               "active": true,
               "note": "Standard Group/Pool for Tickets.",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:51:13.449Z",
               "updated_at": "2021-11-08T13:37:57.093Z",
               "user_ids": [
                  4,
                  5,
                  3
               ]
            },
            "2": {
               "id": 2,
               "signature_id": null,
               "email_address_id": null,
               "name": "2nd Level",
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "follow_up_assignment": true,
               "active": true,
               "note": null,
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:15.802Z",
               "updated_at": "2021-11-08T13:37:57.097Z",
               "user_ids": [
                  4,
                  5,
                  3
               ]
            },
            "3": {
               "id": 3,
               "signature_id": null,
               "email_address_id": null,
               "name": "Service Desk",
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "follow_up_assignment": true,
               "active": true,
               "note": null,
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:15.807Z",
               "updated_at": "2021-11-08T13:37:57.102Z",
               "user_ids": [
                  4,
                  5,
                  3
               ]
            }
         },
         "Organization": {
            "2": {
               "id": 2,
               "name": "Chrispresso Inc.",
               "shared": true,
               "domain": "",
               "domain_assignment": false,
               "active": true,
               "note": "Manufacturer of individual coffee products.",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:15.817Z",
               "updated_at": "2021-11-08T13:22:38.145Z",
               "member_ids": [
                  3,
                  4
               ]
            },
            "7": {
               "id": 7,
               "name": "Sample Corp.",
               "shared": false,
               "domain": "",
               "domain_assignment": false,
               "active": true,
               "note": "This was a triump - I'm making a note here - H-U-G-E success!",
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2021-11-03T17:48:52.613Z",
               "updated_at": "2021-11-08T13:22:38.148Z",
               "member_ids": [
                  5,
                  11,
                  16
               ]
            },
            "3": {
               "id": 3,
               "name": "Awesome Customer Inc.",
               "shared": true,
               "domain": "",
               "domain_assignment": false,
               "active": true,
               "note": "Global distributor of communication and security products, electrical and electronic wire &amp; cable.",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2021-11-03T11:57:15.825Z",
               "updated_at": "2021-11-03T11:57:15.825Z",
               "member_ids": [
                  6,
                  7,
                  8
               ]
            }
         }
      }
   }

.. warning::

   ``tickets_count`` returns the *current* number of returned tickets, not
   *the total amount*.

Show
====

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets/{ticket id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok
   
   {
      "id": 3,
      "group_id": 1,
      "priority_id": 2,
      "state_id": 4,
      "organization_id": 3,
      "number": "22003",
      "title": "Order 787556",
      "owner_id": 3,
      "customer_id": 7,
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
      "last_contact_at": "2021-06-03T09:57:17.987Z",
      "last_contact_agent_at": "2021-06-03T09:57:17.987Z",
      "last_contact_customer_at": "2021-06-01T11:57:17.935Z",
      "last_owner_update_at": null,
      "create_article_type_id": 1,
      "create_article_sender_id": 2,
      "article_count": 2,
      "escalation_at": null,
      "pending_time": null,
      "type": null,
      "time_unit": null,
      "preferences": {},
      "updated_by_id": 4,
      "created_by_id": 7,
      "created_at": "2021-06-01T11:57:17.935Z",
      "updated_at": "2021-11-03T11:57:17.997Z"
   }

Create
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

   .. tip:: 

      **🐱‍👤 On behalf of users**

      If you want to create tickets on behalf other users, use 
      the ``customer_id`` attribute. ``ticket.agent`` is mandatory for this. 
      Use ``guess:{email address}`` to save an API call if you don't know the 
      users ID or want to create the user in question.

      **📣 Add mention subscription right away**

      Add the ``mentions`` attribute to your ticket payload and provide 
      an array of user ids to directly subscribe them during ticket creation. 

      *E.g.:* ``"mentions": [1, 5, 7, 8],``

``POST``-Request sent: ``/api/v1/tickets``

.. code-block:: json
   
   {
      "title": "Help me!",
      "group": "2nd Level",
      "customer": "david@example.com",
      "article": {
         "subject": "My subject",
         "body": "I am a message!",
         "type": "note",
         "internal": false
      }
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created
   
   {
      "id": 19,
      "group_id": 2,
      "priority_id": 2,
      "state_id": 1,
      "organization_id": null,
      "number": "22019",
      "title": "Help me!",
      "owner_id": 1,
      "customer_id": 10,
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
      "last_contact_at": null,
      "last_contact_agent_at": null,
      "last_contact_customer_at": null,
      "last_owner_update_at": null,
      "create_article_type_id": 10,
      "create_article_sender_id": 1,
      "article_count": 1,
      "escalation_at": null,
      "pending_time": null,
      "type": null,
      "time_unit": null,
      "preferences": {},
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T14:17:41.913Z",
      "updated_at": "2021-11-08T14:17:41.994Z",
      "article_ids": [
         30
      ],
      "ticket_time_accounting_ids": []
   }

.. hint::

   For more article attributes and options have a look into :doc:`articles`.

Update
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``PUT``-Request sent: ``/api/v1/tickets/{ticket id}``

.. code-block:: json
   :force:
   
   {
      "title": "No help for you",
      "group": "Sales",
      "state": "open",
      "priority": "3 high",
      "article": {
         "subject": "Update via API",
         "body": "Here's my reason for updating this ticket...",
         "internal": true
      }
   }

   .. note::

      Above example provides an article. This article is a *new article* and
      does not affect any existing ones.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok
   
   {
      "id": 19,
      "group_id": 1,
      "priority_id": 3,
      "state_id": 2,
      "organization_id": null,
      "number": "22019",
      "title": "No help for you",
      "owner_id": 1,
      "customer_id": 10,
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
      "last_contact_at": null,
      "last_contact_agent_at": null,
      "last_contact_customer_at": null,
      "last_owner_update_at": null,
      "create_article_type_id": 10,
      "create_article_sender_id": 1,
      "article_count": 2,
      "escalation_at": null,
      "pending_time": null,
      "type": null,
      "time_unit": null,
      "preferences": {},
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T14:17:41.913Z",
      "updated_at": "2021-11-08T14:18:53.426Z",
      "article_ids": [
         31,
         30
      ],
      "ticket_time_accounting_ids": []
   }

.. tip:: **Adding attachments**

   Attachment payloads are identical to the ``POST`` method, just use ``PUT`` 
   instead.

Delete
======

Required permission: ``admin``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing tickets cannot be undone.
   All data (e.g.: articles & attachments) will be lost.

``DELETE``-Request sent: ``/api/v1/tickets/{ticket id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok
   {}
