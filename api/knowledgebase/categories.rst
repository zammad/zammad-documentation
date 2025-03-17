Categories
==========

Show
----

Required permission: ``knowledge_base.reader`` or ``knowledge_base.editor``

``GET``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories/{ID of category}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 1,
      "knowledge_base_id": 1,
      "parent_id": null,
      "category_icon": "f115",
      "position": 0,
      "created_at": "2025-03-12T14:50:42.533Z",
      "updated_at": "2025-03-12T14:52:38.025Z",
      "translation_ids": [
         1
      ],
      "answer_ids": [
         1
      ],
      "child_ids": [
         1
      ],
      "permission_ids": [],
      "permissions_effective": []
   }

Create
------

Required permission: ``knowledge_base.editor``

``POST``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories``

.. code-block:: json
   :force:

   {
      "category_icon": "f115",
      "parent_id": "",
      "translations_attributes": [
         {
            "content_attributes": {
               "body": ""
            },
            "kb_locale_id": 1,
            "title": "New Category 6"
         }
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 6,
      "knowledge_base_id": 1,
      "parent_id": null,
      "category_icon": "f115",
      "position": 5,
      "created_at": "2025-03-13T10:40:37.096Z",
      "updated_at": "2025-03-13T10:40:37.104Z",
      "translation_ids": [
         6
      ],
      "answer_ids": [],
      "child_ids": [
         6
      ],
      "permission_ids": [],
      "permissions_effective": []
   }

Change
------

Required permission: ``knowledge_base.editor``

``PATCH``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories/{ID of category}``

.. code-block:: json
   :force:

   {
      "category_icon": "f00c",
      "parent_id": "2",
      "translations_attributes": [
         {
            "id": 3,
            "title": "My new category"
         }
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "knowledge_base_id": 1,
      "parent_id": 2,
      "category_icon": "f00c",
      "id": 3,
      "position": 0,
      "created_at": "2025-03-13T10:15:33.217Z",
      "updated_at": "2025-03-13T10:32:32.559Z",
      "translation_ids": [
         3
      ],
      "answer_ids": [],
      "child_ids": [
         3
      ],
      "permission_ids": [],
      "permissions_effective": []
   }

Delete
------

Required permission: ``knowledge_base.editor``

``DELETE``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories/{ID of category}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}

Show Permissions
----------------

Required permission: ``knowledge_base.editor``

``GET``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories/{ID of category}/permissions``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "roles_reader": [],
      "roles_editor": [
         {
            "id": 1,
            "name": "Admin"
         },
         {
            "id": 2,
            "name": "Agent"
         }
      ],
      "permissions": [
         {
            "id": 1,
            "access": "editor",
            "role_id": 1
         },
         {
            "id": 2,
            "access": "reader",
            "role_id": 2
         }
      ],
      "inherited": []
   }

Change Permissions
------------------

Required permission: ``knowledge_base.editor``

``PUT``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories/{ID of category}/permissions``

.. code-block:: json
   :force:

   {
      "permissions_dialog": {
         "permissions": {
            "1": "editor",
            "2": "reader"
         }
      }
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "roles_reader": [],
      "roles_editor": [
         {
            "id": 1,
            "name": "Admin"
         },
         {
            "id": 2,
            "name": "Agent"
         }
      ],
      "permissions": [
         {
            "id": 1,
            "access": "editor",
            "role_id": 1
         },
         {
            "id": 2,
            "access": "reader",
            "role_id": 2
         }
      ],
      "inherited": []
   }

Reorder Answers
---------------

Required permission: ``knowledge_base.editor``

``PATCH``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/categories/{ID of category}/reorder_answers``

