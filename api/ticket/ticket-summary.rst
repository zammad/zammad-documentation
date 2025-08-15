Ticket Summary
==============

Show/Trigger
------------

Required permission: ``ticket.agent``

``POST``-Request sent: ``/api/v1/tickets/{ticket id}/enqueue_summarize``

The following ``POST`` request fetches an existing summary, if there is one
available in the ticket. If there is no summary available or the ticket was
changed after the existing summary was created, a new summary is triggered.
In such a case, you won't get a response with the summary. To get a summary, you
have to re-send the request with a small delay considering the AI job may take
a few seconds.

Sample response if the generation of a new summary was just triggered by the
request:

.. code-block:: json
   :force:

   // HTTP Code 200 Ok

   {
      " result": null
   }

Sample response for an existing summary (e.g. for the same ticket like above
after waiting a few seconds):

.. code-block:: json
   :force:

   // HTTP Code 200 Ok

   {
      "result": {
         "language": "en-US",
         "customer_mood": "frustrated",
         "open_questions": [],
         "upcoming_events": [
            "2023-03-15T14:00:00Z"
         ],
         "customer_emotion": "😐",
         "customer_request": "complaint wrong delivery of order #51519891",
         "conversation_summary": "Customer David Bell complains about the wrong delivery of his order. Agent Emma Taylor responds with a generic apology, but then Christopher Miller takes over and provides more detailed information about the correct items being prepared for shipment.",
         "fingerprint_md5": "7a7a3daecf4c93a1460cc9ea6e9168cb",
         "relevant_for_current_user": false
      }
   }
