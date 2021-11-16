Articles
********

General information about ticket articles
-----------------------------------------

Some attributes of articles might not be straight forward or come with
fairly many options - below list hopefully helps you on this journey.

content_type
   Zammad supports ``text/html`` for HTML formatted text or ``text/plain`` for
   plain text. This allows you to have better formatting options if you need
   them.

   .. hint::

      Zammad web UI usually uses ``text/html``.

type
   Zammad supports a huge number of article types.
   Below list may be incomplete depending on your instance and possibly
   installed add-ons / custom changes.

   .. note:: 

      💬 If not stated otherwise, all article types below are communication
      articles and thus affecting SLA calculation in Zammad defaults.

      😖 What's the difference?!
         Communication articles provide the option to reply automatically.
         Which actions exactly are available depends on the article type
         and e.g. recipient lists.

         .. figure:: /images/api/ticket-article_reply-buttons.png
            :alt: Reply and forward buttons on email article
            :width: 90%

   ``email``
      This allows you to create incoming or outgoing email articles.

         .. hint::

            This allows you to send Email via API.
            However, this highly depends on the chosen ``sender``.

   ``phone``
      Indicates phone notes.

   ``web``
      Usually used by customers only.
      This type is being used when ever your customer uses the web UI to
      create articles.

   ``note``
      When ever a communication does not fit (e.g.: internal notes) choose note.
      Zammad also uses this article type as default fall back.

         .. note::

            😶 This *is not* a communication article.

   ``sms``
      This type is being used for Zammads SMS integration.

   ``chat``
      This article type is technically a place holder and is only available
      via API.

   ``fax``
      This article type is technically a place holder and is only available
      via API.

   ``twitter status`` & ``twitter direct-message``
      These articles types are used by Zammads twitter channel.
      Technically you can use these to automatically respond to existing
      requests via twitter.

   ``facebook feed post`` & ``facebook feed comment``
      These articles types are used by Zammads facebook channel.
      Technically you can use these to automatically respond to existing
      requests via facebook.

   ``telegram personal-message``
      Used by Zammads Telegram channel.
      Technically you can use these to automatically respond to existing
      requests via Telegram.

internal
   This attribute allows you to set the visibility of your articles.
   For internal visible only use ``true``, for visibly for your customers as
   well use ``false``.

      .. warning:: **🔒 Visibility: internal doesn't mean it's silent**

         If you set an article to ``internal: true`` but choose to send
         an email, please be aware that said Email is still being sent out!

sender
   Indicates which use did create the article. You can choose from:

      * ``Agent``
      * ``Customer``
      * ``System``

   .. warning::

      Depending of above selection, some article types may not be available or
      behave different. Please be aware that ``System`` causes users not being
      able to read the bodies (this works similar to Zammads trigger displaying
      in tickets).

.. _retrieve_articles_attachments:

