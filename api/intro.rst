Introduction
============

Zammad provides a powerful REST-API which allows all operations that
are available via UI as well.

This page gives you a first impression for things that generally count for
all endpoints and how to adapt.

API clients
-----------

There are API clients available.
Please note that these clients may not provide access to all available
endpoints listed here.

   * `Ruby Client <https://github.com/zammad/zammad-api-client-ruby>`_
     *(Official)*
   * `PHP Client <https://github.com/zammad/zammad-api-client-php>`_
     *(Official)*
   * `Python Client <https://pypi.org/project/zammad-py/>`_ *(Third-Party)*
   * `.NET Client <https://github.com/Asesjix/Zammad-Client>`_ *(Third-Party)*
   * `Android API-Client <https://github.com/KirkBushman/zammad-android>`_
     *(Third-Party)*
   * `Go Client <https://github.com/AlessandroSechi/zammad-go>`_
     *(Third-Party; API client only, no "ready to use" App)*


Authentication
--------------

Zammad supports three different authentication methods for its API.


HTTP Basic Authentication (username/password)
   | The username / password must be provided as HTTP header in the HTTP call.
   | This authentication method can be disabled and may not be available in your
     system.

   .. code-block:: sh

      $ curl -u {username}:{password} https://{fqdn}/{endpoint}

   .. note::

      We strongly suggest against using basic authentication.
      Use access tokens when ever possible!

HTTP Token Authentication (access token)
   | The access token must be provided as HTTP header in the HTTP call.
   | Each user can create several access tokens in their user preferences.
   | This authentication method can be disabled and may not be available in your
     system.

   .. code-block:: sh

      $ curl -H "Authorization: Token token={your_token}" https://{fqdn}/{endpoint}


OAuth2 (token access)
   | The token must be provided as HTTP header in your calls.
   | This allows 3rd party applications to authenticate against Zammad.

   .. code-block:: sh

      $ curl -H "Authorization: Bearer {your_token}" https://{fqdn}/{endpoint}

Endpoints and Example Data
--------------------------

For simplicity we'll not provide specific commands on the next pages, but
instead tell the possible call method (e.g. ``GET``) and the endpoint to use
(e.g. ``/api/v1/users``). In case Zammad expects information within these
endpoint urls, we'll put them into curly braces like so:
``/api/v1/users/{user id}``

The response format will be a complete JSON response from a default Zammad
instance. Please keep in mind that you may see more fields or general
information in case you added objects or other information.

Content Type
------------

Zammad returns JSON payloads whenever you retrieve data.
If you're going to provide data, no matter of the general request type,
don't forget to provide the content type ``application/json`` as well.

Response Payloads (Expand)
--------------------------

Zammad always returns information including hints to all relations.
If you need more information than that (because IDs may not be enough) you
can also extend your endpoint calls with ``?expand=true``.

This switch will provide even more information — at least named relations on
top of the ID ones. Below you can find two examples to compare - one for ticket
and user each.

.. tabs::

   .. tab:: User payload

      .. tabs::

         .. tab:: ``?expand=false``

            .. code-block:: json

               {
                  "login_failed": 0,
                  "last_login": "2025-06-30T11:45:19.503Z",
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
                  "source": null,
                  "out_of_office": false,
                  "out_of_office_start_at": null,
                  "out_of_office_end_at": null,
                  "out_of_office_replacement_id": null,
                  "preferences": {
                     "locale": "de-de",
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
                     "keyboard_shortcuts_clues": true,
                     "theme": "light"
                  },
                  "created_by_id": 1,
                  "created_at": "2025-06-24T10:46:48.487Z",
                  "updated_at": "2025-06-30T11:45:19.549Z",
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
               }

         .. tab:: ``?expand=true``

            .. code-block:: json

               {
                  "login_failed": 0,
                  "last_login": "2025-06-30T11:45:19.503Z",
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
                  "source": null,
                  "out_of_office": false,
                  "out_of_office_start_at": null,
                  "out_of_office_end_at": null,
                  "out_of_office_replacement_id": null,
                  "preferences": {
                     "locale": "de-de",
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
                     "keyboard_shortcuts_clues": true,
                     "theme": "light"
                  },
                  "created_by_id": 1,
                  "created_at": "2025-06-24T10:46:48.487Z",
                  "updated_at": "2025-06-30T11:45:19.549Z",
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
                  },
                  "roles": [
                     "Admin",
                     "Agent"
                  ],
                  "two_factor_preferences": [],
                  "organizations": [],
                  "authorizations": [],
                  "overview_sortings": [],
                  "organization": "Chrispresso Inc.",
                  "groups": {
                     "Sales": [
                        "full"
                     ],
                     "2nd Level": [
                        "full"
                     ],
                     "Service Desk": [
                        "full"
                     ]
                  },
                  "created_by": "-",
                  "updated_by": "-"
               }


   .. tab:: Ticket payload

      .. tabs::

         .. tab:: ``?expand=false``

            .. code-block:: json

               {
                  "id": 3,
                  "group_id": 1,
                  "priority_id": 2,
                  "state_id": 4,
                  "organization_id": 3,
                  "number": "53003",
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
                  "last_close_at": null,
                  "last_contact_at": "2025-01-24T08:46:58.510Z",
                  "last_contact_agent_at": "2025-01-24T08:46:58.510Z",
                  "last_contact_customer_at": "2025-01-22T10:46:58.255Z",
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
                  "created_at": "2025-01-22T10:46:58.255Z",
                  "updated_at": "2025-06-24T10:46:58.554Z",
                  "checklist_id": null
               }

         .. tab:: ``?expand=true``

            .. code-block:: json

               {
                  "id": 3,
                  "group_id": 1,
                  "priority_id": 2,
                  "state_id": 4,
                  "organization_id": 3,
                  "number": "53003",
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
                  "last_close_at": null,
                  "last_contact_at": "2025-01-24T08:46:58.510Z",
                  "last_contact_agent_at": "2025-01-24T08:46:58.510Z",
                  "last_contact_customer_at": "2025-01-22T10:46:58.255Z",
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
                  "created_at": "2025-01-22T10:46:58.255Z",
                  "updated_at": "2025-06-24T10:46:58.554Z",
                  "checklist_id": null,
                  "referencing_checklist_ids": [],
                  "article_ids": [
                     5,
                     6
                  ],
                  "ticket_time_accounting_ids": [],
                  "ai_stored_result_ids": [],
                  "referencing_checklists": [],
                  "group": "Sales",
                  "organization": "Awesome Customer Inc.",
                  "ticket_time_accounting": [],
                  "state": "closed",
                  "priority": "2 normal",
                  "owner": "chris@chrispresso.com",
                  "customer": "samuel@example.com",
                  "created_by": "samuel@example.com",
                  "updated_by": "jacob@chrispresso.com",
                  "create_article_type": "email",
                  "create_article_sender": "Customer",
                  "ai_stored_results": []
               }