.. code-block:: json
   :force:

   {
      "ordered_ids": [
         1,
         4,
         5

      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "KnowledgeBaseAnswer": {
         "4": {
            "category_id": 1,
            "position": 1,
            "archived_at": null,
            "internal_at": null,
            "published_at": null,
            "id": 4,
            "promoted": false,
            "internal_note": null,
            "archived_by_id": null,
            "internal_by_id": null,
            "published_by_id": null,
            "created_at": "2025-03-13T11:02:28.728Z",
            "updated_at": "2025-03-13T11:04:17.812Z",
            "translation_ids": [
               4
            ],
            "attachments": [],
            "tags": []
         },
         "5": {
            "category_id": 1,
            "position": 2,
            "archived_at": null,
            "internal_at": null,
            "published_at": null,
            "id": 5,
            "promoted": false,
            "internal_note": null,
            "archived_by_id": null,
            "internal_by_id": null,
            "published_by_id": null,
            "created_at": "2025-03-13T11:02:46.276Z",
            "updated_at": "2025-03-13T11:04:17.872Z",
            "translation_ids": [
               5
            ],
            "attachments": [],
            "tags": []
         },
         "1": {
            "category_id": 1,
            "position": 0,
            "archived_at": null,
            "internal_at": "2025-03-12T14:52:38.014Z",
            "published_at": null,
            "id": 1,
            "promoted": false,
            "internal_note": null,
            "archived_by_id": null,
            "internal_by_id": 3,
            "published_by_id": null,
            "created_at": "2025-03-12T14:50:48.732Z",
            "updated_at": "2025-03-13T11:04:17.734Z",
            "translation_ids": [
               1
            ],
            "attachments": [],
            "tags": []
         }
      },
      "KnowledgeBaseCategory": {
         "1": {
            "id": 1,
            "knowledge_base_id": 1,
            "parent_id": null,
            "category_icon": "f115",
            "position": 0,
            "created_at": "2025-03-12T14:50:42.533Z",
            "updated_at": "2025-03-13T11:04:17.874Z",
            "translation_ids": [
               1
            ],
            "answer_ids": [
               1,
               4,
               5
            ],
            "child_ids": [
               1
            ],
            "permission_ids": [],
            "permissions_effective": []
         }
      },
      "KnowledgeBase": {
         "1": {
            "show_feed_icon": false,
            "custom_address": "mynewaddress.tld",
            "id": 1,
            "iconset": "FontAwesome",
            "color_highlight": "#38ae6a",
            "color_header": "#f9fafb",
            "color_header_link": "hsl(206,8%,50%)",
            "homepage_layout": "grid",
            "category_layout": "grid",
            "active": true,
            "created_at": "2025-03-12T10:09:01.203Z",
            "updated_at": "2025-03-13T09:17:11.874Z",
            "translation_ids": [
               1
            ],
            "kb_locale_ids": [
               1
            ],
            "category_ids": [
               2,
               1
            ],
            "answer_ids": [
               2,
               3,
               1
            ],
            "permission_ids": [],
            "permissions_effective": []
         }
      },
      "KnowledgeBaseLocale": {
         "1": {
            "id": 1,
            "knowledge_base_id": 1,
            "system_locale_id": 1,
            "primary": true,
            "created_at": "2025-03-12T10:09:01.206Z",
            "updated_at": "2025-03-12T10:09:01.206Z",
            "knowledge_base_translation_ids": [
               1
            ],
            "category_translation_ids": [],
            "answer_translation_ids": [],
            "menu_item_ids": []
         }
      },
      "KnowledgeBaseTranslation": {
         "1": {
            "id": 1,
            "title": "Company Knowledge Base",
            "footer_note": "© Company",
            "kb_locale_id": 1,
            "knowledge_base_id": 1,
            "created_at": "2025-03-12T10:09:01.224Z",
            "updated_at": "2025-03-13T09:00:07.809Z"
         }
      },
      "KnowledgeBaseCategoryTranslation": {
         "1": {
            "id": 1,
            "title": "Category 1",
            "kb_locale_id": 1,
            "category_id": 1,
            "created_at": "2025-03-12T14:50:42.547Z",
            "updated_at": "2025-03-12T14:50:42.547Z"
         }
      },
      "KnowledgeBaseAnswerTranslation": {
         "4": {
            "answer_id": 4,
            "title": "Answer 2",
            "id": 4,
            "kb_locale_id": 1,
            "content_id": 4,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-13T11:02:28.746Z",
            "updated_at": "2025-03-13T11:02:35.655Z"
         },
         "5": {
            "answer_id": 5,
            "title": "Answer 3",
            "id": 5,
            "kb_locale_id": 1,
            "content_id": 5,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-13T11:02:46.288Z",
            "updated_at": "2025-03-13T11:02:53.908Z"
         },
         "1": {
            "id": 1,
            "title": "Answer 1",
            "kb_locale_id": 1,
            "answer_id": 1,
            "content_id": 1,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-12T14:50:48.750Z",
            "updated_at": "2025-03-12T14:51:11.559Z"
         }
      },
      "User": {
         "3": {
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
            "last_login": "2025-03-10T15:49:27.097Z",
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
               "intro": true,
               "keyboard_shortcuts_clues": true,
               "locale": "de-de",
               "theme": "light",
               "overviews_last_used": {
                  "1": "2025-03-12T09:19:44.289Z",
                  "2": "2025-03-12T09:19:36.992Z",
                  "3": "2025-03-12T09:19:43.220Z",
                  "5": "2025-03-12T09:19:15.831Z",
                  "6": "2025-03-12T09:19:50.081Z",
                  "12": "2025-03-12T09:19:35.027Z",
                  "13": "2025-03-12T09:19:41.238Z",
                  "4": "2025-03-12T09:19:50.743Z"
               }
            },
            "updated_by_id": 3,
            "created_by_id": 1,
            "created_at": "2025-02-24T14:33:11.408Z",
            "updated_at": "2025-03-12T09:19:51.034Z",
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
               ],
               "12": [
                  "full"
               ],
               "13": [
                  "full"
               ],
               "14": [
                  "full"
               ],
               "15": [
                  "full"
               ],
               "16": [
                  "full"
               ],
               "17": [
                  "full"
               ],
               "18": [
                  "full"
               ],
               "19": [
                  "full"
               ],
               "20": [
                  "full"
               ],
               "21": [
                  "full"
               ]
            }
         }
      }
   }

