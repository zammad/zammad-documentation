Generic CTI
***********

This page describes the generic CTI API scopes and functionalities.
Unlike the rest of Zammads API *this endpoint behaves differently from the
others* - for this endpoint forget everything you've learned in the API intro.

.. hint::

   Generic CTI configuration and the correct endpoint can be found in your
   Zammad integration settings and are documented in our `admin documentation`_.

   Please also note the there listed requirements and limitations.

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

   * a new call (initiation of a call)
   * hangup (call ending)
   * answer (aka picking up the phone)

In some situations Zammad may provide a return on your PBX calls (e.g. a reject)
if you blocked a specific caller. Zammad will never initiate specific actions
with your PBX. Zammad is a passive component in all following cases.

**Event: newCall**

+-------------+------------------------------------------------------------------------------------------+
| Attribute   | Description                                                                              |
+=============+==========================================================================================+
| event       | "newCall"                                                                                |
+-------------+------------------------------------------------------------------------------------------+
| from        | The calling number (e.g. "493055571600" or "anonymous")                                  |
+-------------+------------------------------------------------------------------------------------------+
| to          | The called number (e.g. "491711234567890")                                               |
+-------------+------------------------------------------------------------------------------------------+
| direction   | The direction of the call (either "in" or "out")                                         |
+-------------+------------------------------------------------------------------------------------------+
| callId      | A unique alphanumeric identifier to match events to specific calls (max. 250 characters) |
+-------------+------------------------------------------------------------------------------------------+
| user[]      | The user(s) realname involved. It is the name of the calling user when direction is      |
|             | "out", or of the users receiving the call when direction is "in". Group calls may be     |
|             | received by multiple users. In that case a "user[]" parameter is set for each of these   |
|             | users. It is always "user[]" (not "user"), even if only one user is involved.            |
+-------------+------------------------------------------------------------------------------------------+
| queue       | The queue name (e. g. helpdesk). This field is optional.                                 |
+-------------+------------------------------------------------------------------------------------------+

You can simulate this POST request and test your server with a CURL command:

.. code-block:: sh

   $ curl -X POST --data "event=newCall&from=493055571600&to=491711234567890&direction=in&callId=123456&user[]=Alice&user[]=Bob" http://localhost:3000/api/v1/cti/:token

*The response (optional)*

After sending the POST request to Zammad, your PBX can accept an JSON response to determine what to do (e. g. for `direction=in` to block the caller or for `direction=out` to set a caller id).

Zammad currently supports the following responses for incoming calls:

+--------+--------------------------------------------------------------------------+
| Action | Description                                                              |
+========+==========================================================================+
| reject | Reject call or pretend to be busy (depending on your settings in Zammad) |
+--------+--------------------------------------------------------------------------+

Example 1: Reject call signaling busy

.. code-block:: json

   {
     "action": "reject",
     "reason": "busy"
   }

Zammad currently supports the following responses for outgoing calls:

+--------+-------------------------------------------------------------------------------------------------+
| Action | Description                                                                                     |
+========+=================================================================================================+
| dial   | To set the caller id (depending on your settings in Zammad). Number need to be in E.164 format. |
+--------+-------------------------------------------------------------------------------------------------+

Example 1: Set custom caller id for outgoing call

.. code-block:: json

   {
     "action": "dial",
     "callerId": "493055571642",
     "number": "491711234567890"
   }

**Event: hangup**

+-----------------+---------------------------------------------------------+
| Attribute       | Description                                             |
+=================+=========================================================+
| event           | "hangup"                                                |
+-----------------+---------------------------------------------------------+
| callId          | Same as in newCall-event for a specific call            |
+-----------------+---------------------------------------------------------+
| cause           | The cause for the hangup event (see                     |
+-----------------+---------------------------------------------------------+
| from            | The calling number (e.g. "493055571600" or "anonymous") |
+-----------------+---------------------------------------------------------+
| to              | The called number (e.g. "491711234567890")              |
+-----------------+---------------------------------------------------------+
| direction       | The direction of the call (either "in" or "out")        |
+-----------------+---------------------------------------------------------+
| answeringNumber | The number which was answering                          |
+-----------------+---------------------------------------------------------+

You can simulate this POST request and test your server with a CURL command:

.. code-block:: sh

   $ curl -X POST --data "event=hangup&cause=normalClearing&callId=123456&from=493055571600&to=491711234567890&direction=in&answeringNumber=4921199999999" http://localhost:3000/api/v1/cti/:token


Hangup causes: For these reasons, hangups may occur because of these causes:

+-----------------+-----------------------------------------------------------------+
| Attribute       | Description                                                     |
+=================+=================================================================+
| normalClearing  | One of the parties hung up after the call was established.      |
+-----------------+-----------------------------------------------------------------+
| busy            | The called party was busy                                       |
+-----------------+-----------------------------------------------------------------+
| cancel          | The caller hung up before the called party picked up            |
+-----------------+-----------------------------------------------------------------+
| noAnswer        | The called party rejected the call (e.g. through a DND setting) |
+-----------------+-----------------------------------------------------------------+
| congestion      | The called party could not be reached                           |
+-----------------+-----------------------------------------------------------------+
| notFound        | The called number does not exist or called party is offline     |
+-----------------+-----------------------------------------------------------------+
| forwarded       | The call was forwarded to a different party                     |
+-----------------+-----------------------------------------------------------------+


**Event: answer**

+------------------+-------------------------------------------------------------------------------------------+
| Attribute        | Description                                                                               |
+==================+===========================================================================================+
| event            | "answer"                                                                                  |
+------------------+-------------------------------------------------------------------------------------------+
| callId           | Same as in newCall-event for a specific call                                              |
+------------------+-------------------------------------------------------------------------------------------+
| user             | Name of the user who answered this call. Only incoming calls can have this parameter      |
+------------------+-------------------------------------------------------------------------------------------+
| from             | The calling number (e.g. "492111234567" or "anonymous")                                   |
+------------------+-------------------------------------------------------------------------------------------+
| to               | The called number (e.g. "491711234567890")                                                |
+------------------+-------------------------------------------------------------------------------------------+
| direction        | The direction of the call (either "in" or "out")                                          |
+------------------+-------------------------------------------------------------------------------------------+
| answeringNumber  | The number of the answering destination. Useful when redirecting to multiple destinations |
+------------------+-------------------------------------------------------------------------------------------+


You can simulate this POST request and test your server with a CURL command:

.. code-block:: sh

   $ curl -X POST --data "event=answer&callId=123456&user=John+Doe&from=493055571600&to=491711234567890&direction=in&answeringNumber=21199999999" http://localhost:3000/api/v1/cti/:token
