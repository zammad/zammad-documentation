Roles
*****

List
====

Required permission: ``admin.role``

``GET`` -Request sent: ``/api/v1/roles/?full=true&_={id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "record_ids": [
         1,
         2,
         3
      ],
      "assets": {
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
               "created_at": "2023-07-26T08:44:37.326Z",
               "updated_at": "2023-08-08T09:45:15.315Z",
               "permission_ids": [
                  1,
                  43,
                  55,
                  57,
                  65
               ],
               "knowledge_base_permission_ids": [],
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
             **All roles**  }
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
               "created_at": "2023-07-26T08:44:37.362Z",
               "updated_at": "2023-08-08T09:59:48.202Z",
               "permission_ids": [
                  43,
                  57,
                  60,
                  62,
                  66
               ],
               "knowledge_base_permission_ids": [],
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
               }
            },
            "3": {
               "id": 3,
               "name": "Customer",
               "preferences": {},
               "default_at_signup": true,
               "active": true,
               "note": "People who create Tickets ask for help.",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:37.379Z",
               "updated_at": "2023-08-17T12:14:20.080Z",
               "permission_ids": [
                  44,
                  47,
                  48,
                  50,
                  54,
                  58
               ],
               "knowledge_base_permission_ids": [],
               "group_ids": {}
            }
         },
         "Group": {
            "1": {
               "id": 1,
               "signature_id": 1,
               "email_address_id": 1,
               "name": "Sales",
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": "Standard Group/Pool for Tickets.",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:38.651Z",
               "updated_at": "2023-08-08T09:59:48.072Z",
               "user_ids": [
                  4,
                  5,
                  3
               ]
            },
            "2": {
               "id": 2,
               "signature_id": null,
               "email_address_id": 1,
               "name": "2nd Level",
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": "",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:48.589Z",
               "updated_at": "2023-08-08T09:59:48.148Z",
               "user_ids": [
                  4,
                  5,
                  3
               ]
            },
            "3": {
               "id": 3,
               "signature_id": null,
               "email_address_id": 1,
               "name": "Service Desk",
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": "",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:48.602Z",
               "updated_at": "2023-08-08T09:59:48.185Z",
               "user_ids": [
                  4,
                  5,
                  3
               ]
            }
         },
         "User": {
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
               "created_at": "2023-07-26T08:44:37.217Z",
               "updated_at": "2023-07-26T08:44:37.217Z",
               "role_ids": [],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {}
            },
            "3": {
               "login_failed": 0,
               "last_login": "2023-08-22T06:51:00.458Z",
               "updated_by_id": 1,
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
               "source": null,
               "out_of_office": false,
               "out_of_office_start_at": null,
               "out_of_office_end_at": null,
               "out_of_office_replacement_id": null,
               "preferences": {
                  "locale": "en-us",
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
                  "intro": true,
                  "theme": "light",
                  "two_factor_authentication": {}
               },
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:48.807Z",
               "updated_at": "2023-08-22T06:51:00.492Z",
               "role_ids": [
                  1,
                  2
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
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
               }
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
                  "locale": "en-us",
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
                  "theme": "light"
               },
               "updated_by_id": 4,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:49.390Z",
               "updated_at": "2023-08-18T06:43:28.448Z",
               "role_ids": [
                  1,
                  2
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
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
               }
            },
            "5": {
               "id": 5,
               "organization_id": 2,
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
                  "locale": "en-us",
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
                  "secondaryAction": "closeTab"
               },
               "updated_by_id": 5,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:49.766Z",
               "updated_at": "2023-08-09T09:51:34.110Z",
               "role_ids": [
                  2
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
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
               }
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
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2023-07-26T08:44:48.617Z",
               "updated_at": "2023-08-04T12:01:44.370Z",
               "vip": false,
               "member_ids": [
                  3,
                  4,
                  5
               ],
               "secondary_member_ids": []
            }
         }
      },
      "total_count": 3
   }

Show
====

Required permission: ``admin.role``

``GET`` -Request sent: ``/api/v1/roles/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "id": 2,
      "name": "Agent",
      "preferences": {},
      "default_at_signup": false,
      "active": true,
      "note": "To work on Tickets.",
      "updated_by_id": 3,
      "created_by_id": 1,
      "created_at": "2023-07-26T08:44:37.362Z",
      "updated_at": "2023-08-08T09:59:48.202Z",
      "permission_ids": [
         43,
         57,
         60,
         62,
         66
      ],
      "knowledge_base_permission_ids": [],
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
      }
   }

Create
======

Required permission: ``admin.role``

``POST`` -Request sent: ``/api/v1/roles``

Request:

.. code-block:: json
   :force:

   {
      "active": true,
      "default_at_signup": false,
      "group_ids": {
         "1": "full",
         "2": "full",
         "3": "full"
      },
      "id": "c-12",
      "name": "VIP service",
      "note": "Handling of VIP customers!",
      "permission_ids": [
         "57",
         "58"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 4,
      "name": "VIP service",
      "preferences": {},
      "default_at_signup": false,
      "active": true,
      "note": "Handling of VIP customers!",
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2023-08-22T11:24:02.114Z",
      "updated_at": "2023-08-22T11:24:02.111Z",
      "permission_ids": [
         57,
         58
      ],
      "knowledge_base_permission_ids": [],
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
      }
   }

Update
======

Required permission: ``admin.role``

``PUT`` -Request sent: ``/api/v1/roles/{id}``

Request:

.. code-block:: json
   :force:

   {
      "active": true,
      "default_at_signup": false,
      "group_ids": {
         "1": "full",
         "2": "full",
         "3": "full"
      },
      "name": "Service",
      "note": "Changed text",
      "permission_ids": [
         "57",
         "58"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "updated_at": "2023-08-22T11:36:49.136Z",
      "name": "Service",
      "default_at_signup": false,
      "active": true,
      "note": "Changed text",
      "updated_by_id": 3,
      "id": 3,
      "preferences": {},
      "created_by_id": 1,
      "created_at": "2023-07-26T08:44:37.379Z",
      "permission_ids": [
         57,
         58
      ],
      "knowledge_base_permission_ids": [],
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
      }
   }
