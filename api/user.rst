User
====

.. note:: **🤓 To see or not to see**

   Please note that below samples were provided with ``admin`` and
   ``ticket.agent`` permissions. Some attributes / information may not be
   available in specific situations.

   Please see our :admin-docs:`Permission Guide </manage/roles/index.html#reference-guide-permissions>`
   to get better insights.

Me - Current User
-----------------

Required permission: any

``GET``-Request sent: ``/api/v1/users/me``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
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
      "last_login": "2021-11-03T12:26:53.410Z",
      "source": null,
      "login_failed": 0,
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
                     "no": false
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
                     "no": false
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
                     "subscribed": false,
                     "no": false
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
                     "subscribed": false,
                     "no": false
                  },
                  "channel":
                  {
                     "email": true,
                     "online": true
                  }
               }
            }
         },
         "locale": "en-us",
         "intro": true
      },
      "updated_by_id": 3,
      "created_by_id": 1,
      "created_at": "2021-11-03T11:57:15.975Z",
      "updated_at": "2021-11-03T12:26:55.642Z",
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
      [],
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


List
----

Required permission: ``ticket.agent`` **or** ``admin.user``

.. note:: Technically, any listings will return users own information only.

``GET``-Request sent: ``/api/v1/users``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
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
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:51:12.786Z",
         "updated_at": "2021-11-03T11:51:12.786Z",
         "role_ids":
         [],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
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
         "preferences":
         {
            "tickets_closed": 0,
            "tickets_open": 1
         },
         "updated_by_id": 2,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:51:13.703Z",
         "updated_at": "2021-11-03T12:01:05.411Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
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
         "last_login": "2021-11-03T12:26:53.410Z",
         "source": null,
         "login_failed": 0,
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
                        "no": false
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
                        "no": false
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
                        "subscribed": false,
                        "no": false
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
                        "subscribed": false,
                        "no": false
                     },
                     "channel":
                     {
                        "email": true,
                        "online": true
                     }
                  }
               }
            },
            "locale": "en-us",
            "intro": true
         },
         "updated_by_id": 3,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:15.975Z",
         "updated_at": "2021-11-03T12:26:55.642Z",
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
         [],
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
      },
      {
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
                        "no": false
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
                        "no": false
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
                        "subscribed": false,
                        "no": false
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
                        "subscribed": false,
                        "no": false
                     },
                     "channel":
                     {
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
         [],
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
      },
      {
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
                        "no": false
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
                        "no": false
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
                        "subscribed": false,
                        "no": false
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
                        "subscribed": false,
                        "no": false
                     },
                     "channel":
                     {
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
         "created_at": "2021-11-03T11:57:16.349Z",
         "updated_at": "2021-11-03T11:57:16.409Z",
         "role_ids":
         [
            2
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
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
      },
      {
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
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:16.526Z",
         "updated_at": "2021-11-03T11:57:16.611Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
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
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:16.748Z",
         "updated_at": "2021-11-03T11:57:16.861Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
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
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:17.000Z",
         "updated_at": "2021-11-03T11:57:17.060Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
         "id": 9,
         "organization_id": 4,
         "login": "ryan@example.com",
         "firstname": "Ryan",
         "lastname": "Parker",
         "email": "ryan@example.com",
         "image": "0e405c60b5deb780feb7ebebd37ff5e0",
         "image_source": null,
         "web": "",
         "phone": "0049 30 1234 5678",
         "fax": "",
         "mobile": "",
         "department": null,
         "street": "",
         "zip": "",
         "city": "",
         "country": "",
         "address": "Brandenburger Tor 7\n10117 Berlin",
         "vip": false,
         "verified": false,
         "active": true,
         "note": "no latte but macchiato",
         "last_login": null,
         "source": null,
         "login_failed": 0,
         "out_of_office": false,
         "out_of_office_start_at": null,
         "out_of_office_end_at": null,
         "out_of_office_replacement_id": null,
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:17.190Z",
         "updated_at": "2021-11-03T11:57:17.250Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
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
         "department": null,
         "street": "",
         "zip": "",
         "city": "",
         "country": "",
         "address": "Eiffel Tower\n5 Avenue Anatole France\n75007 Paris",
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
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:17.495Z",
         "updated_at": "2021-11-03T11:57:17.561Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      },
      {
         "id": 11,
         "organization_id": null,
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
         "department": null,
         "street": "",
         "zip": "",
         "city": "",
         "country": "",
         "address": "Westminster\nLondon SW1A 0AA",
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
         "preferences":
         {},
         "updated_by_id": 1,
         "created_by_id": 1,
         "created_at": "2021-11-03T11:57:17.741Z",
         "updated_at": "2021-11-03T11:57:17.794Z",
         "role_ids":
         [
            3
         ],
         "organization_ids":
         [],
         "authorization_ids":
         [],
         "karma_user_ids":
         [],
         "group_ids":
         {}
      }
   ]



Search
------

Required permission: ``ticket.agent`` **or** ``admin.user``

``GET``-Request sent:
``/api/v1/users/search?query=organization.name:{search string}&limit=10``

.. include:: /api/includes/sort_and_order.rst

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
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
         "group_ids": {}
      },
      {
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
         "group_ids": {}
      },
      {
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
         "group_ids": {}
      }
   ]

