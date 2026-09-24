Report Profile
==============

.. note::

   A Report Profile is a saved, reusable filter/condition for
   Zammad's Reporting module, it isn't an automation and doesn't do
   anything by itself. It's a named condition that shows up as a
   selectable view when generating reports in Admin → Reports, scoped
   to whichever roles (``role_ids``) can see it. Compare to
   :doc:`Core Workflow </api/core-workflow>`, which uses a
   similarly-shaped condition object but does not validate referenced
   fields.

List
----

Required permission: ``admin.report_profile``

``GET``-Request sent: ``/api/v1/report_profiles``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   [
      {
         "id": 1,
         "name": "-all-"
      },
      {
         "id": 4,
         "name": "Customer onboarding response (≤1h)"
      },
      {
         "id": 5,
         "name": "Partner onboarding consulting (≤4h)"
      },
      {
         "id": 6,
         "name": "HR requests within committed window (≥95%)"
      },
      {
         "id": 7,
         "name": "IT requests within committed window (≥90%)"
      },
      {
         "id": 8,
         "name": "Product requests delivered as planned (95%)"
      }
   ]

.. note::

   Only ``id`` and ``name`` are shown here. See Show below for the full
   field set of a single profile (``condition``, ``active``,
   ``role_ids``, etc.). Entry ``1`` (``-all-``) is Zammad's built-in
   default profile.

Show
----

Required permission: ``admin.report_profile``

``GET``-Request sent: ``/api/v1/report_profiles/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {
      "id": 4,
      "name": "Example profile",
      "condition": {
         "ticket.state_id": {"operator": "is", "value": ["1", "2"]}
      },
      "active": true,
      "role_ids": [1, 2],
      "created_by_id": 3,
      "updated_by_id": 3
   }

Create
------

Required permission: ``admin.report_profile``

``POST``-Request sent: ``/api/v1/report_profiles``

.. code-block:: json

   {
      "name": "Customer onboarding response (≤1h)",
      "condition": {
         "ticket.type": {"operator": "is", "value": ["Onboarding support"]},
         "ticket.requester_category": {"operator": "is", "value": ["customer"]}
      },
      "active": true,
      "role_ids": [1, 2]
   }

.. note::

   Role ids aren't guaranteed to be the same across instances. Look up
   the ids of the roles you need via :doc:`/api/v1/roles </api/role>`
   first instead of hard-coding them.

Response:

.. code-block:: json
   :force:

   # HTTP-Code 201 Created

   {
      "id": 4,
      "name": "Customer onboarding response (≤1h)",
      "condition": {
         "ticket.type": {"operator": "is", "value": ["Onboarding support"]},
         "ticket.requester_category": {"operator": "is", "value": ["customer"]}
      },
      "active": true,
      "role_ids": [1, 2],
      "created_by_id": 3,
      "updated_by_id": 3
   }

.. note::

   Unlike Core Workflow, Report Profile's ``condition`` **does**
   validate that referenced fields are real, fully-migrated ticket
   fields. Referencing a custom field that exists but hasn't finished
   its schema migration yet (``to_create``/``to_migrate`` still ``true``
   on that field) fails with:

   .. code-block:: json
      :force:

      # HTTP-Code 422 Unprocessable Entity

      {
         "error": "Invalid object selector conditions",
         "error_human": "Invalid object selector conditions",
         "invalid_attribute": {
            "condition": "Invalid object selector conditions"
         }
      }

Update
------

Required permission: ``admin.report_profile``

``PUT``-Request sent: ``/api/v1/report_profiles/{id}``

Same payload shape as Create above. Response is the updated record, same
shape as Create's response.

.. note::

   Sending the full Create payload to an existing profile's ``id``
   updates that record in place. It doesn't create a duplicate.

Delete
------

Required permission: ``admin.report_profile``

.. danger:: **This is a permanent removal**

   Please note that removing report profiles cannot be undone.

``DELETE``-Request sent: ``/api/v1/report_profiles/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}