.. warning::

   Please note that Core Workflows may restrict access to attributes or values.
   See :admin-docs:`Core Workflows limitations </system/core-workflows/limitations.html>`
   to learn more.

Pagination
----------

As Zammad limits the number of returned objects for performance reasons, you
may have to use pagination at some points.

.. note::

   **Number of returned objects:** Zammad has hard limits for the maximum
   returned objects. You can't raise these limits.

   **Number of total to return objects:** Zammad does not provide a total
   count of objects available for your query, unless you explicitly request it.
   To include the amount of search results, use the ``with_total_count`` or
   ``only_total_count`` parameter.

In order to use pagination you'll need two get options:
``per_page`` and ``page``. Combine them like so to receive 5 results from
the first result page: ``?page=1&per_page=5`` - count page up to get
more results.

Search via API
--------------

Endpoint Search
^^^^^^^^^^^^^^^

Some endpoints support a search query. These are:

- :doc:`Groups <group>`
- :doc:`Organizations <organization>`
- :doc:`Roles <role>`
- :doc:`Tickets <ticket>`
- :doc:`Users <user>`

The following endpoints support a search query as well, but they are not
explicitly covered in this documentation:

- Chat Sessions
- Knowledgebase
- Macros
- Overview
- Templates
- Text module



Search example
   ``GET``-Request sent: ``/api/v1/tickets/search?query=welcome``

   Response:

   .. code-block:: json

      [
         {
            "id": 1,
            "group_id": 1,
            "priority_id": 2,
            "state_id": 1,
            "organization_id": 1,
            "number": "20001",
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
            "last_close_at": null,
            "last_contact_at": "2025-01-14T07:45:08.726Z",
            "last_contact_agent_at": null,
            "last_contact_customer_at": "2025-01-14T07:45:08.726Z",
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
            "created_at": "2025-01-14T07:45:08.681Z",
            "updated_at": "2025-01-14T07:45:08.790Z",
            "checklist_id": null,
            "referencing_checklist_ids": [],
            "article_ids": [
               1
            ],
            "ticket_time_accounting_ids": []
         }
      ]

``Expand`` Parameter
   If you want to have additional related information, you can use
   the ``expand`` parameter. Using it resolves the IDs and outputs values/names
   in addition.

   ``GET``-Request sent: ``/api/v1/tickets/search?query=welcome&expand=true``

   .. code-block:: json

      [
         {
            "id": 1,
            "group_id": 1,
            "priority_id": 2,
            "state_id": 1,
            "organization_id": 1,
            "number": "20001",
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
            "last_close_at": null,
            "last_contact_at": "2025-01-14T07:45:08.726Z",
            "last_contact_agent_at": null,
            "last_contact_customer_at": "2025-01-14T07:45:08.726Z",
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
            "created_at": "2025-01-14T07:45:08.681Z",
            "updated_at": "2025-01-14T07:45:08.790Z",
            "checklist_id": null,
            "referencing_checklist_ids": [],
            "article_ids": [
               1
            ],
            "ticket_time_accounting_ids": [],
            "referencing_checklists": [],
            "group": "Users",
            "organization": "Zammad Foundation",
            "ticket_time_accounting": [],
            "state": "new",
            "priority": "2 normal",
            "owner": "-",
            "customer": "nicole.braun@zammad.org",
            "created_by": "nicole.braun@zammad.org",
            "updated_by": "nicole.braun@zammad.org",
            "create_article_type": "phone",
            "create_article_sender": "Customer"
         }
      ]


