Answers
=======

Show
----

Required permission: ``knowledge_base.reader`` or ``knowledge_base.editor``

``GET``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}``

.. tip:: If you want to get the content of an answer, add the parameters
   ``?include_contents={ID of the translated answer}`` to the query URL.
   To find the ID of the translated answer (can be different than the answer
   ID), query the answer and look for ``KnowledgeBaseAnswerTranslation``. Use
   the ID of the translated answer for the above mentioned request (e.g.
   ``[...]/answers/2?include_contents=5``).

   The request for the following response included the parameters.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 1,
      "assets": {
         "KnowledgeBaseAnswer": {
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
         },
         "KnowledgeBaseAnswerTranslationContent": {
            "1": {
               "body": "This is the body of answer 1.",
               "id": 1,
               "attachments": []
            }
         }
      }
   }

Create
------

Required permission: ``knowledge_base.editor``

``POST``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers``

.. code-block:: json
   :force:

   {
      "category_id": "1",
      "translations_attributes": [
         {
            "content_attributes": {
               "body": "This is such an important answer!"
            },
            "kb_locale_id": 1,
            "title": "Very important answer!!"
         }
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 7,
      "assets": {
         "KnowledgeBaseAnswer": {
            "7": {
               "id": 7,
               "category_id": 1,
               "promoted": false,
               "internal_note": null,
               "position": 4,
               "archived_at": null,
               "archived_by_id": null,
               "internal_at": null,
               "internal_by_id": null,
               "published_at": null,
               "published_by_id": null,
               "created_at": "2025-03-13T12:21:27.078Z",
               "updated_at": "2025-03-13T12:21:27.122Z",
               "translation_ids": [
                  7
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
               "updated_at": "2025-03-13T12:21:27.123Z",
               "translation_ids": [
                  1
               ],
               "answer_ids": [
                  1,
                  4,
                  5,
                  6,
                  7
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
            "7": {
               "id": 7,
               "title": "Very important answer!!",
               "kb_locale_id": 1,
               "answer_id": 7,
               "content_id": 7,
               "created_by_id": 3,
               "updated_by_id": 3,
               "created_at": "2025-03-13T12:21:27.096Z",
               "updated_at": "2025-03-13T12:21:27.120Z"
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
         },
         "KnowledgeBaseAnswerTranslationContent": {
            "7": {
               "id": 7,
               "body": "This is such an important answer!",
               "attachments": []
            }
         }
      }
   }

Change
------

Required permission: ``knowledge_base.editor``

``PATCH``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}``

.. code-block:: json
   :force:

   {
      "category_id": "1",,
      "translations_attributes": [
         {
            "content_attributes": {
               "body": "Changed text of answer via API"
            },
            "id": 7,
            "title": "Changed title of answer via API"
         }
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 7,
      "assets": {
         "KnowledgeBaseAnswer": {
            "7": {
               "category_id": 1,
               "archived_at": null,
               "internal_at": null,
               "published_at": null,
               "id": 7,
               "promoted": false,
               "internal_note": null,
               "position": 4,
               "archived_by_id": null,
               "internal_by_id": null,
               "published_by_id": null,
               "created_at": "2025-03-13T12:21:27.078Z",
               "updated_at": "2025-03-13T12:30:14.523Z",
               "translation_ids": [
                  7
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
               "updated_at": "2025-03-13T12:30:14.523Z",
               "translation_ids": [
                  1
               ],
               "answer_ids": [
                  1,
                  4,
                  5,
                  6,
                  7
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
            "7": {
               "answer_id": 7,
               "title": "Changed title of answer via API",
               "id": 7,
               "kb_locale_id": 1,
               "content_id": 7,
               "created_by_id": 3,
               "updated_by_id": 3,
               "created_at": "2025-03-13T12:21:27.096Z",
               "updated_at": "2025-03-13T12:30:14.520Z"
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
         },
         "KnowledgeBaseAnswerTranslationContent": {
            "7": {
               "body": "Changed text of answer via API",
               "id": 7,
               "attachments": []
            }
         }
      }
   }


Delete
------

Required permission: ``knowledge_base.editor``

``DELETE``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}

Manage Publication Status
-------------------------

Required permission: ``knowledge_base.editor``

.. note:: Responses are omitted here. You can expect to get a response like for
   showing an answer with a populated value for ``archived_at``,
   ``published_at`` or ``internal_at``, depending on which request you execute.

Publish Internally:

``POST``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}/internal``

Publish publicly:

``POST``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}/publish``

Archive:

``POST``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}/archive``

Unarchive:

``POST``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}/unarchive``

Manage Attachments
------------------

Required permission: ``knowledge_base.editor``

Add attachment:

``POST``-Request with payload sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}/attachments``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "KnowledgeBaseAnswer": {
         "4": {
            "updated_at": "2025-03-13T13:07:46.955Z",
            "id": 4,
            "category_id": 1,
            "promoted": false,
            "internal_note": null,
            "position": 0,
            "archived_at": null,
            "archived_by_id": null,
            "internal_at": "2025-03-13T12:51:00.000Z",
            "internal_by_id": 3,
            "published_at": null,
            "published_by_id": null,
            "created_at": "2025-03-13T11:02:28.728Z",
            "translation_ids": [
               4
            ],
            "attachments": [
               {
                  "id": 1,
                  "url": "/api/v1/attachments/1",
                  "preview_url": "/api/v1/attachments/1?preview=1",
                  "filename": "html-0dd51a3.zip",
                  "size": "9939339",
                  "preferences": {
                     "Content-Type": "application/zip"
                  }
               },
               {
                  "id": 2,
                  "url": "/api/v1/attachments/2",
                  "preview_url": "/api/v1/attachments/2?preview=1",
                  "filename": "mail-21.eml",
                  "size": "402",
                  "preferences": {
                     "Content-Type": "message/rfc822"
                  }
               },
               {
                  "id": 3,
                  "url": "/api/v1/attachments/3",
                  "preview_url": "/api/v1/attachments/3?preview=1",
                  "filename": "sample_file.txt",
                  "size": "39",
                  "preferences": {
                     "Content-Type": "text/plain"
                  }
               }
            ],
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
            "updated_at": "2025-03-13T13:07:46.956Z",
            "translation_ids": [
               1
            ],
            "answer_ids": [
               5,
               6,
               7,
               4
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
            "updated_at": "2025-03-13T13:07:46.953Z",
            "id": 4,
            "title": "Answer 2",
            "kb_locale_id": 1,
            "content_id": 4,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-13T11:02:28.746Z"
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
               "locale": "en-us",
               "theme": "light",
               "overviews_last_used": {
                  "1": "2025-03-12T09:19:44.289Z",
                  "2": "2025-03-12T09:19:36.992Z",
                  "3": "2025-03-12T09:19:43.220Z",
                  "4": "2025-03-12T09:19:50.743Z",
                  "5": "2025-03-12T09:19:15.831Z",
                  "6": "2025-03-12T09:19:50.081Z",
                  "12": "2025-03-12T09:19:35.027Z",
                  "13": "2025-03-12T09:19:41.238Z"
               }
            },
            "updated_by_id": 3,
            "created_by_id": 1,
            "created_at": "2025-02-24T14:33:11.408Z",
            "updated_at": "2025-03-13T12:51:56.613Z",
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

Delete attachment:

``DELETE``-Request sent: ``/api/v1/knowledge_bases/{ID of your KB}/answers/{ID of answer}/attachments/{ID of attachment}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "KnowledgeBaseAnswer": {
         "4": {
            "updated_at": "2025-03-13T13:16:32.444Z",
            "id": 4,
            "category_id": 1,
            "promoted": false,
            "internal_note": null,
            "position": 0,
            "archived_at": null,
            "archived_by_id": null,
            "internal_at": "2025-03-13T12:51:00.000Z",
            "internal_by_id": 3,
            "published_at": null,
            "published_by_id": null,
            "created_at": "2025-03-13T11:02:28.728Z",
            "translation_ids": [
               4
            ],
            "attachments": [
               {
                  "id": 1,
                  "url": "/api/v1/attachments/1",
                  "preview_url": "/api/v1/attachments/1?preview=1",
                  "filename": "html-0dd51a3.zip",
                  "size": "9939339",
                  "preferences": {
                     "Content-Type": "application/zip"
                  }
               },
               {
                  "id": 2,
                  "url": "/api/v1/attachments/2",
                  "preview_url": "/api/v1/attachments/2?preview=1",
                  "filename": "mail-21.eml",
                  "size": "402",
                  "preferences": {
                     "Content-Type": "message/rfc822"
                  }
               }
            ],
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
            "updated_at": "2025-03-13T13:16:32.444Z",
            "translation_ids": [
               1
            ],
            "answer_ids": [
               5,
               6,
               7,
               4
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
            "updated_at": "2025-03-13T13:16:32.442Z",
            "id": 4,
            "title": "Answer 2",
            "kb_locale_id": 1,
            "content_id": 4,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2025-03-13T11:02:28.746Z"
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
               "locale": "en-us",
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
            "updated_at": "2025-03-13T12:51:56.613Z",
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
