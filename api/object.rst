Object
******

.. danger::

   Adjusting objects via API can cause serious issues with your instance.
   Proceed with absolute caution and ensure to adjust any of Zammads default
   fields.

   If you want to hide fields, consider `Core Workflows`_ instead.
   For states and priorities use either API endpoints or rails console.

.. _Core Workflows:
   https://admin-docs.zammad.org/en/latest/system/core-workflows.html

List
====

Required permission: ``admin.object``

``GET``-Request sent: ``/api/v1/object_manager_attributes``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 2,
         "name": "customer_id",
         "display": "Customer",
         "data_type": "user_autocompletion",
         "data_option": {
            "relation": "User",
            "autocapitalize": false,
            "multiple": false,
            "guess": true,
            "null": false,
            "limit": 200,
            "placeholder": "Enter Person or Organization/Company",
            "minLengt": 2,
            "translate": false,
            "permission": [
               "ticket.agent"
            ]
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_top": {
               "-all-": {
                  "null": false
               }
            },
            "edit": {}
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 10,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.677Z",
         "updated_at": "2021-11-09T13:12:32.677Z",
         "object": "Ticket",
         "deletable": false,
         "not_deletable_reason": "This attribute is referenced by Overview: My Tickets and thus cannot be deleted!"
      },
      {
         "id": 1,
         "name": "title",
         "display": "Title",
         "data_type": "input",
         "data_option": {
            "type": "text",
            "maxlength": 200,
            "null": false,
            "translate": false
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_top": {
               "-all-": {
                  "null": false
               }
            },
            "edit": {}
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 15,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.671Z",
         "updated_at": "2021-11-09T13:12:32.671Z",
         "object": "Ticket",
         "deletable": false
      },
      {
         "id": 3,
         "name": "type",
         "display": "Type",
         "data_type": "select",
         "data_option": {
            "default": "",
            "options": {
               "Incident": "Incident",
               "Problem": "Problem",
               "Request for Change": "Request for Change"
            },
            "nulloption": true,
            "multiple": false,
            "null": true,
            "translate": true,
            "maxlength": 255
         },
         "data_option_new": {},
         "editable": true,
         "active": false,
         "screens": {
            "create_middle": {
               "-all-": {
                  "null": false,
                  "item_class": "column"
               }
            },
            "edit": {
               "ticket.agent": {
                  "null": false
               }
            }
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 20,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.686Z",
         "updated_at": "2021-11-09T13:12:32.686Z",
         "object": "Ticket",
         "deletable": true
      },
      {
         "id": 4,
         "name": "group_id",
         "display": "Group",
         "data_type": "select",
         "data_option": {
            "default": "",
            "relation": "Group",
            "relation_condition": {
               "access": "full"
            },
            "nulloption": true,
            "multiple": false,
            "null": false,
            "translate": false,
            "only_shown_if_selectable": true,
            "permission": [
               "ticket.agent",
               "ticket.customer"
            ],
            "maxlength": 255
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_middle": {
               "-all-": {
                  "null": false,
                  "item_class": "column"
               }
            },
            "edit": {
               "ticket.agent": {
                  "null": false
               }
            }
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 25,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.690Z",
         "updated_at": "2021-11-09T13:12:32.690Z",
         "object": "Ticket",
         "deletable": false
      },
      {
         "id": 5,
         "name": "owner_id",
         "display": "Owner",
         "data_type": "select",
         "data_option": {
            "default": "",
            "relation": "User",
            "relation_condition": {
               "roles": "Agent"
            },
            "nulloption": true,
            "multiple": false,
            "null": true,
            "translate": false,
            "permission": [
               "ticket.agent"
            ],
            "maxlength": 255
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_middle": {
               "-all-": {
                  "null": true,
                  "item_class": "column"
               }
            },
            "edit": {
               "-all-": {
                  "null": true
               }
            }
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 30,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.694Z",
         "updated_at": "2021-11-09T13:12:32.694Z",
         "object": "Ticket",
         "deletable": false,
         "not_deletable_reason": "This attribute is referenced by Trigger: customer notification (on owner change); Overview: My assigned Tickets,My pending reached Tickets,Unassigned & Open and thus cannot be deleted!"
      },
      {
         "id": 6,
         "name": "state_id",
         "display": "State",
         "data_type": "select",
         "data_option": {
            "relation": "TicketState",
            "nulloption": true,
            "multiple": false,
            "null": false,
            "default": 2,
            "translate": true,
            "filter": [
               2,
               1,
               3,
               4,
               6,
               7
            ],
            "maxlength": 255
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_middle": {
               "ticket.agent": {
                  "null": false,
                  "item_class": "column",
                  "filter": [
                     2,
                     1,
                     3,
                     4,
                     7
                  ]
               },
               "ticket.customer": {
                  "item_class": "column",
                  "nulloption": false,
                  "null": true,
                  "filter": [
                     1,
                     4
                  ],
                  "default": 1
               }
            },
            "edit": {
               "ticket.agent": {
                  "nulloption": false,
                  "null": false,
                  "filter": [
                     2,
                     3,
                     4,
                     7
                  ]
               },
               "ticket.customer": {
                  "nulloption": false,
                  "null": true,
                  "filter": [
                     2,
                     4
                  ],
                  "default": 2
               }
            }
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 40,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.706Z",
         "updated_at": "2021-11-09T13:12:32.706Z",
         "object": "Ticket",
         "deletable": false,
         "not_deletable_reason": "This attribute is referenced by Trigger: auto reply (on new tickets); Overview: My Organization Tickets,My Tickets,My assigned Tickets,My pending reached Tickets,My replacement Tickets,Open,Open Banana Items,Pending reached,Unassigned & Open,VIP Customers and thus cannot be deleted!"
      },
      {
         "id": 7,
         "name": "pending_time",
         "display": "Pending till",
         "data_type": "datetime",
         "data_option": {
            "future": true,
            "past": false,
            "diff": 24,
            "null": true,
            "translate": true,
            "permission": [
               "ticket.agent"
            ]
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_middle": {
               "-all-": {
                  "null": false,
                  "item_class": "column"
               }
            },
            "edit": {
               "-all-": {
                  "null": false
               }
            }
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 41,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.713Z",
         "updated_at": "2021-11-09T13:12:32.713Z",
         "object": "Ticket",
         "deletable": false,
         "not_deletable_reason": "This attribute is referenced by Overview: My pending reached Tickets,Pending reached and thus cannot be deleted!"
      },
      {
         "id": 8,
         "name": "priority_id",
         "display": "Priority",
         "data_type": "select",
         "data_option": {
            "relation": "TicketPriority",
            "nulloption": false,
            "multiple": false,
            "null": false,
            "default": 2,
            "translate": true,
            "maxlength": 255
         },
         "data_option_new": {},
         "editable": false,
         "active": true,
         "screens": {
            "create_middle": {
               "ticket.agent": {
                  "null": false,
                  "item_class": "column"
               }
            },
            "edit": {
               "ticket.agent": {
                  "null": false
               }
            }
         },
         "to_create": false,
         "to_migrate": false,
         "to_delete": false,
         "to_config": false,
         "position": 80,
         "created_by_id": 1,
         "updated_by_id": 1,
         "created_at": "2021-11-09T13:12:32.718Z",
         "updated_at": "2021-11-09T13:12:32.718Z",
         "object": "Ticket",
         "deletable": false
      },
      
      [ ... ]
   ]

