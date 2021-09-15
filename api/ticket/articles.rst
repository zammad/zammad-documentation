Articles
********

List Articles by Ticket
=======================

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_articles/by_ticket/{ticket-id}``

Sample response:

.. code-block:: json
   :force:

   # HTTP-Code 200 OK
   [
      {
         "id": 3,
         "ticket_id": 3,
         "from": "Bob Smith",
         "to": "",
         "cc": "",
         "subject": "some subject",
         "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
         "content_type": "text/html",
         "type": "note",
         "internal": false,
         ...
         "updated_at": "2016-08-15T07:55:42.119Z",
         "created_at": "2016-08-15T07:55:42.119Z"
      },
      {
         "id": 4,
         "ticket_id": 3,
         "from": "Bob Smith",
         "to": "",
         "cc": "",
         "subject": "some subject",
         "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
         "content_type": "text/html",
         "type": "note",
         "internal": false,
         ...
         "updated_at": "2016-08-16T07:55:42.119Z",
         "created_at": "2016-08-16T07:55:42.119Z"
      },
   ]

List specific article
=====================

Required permission: ``ticket.agent`` **or** ``ticket.customer``

``GET``-Request sent: ``/api/v1/ticket_articles/{article-id}``

.. code-block:: json
   :force:

   # HTTP-Code 200 OK
   {
      "id": 3,
      "ticket_id": 3,
      "from": "Bob Smith",
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
      "content_type": "text/html",
      "type": "note",
      "internal": false,
      "attachments": [
         {
            "id": 123,
            "filename": "some_file1.txt",
            "preferences": {
               "Mime-Type": "text/plain"
            }
         },
         {
            "id": 124,
            "filename": "some_file2.txt",
            "preferences": {
               "Mime-Type": "text/plain"
         }
         }
      ],
      "created_at": "2016-10-19T10:07:12.011Z",
      "updated_at": "2017-01-18T12:45:53.420Z",
      ...
   }


Create
======

Required permission: ``ticket.agent`` **or** ``ticket.customer``

   .. tip:: 

      If you want to create articles on behalf other users (e.g. for a phone 
      note), use the ``origin_by_id`` attribute. ``ticket.agent`` is mandatory 
      for this.

``POST``-Request sent: ``/api/v1/ticket_articles``

.. code-block:: json

   {
      "ticket_id": 3,
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
      "content_type": "text/html",
      "type": "note",
      "internal": false,
      "time_unit": "12"
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created
   {
      "id": 3,
      "ticket_id": 3,
      "from": "Bob Smith",
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
      "content_type": "text/html",
      "type": "note",
      "internal": false,
      "time_unit": "12.0",
      "created_at": "2016-10-19T10:07:12.011Z",
      "updated_at": "2017-01-18T12:45:53.420Z",
      ...
   }

If you want to create articles with attachments, use:

``POST``-Request sent: ``/api/v1/ticket_articles``

.. code-block:: json

   {
      "ticket_id": 3,
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
      "content_type": "text/html",
      "type": "note",
      "internal": false,
      "time_unit": "12",
      "attachments": [
         {
            "filename": "some_file1.txt",
            "data": "content in base64",
            "mime-type": "text/plain"
         },
         {
            "filename": "some_file2.txt",
            "data": "content in base64",
            "mime-type": "text/plain"
         }
      ]
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created
   {
      "id": 3,
      "from": "Bob Smith",
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
      "content_type": "text/html",
      "type": "note",
      "internal": false,
      "time_unit": "12.0",
      "attachments": [
         {
            "id": 123,
            "filename": "some_file1.txt",
            "preferences": {
               "Mime-Type": "text/plain"
            }
         },
         {
            "id": 124,
            "filename": "some_file2.txt",
            "preferences": {
               "Mime-Type": "text/plain"
            }
         }
      ],
      "created_at": "2016-10-19T10:07:12.011Z",
      "updated_at": "2017-01-18T12:45:53.420Z",
      ...
   }

In order to retrieve attachments, use this ``GET``-Request: 
``/api/v1/ticket_attachment/#{ticket-id}/#{article-id}/#{attachment-id}``

Zammad supports inline images in article bodies, use data URIs in your HTML 
markup like so:

``POST``-Request sent: ``/api/v1/ticket_articles``

.. code-block:: json

   {
      "ticket_id": 3,
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "<b>some</b> message with inline image <img src=\"data:image/jpeg;base64,ABCDEFG==\">"
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
      "id": 3,
      "ticket_id": 3,
      "from": "Bob Smith",
      "to": "",
      "cc": "",
      "subject": "some subject",
      "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
      "content_type": "text/html",
      "type": "note",
      "internal": false,
      "time_unit": "12.0",
      "attachments": [
         {
            "id": 123,
            "filename": "44.262871107@zammad.example.com",
            "preferences": {
               "Mime-Type": "image/jpeg",
               "Content-ID": "44.262871107@zammad.example.com",
               "Content-Disposition": "inline"
            }
         }
      ],
      "created_at": "2016-10-19T10:07:12.011Z",
      "updated_at": "2017-01-18T12:45:53.420Z",
      ...
   }
