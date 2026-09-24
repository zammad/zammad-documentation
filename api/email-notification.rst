Email Notification
==================

.. note::

   This page covers the system's outbound **notification** email
   configuration: the SMTP (or local MTA) settings Zammad uses to send
   its own internal notifications, like "you were assigned a ticket",
   plus the local sender identity (``EmailAddress``) that gets attached
   to it. This is distinct from a ticket mailbox / support-inbox
   channel (Admin → Channels → Email, for customer correspondence),
   which is a separate feature not covered by this page.

List
----

Required permission: ``admin.channel_email``

``GET``-Request sent: ``/api/v1/channels_email``

This is a combined index: it returns the notification channel(s), the
ticket mailbox channel(s) (empty in this example), and the local sender
addresses in one response. The response below is
trimmed to the fields relevant to notification email configuration.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "notification_channel_ids": [1],
      "account_channel_ids": [],
      "email_address_ids": [1],
      "assets": {
         "Channel": {
            "1": {
               "id": 1,
               "group_id": null,
               "area": "Email::Notification",
               "options": {
                  "outbound": {
                     "adapter": "smtp",
                     "options": {
                        "host": "mailpit",
                        "port": 1025,
                        "ssl": false,
                        "ssl_verify": false,
                        "user": "",
                        "password": "",
                        "domain": "your-zammad-host",
                        "enable_starttls_auto": true
                     }
                  }
               },
               "active": true
            },
            "2": {
               "id": 2,
               "group_id": null,
               "area": "Email::Notification",
               "options": {
                  "outbound": {"adapter": "sendmail"}
               },
               "active": false
            }
         }
      },
      "channel_driver": {
         "email": {
            "inbound": {"imap": "IMAP", "pop3": "POP3"},
            "outbound": {
               "smtp": "SMTP - configure your own outgoing SMTP settings",
               "sendmail": "Local MTA (Sendmail/Postfix/Exim/…) - use server setup"
            }
         }
      },
      "config": {
         "notification_sender": "\"Zammad Helpdesk\" <noreply@your-zammad-host>"
      }
   }

.. note::

   Only one channel can be ``active: true`` per notification setup
   at a time. Configuring a new one (see *Configure* below)
   automatically deactivates whichever one was previously active, in
   the response above, ``sendmail`` (id ``2``) is now ``active: false``
   because ``smtp`` (id ``1``) was configured afterward.

Configure
---------

Required permission: ``admin.channel_email``

``POST``-Request sent: ``/api/v1/channels_email_notification``

.. note::

   Pass the adapter settings in a top-level ``options`` key as shown
   below. Other key names, such as ``new_configuration`` (the parameter
   name of the internal service class
   ``Service::System::SetEmailNotificationConfiguration``), are not
   rejected with a validation error. The request fails with an unhandled
   ``undefined method 'key?' for nil`` error instead.

.. code-block:: json

   {
      "adapter": "smtp",
      "options": {
         "host": "mailpit",
         "port": 1025,
         "ssl": false,
         "ssl_verify": false,
         "user": "",
         "password": ""
      }
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "result": "ok"
   }

.. note::

   This call does double duty: it tests the connection live, sending
   a real test email as a side effect, and if the test succeeds, saves
   the configuration as the active notification channel in the same
   call. There is no separate "save" step; ``notification_channel_ids``
   in ``/api/v1/channels_email`` immediately reflects the new channel.

.. note::

   ``POST /api/v1/channels_email_probe`` is not an alternative to this
   endpoint for a notification-only setup. It always validates a *full*
   inbound and outbound mailbox (``EmailHelper::Probe.full``). Sending
   outbound-only SMTP settings to it returns
   ``{"result": "failed", "reason": "inbound failed"}``, even when the
   outbound settings are correct.

Sender Address
--------------

The local sender identity used for outbound notification email is
managed as an ``EmailAddress`` resource.

List
^^^^

Required permission: ``admin.channel_email`` **or** ``ticket.agent``

``GET``-Request sent: ``/api/v1/email_addresses``

Returns an array of objects, each shaped like the single object shown in
the *Show* response below.

Show
^^^^

Required permission: ``admin.channel_email`` **or** ``ticket.agent``

``GET``-Request sent: ``/api/v1/email_addresses/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 1,
      "channel_id": 1,
      "name": "Example Sender",
      "email": "sender@example.com",
      "note": null,
      "active": true,
      "created_by_id": 3,
      "updated_by_id": 3,
      "group_ids": [1]
   }

Create
^^^^^^

Required permission: ``admin.channel_email``

``POST``-Request sent: ``/api/v1/email_addresses``

.. note::

   ``channel_id`` must reference the ``id`` of the active
   notification channel from *List*/*Configure* above.

.. code-block:: json

   {
      "email": "zammad@local.test",
      "name": "Local Zammad",
      "channel_id": 1,
      "note": "Local-only sender captured by Mailpit."
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 1,
      "channel_id": 1,
      "name": "Local Zammad",
      "email": "zammad@local.test",
      "note": "Local-only sender captured by Mailpit.",
      "active": true,
      "created_by_id": 3,
      "updated_by_id": 3,
      "group_ids": [1, 2, 11]
   }

.. note::

   ``group_ids`` here reflects which Groups have their outbound mail
   pointed at this address. That's set separately, via ``PUT
   /api/v1/groups/{id}`` with ``{"email_address_id": <this id>}``, it
   isn't part of this resource's own payload.

Update
^^^^^^

Required permission: ``admin.channel_email``

``PUT``-Request sent: ``/api/v1/email_addresses/{id}``

Same payload shape as Create above. Sending the full Create payload to
an existing address's ``id`` updates that record in place. It doesn't
create a duplicate. Response is the updated record, same shape as the
Create response above.

Delete
^^^^^^

Required permission: ``admin.channel_email``

.. danger:: **This is a permanent removal**

   Please note that removing email addresses cannot be undone.

   Groups that use the deleted address as their sender address
   (``email_address_id``) are reset to no sender address.

``DELETE``-Request sent: ``/api/v1/email_addresses/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