``Full`` Parameter
   You can even extend the response by using the ``full`` parameter. Be aware
   that this response can be huge. It outputs all assets including related
   attributes and a ``total_count`` of search results as well.

   ``GET``-Request sent: ``/api/v1/tickets/search?query=welcome&full=true``

   Response:

   .. code-block:: json

      {
         "record_ids": [
            1
         ],
         "assets": {
            "Ticket": {
               "1": {
                  "id": 1,
                  "group_id": 1,
                  "priority_id": 2,
                  "state_id": 1,
                  "organization_id": 1,
                  "number": "20001",
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
                  "last_close_at": null,
                  "last_contact_at": "2025-01-14T07:45:08.726Z",
                  "last_contact_agent_at": null,
                  "last_contact_customer_at": "2025-01-14T07:45:08.726Z",
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
                  "created_at": "2025-01-14T07:45:08.681Z",
                  "updated_at": "2025-01-14T07:45:08.790Z",
                  "checklist_id": null,
                  "referencing_checklist_ids": [],
                  "article_ids": [
                     1
                  ],
                  "ticket_time_accounting_ids": []
               }
            },
            "Group": {
               "1": {
                  "id": 1,
                  "signature_id": 1,
                  "email_address_id": 1,
                  "name": "Users",
                  "name_last": "Users",
                  "parent_id": null,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": "Standard Group/Pool for Tickets.",
                  "updated_by_id": 3,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:45:08.274Z",
                  "updated_at": "2025-01-14T07:46:20.513Z",
                  "user_ids": [
                     3
                  ]
               },
               "2": {
                  "id": 2,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Support",
                  "name_last": "Support",
                  "parent_id": null,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:20.548Z",
                  "updated_at": "2025-01-14T07:46:20.636Z",
                  "user_ids": [
                     4,
                     10,
                     3
                  ]
               },
               "3": {
                  "id": 3,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Support::1st Level",
                  "name_last": "1st Level",
                  "parent_id": 2,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:20.696Z",
                  "updated_at": "2025-01-14T07:46:20.895Z",
                  "user_ids": [
                     7,
                     6,
                     8,
                     4,
                     9,
                     5,
                     10,
                     3
                  ]
               },
               "4": {
                  "id": 4,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Support::2nd Level",
                  "name_last": "2nd Level",
                  "parent_id": 2,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:20.946Z",
                  "updated_at": "2025-01-14T07:46:21.085Z",
                  "user_ids": [
                     7,
                     6,
                     4,
                     5,
                     10,
                     3
                  ]
               },
               "5": {
                  "id": 5,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Sales",
                  "name_last": "Sales",
                  "parent_id": null,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.149Z",
                  "updated_at": "2025-01-14T07:46:21.249Z",
                  "user_ids": [
                     14,
                     13,
                     10,
                     3
                  ]
               },
               "6": {
                  "id": 6,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Logistics Department",
                  "name_last": "Logistics Department",
                  "parent_id": null,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.307Z",
                  "updated_at": "2025-01-14T07:46:21.389Z",
                  "user_ids": [
                     13,
                     10,
                     3
                  ]
               },
               "7": {
                  "id": 7,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Logistics Department::Shipping",
                  "name_last": "Shipping",
                  "parent_id": 6,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.447Z",
                  "updated_at": "2025-01-14T07:46:21.531Z",
                  "user_ids": [
                     13,
                     10,
                     3
                  ]
               },
               "8": {
                  "id": 8,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "Logistics Department::Returns Processing",
                  "name_last": "Returns Processing",
                  "parent_id": 6,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.570Z",
                  "updated_at": "2025-01-14T07:46:21.633Z",
                  "user_ids": [
                     13,
                     10,
                     3
                  ]
               },
               "9": {
                  "id": 9,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "IT Internal",
                  "name_last": "IT Internal",
                  "parent_id": null,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.673Z",
                  "updated_at": "2025-01-14T07:46:21.761Z",
                  "user_ids": [
                     11,
                     10,
                     3
                  ]
               },
               "10": {
                  "id": 10,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "IT Internal::Infrastructure",
                  "name_last": "Infrastructure",
                  "parent_id": 9,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.813Z",
                  "updated_at": "2025-01-14T07:46:21.881Z",
                  "user_ids": [
                     11,
                     10,
                     3
                  ]
               },
               "11": {
                  "id": 11,
                  "signature_id": null,
                  "email_address_id": null,
                  "name": "IT Internal::IT Support",
                  "name_last": "IT Support",
                  "parent_id": 9,
                  "assignment_timeout": null,
                  "follow_up_possible": "yes",
                  "reopen_time_in_days": null,
                  "follow_up_assignment": true,
                  "active": true,
                  "shared_drafts": true,
                  "note": null,
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:21.932Z",
                  "updated_at": "2025-01-14T07:46:21.995Z",
                  "user_ids": [
                     12,
                     10,
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
                  "created_at": "2025-01-14T07:45:07.542Z",
                  "updated_at": "2025-01-14T07:45:07.542Z",
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
                  "login": "lauren@fastlane.inc",
                  "firstname": "Lauren",
                  "lastname": "Brooks",
                  "email": "lauren@fastlane.inc",
                  "image": "775c807d577dbd6bd95569ec1872f338",
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
                  "last_login": "2025-01-14T07:46:54.082Z",
                  "source": null,
                  "login_failed": 0,
                  "out_of_office": false,
                  "out_of_office_start_at": null,
                  "out_of_office_end_at": null,
                  "out_of_office_replacement_id": null,
                  "preferences": {
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "created_at": "2025-01-14T07:46:17.855Z",
                  "updated_at": "2025-01-14T07:46:58.108Z",
                  "role_ids": [
                     2,
                     1
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
                     ],
                     "4": [
                        "full"
                     ],
                     "5": [
                        "full"
                     ],
                     "6": [
                        "full"
                     ],
                     "7": [
                        "full"
                     ],
                     "8": [
                        "full"
                     ],
                     "9": [
                        "full"
                     ],
                     "10": [
                        "full"
                     ],
                     "11": [
                        "full"
                     ]
                  }
               },
               "4": {
                  "id": 4,
                  "organization_id": 2,
                  "login": "ethan@fastlane.inc",
                  "firstname": "Ethan",
                  "lastname": "Kwan",
                  "email": "ethan@fastlane.inc",
                  "image": "3c3a37e93647e40c595937e336953de8",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:18.901Z",
                  "updated_at": "2025-01-14T07:46:26.067Z",
                  "role_ids": [
                     2
                  ],
                  "two_factor_preference_ids": [],
                  "organization_ids": [],
                  "authorization_ids": [],
                  "overview_sorting_ids": [],
                  "group_ids": {
                     "2": [
                        "full"
                     ],
                     "3": [
                        "full"
                     ],
                     "4": [
                        "full"
                     ]
                  }
               },
               "5": {
                  "id": 5,
                  "organization_id": 2,
                  "login": "julian@fastlane.inc",
                  "firstname": "Julian",
                  "lastname": "Reyes",
                  "email": "julian@fastlane.inc",
                  "image": "5ead44f8048cd52d94198bbb7aa1c0cc",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.051Z",
                  "updated_at": "2025-01-14T07:46:26.113Z",
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
                     "4": [
                        "full"
                     ]
                  }
               },
               "6": {
                  "id": 6,
                  "organization_id": 2,
                  "login": "thomas@fastlane.inc",
                  "firstname": "Thomas",
                  "lastname": "Lee",
                  "email": "thomas@fastlane.inc",
                  "image": "32340889dbe9bc093f9304d1f708ca6f",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.161Z",
                  "updated_at": "2025-01-14T07:46:26.156Z",
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
                     "4": [
                        "full"
                     ]
                  }
               },
               "7": {
                  "id": 7,
                  "organization_id": 2,
                  "login": "liam@fastlane.inc",
                  "firstname": "Liam",
                  "lastname": "Chen",
                  "email": "liam@fastlane.inc",
                  "image": "548f5e2072493a829319359384ba3c49",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.288Z",
                  "updated_at": "2025-01-14T07:46:26.202Z",
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
                     "4": [
                        "full"
                     ]
                  }
               },
               "8": {
                  "id": 8,
                  "organization_id": 2,
                  "login": "alex@fastlane.inc",
                  "firstname": "Alexander",
                  "lastname": "Jensen",
                  "email": "alex@fastlane.inc",
                  "image": "8e837e5b08ef314f920f13e6b8e44b3f",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.401Z",
                  "updated_at": "2025-01-14T07:46:26.245Z",
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
                     ]
                  }
               },
               "9": {
                  "id": 9,
                  "organization_id": 2,
                  "login": "emily@fastlane.inc",
                  "firstname": "Emily",
                  "lastname": "Wilson",
                  "email": "emily@fastlane.inc",
                  "image": "f527a90b9dc0c731005f5756bbd5a432",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.514Z",
                  "updated_at": "2025-01-14T07:46:26.301Z",
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
                     ]
                  }
               },
               "10": {
                  "id": 10,
                  "organization_id": 2,
                  "login": "hannah@fastlane.inc",
                  "firstname": "Hannah",
                  "lastname": "Taylor",
                  "email": "hannah@fastlane.inc",
                  "image": "7b590e70915e7c33fff328f7e8fa0bb9",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.638Z",
                  "updated_at": "2025-01-14T07:46:26.406Z",
                  "role_ids": [
                     2,
                     1
                  ],
                  "two_factor_preference_ids": [],
                  "organization_ids": [],
                  "authorization_ids": [],
                  "overview_sorting_ids": [],
                  "group_ids": {
                     "2": [
                        "full"
                     ],
                     "3": [
                        "full"
                     ],
                     "4": [
                        "full"
                     ],
                     "5": [
                        "full"
                     ],
                     "6": [
                        "full"
                     ],
                     "7": [
                        "full"
                     ],
                     "8": [
                        "full"
                     ],
                     "9": [
                        "full"
                     ],
                     "10": [
                        "full"
                     ],
                     "11": [
                        "full"
                     ]
                  }
               },
               "11": {
                  "id": 11,
                  "organization_id": 2,
                  "login": "jackson@fastlane.inc",
                  "firstname": "Jackson",
                  "lastname": "Lee",
                  "email": "jackson@fastlane.inc",
                  "image": "f60bee881cf1856275d4f770ab9f6063",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.779Z",
                  "updated_at": "2025-01-14T07:46:26.451Z",
                  "role_ids": [
                     2,
                     1
                  ],
                  "two_factor_preference_ids": [],
                  "organization_ids": [],
                  "authorization_ids": [],
                  "overview_sorting_ids": [],
                  "group_ids": {
                     "9": [
                        "full"
                     ],
                     "10": [
                        "full"
                     ]
                  }
               },
               "12": {
                  "id": 12,
                  "organization_id": 2,
                  "login": "emily.t@fastlane.inc",
                  "firstname": "Emily",
                  "lastname": "Tran",
                  "email": "emily.t@fastlane.inc",
                  "image": "c9a8e23fe76079f0d249c87bcd145f95",
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
                     "intro": true,
                     "keyboard_shortcuts_clues": true,
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
                  "updated_by_id": 3,
                  "created_by_id": 3,
                  "created_at": "2025-01-14T07:46:19.893Z",
                  "updated_at": "2025-01-14T07:46:26.493Z",
                  "role_ids": [
                     2,
                     1
                  ],
                  "two_factor_preference_ids": [],
                  "organization_ids": [],
                  "authorization_ids": [],
                  "overview_sorting_ids": [],
                  "group_ids": {
                     "11": [
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
                     "tickets_closed": 0,
                     "tickets_open": 1
                  },
                  "updated_by_id": 2,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:45:08.641Z",
                  "updated_at": "2025-01-14T07:45:20.373Z",
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
               "2": {
                  "id": 2,
                  "name": "Agent",
                  "preferences": {},
                  "default_at_signup": false,
                  "active": true,
                  "note": "To work on Tickets.",
                  "updated_by_id": 3,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:45:07.649Z",
                  "updated_at": "2025-01-14T07:46:18.906Z",
                  "permission_ids": [
                     53,
                     55,
                     58,
                     61,
                     63
                  ],
                  "knowledge_base_permission_ids": [],
                  "group_ids": {}
               },
               "1": {
                  "id": 1,
                  "name": "Admin",
                  "preferences": {},
                  "default_at_signup": false,
                  "active": true,
                  "note": "To configure your system.",
                  "updated_by_id": 3,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:45:07.630Z",
                  "updated_at": "2025-01-14T07:46:19.646Z",
                  "permission_ids": [
                     1,
                     57,
                     59,
                     63
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
                  "updated_by_id": 3,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:45:07.659Z",
                  "updated_at": "2025-01-14T07:46:20.165Z",
                  "permission_ids": [
                     62,
                     64,
                     65,
                     66,
                     68,
                     69,
                     72
                  ],
                  "knowledge_base_permission_ids": [],
                  "group_ids": {}
               }
            },
            "Organization": {
               "2": {
                  "id": 2,
                  "name": "Fast Lane Hardware",
                  "shared": true,
                  "domain": "",
                  "domain_assignment": false,
                  "active": true,
                  "vip": false,
                  "note": "IT hardware and custom PC builds",
                  "updated_by_id": 1,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:46:17.574Z",
                  "updated_at": "2025-01-14T07:46:17.574Z",
                  "member_ids": [
                     3,
                     4,
                     5,
                     6,
                     7,
                     8,
                     9,
                     10,
                     11,
                     12,
                     13,
                     14
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
                  "vip": false,
                  "note": "",
                  "updated_by_id": 1,
                  "created_by_id": 1,
                  "created_at": "2025-01-14T07:45:08.597Z",
                  "updated_at": "2025-01-14T07:45:08.699Z",
                  "member_ids": [
                     2
                  ],
                  "secondary_member_ids": []
               }
            }
         },
         "total_count": 1
      }

``With Total Count`` Parameter
   Using this parameter will additionally output the amount of search results.
   It can be combined with ``full`` and ``expand``.

   ``GET``-Request sent: ``/api/v1/tickets/search?query=welcome&full=true&with_total_count=true``

   .. code-block:: json

      {
         "record_ids": [
            2,
            1
         ],
         "assets": {
            "Ticket": {
               "1": {
               "id": 1,
               "group_id": 1,
               "priority_id": 2,
               "state_id": 1,
               "organization_id": 1,
               "number": "97001",
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
               "last_close_at": null,
               "last_contact_at": "2025-06-27T08:35:35.210Z",
               "last_contact_agent_at": null,
               "last_contact_customer_at": "2025-06-27T08:35:35.210Z",
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
               "created_at": "2025-06-27T08:35:35.005Z",
               "updated_at": "2025-06-27T08:35:35.306Z",
               "checklist_id": null,
               "referencing_checklist_ids": [],
               "article_ids": [
                  1
               ],
               "ticket_time_accounting_ids": [],
               "ai_stored_result_ids": []
               },
               "2": {
               "id": 2,
               "group_id": 1,
               "priority_id": 2,
               "state_id": 2,
               "organization_id": 1,
               "number": "97002",
               "title": "Welcome again",
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
               "last_close_at": null,
               "last_contact_at": "2025-07-02T11:46:41.117Z",
               "last_contact_agent_at": null,
               "last_contact_customer_at": "2025-07-02T11:46:41.117Z",
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
               "created_at": "2025-07-02T11:46:41.040Z",
               "updated_at": "2025-07-02T11:46:41.210Z",
               "checklist_id": null,
               "referencing_checklist_ids": [],
               "article_ids": [
                  2
               ],
               "ticket_time_accounting_ids": [],
               "ai_stored_result_ids": []
               }
            },
            "Organization": {
               "1": {
               "id": 1,
               "name": "Zammad Foundation",
               "shared": true,
               "domain": "",
               "domain_assignment": false,
               "active": true,
               "vip": false,
               "note": "",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2025-06-27T08:35:34.797Z",
               "updated_at": "2025-07-02T11:46:41.105Z",
               "member_ids": [
                  2
               ],
               "secondary_member_ids": []
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
               "created_at": "2025-06-27T08:35:31.793Z",
               "updated_at": "2025-06-27T08:35:31.793Z",
               "role_ids": [],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {}
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
                  "tickets_closed": 0,
                  "tickets_open": 2
               },
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2025-06-27T08:35:34.872Z",
               "updated_at": "2025-07-02T11:46:41.840Z",
               "role_ids": [
                  3
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {}
               },
               "3": {
               "login_failed": 0,
               "last_login": "2025-07-02T08:54:52.403Z",
               "updated_by_id": 1,
               "id": 3,
               "organization_id": null,
               "login": "admin@example.com",
               "firstname": "Test",
               "lastname": "Admin",
               "email": "admin@example.com",
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
               "source": null,
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
                  "keyboard_shortcuts_clues": true,
                  "overviews_last_used": {
                     "1": "2025-06-27T09:27:26.333Z",
                     "5": "2025-06-27T09:27:28.222Z"
                  },
                  "theme": "light"
               },
               "created_by_id": 1,
               "created_at": "2025-06-27T09:27:00.302Z",
               "updated_at": "2025-07-02T08:54:52.433Z",
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
                  ]
                  }
               }
            }
         },
         "total_count": 2
      }

