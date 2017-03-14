Trigger
*******

Triggers will be executed (ordered by name) on every ticket create or update to execute changes on tickets or to send notifications.


Use cases
=========

Example of use cases where triggers are useful.

* Send auto reply for new tickets to customer to let them know that a ticket has been created.
* Set ticket owner on first reply if no owner is set.


Conditions
==========

Based on matching conditions certain changes on tickets will be made and/or notifications will be sent.

* Ticket-Attributes: Define matching ticket attributes where a trigger will executed. You can also distinguish between creating and updating tickets (it's called action).

* Article-Attributes: If you define article attributes, the changed ticket must have a new article and the new article must match selected attributes.

* Customer-Attributes: The customer attributes of the changed ticket must match with these selected attributes.

* Organization-Attributes: The organization attributes of the changed ticket must match with these selected attributes.


Execution
=========
Defines what to do if conditions are matching. For example, new tickets of a VIP customer will have always high ticket priority.
