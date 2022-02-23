Generic CTI
***********

This page describes the generic CTI API scopes and functionalities.
Unlike the rest of Zammads API *this endpoint behaves differently from the
others* - for this endpoint forget everything you've learned in the API intro.

.. hint::

   Generic CTI configuration and the correct endpoint can be found in your
   Zammad integration settings and are documented in our `admin documentation`_.

   | Please also note the there listed requirements and limitations.
   | All options that require returns (e.g. blocking, manipulating outgoing
     caller IDs) rely on configurations within the Zammad CTI integration page.

.. _admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/generic-cti.html

Endpoint
========

The endpoint can be found in the generic CTI integration and contains a unique
token which acts as authentication. Make sure to keep this endpoint URL safe.

Events
======

There are several events in terms of a ongoing call.
These actions always come from your PBX system and may be:

   * :ref:`a new call <cti-newcall>` (initiation of a call)
   * :ref:`hangup <cti-hangup>` (call ending)
   * :ref:`answer <cti-answer>` (aka picking up the phone)

In some situations Zammad may provide a return on your PBX calls (e.g. a reject)
if you blocked a specific caller. Zammad will never initiate specific actions
with your PBX. Zammad is a passive component in all described cases.

.. _cti-newcall:

New Call
--------

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

There's two options on how to ``POST`` the relevant data to Zammad.

.. tabs::

   .. tab:: JSON (recommended)

      .. include:: /api/includes/generic-cti_context-note-configuration.rst

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

   .. tab:: form-data

      .. include:: /api/includes/generic-cti_context-note-configuration.rst

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

      .. include:: /api/includes/generic-cti_no-more-url-varibales.rst

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

.. _cti-hangup:

Call Hangup
-----------

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

.. tabs::

   .. tab:: JSON (recommended)

      .. include:: /api/includes/generic-cti_context-note-configuration.rst

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

   .. tab:: form-data

      .. include:: /api/includes/generic-cti_context-note-configuration.rst

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

      .. include:: /api/includes/generic-cti_no-more-url-varibales.rst

.. _cti-answer:

Call answered
-------------

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

There's two options on how to ``POST`` the relevant data to Zammad.

.. tabs::

   .. tab:: JSON (recommended)

      .. include:: /api/includes/generic-cti_context-note-configuration.rst

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
               "callId": "9f1840cb-8be9-4d3a-8200-3da2937085f0"
            }


         Response:

         .. code-block:: json

            {}

      Inbound
         Payload:

         .. code-block:: json

            {
               "event": "answer",
               "from": "493023125741",
               "to": "492214710334",
               "direction": "in",
               "callId": "307fa962-de8d-4ffc-817b-7f6993204159",
               "user": "Emma Taylor",
               "answeringNumber": "emma@chrispresso.com"
            }

         Response:

         .. code-block:: json

            {}

   .. tab:: form-data

      .. include:: /api/includes/generic-cti_context-note-configuration.rst

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
               --form 'callId="371e2cd7-67ff-4fd9-892b-030c8d128fb1"'

      Inbound
         Payload:

         .. code-block::

            event:"answer"
            from:"493023125741"
            to:"492214710334"
            direction:"in"
            callId:"61868f1e-2171-4313-970b-25982f0c5ce1"
            user:"Emma Taylor"
            answeringNumber:"emma@chrispresso.com",

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
               --form 'user[]="Christopher Miller"' \
               --form 'user[]="Emma Taylor"' \
               --form 'answeringNumber="emma@chrispresso.com"'

   .. tab:: URL variables

      .. include:: /api/includes/generic-cti_no-more-url-varibales.rst
