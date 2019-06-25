Ticket Article
******

By Ticket
====

Required permission:

* ticket.agent (access to related ticket)
* ticket.customer (access to related ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 GET /api/v1/ticket_articles/by_ticket/{ticketId}

Response::

 Status: 200 Ok
 
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

Show
====

Required permission:

* ticket.agent (access to related ticket)
* ticket.customer (access to related ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 GET /api/v1/ticket_articles/{id}


Response::

 Status: 200 Ok

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
    ...
    "created_at": "2016-10-19T10:07:12.011Z",
    "updated_at": "2017-01-18T12:45:53.420Z"
 }


Create
======

Required permission:

* ticket.agent (access to related ticket)
* ticket.customer (access to related ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 POST /api/v1/ticket_articles

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

Response::

 Status: 201 Created

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
    "time_unit": "12.0"
    ...
    "created_at": "2016-10-19T10:07:12.011Z",
    "updated_at": "2017-01-18T12:45:53.420Z"
 }


If you want to include attachments of articles, the payload looks like:

Request::

 POST /api/v1/ticket_articles

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

Response::

 Status: 201 Created

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
    "time_unit": "12.0"
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
    ...
    "created_at": "2016-10-19T10:07:12.011Z",
    "updated_at": "2017-01-18T12:45:53.420Z"
 }

To download attachments you need to call "GET /api/v1/ticket_attachment/#{ticket_id}/#{article_id}/#{id}".


If you want to add inline images, just use data URIs in HTML markup:

Request::

 POST /api/v1/ticket_articles

 {
    "ticket_id": 3,
    "to": "",
    "cc": "",
    "subject": "some subject",
    "body": "<b>some</b> message witn inline image <img src=\"data:image/jpeg;base64,ABCDEFG==\">"
    "content_type": "text/html",
    "type": "note",
    "internal": false,
    "time_unit": "12"
 }

Response::

 Status: 201 Created

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
    "time_unit": "12.0"
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
    ...
    "created_at": "2016-10-19T10:07:12.011Z",
    "updated_at": "2017-01-18T12:45:53.420Z"
 }

To download attachments you need to call "GET /api/v1/ticket_attachment/#{ticket_id}/#{article_id}/#{id}".

If you want to create a phone ticket on behalf for a specific customer, use origin_by_id:

Required permission:

* ticket.agent (access to related ticket)

Request::

 POST /api/v1/ticket_articles

 {
    "ticket_id": 3,
    "origin_by_id": 5,
    "to": "",
    "cc": "",
    "subject": "some subject",
    "body": "<b>some</b> message witn inline image <img src=\"data:image/jpeg;base64,ABCDEFG==\">"
    "content_type": "text/html",
    "sender": "Customer",
    "type": "phone",
    "internal": false,
    "time_unit": "12"
 }
