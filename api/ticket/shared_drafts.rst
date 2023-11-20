Shared Drafts
*************

Show
====

Required permission: ``ticket.agent``.

``GET``-Request sent: ``/api/v1/tickets/{ticket id}/shared_draft``

Sample response (base64 coded inline image is cut off):

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "shared_draft_id": 2,
      "assets": {
         "TicketSharedDraftZoom": {
            "2": {
               "id": 2,
               "ticket_id": 58,
               "new_article": {
                  "body": "<div>Some text for a shared draft. <br></div><div><br></div><div>Some inline image:<img tabindex=\"0\" style=\"width: 1000px; max-width: 100%;\" src=\"data:image/jpeg;base64,/9j/4AAQSkZJRg[...]",
                  "type": "email",
                  "internal": false,
                  "subtype": "",
                  "in_reply_to": "",
                  "to": "jane@doe.com",
                  "cc": "",
                  "subject": "",
                  "from": "Christopher Miller",
                  "ticket_id": 58,
                  "content_type": "text/html",
                  "sender_id": 1,
                  "type_id": 1,
                  "preferences": {
                     "security": {
                        "encryption": {},
                        "sign": {
                           "success": true
                        },
                        "type": "S/MIME"
                     }
                  }
               },
               "ticket_attributes": {
                  "group_id": "2",
                  "owner_id": "4",
                  "state_id": "2",
                  "priority_id": "2"
               },
               "created_by_id": 3,
               "updated_by_id": 3,
               "created_at": "2023-08-18T13:28:13.279Z",
               "updated_at": "2023-08-18T13:28:13.279Z"
            }
         },
         "User": {
            "3": {
               "login_failed": 0,
               "last_login": "2023-08-18T12:31:24.645Z",
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
               "updated_at": "2023-08-18T12:31:24.670Z",
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
                     }
                  },
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
               }
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
      }
   }

Create
======

Required permission: ``ticket.agent``.

``PUT``-Request sent: ``/api/v1/tickets/{ticket id}/shared_draft``

.. code-block:: json
   :force:

   {
   	"form_id": "367646073",
   	"new_article": {
   		"body": "This is some text.",
   		"cc": "",
   		"content_type": "text/html",
   		"from": "Christopher Miller",
   		"in_reply_to": "",
   		"internal": true,
   		"sender_id": 1,
   		"subject": "",
   		"subtype": "",
   		"ticket_id": 61,
   		"to": "",
   		"type": "note",
   		"type_id": 10
   	},
   	"ticket_attributes": {
   		"group_id": "2",
   		"owner_id": "4",
   		"priority_id": "2",
   		"state_id": "2"
   	}
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Create

   {
      "shared_draft_id": 8,
      "assets": {
         "TicketSharedDraftZoom": {
            "8": {
               "id": 8,
               "ticket_id": 61,
               "new_article": {
                  "body": "This is some text.",
                  "cc": "",
                  "content_type": "text/html",
                  "from": "Christopher Miller",
                  "in_reply_to": "",
                  "internal": true,
                  "sender_id": 1,
                  "subject": "",
                  "subtype": "",
                  "ticket_id": 61,
                  "to": "",
                  "type": "note",
                  "type_id": 10
               },
               "ticket_attributes": {
                  "group_id": "2",
                  "owner_id": "4",
                  "priority_id": "2",
                  "state_id": "2"
               },
               "created_by_id": 3,
               "updated_by_id": 3,
               "created_at": "2023-08-21T06:27:46.889Z",
               "updated_at": "2023-08-21T06:27:46.889Z"
            }
         },
         "User": {
            "3": {
               "login_failed": 0,
               "last_login": "2023-08-21T06:23:06.390Z",
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
               "updated_at": "2023-08-21T06:23:06.430Z",
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
                     }
                  },
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
               }
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
      }
   }

Update
======

Required permission: ``ticket.agent``

``PATCH``-Request sent: ``/api/v1/tickets/{ticket id}/shared_draft``


.. code-block:: json
   :force:

   {
   	"form_id": "367646073",
   	"new_article": {
   		"body": "Changed body.",
   		"cc": "",
   		"content_type": "text/html",
   		"from": "Jacob Smith",
   		"in_reply_to": "",
   		"internal": false,
   		"preferences": {
   			"security": {
   				"encryption": {},
   				"sign": {
   					"success": true
   				},
   				"type": "S/MIME"
   			}
   		},
   		"sender_id": 1,
   		"subject": "",
   		"subtype": "",
   		"ticket_id": 61,
   		"to": "nicole.braun@zammad.org",
   		"type": "email",
   		"type_id": 1
   	}
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "shared_draft_id": 8,
      "assets": {
         "TicketSharedDraftZoom": {
            "8": {
               "ticket_id": 61,
               "new_article": {
                  "body": "Changed body.",
                  "cc": "",
                  "content_type": "text/html",
                  "from": "Jacob Smith",
                  "in_reply_to": "",
                  "internal": false,
                  "preferences": {
                     "security": {
                        "encryption": {},
                        "sign": {
                           "success": true
                        },
                        "type": "S/MIME"
                     }
                  },
                  "sender_id": 1,
                  "subject": "",
                  "subtype": "",
                  "ticket_id": 61,
                  "to": "nicole.braun@zammad.org",
                  "type": "email",
                  "type_id": 1
               },
               "updated_by_id": 3,
               "id": 8,
               "ticket_attributes": {
                  "group_id": "2",
                  "owner_id": "4",
                  "priority_id": "2",
                  "state_id": "2"
               },
               "created_by_id": 3,
               "created_at": "2023-08-21T06:27:46.889Z",
               "updated_at": "2023-08-21T06:39:14.776Z"
            }
         },
         "User": {
            "3": {
               "login_failed": 0,
               "last_login": "2023-08-21T06:23:06.390Z",
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
               "updated_at": "2023-08-21T06:23:06.430Z",
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
                     }
                  },
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
               }
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
      }
   }

Remove
======

Required permission: ``ticket.agent``

``DELETE``-Request sent: ``/api/v1/tickets/{ticket id}/shared_draft``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK

   {
      "shared_draft_id": 3
   }