User Access Token
*****************

List
====

Required permission: ``user_preferences.access_token``

``GET``-Request sent: ``/api/v1/user_access_token``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "tokens": [
         {
            "id": 2,
            "user_id": 3,
            "action": "api",
            "label": "test",
            "preferences": {
               "permission": [
                  "user_preferences.access_token"
               ]
            },
            "last_used_at": "2021-11-11T14:29:22.765Z",
            "expires_at": null,
            "created_at": "2021-11-10T23:17:46.570Z",
            "updated_at": "2021-11-11T14:29:22.765Z"
         },
         {
            "id": 1,
            "user_id": 3,
            "action": "api",
            "label": "full",
            "preferences": {
               "permission": [
                  "admin",
                  "ticket.agent"
               ]
            },
            "last_used_at": "2021-11-10T23:12:06.078Z",
            "expires_at": null,
            "created_at": "2021-11-09T13:17:20.446Z",
            "updated_at": "2021-11-10T23:12:06.078Z"
         }
      ],
      "permissions": [
         {
            "id": 1,
            "name": "admin",
            "note": "Admin Interface",
            "preferences": {},
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.544Z",
            "updated_at": "2021-11-09T13:12:31.544Z"
         },
         {
            "id": 32,
            "name": "admin.api",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "API"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.754Z",
            "updated_at": "2021-11-09T13:12:31.754Z"
         },
         {
            "id": 26,
            "name": "admin.branding",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Branding"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.713Z",
            "updated_at": "2021-11-09T13:12:31.713Z"
         },
         {
            "id": 11,
            "name": "admin.calendar",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Calendar"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.626Z",
            "updated_at": "2021-11-09T13:12:31.626Z"
         },
         {
            "id": 25,
            "name": "admin.channel_chat",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Chat"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.704Z",
            "updated_at": "2021-11-09T13:12:31.704Z"
         },
         {
            "id": 18,
            "name": "admin.channel_email",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Email"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.665Z",
            "updated_at": "2021-11-09T13:12:31.665Z"
         },
         {
            "id": 20,
            "name": "admin.channel_facebook",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Facebook"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.676Z",
            "updated_at": "2021-11-09T13:12:31.676Z"
         },
         {
            "id": 17,
            "name": "admin.channel_formular",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Formular"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.659Z",
            "updated_at": "2021-11-09T13:12:31.659Z"
         },
         {
            "id": 22,
            "name": "admin.channel_google",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Google"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.687Z",
            "updated_at": "2021-11-09T13:12:31.687Z"
         },
         {
            "id": 23,
            "name": "admin.channel_microsoft365",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Microsoft 365"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.693Z",
            "updated_at": "2021-11-09T13:12:31.693Z"
         },
         {
            "id": 24,
            "name": "admin.channel_sms",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - SMS"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.699Z",
            "updated_at": "2021-11-09T13:12:31.699Z"
         },
         {
            "id": 21,
            "name": "admin.channel_telegram",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Telegram"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.682Z",
            "updated_at": "2021-11-09T13:12:31.682Z"
         },
         {
            "id": 19,
            "name": "admin.channel_twitter",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Twitter"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.671Z",
            "updated_at": "2021-11-09T13:12:31.671Z"
         },
         {
            "id": 16,
            "name": "admin.channel_web",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Channel - Web"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.654Z",
            "updated_at": "2021-11-09T13:12:31.654Z"
         },
         {
            "id": 40,
            "name": "admin.core_workflow",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Core Workflow"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.807Z",
            "updated_at": "2021-11-09T13:12:31.807Z"
         },
         {
            "id": 36,
            "name": "admin.data_privacy",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Data Privacy"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.783Z",
            "updated_at": "2021-11-09T13:12:31.783Z"
         },
         {
            "id": 3,
            "name": "admin.group",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Groups"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.565Z",
            "updated_at": "2021-11-09T13:12:31.565Z"
         },
         {
            "id": 31,
            "name": "admin.integration",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Integrations"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.748Z",
            "updated_at": "2021-11-09T13:12:31.748Z"
         },
         {
            "id": 59,
            "name": "admin.knowledge_base",
            "note": "Create and setup %s",
            "preferences": {
               "translations": [
                  "Knowledge Base"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.992Z",
            "updated_at": "2021-11-09T13:12:31.992Z"
         },
         {
            "id": 9,
            "name": "admin.macro",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Macros"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.612Z",
            "updated_at": "2021-11-09T13:12:31.612Z"
         },
         {
            "id": 37,
            "name": "admin.maintenance",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Maintenance"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.789Z",
            "updated_at": "2021-11-09T13:12:31.789Z"
         },
         {
            "id": 35,
            "name": "admin.monitoring",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Monitoring"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.777Z",
            "updated_at": "2021-11-09T13:12:31.777Z"
         },
         {
            "id": 33,
            "name": "admin.object",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Objects"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.760Z",
            "updated_at": "2021-11-09T13:12:31.760Z"
         },
         {
            "id": 5,
            "name": "admin.organization",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Organizations"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.579Z",
            "updated_at": "2021-11-09T13:12:31.579Z"
         },
         {
            "id": 6,
            "name": "admin.overview",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Overviews"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.591Z",
            "updated_at": "2021-11-09T13:12:31.591Z"
         },
         {
            "id": 30,
            "name": "admin.package",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Packages"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.738Z",
            "updated_at": "2021-11-09T13:12:31.738Z"
         },
         {
            "id": 15,
            "name": "admin.report_profile",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Report Profiles"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.648Z",
            "updated_at": "2021-11-09T13:12:31.648Z"
         },
         {
            "id": 4,
            "name": "admin.role",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Roles"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.572Z",
            "updated_at": "2021-11-09T13:12:31.572Z"
         },
         {
            "id": 14,
            "name": "admin.scheduler",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Scheduler"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.642Z",
            "updated_at": "2021-11-09T13:12:31.642Z"
         },
         {
            "id": 28,
            "name": "admin.security",
            "note": "Manage %s Settings",
            "preferences": {
               "translations": [
                  "Security"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.725Z",
            "updated_at": "2021-11-09T13:12:31.725Z"
         },
         {
            "id": 38,
            "name": "admin.session",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Sessions"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.795Z",
            "updated_at": "2021-11-09T13:12:31.795Z"
         },
         {
            "id": 27,
            "name": "admin.setting_system",
            "note": "Manage %s Settings",
            "preferences": {
               "translations": [
                  "System"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.719Z",
            "updated_at": "2021-11-09T13:12:31.719Z"
         },
         {
            "id": 12,
            "name": "admin.sla",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "SLA"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.631Z",
            "updated_at": "2021-11-09T13:12:31.631Z"
         },
         {
            "id": 10,
            "name": "admin.tag",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Tags"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.619Z",
            "updated_at": "2021-11-09T13:12:31.619Z"
         },
         {
            "id": 7,
            "name": "admin.text_module",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Text Modules"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.598Z",
            "updated_at": "2021-11-09T13:12:31.598Z"
         },
         {
            "id": 29,
            "name": "admin.ticket",
            "note": "Manage %s Settings",
            "preferences": {
               "translations": [
                  "Ticket"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.731Z",
            "updated_at": "2021-11-09T13:12:31.731Z"
         },
         {
            "id": 8,
            "name": "admin.time_accounting",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Time Accounting"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.606Z",
            "updated_at": "2021-11-09T13:12:31.606Z"
         },
         {
            "id": 34,
            "name": "admin.translation",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Translations"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.767Z",
            "updated_at": "2021-11-09T13:12:31.767Z"
         },
         {
            "id": 13,
            "name": "admin.trigger",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Triggers"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.637Z",
            "updated_at": "2021-11-09T13:12:31.637Z"
         },
         {
            "id": 2,
            "name": "admin.user",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Users"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.556Z",
            "updated_at": "2021-11-09T13:12:31.556Z"
         },
         {
            "id": 39,
            "name": "admin.webhook",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Webhooks"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.801Z",
            "updated_at": "2021-11-09T13:12:31.801Z"
         },
         {
            "id": 55,
            "name": "chat",
            "note": "Access to %s",
            "preferences": {
               "translations": [
                  "Chat"
               ],
               "disabled": true
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.901Z",
            "updated_at": "2021-11-09T13:12:31.901Z"
         },
         {
            "id": 56,
            "name": "chat.agent",
            "note": "Access to %s",
            "preferences": {
               "translations": [
                  "Chat"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.909Z",
            "updated_at": "2021-11-09T13:12:31.909Z"
         },
         {
            "id": 57,
            "name": "cti",
            "note": "CTI",
            "preferences": {
               "disabled": true
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.916Z",
            "updated_at": "2021-11-09T13:12:31.916Z"
         },
         {
            "id": 58,
            "name": "cti.agent",
            "note": "Access to %s",
            "preferences": {
               "translations": [
                  "CTI"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.922Z",
            "updated_at": "2021-11-09T13:12:31.922Z"
         },
         {
            "id": 60,
            "name": "knowledge_base",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Knowledge Base"
               ],
               "disabled": true
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.999Z",
            "updated_at": "2021-11-09T13:12:31.999Z"
         },
         {
            "id": 61,
            "name": "knowledge_base.editor",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Knowledge Base Editor"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:32.006Z",
            "updated_at": "2021-11-09T13:12:32.006Z"
         },
         {
            "id": 62,
            "name": "knowledge_base.reader",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Knowledge Base Reader"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:32.012Z",
            "updated_at": "2021-11-09T13:12:32.012Z"
         },
         {
            "id": 51,
            "name": "report",
            "note": "Report Interface",
            "preferences": {},
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.875Z",
            "updated_at": "2021-11-09T13:12:31.875Z"
         },
         {
            "id": 52,
            "name": "ticket",
            "note": "Ticket Interface",
            "preferences": {
               "disabled": true
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.880Z",
            "updated_at": "2021-11-09T13:12:31.880Z"
         },
         {
            "id": 53,
            "name": "ticket.agent",
            "note": "Access to Agent Tickets based on Group Access",
            "preferences": {
               "plugin": [
                  "groups"
               ]
            },
            "active": true,
            "allow_signup": false,
            "created_at": "2021-11-09T13:12:31.888Z",
            "updated_at": "2021-11-09T13:12:31.888Z"
         },
         {
            "id": 41,
            "name": "user_preferences",
            "note": "User Preferences",
            "preferences": {},
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.812Z",
            "updated_at": "2021-11-09T13:12:31.812Z"
         },
         {
            "id": 44,
            "name": "user_preferences.access_token",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Token Access"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.829Z",
            "updated_at": "2021-11-09T13:12:31.829Z"
         },
         {
            "id": 48,
            "name": "user_preferences.avatar",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Avatar"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.852Z",
            "updated_at": "2021-11-09T13:12:31.852Z"
         },
         {
            "id": 49,
            "name": "user_preferences.calendar",
            "note": "Access to %s",
            "preferences": {
               "translations": [
                  "Calendars"
               ],
               "required": [
                  "ticket.agent"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.857Z",
            "updated_at": "2021-11-09T13:12:31.857Z"
         },
         {
            "id": 47,
            "name": "user_preferences.device",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Devices"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.847Z",
            "updated_at": "2021-11-09T13:12:31.847Z"
         },
         {
            "id": 45,
            "name": "user_preferences.language",
            "note": "Change %s",
            "preferences": {
               "translations": [
                  "Language"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.834Z",
            "updated_at": "2021-11-09T13:12:31.834Z"
         },
         {
            "id": 46,
            "name": "user_preferences.linked_accounts",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Linked Accounts"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.840Z",
            "updated_at": "2021-11-09T13:12:31.840Z"
         },
         {
            "id": 43,
            "name": "user_preferences.notifications",
            "note": "Manage %s",
            "preferences": {
               "translations": [
                  "Notifications"
               ],
               "required": [
                  "ticket.agent"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.823Z",
            "updated_at": "2021-11-09T13:12:31.823Z"
         },
         {
            "id": 50,
            "name": "user_preferences.out_of_office",
            "note": "Change %s",
            "preferences": {
               "translations": [
                  "Out of Office"
               ],
               "required": [
                  "ticket.agent"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.868Z",
            "updated_at": "2021-11-09T13:12:31.868Z"
         },
         {
            "id": 42,
            "name": "user_preferences.password",
            "note": "Change %s",
            "preferences": {
               "translations": [
                  "Password"
               ]
            },
            "active": true,
            "allow_signup": true,
            "created_at": "2021-11-09T13:12:31.818Z",
            "updated_at": "2021-11-09T13:12:31.818Z"
         }
      ]
   }

Create
======

Required permission: ``user_preferences.access_token``

``POST``-Request sent: ``/api/v1/user_access_token``

.. code-block:: json

   {
      "label": "My amazing test",
      "permission": ["cti.agent","ticket.agent"],
      "expires_at": "2021-12-21"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "name": "M4oXJgB_8WiMNWzSdrDv3K3YXJywDh52BqC7IKV-NnM_Cf_bd_SkS6zyIWNZKJXw"
   }

.. note::

   Above returned ``name`` is the API token. This value is provided once after
   creation and can't be retrieved after.

Delete
======

Required permission: ``user_preferences.access_token``

``DELETE``-Request sent: ``/api/v1/user_access_token/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