Show
----

Required permission: ``ticket.agent`` **or** ``admin.user`` **or**
``ticket.customer`` (shared organization)

.. note:: Technically, any listings will return user's own information only.

``GET``-Request sent: ``/api/v1/users/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 11,
      "organization_id": null,
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
      "department": null,
      "street": "",
      "zip": "",
      "city": "",
      "country": "",
      "address": "Westminster\nLondon SW1A 0AA",
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
      "preferences": {},
      "updated_by_id": 1,
      "created_by_id": 1,
      "created_at": "2021-11-03T11:57:17.741Z",
      "updated_at": "2021-11-03T11:57:17.794Z",
      "role_ids": [
         3
      ],
      "organization_ids": [],
      "authorization_ids": [],
      "karma_user_ids": [],
      "group_ids": {}
   }

Create
------

Required permission: ``admin.user`` **or** ``ticket.agent``

.. note:: **🤓 This depends on permissions**

   Agents can't set user passwords, roles or group permission. Instead
   Zammad will apply to :admin-docs:`default sign up role </manage/roles/index.html#role-details>`.

   Technically, unauthenticated user creation is possible if you manage
   to provide the required CSRF token (out of scope of this documentation).
   If you don't want that, consider :admin-docs:`disabling user registration </settings/security/base.html>`.

.. tip:: **🧐 Creation payloads can be big**

   Unsure which attributes you can use or set? Run a GET query on any
   fitting user existing in your instance already.

``POST``-Request sent: ``/api/v1/users``

.. code-block:: json

   {
     "firstname": "Jane",
     "lastname": "Doe",
     "email": "jdoe@example.com",
     "login": "jdoe",
     "organization": "Sample Corp.",
     "roles": [
         "Agent",
         "Customer"
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 16,
      "organization_id": 5,
      "login": "jdoe",
      "firstname": "Jane",
      "lastname": "Doe",
      "email": "jdoe@example.com",
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
      "updated_at": "2021-11-03T14:42:36.855Z",
      "role_ids": [
         2,
         3
      ],
      "organization_ids": [],
      "authorization_ids": [],
      "karma_user_ids": [],
      "group_ids": {}
   }

Update
------

Required permission: ``admin.user`` **or** ``ticket.agent``

.. note:: **🤓 This depends on permissions**

   Agents can't set user passwords, roles or group permission. Instead
   Zammad will apply to :admin-docs:`default sign up role </manage/roles/index.html#role-details>`.

``PUT``-Request sent: ``/api/v1/users/{id}``

.. code-block:: json

   {
      "phone": "+49 30 55 57 160 00",
      "department": "Sales",
      "address": "Marienstr. 18\n10117 Berlin"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 16,
      "organization_id": 5,
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
      "address": "Marienstr. 18\n10117 Berlin",
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
      "updated_at": "2021-11-03T14:49:20.018Z",
      "role_ids": [
         2,
         3
      ],
      "organization_ids": [],
      "authorization_ids": [],
      "karma_user_ids": [],
      "group_ids": {}
   }

Delete
------

Required permission: ``admin.user``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing users cannot be undone.
   Zammad will also remove references - thus potentially tickets!

   Removing users with references in e.g. activity streams is not possible
   via API - this will be indicated by
   ``"error": "Can't delete, object has references."``. This is *not* a bug.

   Consider using :admin-docs:`Data Privacy </system/data-privacy.html>` via UI
   for more control instead.

``DELETE``-Request sent: ``/api/v1/users/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
