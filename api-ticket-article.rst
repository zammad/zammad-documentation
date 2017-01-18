Ticket Article
******

Create
======

Required permission:

* ticket.agent (create in all allocated groups)
* ticket.customer

Request::

 PUT /api/v1/tickets/:id

 {
     "number": "72003",
     "title": "test",
     "group_id": "1",
     "owner_id": 1,
     "customer_id": 6,
     "state_id": "1",
     "priority_id": "2",
     "article": {
         "from": "Harald Habebe",
         "to": "",
         "cc": "",
         "body": "huhuhuu<br>huhuhuu<br>huhuhuu<br><br>",
         "content_type": "text/html",
         "ticket_id": 3,
         "type_id": 10,
         "sender_id": 1,
         "internal": "true",
         "in_reply_to": "",
         "form_id": "1111111",
         "time_unit": "12"
     },
     "updated_at": "2017-01-18T11:56:13.561Z",
     "pending_time": null,
     "aaaaa": "",
     "anrede": "",
     "asdf": "",
     "id": 3
 }

Response::

 Status: 201 Created

 {
     "id": 3,
     "group_id": 1,
     "priority_id": 2,
     "state_id": 1,
     "organization_id": 3,
     "number": "72003",
     "title": "test",
     "owner_id": 1,
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
     "last_contact_at": "2016-10-19T10:07:12.072Z",
     "last_contact_agent_at": null,
     "last_contact_customer_at": "2016-10-19T10:07:12.072Z",
     "create_article_type_id": 11,
     "create_article_sender_id": 2,
     "article_count": 9,
     "escalation_at": null,
     "pending_time": null,
     "type": null,
     "preferences": {
         "escalation_calculation": {}
     },
     "updated_by_id": 3,
     "created_by_id": 6,
     "created_at": "2016-10-19T10:07:12.011Z",
     "updated_at": "2017-01-18T12:45:53.420Z",
     "anrede": "",
     "asdf": "",
     "time_unit": "62.0",
     "aaaaa": ""
 }






