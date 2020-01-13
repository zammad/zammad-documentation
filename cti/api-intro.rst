Introduction
************

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


 * if supported by the PBX/telephone system


