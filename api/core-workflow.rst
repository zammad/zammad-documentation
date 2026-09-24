Core Workflow
=============

.. note::

   Core Workflows are different from Triggers: they control the ticket
   create/edit form while someone fills it out, for example by restricting
   which values are selectable in another field. The form sends its current
   values to Zammad, which evaluates the workflows and returns the resulting
   field changes. Unlike Triggers, they don't act on existing tickets in the
   background.

   See the :admin-docs:`Core Workflows admin documentation </system/core-workflows.html>`
   for the conceptual/UI-side picture of this feature, and
   :admin-docs:`Core Workflows limitations </system/core-workflows/limitations.html>`
   for how they can restrict attributes/values you see elsewhere in the API.
   Compare to :doc:`Report Profile </api/report-profile>`, whose ``condition``
   field, unlike Core Workflow, does validate that referenced fields are real.

List
----

Required permission: ``admin.core_workflow``

``GET``-Request sent: ``/api/v1/core_workflows``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 11,
         "name": "Ticket eligibility – Incident",
         "object": "Ticket",
         "condition_saved": {},
         "condition_selected": {
            "ticket.type": {
               "operator": "is",
               "value": ["Incident"]
            }
         },
         "perform": {
            "ticket.requester_category": {
               "operator": "set_fixed_to",
               "set_fixed_to": ["internal", "partner", "customer"]
            }
         },
         "active": true,
         "stop_after_match": false,
         "changeable": true,
         "priority": 100
      }
   ]

.. note::

   This endpoint only returns workflows with ``changeable: true``.
   Zammad's built-in system workflows are not changeable and are not
   included, so the response on a fresh instance is an empty array.
   Show, Update and Delete also only operate on changeable workflows.

Show
----

Required permission: ``admin.core_workflow``

``GET``-Request sent: ``/api/v1/core_workflows/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 11,
      "name": "Ticket eligibility – Incident",
      "object": "Ticket",
      "condition_saved": {},
      "condition_selected": {
         "ticket.type": {
            "operator": "is",
            "value": ["Incident"]
         }
      },
      "perform": {
         "ticket.requester_category": {
            "operator": "set_fixed_to",
            "set_fixed_to": ["internal", "partner", "customer"]
         }
      },
      "active": true,
      "stop_after_match": false,
      "changeable": true,
      "priority": 100
   }

Create
------

Required permission: ``admin.core_workflow``

``POST``-Request sent: ``/api/v1/core_workflows``

.. code-block:: json

   {
      "name": "Ticket eligibility – Incident",
      "object": "Ticket",
      "condition_saved": {},
      "condition_selected": {
         "ticket.type": {
            "operator": "is",
            "value": ["Incident"]
         }
      },
      "perform": {
         "ticket.requester_category": {
            "operator": "set_fixed_to",
            "set_fixed_to": ["internal", "partner", "customer"]
         }
      },
      "active": true,
      "stop_after_match": false,
      "changeable": true,
      "priority": 100
   }

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 11,
      "name": "Ticket eligibility – Incident",
      "object": "Ticket",
      "condition_saved": {},
      "condition_selected": {
         "ticket.type": {
            "operator": "is",
            "value": ["Incident"]
         }
      },
      "perform": {
         "ticket.requester_category": {
            "operator": "set_fixed_to",
            "set_fixed_to": ["internal", "partner", "customer"]
         }
      },
      "active": true,
      "stop_after_match": false,
      "changeable": true,
      "priority": 100
   }

.. note::

   Core Workflow does **not** validate that fields referenced in
   ``condition_selected`` or ``perform`` exist. A workflow that references
   a field that doesn't exist yet is saved without error. It has no
   visible effect in the ticket form until the referenced field exists.

Update
------

Required permission: ``admin.core_workflow``

``PUT``-Request sent: ``/api/v1/core_workflows/{id}``

Same payload shape as Create above. Response is the updated record, same
shape as Show/Create.

.. note::

   Sending the full Create payload to an existing workflow's ``id``
   updates that record in place. It doesn't create a duplicate.

Delete
------

Required permission: ``admin.core_workflow``

.. danger:: **This is a permanent removal**

   Please note that removing core workflows cannot be undone.

``DELETE``-Request sent: ``/api/v1/core_workflows/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