Show
====

Required permission: ``admin.object``

``GET``-Request sent: ``/api/v1/object_manager_attributes/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 18,
      "object_lookup_id": 1,
      "name": "email",
      "display": "Email",
      "data_type": "input",
      "data_option": {
         "type": "email",
         "maxlength": 150,
         "null": true,
         "item_class": "formGroup--halfSize"
      },
      "data_option_new": {},
      "editable": false,
      "active": true,
      "screens": {
         "signup": {
            "-all-": {
               "null": false
            }
         },
         "invite_agent": {
            "-all-": {
               "null": false
            }
         },
         "invite_customer": {
            "-all-": {
               "null": false
            }
         },
         "edit": {
            "-all-": {
               "null": true
            }
         },
         "create": {
            "-all-": {
               "null": true
            }
         },
         "view": {
            "-all-": {
               "shown": true
            }
         }
      },
      "to_create": false,
      "to_migrate": false,
      "to_delete": false,
      "to_config": false,
      "position": 400,
      "created_by_id": 1,
      "updated_by_id": 1,
      "created_at": "2021-11-09T13:12:32.784Z",
      "updated_at": "2021-11-09T13:12:32.784Z"
   }

.. _create_object:

Create
======

Required permission: ``admin.object``

``POST``-Request sent: ``/api/v1/object_manager_attributes``

