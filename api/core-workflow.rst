Core Workflow
=============

.. note::

   Core Workflows are different from Triggers: they run **client-side**,
   inside the ticket create/edit form UI, live-evaluating their conditions
   as an agent or customer fills out the form and applying their
   ``perform`` actions immediately, for example restricting which values
   are selectable in another field. They never touch existing tickets and
   never run server-side or in the background; they only affect what's
   selectable in the form UI at the moment someone is filling it out.

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

   A fresh Zammad instance ships with **zero** Core Workflows, this
   endpoint only returns what's actually been configured. For reference,
   here's a full example list (6 workflows, all created by this project):

   .. code-block:: text

      id  name                                     priority  active
      11  Ticket eligibility – Incident             100       true
      12  Ticket eligibility – Customer support     110       true
      13  Ticket eligibility – Internal requests     120       true
      14  Ticket eligibility – Product request        130       true
      15  Assignment eligibility – L1 Front Desk       140       true
      16  Assignment eligibility – L2/L3                150       true

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

   🤓 Core Workflow does **not** validate that fields referenced in
   ``condition_selected``/``perform`` actually exist as real ticket
   fields. A workflow referencing a field that doesn't exist yet is
   accepted and saved without error, it just has no visible effect in the
   ticket form until the referenced field actually exists.

   This was confirmed directly: ``Assignment eligibility – L1 Front Desk``
   was created successfully despite ``ticket.support_tier`` not existing on
   the instance at creation time:

   .. code-block:: json

      {
         "name": "Assignment eligibility – L1 Front Desk",
         "object": "Ticket",
         "condition_saved": {},
         "condition_selected": {
            "ticket.support_tier": {
               "operator": "is",
               "value": ["l1"]
            }
         },
         "perform": {
            "ticket.assignee_organisation": {
               "operator": "set_fixed_to",
               "set_fixed_to": ["pharos_front_desk"]
            }
         },
         "active": true,
         "stop_after_match": false,
         "changeable": true,
         "priority": 140
      }

Update
------

Required permission: ``admin.core_workflow``

``PUT``-Request sent: ``/api/v1/core_workflows/{id}``

Same payload shape as Create above. Response is the updated record, same
shape as Show/Create.

.. note::

   Re-sending the same payload to an already-existing workflow's
   ``id`` updates that record in place rather than creating a duplicate.
