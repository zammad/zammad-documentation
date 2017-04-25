Trigger
*******

Triggers will be executed (ordered by name) on every ticket creation or update. They execute changes on tickets or to send notifications.


Use cases
=========

Examples for using triggers:

* Sending auto replies for new tickets to customers to let them know that a ticket has been created.
* Setting the ticket owner on first reply if no owner is set.


Conditions
==========

Based on matching conditions, certain changes on tickets will be made and/or notifications will be sent.

* Ticket attributes: Define matching ticket attributes for which a trigger will be executed. You can also distinguish between creating and updating tickets (it's called action).

* Article attributes: If you define article attributes, the changed ticket must have a new article and the new article must match the selected attributes.

* Customer attributes: The customer attributes of the changed ticket must match these selected attributes.

* Organization attributes: The organization attributes of the changed ticket must match these selected attributes.


Execution
=========
Defines what to do if conditions are matching. For example, new tickets of a VIP customer will have always high ticket priority.
