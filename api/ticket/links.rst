Linking Tickets
*******************

Get
===

Required permission: ``ticket.agent`` **or** ``admin``

``GET``-Request sent: ``/api/v1/links``

.. code-block:: json
   :force:

   {
      "link_object": "Ticket", 
      "link_object_value": "5"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
	"links": [
		{
			"link_type": "normal",
			"link_object": "Ticket",
			"link_object_value": 41
		}
	],
	"assets": {
		"Ticket": {
			"41": {
				"id": 41,
				"group_id": 2,
				"priority_id": 2,
				"state_id": 4,
				"organization_id": 1,
				"number": "93039",
				"title": "test",
				"owner_id": 1,
				"customer_id": 2,
				"note": null,
				"first_response_at": null,
				"first_response_escalation_at": null,
				"first_response_in_min": null,
				"first_response_diff_in_min": null,
				"close_at": "2023-08-04T14:37:07.884Z",
				"close_escalation_at": null,
				"close_in_min": null,
				"close_diff_in_min": null,
				"update_escalation_at": null,
				"update_in_min": null,
				"update_diff_in_min": null,
				"last_close_at": "2023-08-04T14:37:07.883Z",
				"last_contact_at": "2023-08-04T12:02:00.036Z",
				"last_contact_agent_at": null,
				"last_contact_customer_at": "2023-08-04T12:02:00.036Z",
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
				"created_at": "2023-08-04T12:01:59.897Z",
				"updated_at": "2023-08-08T09:24:43.977Z",
				"article_ids": [
					64,
					63
				],
				"ticket_time_accounting_ids": []
			}
		},
		"Group": {
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
				"updated_at": "2023-07-27T13:04:25.495Z",
				"user_ids": [
					3,
					4,
					5
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
				"updated_at": "2023-07-26T09:28:36.505Z",
				"user_ids": [
					3,
					4,
					5
				]
			},
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
				"updated_at": "2023-07-26T09:31:54.224Z",
				"user_ids": [
					3,
					4,
					5
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
				"last_login": "2023-08-08T08:03:40.962Z",
				"source": null,
				"login_failed": 1,
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
					"theme": "light"
				},
				"updated_by_id": 3,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:48.807Z",
				"updated_at": "2023-08-08T08:51:50.662Z",
				"role_ids": [
					1,
					2
				],
				"two_factor_preference_ids": [],
				"organization_ids": [],
				"authorization_ids": [],
				"overview_sorting_ids": [],
				"group_ids": {
					"3": [
						"full"
					],
					"1": [
						"full"
					],
					"2": [
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
						}
					}
				},
				"updated_by_id": 1,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:49.390Z",
				"updated_at": "2023-07-26T08:44:49.585Z",
				"role_ids": [
					1,
					2
				],
				"two_factor_preference_ids": [],
				"organization_ids": [],
				"authorization_ids": [],
				"overview_sorting_ids": [],
				"group_ids": {
					"3": [
						"full"
					],
					"1": [
						"full"
					],
					"2": [
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
					}
				},
				"updated_by_id": 1,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:49.766Z",
				"updated_at": "2023-07-26T08:44:49.970Z",
				"role_ids": [
					2
				],
				"two_factor_preference_ids": [],
				"organization_ids": [],
				"authorization_ids": [],
				"overview_sorting_ids": [],
				"group_ids": {
					"3": [
						"full"
					],
					"1": [
						"full"
					],
					"2": [
						"full"
					]
				}
			},
			"2": {
				"id": 2,
				"organization_id": 1,
				"login": "nicole.braun@zammad.org",
				"firstname": "Nicole",
				"lastname": "Braun",
				"email": "nicole.braun@zammad.org",
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
					"tickets_closed": 22,
					"tickets_open": 1
				},
				"updated_by_id": 3,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:39.646Z",
				"updated_at": "2023-08-04T14:37:11.400Z",
				"role_ids": [
					3
				],
				"two_factor_preference_ids": [],
				"organization_ids": [],
				"authorization_ids": [],
				"overview_sorting_ids": [],
				"group_ids": {}
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
				"updated_by_id": 1,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:37.326Z",
				"updated_at": "2023-07-26T08:44:37.326Z",
				"permission_ids": [
					1,
					43,
					55,
					65
				],
				"knowledge_base_permission_ids": [],
				"group_ids": {}
			},
			"2": {
				"id": 2,
				"name": "Agent",
				"preferences": {},
				"default_at_signup": false,
				"active": true,
				"note": "To work on Tickets.",
				"updated_by_id": 1,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:37.362Z",
				"updated_at": "2023-07-26T08:44:37.362Z",
				"permission_ids": [
					43,
					57,
					60,
					62,
					66
				],
				"knowledge_base_permission_ids": [],
				"group_ids": {}
			},
			"3": {
				"id": 3,
				"name": "Customer",
				"preferences": {},
				"default_at_signup": true,
				"active": true,
				"note": "People who create Tickets ask for help.",
				"updated_by_id": 1,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:37.379Z",
				"updated_at": "2023-07-28T07:22:53.613Z",
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
		"Organization": {
			"2": {
				"name": "Chrispresso Inc.",
				"shared": true,
				"domain": "",
				"domain_assignment": false,
				"active": true,
				"note": "Manufacturer of individual coffee products.",
				"vip": false,
				"updated_by_id": 3,
				"id": 2,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:48.617Z",
				"updated_at": "2023-08-04T12:01:44.370Z",
				"member_ids": [
					3,
					4,
					5
				],
				"secondary_member_ids": []
			},
			"1": {
				"id": 1,
				"name": "Zammad Foundation",
				"shared": true,
				"domain": "",
				"domain_assignment": false,
				"active": true,
				"note": "",
				"updated_by_id": 1,
				"created_by_id": 1,
				"created_at": "2023-07-26T08:44:39.608Z",
				"updated_at": "2023-08-04T12:02:00.018Z",
				"vip": false,
				"member_ids": [
					2
				],
				"secondary_member_ids": []
			}
		}
	}
   }


Add
===

Required permission: ``ticket.agent`` **or** ``admin``

``POST``-Request sent: ``/api/v1/links/add``

.. code-block:: json
   :force:

   {
      "link_type": "normal",
      "link_object_target": "Ticket",
      "link_object_target_value": 11,
      "link_object_source": "Ticket",
      "link_object_source_number": "93010"
   }

.. note:: The value for ``link_object_target`` has to be the *ticket ID*. The
   value for the ``link_object_source_number`` has to be ticket *ticket number*. 

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 11,
      "link_type_id": 1,
      "link_object_source_id": 1,
      "link_object_source_value": 10,
      "link_object_target_id": 1,
      "link_object_target_value": 11,
      "created_at": "2023-08-08T11:46:44.108Z",
      "updated_at": "2023-08-08T11:46:44.108Z"
   }

Delete
======

Required permission: ``ticket.agent`` **or** ``admin``

``DELETE``-Request sent: ``/api/v1/links/remove``

.. code-block:: json
   :force:

   {
      "link_type": "normal",
      "link_object_source": "Ticket",
      "link_object_source_value": 93010,
      "link_object_target": "Ticket",
      "link_object_target_value": 11
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   { }
