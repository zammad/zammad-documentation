CTI API
****

In many use cases, agents work in connection customer conversations over the phone. 

It is a great relief when the telephone system (PBX) is integrated with Zammad, which makes processes with agents more effective.

The goal of the document is to provide the necessary API documentation to enable PBX vendors to easily integrate with Zammad.

Feature list
============

**Inbound**

* Caller identification based on the CallerID (open a customer profile with just one click)
* Display of open and closed tickets of a customer in a special overview. This overview should also give the possibility to create a ticket for the given customer.
* Intelligent mapping of CallerIDs with direct (e.g. directly at the contact) and not direct (e.g. telephone numbers from the signature)
* Caller Journal (which calls have been made and which have been handled and which require a callback)
* Blocking of CallerIDs (already during the call) *
* Support to allow an agent to set a DND - like state *
* Overview of agents who currently handle a call 


**Outbound**

* Direct dialling of the customer telephone number and indexing of the call *
* Set the outbound caller ID based on the line phone number (e. g. set sender caller id based on country of destination caller id) *


 _* if supported by the PBX/telephone system_

CTI Push API
============

**How it works**

Events can be transferred in realtime from the telephone system to the Zammad CTI Push API (REST API) via a generic interface.

Depending on the event, Zammad offers various functions to quickly and easily identify callers and the corresponding tickets, for example, or to provide a caller log. Or to modify the incoming or outgoing call.

**Endpoint**

The endpoint of your Zammad CTI Push API looks like http://localhost:3000/api/v1/integration/cti/:token and can be found in Zammad -> Admin -> Integrations -> CTI (generic) -> Endpoint


**Events**

Zammad supports the following three events (newCall, hangup and answer) in version 2.x.

*Event: newCall*

+-------------+---------------------------------------------------------+
| Attribute   | Description                                             |
+=============+=========================================================+
| event       | "newCall"                                               |
+-------------+---------------------------------------------------------+
| from        | The calling number (e.g. "493055571600" or "anonymous") |
+-------------+---------------------------------------------------------+
| to          | The called number (e.g. "491711234567890")              |
+-------------+---------------------------------------------------------+
| direction   | The direction of the call (either "in" or "out")        |
+-------------+---------------------------------------------------------+
| callId      | A unique alphanumeric identifier to match events to specific calls (max. 250 characters) |
+-------------+---------------------------------------------------------+
| user[]      | The user(s) realname involved. It is the name of the calling user when direction is "out", or of the users receiving the call when direction is "in". Group calls may be received by multiple users. In that case a "user[]" parameter is set for each of these users. It is always "user[]" (not "user"), even if only one user is involved. |
+-------------+---------------------------------------------------------+

You can simulate this POST request and test your server with a CURL command:

::

  curl -X POST --data "event=newCall&from=493055571600&to=491711234567890&direction=in&callId=123456&user[]=Alice&user[]=Bob" http://localhost:3000/api/v1/integration/cti/:token


#### The response (optional)

After sending the POST request to Zammad, your PBX can accept an JSON response to determine what to do (e. g. for `direction=in` to block the caller or for `direction=out` to set a caller id).

Zammad currently supports the following responses for incoming calls:

+--------+--------------------------------------------------------------------------+
| Action | Description                                                              |
+========+==========================================================================+
| reject | Reject call or pretend to be busy (depending on your settings in Zammad) |
+-------------+---------------------------------------------------------------------+

Example 1: Reject call signaling busy

::

  {
    "action": "reject",
    "reason": "busy"
  }

Zammad currently supports the following responses for outgoing calls:

Action | Description
-- | --
dial | To set the caller id (depending on your settings in Zammad). Number need to be in E.164 format.


Example 1: Set custom caller id for outgoing call

::

  {
    "action": "dial",
    "callerId": "493055571642",
    "number": "491711234567890"
  }

*Event: hangup*

Attribute | Description
-- | --
event | "hangup"
callId | Same as in newCall-event for a specific call
cause | The cause for the hangup event (see below) 
from | The calling number (e.g. "493055571600" or "anonymous")
to | The called number (e.g. "491711234567890")
direction | The direction of the call (either "in" or "out")
answeringNumber | The number which was answering 


You can simulate this POST request and test your server with a CURL command:

::

  curl -X POST --data "event=hangup&cause=normalClearing&callId=123456&from=493055571600&to=491711234567890&direction=in&answeringNumber=4921199999999" http://localhost:3000/api/v1/integration/cti/:token


Hangup causes: For these reasons, hangups may occur because of these causes:

Attribute | Description
-- | --
normalClearing | One of the parties hung up after the call was established.
busy | The called party was busy
cancel | The caller hung up before the called party picked up
noAnswer | The called party rejected the call (e.g. through a DND setting)
congestion | The called party could not be reached
notFound | The called number does not exist or called party is offline
forwarded | The call was forwarded to a different party

*Event: answer*

Attribute | Description
-- | --
event | "answer"
callId | Same as in newCall-event for a specific call
user | Name of the user who answered this call. Only incoming calls can have this parameter
from | The calling number (e.g. "492111234567" or "anonymous")
to | The called number (e.g. "491711234567890")
direction | The direction of the call (either "in" or "out")
answeringNumber | The number of the answering destination. Useful when redirecting to multiple destinations


You can simulate this POST request and test your server with a CURL command:

::

  curl -X POST --data "event=answer&callId=123456&user=John+Doe&from=493055571600&to=491711234567890&direction=in&answeringNumber=21199999999" http://localhost:3000/api/v1/integration/cti/:token



