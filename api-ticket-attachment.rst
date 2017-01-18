Ticket Attachment
******

Create form id for you upload
====

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Javascript::

 var formId = new Date().getTime() + Math.floor( Math.random() * 99999 );
 formId = formId.toString().substr(formId.toString().length-9, 9);

Result::

 737077480

Upload Attachment
======

To upload an attachment you need to save the attachment to a form id. The uploaded attachment will be saved in a temporarily
storage and you need to create an article with the given form_id to actually save the uploaded attachment to the ticket (Article_).

.. _Article: api-ticket-article.rst#Create

Required permission:

* ticket.agent (access to all ticket in allocated groups)
* ticket.customer (access to all ticket with customer_id ** current_user.id || organization_id ** current_user.organization_id)

Request::

 /api/v1/ticket_attachment_upload

 -----------------------------51522973421953
 Content-Disposition: form-data; name="form_id"

 740771433
 -----------------------------51522973421953
 Content-Disposition: form-data; name="File"; filename="IMG_20160712_194017.jpg"
 Content-Type: image/jpeg

 ...

Response::

 Status: 200 Ok

 {
     "success": true,
     "data": {
         "store_id": 5,
         "filename": "IMG_20160712_194017.jpg",
         "size": "1294722"
     }
 }
