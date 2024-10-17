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
                  "active": true,
                  "login_failed": 0,
                  "verified": false,
                  "source": null,
                  "login": "chris@chrispresso.com",
                  "last_login": "2021-09-23T13:17:24.817Z",
                  "id": 3,
                  "updated_by_id": 1,
                  "organization_id": 2,
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
                  "note": "",
                  "out_of_office": false,
                  "out_of_office_start_at": null,
                  "out_of_office_end_at": null,
                  "out_of_office_replacement_id": null,
                  "preferences":
                  {
                     "notification_config":
                     {
                        "matrix":
                        {
                           "create":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": true,
                                 "subscribed": true,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           },
                           "update":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": true,
                                 "subscribed": true,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           },
                           "reminder_reached":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": false,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           },
                           "escalation":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": false,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           }
                        },
                        "group_ids":
                        [
                           "2",
                           "1",
                           "3"
                        ]
                     },
                     "locale": "de-de",
                     "intro": true,
                     "notification_sound":
                     {
                        "file": "Xylo.mp3",
                        "enabled": true
                     },
                     "cti": true,
                     "tickets_closed": 0,
                     "tickets_open": 1
                  },
                  "created_by_id": 1,
                  "created_at": "2021-07-26T14:44:41.066Z",
                  "updated_at": "2021-09-23T13:17:24.825Z",
                  "role_ids":
                  [
                     1,
                     2
                  ],
                  "organization_ids":
                  [],
                  "authorization_ids":
                  [],
                  "karma_user_ids":
                  [
                     1
                  ],
                  "group_ids":
                  {
                     "1":
                     [
                        "full"
                     ],
                     "2":
                     [
                        "full"
                     ],
                     "3":
                     [
                        "full"
                     ]
                  }
               }

         .. tab:: ``?expand=true``

            .. code-block:: json

               {
                  "active": true,
                  "login_failed": 0,
                  "verified": false,
                  "source": null,
                  "login": "chris@chrispresso.com",
                  "last_login": "2021-09-23T13:17:24.817Z",
                  "id": 3,
                  "updated_by_id": 1,
                  "organization_id": 2,
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
                  "note": "",
                  "out_of_office": false,
                  "out_of_office_start_at": null,
                  "out_of_office_end_at": null,
                  "out_of_office_replacement_id": null,
                  "preferences":
                  {
                     "notification_config":
                     {
                        "matrix":
                        {
                           "create":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": true,
                                 "subscribed": true,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           },
                           "update":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": true,
                                 "subscribed": true,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           },
                           "reminder_reached":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": false,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           },
                           "escalation":
                           {
                              "criteria":
                              {
                                 "owned_by_me": true,
                                 "owned_by_nobody": false,
                                 "no": true
                              },
                              "channel":
                              {
                                 "email": true,
                                 "online": true
                              }
                           }
                        },
                        "group_ids":
                        [
                           "2",
                           "1",
                           "3"
                        ]
                     },
                     "locale": "de-de",
                     "intro": true,
                     "notification_sound":
                     {
                        "file": "Xylo.mp3",
                        "enabled": true
                     },
                     "cti": true,
                     "tickets_closed": 0,
                     "tickets_open": 1
                  },
                  "created_by_id": 1,
                  "created_at": "2021-07-26T14:44:41.066Z",
                  "updated_at": "2021-09-23T13:17:24.825Z",
                  "role_ids":
                  [
                     1,
                     2
                  ],
                  "organization_ids":
                  [],
                  "authorization_ids":
                  [],
                  "karma_user_ids":
                  [
                     1
                  ],
                  "group_ids":
                  {
                     "1":
                     [
                        "full"
                     ],
                     "2":
                     [
                        "full"
                     ],
                     "3":
                     [
                        "full"
                     ]
                  },
                  "roles":
                  [
                     "Admin",
                     "Agent"
                  ],
                  "organizations":
                  [],
                  "authorizations":
                  [],
                  "organization": "Chrispresso Inc.",
                  "groups":
                  {
                     "Sales":
                     [
                        "full"
                     ],
                     "2nd Level":
                     [
                        "full"
                     ],
                     "Service/Desk":
                     [
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
                  "number": "71003",
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
                  "last_contact_at": "2021-02-26T12:44:43.888Z",
                  "last_contact_agent_at": "2021-02-26T12:44:43.888Z",
                  "last_contact_customer_at": "2021-02-24T14:44:43.828Z",
                  "last_owner_update_at": null,
                  "create_article_type_id": 1,
                  "create_article_sender_id": 2,
                  "article_count": 2,
                  "escalation_at": null,
                  "pending_time": null,
                  "type": null,
                  "time_unit": null,
                  "preferences":
                  {},
                  "updated_by_id": 4,
                  "created_by_id": 7,
                  "created_at": "2021-02-24T14:44:43.828Z",
                  "updated_at": "2021-07-26T14:44:43.906Z"
               }

         .. tab:: ``?expand=true``

            .. code-block:: json

               {
                  "id": 3,
                  "group_id": 1,
                  "priority_id": 2,
                  "state_id": 4,
                  "organization_id": 3,
                  "number": "71003",
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
                  "last_contact_at": "2021-02-26T12:44:43.888Z",
                  "last_contact_agent_at": "2021-02-26T12:44:43.888Z",
                  "last_contact_customer_at": "2021-02-24T14:44:43.828Z",
                  "last_owner_update_at": null,
                  "create_article_type_id": 1,
                  "create_article_sender_id": 2,
                  "article_count": 2,
                  "escalation_at": null,
                  "pending_time": null,
                  "type": null,
                  "time_unit": null,
                  "preferences":
                  {},
                  "updated_by_id": 4,
                  "created_by_id": 7,
                  "created_at": "2021-02-24T14:44:43.828Z",
                  "updated_at": "2021-07-26T14:44:43.906Z",
                  "article_ids":
                  [
                     5,
                     6
                  ],
                  "ticket_time_accounting_ids":
                  [],
                  "group": "Sales",
                  "organization": "Awesome Customer Inc.",
                  "ticket_time_accounting":
                  [],
                  "state": "closed",
                  "priority": "2 normal",
                  "owner": "chris@chrispresso.com",
                  "customer": "samuel@example.com",
                  "created_by": "samuel@example.com",
                  "updated_by": "jacob@chrispresso.com",
                  "create_article_type": "email",
                  "create_article_sender": "Customer"
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
      count of objects available for your query. This forces you to cycle
      through the pages until Zammad no longer returns further objects.

In order to use pagination you'll need two get options:
``per_page`` and ``page``. Combine them like so to receive 5 results from
the first result page: ``?page=1&per_page=5`` - count page up to get
more results.

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
