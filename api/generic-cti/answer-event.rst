Call answered
=============

.. include:: /api/generic-cti/cti-endpoint-limitations.include.rst

.. list-table:: Available attributes and sample data for answered events
   :widths: 20, 40, 40
   :header-rows: 1

   * - Attribute
     - Possible value
     - Description
   * - ``event``
     - ``answer``
     - Tell Zammad there's a new call
   * - ``from``
     - e.g. ``493055571600``, ``02214710334``, ``anonymous``
     - Number that initiated the call
   * - ``to``
     - e.g. ``49221470334``, ``03023125771``
     - Number that is being called
   * - ``direction``
     - ``in`` or ``out``
     - The call direction - if your agent initiates a call this will be ``out``
   * - ``callId``
     - e.g. ``53ba82e2bd6d12d9fb2d3838f0cfb070``, ``5fb9532f40da834a``,
       ``123456789``
     - This is the CallID from the ``newCall`` event.
   * - ``answeringNumber``
     - e.g. ``42``, ``jdoe``, ``jdoe@example.com``, ``3``
     - Zammad will look up for a user with given value, the following
       attributes will be evaluated in given order:

          * ``user.phone``
          * ``user.login``
          * ``user.id``

       This value is optional.
   * - ``user``
     - e.g. ``[John Doe]``, ``[Alice, Bob]``
     - The user(s) real name involved.

       | If the direction is ``out``, this is the name of the calling person(s).
       | If the direction is ``in``, this is the name of the called person(s).

       This value is optional.

There's two options on how to ``POST`` the relevant data to Zammad.

.. include:: /api/generic-cti/generic-cti_context-note-configuration.include.rst

.. tabs::

   .. tab:: JSON (recommended)

      ``POST``-Request sent:
      ``https://{FQDN-Zammad}/api/v1/cti/{instance specific token}``

      Outbound
         Payload:

            .. code-block:: json

               {
                  "event": "answer",
                  "from": "493023125741",
                  "to": "492214710334",
                  "direction": "out",
                  "callId": "9f1840cb-8be9-4d3a-8200-3da2937085f0",
                  "caller": "Christopher Miller"
               }


         Response:

            .. code-block:: json

               {}

         Sample curl command:

            .. code-block:: sh

               $ curl --request POST 'https://mh-docs-dev.zammad.com/api/v1/cti/PhXp3ZG63QyJfcb1pVOnBKJWIbI' \
                  --header 'Content-Type: application/json' \
                  --data-raw '{
                     "event": "answer",
                     "from": "493023125741",
                     "to": "492214710334",
                     "direction": "out",
                     "callId": "9f1840cb-8be9-4d3a-8200-3da2937085f0",
                     "caller": "Christopher Miller"
                  }'

      Inbound
         Payload:

            .. code-block:: json

               {
                  "event": "answer",
                  "from": "493023125741",
                  "to": "492214710334",
                  "direction": "in",
                  "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
                  "answeringNumber": "emma@chrispresso.com",
                  "caller": ["Christopher Miller", "Emma Taylor"]
               }

         Response:

            .. code-block:: json

               {}

         Sample curl command:

            .. code-block:: sh

               $ curl --request POST 'https://mh-docs-dev.zammad.com/api/v1/cti/PhXp3ZG63QyJfcb1pVOnBKJWIbI' \
                  --header 'Content-Type: application/json' \
                  --data-raw '{
                     "event": "answer",
                     "from": "493023125741",
                     "to": "492214710334",
                     "direction": "in",
                     "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
                     "answeringNumber": "emma@chrispresso.com",
                     "caller": ["Christopher Miller", "Emma Taylor"]
                  }'

   .. tab:: form-data

      ``POST``-Request sent:
      ``https://{FQDN-Zammad}/api/v1/cti/{instance specific token}``

      Outbound
         Payload:

            .. code-block::

               event:"answer"
               from:"493023125741"
               to:"492214710334"
               direction:"out"
               callId:"371e2cd7-67ff-4fd9-892b-030c8d128fb1"
               caller[]:"Christopher Miller"
               caller[]:"Emma Taylor"

         Returns:

            .. code-block:: json

               {}

         Sample curl command:
         
            .. code-block:: sh

               $ curl --request POST 'https://{FQDN-Zammad}/api/v1/cti/{instance specific token}' \
                  --form 'event="answer"' \
                  --form 'from="493023125741"' \
                  --form 'to="492214710334"' \
                  --form 'direction="out"' \
                  --form 'callId="371e2cd7-67ff-4fd9-892b-030c8d128fb1"' \
                  --form 'caller[]="Christopher Miller"' \
                  --form 'caller[]="Emma Taylor"'

      Inbound
         Payload:

            .. code-block::

               event:"answer"
               from:"493023125741"
               to:"492214710334"
               direction:"in"
               callId:"61868f1e-2171-4313-970b-25982f0c5ce1"
               answeringNumber:"emma@chrispresso.com"
               caller="Emma Taylor"

         Returns:

            .. code-block:: json

               {}

         Sample curl command:
         
            .. code-block:: sh

               $ curl --request POST 'https://{FQDN-Zammad}/api/v1/cti/{instance specific token}' \
                  --form 'event="answer"' \
                  --form 'from="493023125741"' \
                  --form 'to="492214710334"' \
                  --form 'direction="in"' \
                  --form 'callId="61868f1e-2171-4313-970b-25982f0c5ce1"' \
                  --form 'answeringNumber="emma@chrispresso.com"' \
                  --form 'caller="Emma Taylor"'

   .. tab:: URL variables

      .. include:: /api/generic-cti/generic-cti_no-more-url-varibales.include.rst

The next logical step within call session context would be:
   * :doc:`hangup <hangup-event>` (call ending)
