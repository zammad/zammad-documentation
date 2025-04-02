Tickets
=======

.. warning::

   Ticket endpoints depend on group permissions and if the user you're
   using is an **agent**. Because of this tickets may or may not be available.

List
----

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 1,
         "group_id": 1,
         "priority_id": 2,
         "state_id": 1,
         "organization_id": 1,
         "number": "22001",
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
         "last_contact_at": "2021-11-03T11:51:13.790Z",
         "last_contact_agent_at": null,
         "last_contact_customer_at": "2021-11-03T11:51:13.790Z",
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
         "created_at": "2021-11-03T11:51:13.759Z",
         "updated_at": "2021-11-03T11:51:13.809Z"
      },
      {
         "id": 2,
         "group_id": 1,
         "priority_id": 2,
         "state_id": 4,
         "organization_id": 3,
         "number": "22002",
         "title": "Order 777555",
         "owner_id": 3,
         "customer_id": 6,
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
         "last_contact_at": "2021-05-04T16:57:17.920Z",
         "last_contact_agent_at": "2021-05-03T10:57:17.904Z",
         "last_contact_customer_at": "2021-05-04T16:57:17.920Z",
         "last_owner_update_at": null,
         "create_article_type_id": 1,
         "create_article_sender_id": 2,
         "article_count": 3,
         "escalation_at": null,
         "pending_time": null,
         "type": null,
         "time_unit": null,
         "preferences": {},
         "updated_by_id": 6,
         "created_by_id": 6,
         "created_at": "2021-05-03T09:57:17.837Z",
         "updated_at": "2021-11-03T11:57:17.927Z"
      },

      ...
   ]

Show
----

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets/{ticket id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 3,
      "group_id": 1,
      "priority_id": 2,
      "state_id": 4,
      "organization_id": 3,
      "number": "22003",
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
      "last_contact_at": "2021-06-03T09:57:17.987Z",
      "last_contact_agent_at": "2021-06-03T09:57:17.987Z",
      "last_contact_customer_at": "2021-06-01T11:57:17.935Z",
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
      "created_at": "2021-06-01T11:57:17.935Z",
      "updated_at": "2021-11-03T11:57:17.997Z"
   }

Create
------

Required permission: ``ticket.agent`` **or** ``ticket.customer``

.. tip::

   **🐱‍👤 On behalf of users**

   If you want to create tickets on behalf of other users, use
   the ``customer_id`` attribute. ``ticket.agent`` is mandatory for this.
   Use ``guess:{email address}`` to save an API call if you don't know the
   user's ID or want to create the user in question
   (``"customer_id": "guess:jane@doe.com"``).

   **📣 Add mention subscription right away**

   Add the ``mentions`` attribute to your ticket payload and provide
   an array of user ids to directly subscribe them during ticket creation.

   *E.g.:* ``"mentions": [1, 5, 7, 8],``

``POST``-Request sent: ``/api/v1/tickets``

.. code-block:: json

   {
      "title": "Help me!",
      "group": "2nd Level",
      "customer": "david@example.com",
      "article": {
         "subject": "My subject",
         "body": "I am a message!",
         "type": "note",
         "internal": false
      }
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 19,
      "group_id": 2,
      "priority_id": 2,
      "state_id": 1,
      "organization_id": null,
      "number": "22019",
      "title": "Help me!",
      "owner_id": 1,
      "customer_id": 10,
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
      "last_contact_at": null,
      "last_contact_agent_at": null,
      "last_contact_customer_at": null,
      "last_owner_update_at": null,
      "create_article_type_id": 10,
      "create_article_sender_id": 1,
      "article_count": 1,
      "escalation_at": null,
      "pending_time": null,
      "type": null,
      "time_unit": null,
      "preferences": {},
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T14:17:41.913Z",
      "updated_at": "2021-11-08T14:17:41.994Z",
      "article_ids": [
         30
      ],
      "ticket_time_accounting_ids": []
   }

.. hint::

   For more article attributes and options have a look into :doc:`articles`.

Update
------

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``PUT``-Request sent: ``/api/v1/tickets/{ticket id}``

.. code-block:: json
   :force:

   {
      "title": "No help for you",
      "group": "Sales",
      "state": "open",
      "priority": "3 high",
      "article": {
         "subject": "Update via API",
         "body": "Here's my reason for updating this ticket...",
         "internal": true
      }
   }

.. note::

   Above example provides an article. This article is a *new article* and
   does not affect any existing ones.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 19,
      "group_id": 1,
      "priority_id": 3,
      "state_id": 2,
      "organization_id": null,
      "number": "22019",
      "title": "No help for you",
      "owner_id": 1,
      "customer_id": 10,
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
      "last_contact_at": null,
      "last_contact_agent_at": null,
      "last_contact_customer_at": null,
      "last_owner_update_at": null,
      "create_article_type_id": 10,
      "create_article_sender_id": 1,
      "article_count": 2,
      "escalation_at": null,
      "pending_time": null,
      "type": null,
      "time_unit": null,
      "preferences": {},
      "updated_by_id": 3,
      "created_by_id": 3,
      "created_at": "2021-11-08T14:17:41.913Z",
      "updated_at": "2021-11-08T14:18:53.426Z",
      "article_ids": [
         31,
         30
      ],
      "ticket_time_accounting_ids": []
   }

.. tip:: **Adding attachments**

   Attachment payloads are identical to the ``POST`` method, just use ``PUT``
   instead.

Delete
------

Required permission: ``admin``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing tickets cannot be undone.
   All data (e.g.: articles & attachments) will be lost.

``DELETE``-Request sent: ``/api/v1/tickets/{ticket id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok
   {}
