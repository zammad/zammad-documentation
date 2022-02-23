Call Hangup
===========

.. list-table:: Available attributes and sample data for hangup events
   :widths: 20, 40, 40
   :header-rows: 1

   * - Attribute
     - Possible value
     - Description
   * - ``event``
     - ``hangup``
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
   * - ``cause``
     - .. list-table::
          :widths: 10, 30
          :header-rows: 1
          
          * - Cause type
            - Description
          * - ``normalClearing``
            - One of the parties hung up after the call was established.
          * - ``busy``
            - The called party was busy
          * - ``cancel``
            - The caller hung up before the called party picked up
          * - ``noAnswer``
            - The called party rejected the call (e.g. through a DND setting)
          * - ``congestion``
            - The called party could not be reached
          * - ``notFound``
            - The called number does not exist or called party is offline
          * - ``forwarded``
            - The call was forwarded to a different party
     - This defines the reason of the hangup. Zammad evaluates the cause
       and indicates e.g. missed calls accordingly in the caller log.
   * - ``answeringNumber``
     - e.g. ``42``, ``jdoe``, ``jdoe@example.com``, ``3``
     - Zammad will look up for a user with given value, the following
       attributes will be evaluated in given order:

          * ``user.phone``
          * ``user.login``
          * ``user.id``

       This value is optional.

There's two options on how to ``POST`` the relevant data to Zammad.

.. include:: /api/generic-cti/generic-cti_context-note-configuration.include.rst

.. tabs::

   .. tab:: JSON (recommended)

      ``POST``-Request send:
      ``https://{FQDN-Zammad}/api/v1/cti/{instance specific token}``

      Outbound
         Payload:

         .. code-block:: json

            {
               "event": "hangup",
               "from": "493023125741",
               "to": "492214710334",
               "direction": "out",
               "callId": "f4ebd2be-7b9a-4d58-94c2-eb06a3c2ce76",
               "user": "Christopher Miller",
               "cause": "cancel"
            }

         Response:

         .. code-block:: json

            {}

         Sample curl command:

         .. code-block:: sh

            $ curl --request POST 'https://mh-docs-dev.zammad.com/api/v1/cti/PhXp3ZG63QyJfcb1pVOnBKJWIbI' \
               --header 'Content-Type: application/json' \
               --data-raw '{
                  "event": "hangup",
                  "from": "493023125741",
                  "to": "492214710334",
                  "direction": "out",
                  "callId": "f4ebd2be-7b9a-4d58-94c2-eb06a3c2ce76",
                  "user": "Christopher Miller",
                  "cause": "cancel"
               }'

      Inbound
         Payload:

         .. code-block:: json

            {
               "event": "hangup",
               "from": "493023125741",
               "to": "492214710334",
               "direction": "in",
               "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
               "user": "Emma Taylor",
               "answeringNumber": "emma@chrispresso.com",
               "cause": "normalClearing"
            }

         Response:

         .. code-block:: json

            {}

         Sample curl command:

         .. code-block:: sh

            $ curl --request POST 'https://mh-docs-dev.zammad.com/api/v1/cti/PhXp3ZG63QyJfcb1pVOnBKJWIbI' \
               --header 'Content-Type: application/json' \
               --data-raw '{
                  "event": "hangup",
                  "from": "493023125741",
                  "to": "492214710334",
                  "direction": "in",
                  "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
                  "user": "Emma Taylor",
                  "answeringNumber": "emma@chrispresso.com",
                  "cause": "normalClearing"
               }'

   .. tab:: form-data

      ``POST``-Request sent:
      ``https://{FQDN-Zammad}/api/v1/cti/{instance specific token}``

      Outbound
         Payload:

         .. code-block::

            event:"hangup"
            from:"493023125741"
            to:"492214710334"
            direction:"out"
            callId:"da7cf8b8-2de2-4120-93c8-7db1f55225dc"
            user:"Christopher Miller"
            cause:"cancel"

         Returns:

         .. code-block:: json

            {}

         Sample curl command:
         
         .. code-block:: sh

            $ curl --request POST 'https://{FQDN-Zammad}/api/v1/cti/{instance specific token}' \
               --form 'event="hangup"' \
               --form 'from="493023125741"' \
               --form 'to="492214710334"' \
               --form 'direction="out"' \
               --form 'callId="da7cf8b8-2de2-4120-93c8-7db1f55225dc"' \
               --form 'user[]="Christopher Miller"' \
               --form 'cause="cancel"'

      Inbound
         Payload:

         .. code-block::

            event:"hangup"
            from:"493023125741"
            to:"492214710334"
            direction:"in"
            callId:"2d77882f-68df-40f0-8c62-b642589c00bc"
            user:"Emma Taylor"
            answeringNumber:"emma@chrispresso.com",
            cause:"normalClearing"

         Returns:

         .. code-block:: json

            {}

         Sample curl command:
         
         .. code-block:: sh

            $ curl --request POST 'https://{FQDN-Zammad}/api/v1/cti/{instance specific token}' \
               --form 'event="hangup"' \
               --form 'from="493023125741"' \
               --form 'to="492214710334"' \
               --form 'direction="in"' \
               --form 'callId="2d77882f-68df-40f0-8c62-b642589c00bc"' \
               --form 'user[]="Christopher Miller"' \
               --form 'user[]="Emma Taylor"' \
               --form 'answeringNumber="emma@chrispresso.com"' \
               --form 'cause="normalClearing"'

   .. tab:: URL variables

      .. include:: /api/generic-cti/generic-cti_no-more-url-varibales.include.rst