``Only Total Count`` Parameter
   Using this parameter will output only the amount of search results.

   ``GET``-Request sent: ``/api/v1/tickets/search?query=welcome&only_total_count=true``

   .. code-block:: json

      {
         "total_count": 1
      }

Global Search
^^^^^^^^^^^^^

If you need to search not only in a specific object type, you can do so by
using the global search without specifying an object. The response may include
users, tickets, organizations, knowledgebase articles and answers and chats,
depending on your system and content. This global search behaves like the
search in Zammad's UI in the left task bar. The available parameters are
different to the ones for the endpoint search.

``GET``-Request sent: ``/api/v1/search?query=welcome``

.. code-block:: json

   {
      "assets": {
         "Ticket": {
            "1": {
               "id": 1,
               "group_id": 1,
               "priority_id": 2,
               "state_id": 1,
               "organization_id": 1,
               "number": "20001",
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
               "last_close_at": null,
               "last_contact_at": "2025-01-14T07:45:08.726Z",
               "last_contact_agent_at": null,
               "last_contact_customer_at": "2025-01-14T07:45:08.726Z",
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
               "created_at": "2025-01-14T07:45:08.681Z",
               "updated_at": "2025-01-14T07:45:08.790Z",
               "checklist_id": null,
               "referencing_checklist_ids": [],
               "article_ids": [
                  1
               ],
               "ticket_time_accounting_ids": []
            }
         },
         "Group": {
            "1": {
               "id": 1,
               "signature_id": 1,
               "email_address_id": 1,
               "name": "Users",
               "name_last": "Users",
               "parent_id": null,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": "Standard Group/Pool for Tickets.",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:45:08.274Z",
               "updated_at": "2025-01-14T07:46:20.513Z",
               "user_ids": [
                  3
               ]
            },
            "2": {
               "id": 2,
               "signature_id": null,
               "email_address_id": null,
               "name": "Support",
               "name_last": "Support",
               "parent_id": null,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:20.548Z",
               "updated_at": "2025-01-14T07:46:20.636Z",
               "user_ids": [
                  4,
                  10,
                  3
               ]
            },
            "3": {
               "id": 3,
               "signature_id": null,
               "email_address_id": null,
               "name": "Support::1st Level",
               "name_last": "1st Level",
               "parent_id": 2,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:20.696Z",
               "updated_at": "2025-01-14T07:46:20.895Z",
               "user_ids": [
                  7,
                  6,
                  8,
                  4,
                  9,
                  5,
                  10,
                  3
               ]
            },
            "4": {
               "id": 4,
               "signature_id": null,
               "email_address_id": null,
               "name": "Support::2nd Level",
               "name_last": "2nd Level",
               "parent_id": 2,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:20.946Z",
               "updated_at": "2025-01-14T07:46:21.085Z",
               "user_ids": [
                  7,
                  6,
                  4,
                  5,
                  10,
                  3
               ]
            },
            "5": {
               "id": 5,
               "signature_id": null,
               "email_address_id": null,
               "name": "Sales",
               "name_last": "Sales",
               "parent_id": null,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.149Z",
               "updated_at": "2025-01-14T07:46:21.249Z",
               "user_ids": [
                  14,
                  13,
                  10,
                  3
               ]
            },
            "6": {
               "id": 6,
               "signature_id": null,
               "email_address_id": null,
               "name": "Logistics Department",
               "name_last": "Logistics Department",
               "parent_id": null,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.307Z",
               "updated_at": "2025-01-14T07:46:21.389Z",
               "user_ids": [
                  13,
                  10,
                  3
               ]
            },
            "7": {
               "id": 7,
               "signature_id": null,
               "email_address_id": null,
               "name": "Logistics Department::Shipping",
               "name_last": "Shipping",
               "parent_id": 6,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.447Z",
               "updated_at": "2025-01-14T07:46:21.531Z",
               "user_ids": [
                  13,
                  10,
                  3
               ]
            },
            "8": {
               "id": 8,
               "signature_id": null,
               "email_address_id": null,
               "name": "Logistics Department::Returns Processing",
               "name_last": "Returns Processing",
               "parent_id": 6,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.570Z",
               "updated_at": "2025-01-14T07:46:21.633Z",
               "user_ids": [
                  13,
                  10,
                  3
               ]
            },
            "9": {
               "id": 9,
               "signature_id": null,
               "email_address_id": null,
               "name": "IT Internal",
               "name_last": "IT Internal",
               "parent_id": null,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.673Z",
               "updated_at": "2025-01-14T07:46:21.761Z",
               "user_ids": [
                  11,
                  10,
                  3
               ]
            },
            "10": {
               "id": 10,
               "signature_id": null,
               "email_address_id": null,
               "name": "IT Internal::Infrastructure",
               "name_last": "Infrastructure",
               "parent_id": 9,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.813Z",
               "updated_at": "2025-01-14T07:46:21.881Z",
               "user_ids": [
                  11,
                  10,
                  3
               ]
            },
            "11": {
               "id": 11,
               "signature_id": null,
               "email_address_id": null,
               "name": "IT Internal::IT Support",
               "name_last": "IT Support",
               "parent_id": 9,
               "assignment_timeout": null,
               "follow_up_possible": "yes",
               "reopen_time_in_days": null,
               "follow_up_assignment": true,
               "active": true,
               "shared_drafts": true,
               "note": null,
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:21.932Z",
               "updated_at": "2025-01-14T07:46:21.995Z",
               "user_ids": [
                  12,
                  10,
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
               "created_at": "2025-01-14T07:45:07.542Z",
               "updated_at": "2025-01-14T07:45:07.542Z",
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
               "login": "lauren@fastlane.inc",
               "firstname": "Lauren",
               "lastname": "Brooks",
               "email": "lauren@fastlane.inc",
               "image": "775c807d577dbd6bd95569ec1872f338",
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
               "last_login": "2025-01-14T07:46:54.082Z",
               "source": null,
               "login_failed": 0,
               "out_of_office": false,
               "out_of_office_start_at": null,
               "out_of_office_end_at": null,
               "out_of_office_replacement_id": null,
               "preferences": {
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "created_at": "2025-01-14T07:46:17.855Z",
               "updated_at": "2025-01-14T07:46:58.108Z",
               "role_ids": [
                  2,
                  1
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
                  ],
                  "4": [
                     "full"
                  ],
                  "5": [
                     "full"
                  ],
                  "6": [
                     "full"
                  ],
                  "7": [
                     "full"
                  ],
                  "8": [
                     "full"
                  ],
                  "9": [
                     "full"
                  ],
                  "10": [
                     "full"
                  ],
                  "11": [
                     "full"
                  ]
               }
            },
            "4": {
               "id": 4,
               "organization_id": 2,
               "login": "ethan@fastlane.inc",
               "firstname": "Ethan",
               "lastname": "Kwan",
               "email": "ethan@fastlane.inc",
               "image": "3c3a37e93647e40c595937e336953de8",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:18.901Z",
               "updated_at": "2025-01-14T07:46:26.067Z",
               "role_ids": [
                  2
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {
                  "2": [
                     "full"
                  ],
                  "3": [
                     "full"
                  ],
                  "4": [
                     "full"
                  ]
               }
            },
            "5": {
               "id": 5,
               "organization_id": 2,
               "login": "julian@fastlane.inc",
               "firstname": "Julian",
               "lastname": "Reyes",
               "email": "julian@fastlane.inc",
               "image": "5ead44f8048cd52d94198bbb7aa1c0cc",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.051Z",
               "updated_at": "2025-01-14T07:46:26.113Z",
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
                  "4": [
                     "full"
                  ]
               }
            },
            "6": {
               "id": 6,
               "organization_id": 2,
               "login": "thomas@fastlane.inc",
               "firstname": "Thomas",
               "lastname": "Lee",
               "email": "thomas@fastlane.inc",
               "image": "32340889dbe9bc093f9304d1f708ca6f",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.161Z",
               "updated_at": "2025-01-14T07:46:26.156Z",
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
                  "4": [
                     "full"
                  ]
               }
            },
            "7": {
               "id": 7,
               "organization_id": 2,
               "login": "liam@fastlane.inc",
               "firstname": "Liam",
               "lastname": "Chen",
               "email": "liam@fastlane.inc",
               "image": "548f5e2072493a829319359384ba3c49",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.288Z",
               "updated_at": "2025-01-14T07:46:26.202Z",
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
                  "4": [
                     "full"
                  ]
               }
            },
            "8": {
               "id": 8,
               "organization_id": 2,
               "login": "alex@fastlane.inc",
               "firstname": "Alexander",
               "lastname": "Jensen",
               "email": "alex@fastlane.inc",
               "image": "8e837e5b08ef314f920f13e6b8e44b3f",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.401Z",
               "updated_at": "2025-01-14T07:46:26.245Z",
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
                  ]
               }
            },
            "9": {
               "id": 9,
               "organization_id": 2,
               "login": "emily@fastlane.inc",
               "firstname": "Emily",
               "lastname": "Wilson",
               "email": "emily@fastlane.inc",
               "image": "f527a90b9dc0c731005f5756bbd5a432",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.514Z",
               "updated_at": "2025-01-14T07:46:26.301Z",
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
                  ]
               }
            },
            "10": {
               "id": 10,
               "organization_id": 2,
               "login": "hannah@fastlane.inc",
               "firstname": "Hannah",
               "lastname": "Taylor",
               "email": "hannah@fastlane.inc",
               "image": "7b590e70915e7c33fff328f7e8fa0bb9",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.638Z",
               "updated_at": "2025-01-14T07:46:26.406Z",
               "role_ids": [
                  2,
                  1
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {
                  "2": [
                     "full"
                  ],
                  "3": [
                     "full"
                  ],
                  "4": [
                     "full"
                  ],
                  "5": [
                     "full"
                  ],
                  "6": [
                     "full"
                  ],
                  "7": [
                     "full"
                  ],
                  "8": [
                     "full"
                  ],
                  "9": [
                     "full"
                  ],
                  "10": [
                     "full"
                  ],
                  "11": [
                     "full"
                  ]
               }
            },
            "11": {
               "id": 11,
               "organization_id": 2,
               "login": "jackson@fastlane.inc",
               "firstname": "Jackson",
               "lastname": "Lee",
               "email": "jackson@fastlane.inc",
               "image": "f60bee881cf1856275d4f770ab9f6063",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.779Z",
               "updated_at": "2025-01-14T07:46:26.451Z",
               "role_ids": [
                  2,
                  1
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {
                  "9": [
                     "full"
                  ],
                  "10": [
                     "full"
                  ]
               }
            },
            "12": {
               "id": 12,
               "organization_id": 2,
               "login": "emily.t@fastlane.inc",
               "firstname": "Emily",
               "lastname": "Tran",
               "email": "emily.t@fastlane.inc",
               "image": "c9a8e23fe76079f0d249c87bcd145f95",
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
                  "intro": true,
                  "keyboard_shortcuts_clues": true,
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
               "updated_by_id": 3,
               "created_by_id": 3,
               "created_at": "2025-01-14T07:46:19.893Z",
               "updated_at": "2025-01-14T07:46:26.493Z",
               "role_ids": [
                  2,
                  1
               ],
               "two_factor_preference_ids": [],
               "organization_ids": [],
               "authorization_ids": [],
               "overview_sorting_ids": [],
               "group_ids": {
                  "11": [
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
                  "tickets_closed": 0,
                  "tickets_open": 1
               },
               "updated_by_id": 2,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:45:08.641Z",
               "updated_at": "2025-01-14T07:45:20.373Z",
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
            "2": {
               "id": 2,
               "name": "Agent",
               "preferences": {},
               "default_at_signup": false,
               "active": true,
               "note": "To work on Tickets.",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:45:07.649Z",
               "updated_at": "2025-01-14T07:46:18.906Z",
               "permission_ids": [
                  53,
                  55,
                  58,
                  61,
                  63
               ],
               "knowledge_base_permission_ids": [],
               "group_ids": {}
            },
            "1": {
               "id": 1,
               "name": "Admin",
               "preferences": {},
               "default_at_signup": false,
               "active": true,
               "note": "To configure your system.",
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:45:07.630Z",
               "updated_at": "2025-01-14T07:46:19.646Z",
               "permission_ids": [
                  1,
                  57,
                  59,
                  63
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
               "updated_by_id": 3,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:45:07.659Z",
               "updated_at": "2025-01-14T07:46:20.165Z",
               "permission_ids": [
                  62,
                  64,
                  65,
                  66,
                  68,
                  69,
                  72
               ],
               "knowledge_base_permission_ids": [],
               "group_ids": {}
            }
         },
         "Organization": {
            "2": {
               "id": 2,
               "name": "Fast Lane Hardware",
               "shared": true,
               "domain": "",
               "domain_assignment": false,
               "active": true,
               "vip": false,
               "note": "IT hardware and custom PC builds",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:46:17.574Z",
               "updated_at": "2025-01-14T07:46:17.574Z",
               "member_ids": [
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,
                  9,
                  10,
                  11,
                  12,
                  13,
                  14
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
               "vip": false,
               "note": "",
               "updated_by_id": 1,
               "created_by_id": 1,
               "created_at": "2025-01-14T07:45:08.597Z",
               "updated_at": "2025-01-14T07:45:08.699Z",
               "member_ids": [
                  2
               ],
               "secondary_member_ids": []
            }
         }
      },
      "result": [
         {
            "type": "Ticket",
            "id": 1
         }
      ]
   }


Condition Based Search
^^^^^^^^^^^^^^^^^^^^^^

You can even use conditions like for triggers and schedulers to search via
API. If you don't want to build such conditions manually, you can find a hint
below how to quickly build a condition structure via UI and fetch it for you API
request.

So, how do I build such a condition based request?

- In Zammad, go to the admin interface and create a condition, e.g. by creating
  a new overview or trigger. It can be inactive so you won't have any unwanted
  actions or changes.
- Go to the :doc:`Rails console </admin/console>`, either by using ``rails c`` /
  ``zammad run rails c`` or adding the prefix ``rails r`` /
  ``zammad run rails r`` in front of the commands below, depending on your
  setup.
- Search for the created condition, adjust the following examples to your needs:

.. code-block:: ruby

   puts Overview.find_by(name: 'My test overview').attributes.slice('condition').to_json

.. code-block:: ruby

   puts Trigger.find_by(name: 'My new test trigger').attributes.slice('condition').to_json

This leads to an output like the following:

.. code-block:: json

   {"condition":{"ticket.state_id":{"operator":"is","value":["2"]},"ticket.title":{"operator":"contains","value":"Test"}}}

Use this as payload in your ``POST``-Request in an endpoint search. The response
includes the same objects as the trigger or overview you created.

.. _sort_search_results:

Sorting Search Results
----------------------

Zammad allows you to sort your search results by field if needed.

sort_by
   Append ``?sort_by={row name}`` to your query to sort by a specific row
   that appears in the search result.

order_by
   Append ``?order_by={direction}`` to your query to switch in between ascending
   and descending order.

   Directions are: ``asc`` and ``desc``.

.. note::

   Usually you'll want to combine both parameters in your searches - e.g.:
   ``?query={search string}&sort_by={row name}&order_by={direction}``

Actions On Behalf of Other Users
--------------------------------

**Requirement:** the user used for running the query on behalf requires
``admin.user`` permission.

Running API queries on behalf of other users allows you to e.g. create tickets
by a different user.

To do so, add a new HTTP header named ``From`` to your request.
The value of this header can be one of the following:

   * user ID
   * user login
   * user email

``From`` is available for all endpoints.

Encoding
--------

The API expects UTF-8 encoding.
Keep in mind that especially when using URLs with get options
(e.g. ``?query=this``) you may need to encode your URL accordingly.

If you want to learn more about URL encoding,
`this Wikipedia article <https://en.wikipedia.org/wiki/Percent-encoding>`_
may be of help
