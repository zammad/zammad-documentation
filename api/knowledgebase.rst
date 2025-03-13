Knowledge Base
==============

Zammad has different knowledge base related endpoints. You can find the general
one about knowledge bases itself on this page. The sub-endpoints have been split
off into separate pages:

   .. toctree::
      :maxdepth: 1
      :glob:

      /api/knowledgebase/answers
      /api/knowledgebase/categories

.. /api/knowledgebase/settings

.. hint::

   The request and response examples include the knowledge base ID ``1``.
   Your ID may be different, for example if you created a knowledge base before,
   dropped it and created a new one.

Knowledge Base Overview
-----------------------

Required permission: ``knowledge_base.editor``

``POST``-Request sent: ``/api/v1/knowledge_bases/init``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "KnowledgeBase": {
         "1": {
            "id": 1,
            "iconset": "FontAwesome",
            "color_highlight": "#38ae6a",
            "color_header": "#f9fafb",
            "color_header_link": "hsl(206,8%,50%)",
            "homepage_layout": "grid",
            "category_layout": "grid",
            "active": true,
            "show_feed_icon": false,
            "custom_address": null,
            "created_at": "2025-03-12T10:09:01.203Z",
            "updated_at": "2025-03-13T09:00:07.819Z",
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
      "KnowledgeBaseCategory": {
         "1": {
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
         },
         "2": {
            "id": 2,
            "knowledge_base_id": 1,
            "parent_id": null,
            "category_icon": "f015",
            "position": 1,
            "created_at": "2025-03-12T14:51:29.019Z",
            "updated_at": "2025-03-12T14:52:21.782Z",
            "translation_ids": [
               2
            ],
            "answer_ids": [
               2,
               3
            ],
            "child_ids": [
               2
            ],
            "permission_ids": [],
            "permissions_effective": []
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
         },
         "2": {
            "id": 2,
            "title": "Category 2",
            "kb_locale_id": 1,
            "category_id": 2,
            "created_at": "2025-03-12T14:51:29.024Z",
            "updated_at": "2025-03-12T14:51:29.024Z"
         }
      },
      "KnowledgeBaseAnswer": {
         "1": {
            "internal_at": "2025-03-12T14:52:38.014Z",
            "category_id": 1,
            "archived_at": null,
            "internal_by_id": 3,
            "published_at": null,
            "id": 1,
            "promoted": false,
            "internal_note": null,
            "position": 0,
            "archived_by_id": null,
            "published_by_id": null,
            "created_at": "2025-03-12T14:50:48.732Z",
            "updated_at": "2025-03-12T14:52:38.022Z",
            "translation_ids": [
               1
            ],
            "attachments": [],
            "tags": []
         },
         "2": {
            "id": 2,
            "category_id": 2,
            "promoted": false,
            "internal_note": null,
            "position": 0,
            "archived_at": null,
            "archived_by_id": null,
            "internal_at": null,
            "internal_by_id": null,
            "published_at": null,
            "published_by_id": null,
            "created_at": "2025-03-12T14:51:34.900Z",
            "updated_at": "2025-03-12T14:51:49.317Z",
            "translation_ids": [
               2
            ],
            "attachments": [],
            "tags": []
         },
         "3": {
            "published_at": "2025-03-12T14:52:21.767Z",
            "category_id": 2,
            "archived_at": null,
            "internal_at": null,
            "published_by_id": 3,
            "id": 3,
            "promoted": false,
            "internal_note": null,
            "position": 1,
            "archived_by_id": null,
            "internal_by_id": null,
            "created_at": "2025-03-12T14:51:58.755Z",
            "updated_at": "2025-03-12T14:52:21.778Z",
            "translation_ids": [
               3
            ],
            "attachments": [],
            "tags": []
         }
      },
      "KnowledgeBaseAnswerTranslation": {
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
         },
         "2": {
            "answer_id": 2,
            "title": "Answer A",
            "id": 2,
            "kb_locale_id": 1,
            "content_id": 2,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-12T14:51:34.910Z",
            "updated_at": "2025-03-12T14:51:49.346Z"
         },
         "3": {
            "answer_id": 3,
            "title": "Answer B",
            "id": 3,
            "kb_locale_id": 1,
            "content_id": 3,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-12T14:51:58.770Z",
            "updated_at": "2025-03-12T14:52:05.925Z"
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


Show Knowledge Base
-------------------

Required permission: ``knowledge_base.reader`` or ``knowledge_base.editor``

``GET``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 1,
      "iconset": "FontAwesome",
      "color_highlight": "#38ae6a",
      "color_header": "#f9fafb",
      "color_header_link": "hsl(206,8%,50%)",
      "homepage_layout": "grid",
      "category_layout": "grid",
      "active": true,
      "show_feed_icon": false,
      "custom_address": null,
      "created_at": "2025-03-12T10:09:01.203Z",
      "updated_at": "2025-03-12T15:38:47.669Z",
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


Change Knowledge Base Settings
------------------------------

Required permission: ``knowledge_base.editor``

``PATCH``-Request sent: ``/api/v1/knowledge_bases/manage/{ID of your KB}``

.. code-block:: json
   :force:

   {
      "show_feed_icon": false,
      "custom_address": "mynewaddress.tld"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
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

Show Permissions
----------------

``GET``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/permissions``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "roles_reader": [
         {
            "id": 2,
            "name": "Agent"
         }
      ],
      "roles_editor": [
         {
            "id": 1,
            "name": "Admin"
         }
      ],
      "permissions": [],
      "inherited": []
   }

TODO:

Change Permissions
------------------

PUT /api/v1/knowledge_bases/:id/permissions

Reorder Categories
------------------

PATCH /api/v1/knowledge_bases/:knowledge_base_id/categories/:id/reorder_categories

PUT   /api/v1/knowledge_bases/:knowledge_base_id/categories/reorder_root_categories