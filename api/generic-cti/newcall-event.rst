New Call
========

.. list-table:: Available attributes and sample data for newCall events
   :widths: 20, 40, 40
   :header-rows: 1

   * - Attribute
     - Possible value
     - Description
   * - ``event``
     - ``newCall``
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
     - An ID that is unique for the call. Zammad will use this ID to identify
       an existing call with following actions
       (e.g. like answering or hanging up)

       *This ID must be unique per call session*.
   * - ``user``
     - e.g. ``[John Doe]``, ``[Alice, Bob]``
     - The user(s) real name involved.

       | If the direction is ``out``, this is the name of the calling person(s).
       | If the direction is ``in``, this is the name of the called person(s).

       This is always an array except if you're using JSON payloads.
       This value is optional.
   * - ``queue``
     - e.g. ``support``, ``sales``
     - An optional queue name, this option is relevant for the
       `Caller Log Filter <admin documentation>`_

.. _admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/generic-cti.html

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
               "event": "newCall",
               "from": "493023125741",
               "to": "492214710334",
               "direction": "out",
               "callId": "f4ebd2be-7b9a-4d58-94c2-eb06a3c2ce76",
               "user": "Christopher Miller"
            }

         Returns:

         .. code-block:: json

            {
               "action": "dial",
               "caller_id": "496990009111",
               "number": "492214710334"
            }

         Sample curl command:

         .. code-block:: sh

            $ curl --request POST 'https://mh-docs-dev.zammad.com/api/v1/cti/PhXp3ZG63QyJfcb1pVOnBKJWIbI' \
               --header 'Content-Type: application/json' \
               --data-raw '{
                  "event": "newCall",
                  "from": "493023125741",
                  "to": "492214710334",
                  "direction": "out",
                  "callId": "f4ebd2be-7b9a-4d58-94c2-eb06a3c2ce76",
                  "user": "Christopher Miller"
               }'

      Inbound
         Payload:

         .. code-block:: json

            {
               "event": "newCall",
               "from": "493023125741",
               "to": "492214710334",
               "direction": "in",
               "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
               "user": ["Christopher Miller", "Emma Taylor"]
            }

         Response:

         .. code-block:: json

            {}

         Sample curl command:

         .. code-block:: sh

            $ curl --request POST 'https://mh-docs-dev.zammad.com/api/v1/cti/PhXp3ZG63QyJfcb1pVOnBKJWIbI' \
               --header 'Content-Type: application/json' \
               --data-raw '{
                  "event": "newCall",
                  "from": "493023125741",
                  "to": "492214710334",
                  "direction": "in",
                  "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
                  "user": ["Christopher Miller", "Emma Taylor"]
               }'


   .. tab:: form-data

      ``POST``-Request sent:
      ``https://{FQDN-Zammad}/api/v1/cti/{instance specific token}``

      Outbound
         Payload:

         .. code-block::

            event:"newCall"
            from:"493023125741"
            to:"492214710334"
            direction:"out"
            callId:"f0871278-0600-4f5c-a746-bec3acf04f41"
            user:"Christopher Miller"

         Returns:

         .. code-block:: json

            {
               "action": "dial",
               "caller_id": "496990009111",
               "number": "492214710334"
            }

         Sample curl command:
         
         .. code-block:: sh

            $ curl --request POST 'https://{FQDN-Zammad}/api/v1/cti/{instance specific token}' \
               --form 'event="newCall"' \
               --form 'from="493023125741"' \
               --form 'to="492214710334"' \
               --form 'direction="out"' \
               --form 'callId="f0871278-0600-4f5c-a746-bec3acf04f41"' \
               --form 'user[]="Christopher Miller"'

      Inbound
         Payload:

         .. code-block::

            event:"newCall"
            from:"493023125741"
            to:"492214710334"
            direction:"in"
            callId:"25641e3f-3317-4c48-80b3-fc573c7ffe2b"
            user[]:"Christopher Miller"
            user[]:"Emma Taylor"

         Returns:

         .. code-block:: json

            {}

         Sample curl command:
         
         .. code-block:: sh

            $ curl --request POST 'https://{FQDN-Zammad}/api/v1/cti/{instance specific token}' \
               --form 'event="newCall"' \
               --form 'from="493023125741"' \
               --form 'to="492214710334"' \
               --form 'direction="in"' \
               --form 'callId="25641e3f-3317-4c48-80b3-fc573c7ffe2b"' \
               --form 'user[]="Christopher Miller"' \
               --form 'user[]="Emma Taylor"'

   .. tab:: URL variables

      .. include:: /api/generic-cti/generic-cti_no-more-url-varibales.include.rst

Depending on the chosen call direction, Zammad will return either a (optionally)
configured call ID or (optionally) block a caller. If your Zammad hasn't
configured one or both options, the return will be empty.

.. note::

   This has to be supported by your PBX in order to work.

.. tabs::

   .. tab:: Reject blocked caller IDs

      If an incoming new call matches a to block number, Zammad will return
      the following.

         .. code-block:: json

            {
              "action": "reject",
              "reason": "busy"
            }

      If no to block number matches, Zammad will return the following.

         .. code-block:: json

            {}

      .. warning::

         Your PBX still needs to end the call (hangup event).
         Other wise the call will not just appear within Zammads caller log
         but also appear as ringing call.

   .. tab:: Set specific outgoing caller ID

      In case your instance has a matching overwriting caller ID configured,
      Zammad will return the following payload.

         .. code-block:: json

            {
              "action": "dial",
              "callerId": "493055571642",
              "number": "491711234567890"
            }

      If no overwrite match is found or you haven't configured anything,
      Zammad will return the following.

         .. code-block:: json

            {}