.. tabs::

   .. tab:: Boolean

      Payload:

      .. code-block:: json

         {
            "name": "sample_boolean",
            "object": "Ticket",
            "display": "Sample Boolean",
            "active": true,
            "position": 1550,
            "data_type": "boolean",
            "data_option": {
               "options": {
                  "true": "very correct indeed",
                  "false": "very incorrect indeed"
               }
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }
         

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 50,
            "object_lookup_id": 2,
            "name": "sample_boolean",
            "display": "Sample Boolean",
            "data_type": "boolean",
            "data_option": {
               "options": {
                  "false": "very incorrect indeed",
                  "true": "very correct indeed"
               },
               "default": null,
               "null": true,
               "relation": ""
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:18:23.208Z",
            "updated_at": "2021-11-12T18:18:23.208Z"
         }

   .. tab:: Date

      Payload:

      .. code-block:: json

         {
            "name": "sample_date",
            "object": "Ticket",
            "display": "Sample Date",
            "active": true,
            "position": 1550,
            "data_type": "date",
            "data_option": {
               "diff": 120
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 51,
            "object_lookup_id": 2,
            "name": "sample_date",
            "display": "Sample Date",
            "data_type": "date",
            "data_option": {
               "diff": 120,
               "default": null,
               "null": true,
               "options": {},
               "relation": ""
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:19:32.827Z",
            "updated_at": "2021-11-12T18:19:32.827Z"
         }

   .. tab:: Date Time

      Payload:

      .. code-block:: json

         {
            "name": "sample_datetime",
            "object": "Ticket",
            "display": "Sample DateTime",
            "active": true,
            "position": 1550,
            "data_type": "datetime",
            "data_option": {
               "future": true,
               "past": false,
               "diff": 120
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 52,
            "object_lookup_id": 2,
            "name": "sample_datetime",
            "display": "Sample DateTime",
            "data_type": "datetime",
            "data_option": {
               "future": true,
               "past": false,
               "diff": 120,
               "default": null,
               "null": true,
               "options": {},
               "relation": ""
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:30:38.469Z",
            "updated_at": "2021-11-12T18:30:38.469Z"
         }

   .. tab:: Integer

      Payload:

      .. code-block:: json

         {
            "name": "sample_integer",
            "object": "Ticket",
            "display": "Sample Integer",
            "active": true,
            "position": 1550,
            "data_type": "integer",
            "data_option": {
               "default": 1234,
               "min": 4,
               "max": 8
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 53,
            "object_lookup_id": 2,
            "name": "sample_integer",
            "display": "Sample Integer",
            "data_type": "integer",
            "data_option": {
               "default": 1234,
               "min": 4,
               "max": 8,
               "null": true,
               "options": {},
               "relation": ""
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:32:14.213Z",
            "updated_at": "2021-11-12T18:32:14.213Z"
         }

   .. tab:: Select

      Payload:

      .. code-block:: json

         {
            "name": "sample_select",
            "object": "Ticket",
            "display": "Sample Select",
            "active": true,
            "position": 1550,
            "data_type": "select",
            "data_option": {
               "options": {
                  "key-one": "First Key",
                  "key-two": "Second Key",
                  "key-three": "Third Key"
               },
               "default": "key-two",
               "linktemplate": ""
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 54,
            "object_lookup_id": 2,
            "name": "sample_select",
            "display": "Sample Select",
            "data_type": "select",
            "data_option": {
               "options": {
                  "key-one": "First Key",
                  "key-two": "Second Key",
                  "key-three": "Third Key"
               },
               "default": "key-two",
               "linktemplate": "",
               "null": true,
               "relation": "",
               "nulloption": true,
               "maxlength": 255
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:34:08.711Z",
            "updated_at": "2021-11-12T18:34:08.711Z"
         }

   .. tab:: Text

      Payload:

      .. code-block:: json

         {
            "name": "sample_text",
            "object": "Ticket",
            "display": "Sample Text",
            "active": true,
            "position": 1550,
            "data_type": "input",
            "data_option": {
               "default": "amazing default",
               "type": "text",
               "maxlength": 120,
               "linktemplate": "https://www.google.com/search?q=#{ticket.sample_text}"
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }

      .. hint::

         Zammad input fields can have 4 different types:

            * ``email``
            * ``tel``
            * ``text``
            * | ``url``
              | ⚠ *URL* does not support link-templates ⚠

         Depending on the chosen input type, Zammad expects different formats
         of data. E.g.: *email* demands a email address to be provided.

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 55,
            "object_lookup_id": 2,
            "name": "sample_text",
            "display": "Sample Text",
            "data_type": "input",
            "data_option": {
               "default": "amazing default",
               "type": "text",
               "maxlength": 120,
               "linktemplate": "https://www.google.com/search?q=#{ticket.sample_text}",
               "null": true,
               "options": {},
               "relation": ""
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:41:38.031Z",
            "updated_at": "2021-11-12T18:41:38.031Z"
         }

   .. tab:: Tree Select

      Payload:

      .. code-block:: json

         {
            "name": "sample_treeselect",
            "object": "Ticket",
            "display": "Sample Tree Select",
            "active": true,
            "position": 1550,
            "data_type": "tree_select",
            "data_option": {
               "options": [
                  {
                     "name": "row one - maximum child depth",
                     "value": "row one - maximum child depth",
                     "children": [
                        {
                           "name": "row one child level one",
                           "value": "row one - maximum child depth::row one child level one",
                           "children": [
                              {
                                 "name": "row one child level two",
                                 "value": "row one - maximum child depth::row one child level one::row one child level two",
                                 "children": [
                                    {
                                       "name": "row one child level three",
                                       "value": "row one - maximum child depth::row one child level one::row one child level two::row one child level three",
                                       "children": [
                                          {
                                             "name": "row one child level four",
                                             "value": "row one - maximum child depth::row one child level one::row one child level two::row one child level three::row one child level four",
                                             "children": [
                                                {
                                                   "name": "row one child level fize",
                                                   "value": "row one - maximum child depth::row one child level one::row one child level two::row one child level three::row one child level four::row one child level fize"
                                                }
                                             ]
                                          }
                                       ]
                                    }
                                 ]
                              }
                           ]
                        }
                     ]
                  },
                  {
                     "name": "row two - no childs",
                     "value": "row two - no childs"
                  },
                  {
                     "name": "row three - one child",
                     "value": "row three - one child",
                     "children": [
                        {
                           "name": "row three - first and only child",
                           "value": "row three - one child::row three - first and only child"
                        }
                     ]
                  }
               ]
            },
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created

         {
            "id": 56,
            "object_lookup_id": 2,
            "name": "sample_treeselect",
            "display": "Sample Tree Select",
            "data_type": "tree_select",
            "data_option": {
               "options": [
                  {
                     "name": "row one - maximum child depth",
                     "value": "row one - maximum child depth",
                     "children": [
                        {
                           "name": "row one child level one",
                           "value": "row one - maximum child depth::row one child level one",
                           "children": [
                              {
                                 "name": "row one child level two",
                                 "value": "row one - maximum child depth::row one child level one::row one child level two",
                                 "children": [
                                    {
                                       "name": "row one child level three",
                                       "value": "row one - maximum child depth::row one child level one::row one child level two::row one child level three",
                                       "children": [
                                          {
                                             "name": "row one child level four",
                                             "value": "row one - maximum child depth::row one child level one::row one child level two::row one child level three::row one child level four",
                                             "children": [
                                                {
                                                   "name": "row one child level fize",
                                                   "value": "row one - maximum child depth::row one child level one::row one child level two::row one child level three::row one child level four::row one child level fize"
                                                }
                                             ]
                                          }
                                       ]
                                    }
                                 ]
                              }
                           ]
                        }
                     ]
                  },
                  {
                     "name": "row two - no childs",
                     "value": "row two - no childs"
                  },
                  {
                     "name": "row three - one child",
                     "value": "row three - one child",
                     "children": [
                        {
                           "name": "row three - first and only child",
                           "value": "row three - one child::row three - first and only child"
                        }
                     ]
                  }
               ],
               "default": "",
               "null": true,
               "relation": "",
               "nulloption": true,
               "maxlength": 255
            },
            "data_option_new": {},
            "editable": true,
            "active": true,
            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            },
            "to_create": true,
            "to_migrate": true,
            "to_delete": false,
            "to_config": false,
            "position": 1550,
            "created_by_id": 3,
            "updated_by_id": 3,
            "created_at": "2021-11-12T18:48:15.485Z",
            "updated_at": "2021-11-12T18:48:15.485Z"
         }

.. note::

   Please note that above payloads cover ticket objects.
   This is fine in most situations, except if you're looking at the default
   object permissions. This is why we're listing these separate for you to view.

   The attribute ``object`` controls which context is being used:

      * ``Ticket``
      * ``User``
      * ``Organisation``
      * ``Group``

   .. tabs::

      .. tab:: Ticket

         .. code-block:: json

            "screens": {
               "create_middle": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false,
                     "item_class": "column"
                  }
               },
               "edit": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": true
                  }
               }
            }

      .. tab:: User

         .. code-block:: json

            "screens": {
               "create": {
                  "ticket.customer": {
                     "shown": true,
                     "required": false
                  },
                  "ticket.agent": {
                     "shown": true,
                     "required": false
                  },
                  "admin.user": {
                     "shown": true,
                     "required": false
                  }
               },
               "view": {
                  "ticket.customer": {
                     "shown": true
                  },
                  "ticket.agent": {
                     "shown": true
                  },
                  "admin.user": {
                     "shown": true
                  }
               },
               "edit": {
                  "ticket.agent": {
                     "shown": true,
                     "required": false
                  },
                  "admin.user": {
                     "shown": true,
                     "required": false
                  }
               },
               "signup": {
                  "ticket.customer": {
                     "shown": false,
                     "required": false
                  }
               },
               "invite_customer": {
                  "ticket.agent": {
                     "shown": false,
                     "required": false
                  },
                  "admin.user": {
                     "shown": false,
                     "required": false
                  }
               },
               "invite_agent": {
                  "admin.user": {
                     "shown": false,
                     "required": false
                  }
               }
            }

      .. tab:: Organization

         .. code-block:: json

            "screens": {
               "view": {
                  "ticket.customer": {
                     "shown": true
                  },
                  "ticket.agent": {
                     "shown": true
                  },
                  "admin.organization": {
                     "shown": true
                  }
               },
               "create": {
                  "ticket.agent": {
                     "shown": true,
                     "required": false
                  },
                  "admin.organization": {
                     "shown": true,
                     "required": false
                  }
               },
               "edit": {
                  "ticket.agent": {
                     "shown": true,
                     "required": false
                  },
                  "admin.organization": {
                     "shown": true,
                     "required": false
                  }
               }
            }

      .. tab:: Group

         .. code-block:: json

            "screens": {
               "create": {
                  "admin.group": {
                     "shown": true,
                     "required": false
                  }
               },
               "edit": {
                  "admin.group": {
                     "shown": true,
                     "required": false
                  }
               },
               "view": {
                  "admin.group": {
                     "shown": true
                  }
               }
            }

Update
======

Required permission: ``admin.object``

.. tip::

   Except on the request method, payloads or updating and creating objects are
   identical. For full payload samples thus scroll up to :ref:`create_object`.

   Zammad will return two attributes during update: ``data_option`` and
   ``data_option_new``. The first attribute contains the current active values
   and the second one the new to be values
   (they'll become active after executing the database migrations).

``PUT``-Request sent: ``/api/v1/object_manager_attributes/{id}``

.. code-block:: json

   {
      "id": 50,
      "name": "sample_boolean",
      "object": "Ticket",
      "display": "Sample Boolean",
      "data_type": "boolean",
      "position": 1200, 
      "data_option": {
         "options": {
            "true": "yes",
            "false": "no"
         },
         "default": "false"
      }
   }

.. note::

   Ensure to provide ``data_option``. Zammad is very picky if you leave out
   this attribute. Please note that changing the object type *after* creation
   is not possible.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "name": "sample_boolean",
      "display": "Sample Boolean",
      "data_type": "boolean",
      "position": 1200,
      "data_option_new": {
         "options": {
            "false": "no",
            "true": "yes"
         },
         "default": false,
         "null": true,
         "relation": ""
      },
      "data_option": {
         "options": {
            "false": "very incorrect indeed",
            "true": "very correct indeed"
         },
         "default": null,
         "null": true,
         "relation": ""
      },
      "object_lookup_id": 2,
      "to_config": true,
      "editable": true,
      "id": 50,
      "updated_by_id": 3,
      "active": true,
      "screens": {
         "create_middle": {
            "ticket.customer": {
               "shown": true,
               "required": false,
               "item_class": "column"
            },
            "ticket.agent": {
               "shown": true,
               "required": false,
               "item_class": "column"
            }
         },
         "edit": {
            "ticket.customer": {
               "shown": true,
               "required": false
            },
            "ticket.agent": {
               "shown": true,
               "required": true
            }
         }
      },
      "to_create": false,
      "to_migrate": false,
      "to_delete": false,
      "created_by_id": 3,
      "created_at": "2021-11-12T18:18:23.208Z",
      "updated_at": "2021-11-12T19:30:20.883Z"
   }

Delete
======

Required permission: ``admin.object``

``DELETE``-Request sent: ``/api/v1/object_manager_attributes/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}

Execute Database Migrations
===========================

Required permission: ``admin.object``

.. warning::

   After executing the database migrations a restart of Zammad is *mandatory*.
   If configured Zammad also can restart automatically
   (this is the case on Hosted environments) – expect a short downtime.

``POST``-Request sent: ``/api/v1/object_manager_attributes_execute_migrations``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
