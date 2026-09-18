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

   Only ``id`` and ``name`` are shown here, see Create below for the
   full field set a single profile returns (``condition``, ``active``,
   ``role_ids``, etc.). Entry ``1`` (``-all-``) is Zammad's own built-in
   stock profile; the rest were created by this project.

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

   Resolve ``role_ids`` by name via a ``GET`` to
   :doc:`/api/v1/roles </api/role>` first, rather than assuming ids,
   they aren't guaranteed stable across instances. In this example,
   ``[1, 2]`` was resolved to the Admin and Agent roles on the tested
   instance.

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

   🤓 Unlike Core Workflow, Report Profile's ``condition`` **does**
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

   Verified by re-sending the same Create-shaped payload to an
   already-existing profile's ``id`` multiple times, each re-send
   updated the existing record in place (the profile's ``id`` and the
   overall list count stayed stable across reruns) rather than creating
   a duplicate.

Delete
------

Required permission: ``admin.report_profile``

.. danger:: **⚠ This is a permanent removal**

   Please note that removing report profiles cannot be undone.

``DELETE``-Request sent: ``/api/v1/report_profiles/{id}``

Response:

.. code-block:: json
   :force:

   # HTTP-Code 200 Ok

   {}

.. note::

   The exact response body wasn't specifically captured for this
   resource, the deleted profile simply stopped appearing in a
   subsequent ``GET /api/v1/report_profiles`` list. The empty ``{}``
   body shown above follows Zammad's consistent convention for this
   action, as seen on other resources that support delete (Object
   Manager Attribute, and this site's own :doc:`User </api/user>`
   delete example).
