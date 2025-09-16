Ticket Summary
==============

Show/Trigger
------------

Required permission: ``ticket.agent``

``POST``-Request sent: ``/api/v1/tickets/{ticket id}/summarize``

The ticket summarize endpoint uses ``POST`` because creating and fetching the
summary happen in a single operation:

- If a summary exists, it is returned.
- If a summary does not exist, creation is triggered in the background
  (async job).

Using ``GET`` would be incorrect since the call may also create data. If you
want a summary to exist, call the endpoint; if it's not ready yet, retry after
at least 30 seconds.

Sample response if the generation of a new summary was just triggered by the
request:

.. code-block:: json
   :force:

   // HTTP Code 200 Ok

   {
      " result": null
   }

Sample response for an existing summary (e.g. for the same ticket like above
after waiting until creation has finished):

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