List Articles by Ticket
=======================

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_articles/by_ticket/{ticket id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK
   
   [
      {
         "id": 9,
         "ticket_id": 5,
         "type_id": 1,
         "sender_id": 2,
         "from": "David Bell <david@example.com>",
         "to": "order@chrispresso.com",
         "cc": null,
         "subject": null,
         "reply_to": null,
         "message_id": null,
         "message_id_md5": null,
         "in_reply_to": null,
         "content_type": "text/html",
         "references": null,
         "body": "Hi,<br>\n<br>\n<u>please send me:</u><br>\n1 x Café Kopi susu<br>\n4 x Viennese melange<br>\n<br>\n<u>Delivery Address:</u><br>\nDavid Bell<br>\nEiffel Tower<br>\n5 Avenue Anatole France<br>\n75007 Paris<br>\n<span class=\"js-signatureMarker\"></span>\n<br>\nDavid Bell",
         "internal": false,
         "preferences": {},
         "updated_by_id": 10,
         "created_by_id": 10,
         "origin_by_id": null,
         "created_at": "2021-08-02T11:57:18.068Z",
         "updated_at": "2021-08-02T11:57:18.068Z",
         "attachments": [],
         "type": "email",
         "sender": "Customer",
         "created_by": "david@example.com",
         "updated_by": "david@example.com"
      },
      {
         "id": 10,
         "ticket_id": 5,
         "type_id": 1,
         "sender_id": 1,
         "from": "Emma Taylor via <order@chrispresso.com>",
         "to": "David Bell <david@example.com>",
         "cc": null,
         "subject": null,
         "reply_to": null,
         "message_id": null,
         "message_id_md5": null,
         "in_reply_to": null,
         "content_type": "text/html",
         "references": null,
         "body": "Hi David,<br>\n<br>\nnice, we will ship it to your delivery address:<br>\n<br>\nEiffel Tower\n5 Avenue Anatole France\n75007 Paris.<br>\n<br>\nYou will get it till Wednesday.<br>\n<span class=\"js-signatureMarker\"></span>\n<br>\n--<br>\nGreetings,<br>\n<br>\nEmma Taylor<br>",
         "internal": false,
         "preferences": {},
         "updated_by_id": 5,
         "created_by_id": 5,
         "origin_by_id": null,
         "created_at": "2021-08-03T09:57:18.121Z",
         "updated_at": "2021-08-03T09:57:18.121Z",
         "attachments": [],
         "type": "email",
         "sender": "Agent",
         "created_by": "emma@chrispresso.com",
         "updated_by": "emma@chrispresso.com"
      }
   ]

List specific article
=====================

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_articles/{article id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK
   
   {
      "id": 9,
      "ticket_id": 5,
      "type_id": 1,
      "sender_id": 2,
      "from": "David Bell <david@example.com>",
      "to": "order@chrispresso.com",
      "cc": null,
      "subject": null,
      "reply_to": null,
      "message_id": null,
      "message_id_md5": null,
      "in_reply_to": null,
      "content_type": "text/html",
      "references": null,
      "body": "Hi,<br>\n<br>\n<u>please send me:</u><br>\n1 x Café Kopi susu<br>\n4 x Viennese melange<br>\n<br>\n<u>Delivery Address:</u><br>\nDavid Bell<br>\nEiffel Tower<br>\n5 Avenue Anatole France<br>\n75007 Paris<br>\n<span class=\"js-signatureMarker\"></span>\n<br>\nDavid Bell",
      "internal": false,
      "preferences": {},
      "updated_by_id": 10,
      "created_by_id": 10,
      "origin_by_id": null,
      "created_at": "2021-08-02T11:57:18.068Z",
      "updated_at": "2021-08-02T11:57:18.068Z",
      "attachments": [],
      "type": "email",
      "sender": "Customer",
      "created_by": "david@example.com",
      "updated_by": "david@example.com"
   }


Create
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

   .. tip:: 

      If you want to create articles on behalf other users (e.g. for a phone 
      note), use the ``origin_by_id`` attribute. ``ticket.agent`` permission
      is mandatory for this.

``POST``-Request sent: ``/api/v1/ticket_articles``

.. tabs::

   .. tab:: Plain article

      .. code-block:: json

         {
            "ticket_id": 5,
            "subject": "Call note",
            "body": "Called the customer and discussed their issues.<br/>Turns out these were caused by invalid configurations - solved.",
            "content_type": "text/html",
            "type": "phone",
            "internal": false,
            "sender": "Agent",
            "time_unit": "15"
         }


      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created
         
         {
            "id": 33,
            "ticket_id": 5,
            "type_id": 5,
            "sender_id": 1,
            "from": "Christopher Miller",
            "to": null,
            "cc": null,
            "subject": "Call note",
            "reply_to": null,
            "message_id": null,
            "message_id_md5": null,
            "in_reply_to": null,
            "content_type": "text/html",
            "references": null,
            "body": "Called the customer and discussed their issues.<br>Turns out these were caused by invalid configurations - solved.",
            "internal": false,
            "preferences": {},
            "updated_by_id": 3,
            "created_by_id": 3,
            "origin_by_id": null,
            "created_at": "2021-11-08T16:13:35.962Z",
            "updated_at": "2021-11-08T16:13:35.962Z",
            "attachments": [],
            "type": "phone",
            "sender": "Agent",
            "created_by": "chris@chrispresso.com",
            "updated_by": "chris@chrispresso.com"
         }

   .. tab:: Article with attached files

         .. hint::

            The first attachment example does work, remove the second "generalized"
            part to try the payload out. 🔨

      .. code-block:: json

         {
            "ticket_id": 5,
            "to": "",
            "cc": "",
            "subject": "some subject",
            "body": "Please see attached file...",
            "content_type": "text/plain",
            "type": "note",
            "internal": true,
            "time_unit": "25",
            "attachments": [
               {
                  "filename": "portal.txt",
                  "data": "VGhlIGNha2UgaXMgYSBsaWUhCg==",
                  "mime-type": "text/plain"
               },
               {
                  "filename": "{filename}",
                  "data": "{file content base64 encoded}",
                  "mime-type": "{attachments mime-type}"
               }
            ]
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP-Code 201 Created
         
         {
            "id": 35,
            "ticket_id": 5,
            "type_id": 10,
            "sender_id": 1,
            "from": "Christopher Miller",
            "to": "",
            "cc": "",
            "subject": "some subject",
            "reply_to": null,
            "message_id": null,
            "message_id_md5": null,
            "in_reply_to": null,
            "content_type": "text/plain",
            "references": null,
            "body": "Please see attached file...",
            "internal": true,
            "preferences": {},
            "updated_by_id": 3,
            "created_by_id": 3,
            "origin_by_id": null,
            "created_at": "2021-11-09T12:02:55.434Z",
            "updated_at": "2021-11-09T12:02:55.434Z",
            "attachments": [
               {
                  "id": 17,
                  "filename": "portal.txt",
                  "size": "19",
                  "preferences": {
                     "Mime-Type": "text/plain"
                  }
               }
            ],
            "type": "note",
            "sender": "Agent",
            "created_by": "chris@chrispresso.com",
            "updated_by": "chris@chrispresso.com"
         }

   .. tab:: Article with inline images

      Inline images can be used by providing data URIs in your HTML markup.

      .. code-block:: json

         {
            "ticket_id": 5,
            "to": "",
            "cc": "",
            "subject": "some subject",
            "body": "Let's see the <b>phoenix</b> <img src=\"data:image/png;base64,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\">",
            "content_type": "text/html",
            "type": "note",
            "internal": false,
            "time_unit": "12"
         }

      Response:

      .. code-block:: json
         :force:

         # HTTP Code 201 Created
         
         {
            "id": 37,
            "ticket_id": 5,
            "type_id": 10,
            "sender_id": 1,
            "from": "Christopher Miller",
            "to": "",
            "cc": "",
            "subject": "some subject",
            "reply_to": null,
            "message_id": null,
            "message_id_md5": null,
            "in_reply_to": null,
            "content_type": "text/html",
            "references": null,
            "body": "Let's see the <b>phoenix</b> <img src=\"/api/v1/ticket_attachment/5/37/19?view=inline\" style=\"max-width:100%;\">",
            "internal": false,
            "preferences": {},
            "updated_by_id": 3,
            "created_by_id": 3,
            "origin_by_id": null,
            "created_at": "2021-11-09T12:10:49.375Z",
            "updated_at": "2021-11-09T12:10:49.375Z",
            "attachments": [
               {
                  "id": 19,
                  "filename": "image1.png",
                  "size": "3735",
                  "preferences": {
                     "Content-Type": "image/png",
                     "Mime-Type": "image/png",
                     "Content-ID": "5.e384b84e-bfef-49f7-af22-8546fb99f8dc@fqdn",
                     "Content-Disposition": "inline"
                  }
               }
            ],
            "type": "note",
            "sender": "Agent",
            "created_by": "chris@chrispresso.com",
            "updated_by": "chris@chrispresso.com"
         }

Receive attachments
===================

Now that you have all those fancy attachments within your tickets, you
may want to download specific ones.

``GET``-Request sent: 
``/api/v1/ticket_attachment/{ticket id}/{article id}/{attachment id}``

Response:

   .. figure:: /images/zammad_logo_70x61.png
      :alt: Returned image attachment

.. hint::

   If you're not sure which articles a ticket / article contains, please
   :ref:`retrieve <retrieve_articles_attachments>` affected articles first.
