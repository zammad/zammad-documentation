List of Indexed Attributes
**************************

Below is a comprehensive list of all object attributes indexed by 
Elasticsearch. In other words, if you wish to find a ticket, article, or user 
via the Zammad search box, Elasticsearch can match on any (or all) of the 
fields below.

.. note:: 

   These fields may vary if you created custom fields (objects) in the admin interface.

.. warning::

   Zammad 4.0 introduced breaking changes on the Elasticsearch index.

.. hint:: **🤓 Below list contains functionality hints**

   In order to save space and duplicate information, we'll provide hints to 
   functions within brackets if applicable.

      * (SLA): 
           Attributes marked as SLA attribute are only set if the ticket is 
           affected by SLA calculation. Please note that some attributes may 
           not be set if specific conditions are not met.

         Also note that some attributes may be reset to ``null`` if no 
         longer applicable.
      * ``note`` attribute:
           Note attributes usually are empty if not 
           specified via console or API.
      * Timestamps:
           All timestamps provided by Zammad are UTC by default. 
           This also applies to times provided by Elasticsearch

Ticket
======

.. list-table:: Ticket-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - article
     - #{Article Array}
     - | Array with all articles belonging to the ticket
       | Please see `Article`_ for more details
   * - article_count
     - ``1``
     - Number of articles within the ticket
   * - close_at
     - ``null``, ``2021-03-03T14:50:20.673Z``
     - First close time, set once
   * - close_diff_in_min
     - ``null``, ``239``, ``-5``
     - Depends on ``close_in_min`` and tells how many minutes the ticket was 
       closed relative to SLAs solution time. **(SLA)**
   * - close_escalation_at
     - ``null``, ``2021-03-03T15:50:20.673Z``
     - Time stamp when the ticket would escalate in case solution time 
       is violated. **(SLA)**
   * - close_in_min
     - ``null``, 11
     - Value in minutes for how long the ticket was open based on 
       business hours. **(SLA)**
   * - create_article_sender
     - Contains these attributes:
          * note: ``null``
          * updated_at: ``2021-03-03T14:50:20.812Z``
          * name: ``Customer``
          * created_at: ``2021-03-03T14:50:20.812Z``
          * updated_by_id: ``1``
          * id: ``2``
          * created_by_id: ``1``
     - Sender of the article (System, Agent, Customer)
   * - create_article_sender_id
     - ``1``, ``2``
     - ID of the user that created the article
   * - create_article_type
     - Contains these attributes:

          * note: ``null``
          * updated_at: ``2021-03-03T14:50:20.812Z``
          * name: ``phone``, ``email``, ``web``
          * active: ``true``
          * created_at: ``2021-03-03T14:50:20.812Z``
          * updated_by_id: ``1``
          * id: ``5``
          * created_by_id: ``1``
          * communication: ``true``, ``false``

     - Information of first article type and nature
   * - create_article_type_id
     - ``5``
     - Type ID of first article
   * - created_at
     - ``2021-03-24T16:17:27.210Z``
     - Time stamp of ticket creation
   * - created_by
     - #{user object}
     - | Complete Payload of user that created the ticket
       | Please see `User`_ for more
   * - created_by_id
     - ``3``
     - User ID that created the ticket
   * - customer
     - #{user object}
     - | Complete payload of the customer that created the ticket
       | Please see `User`_ for more
   * - customer_id
     - ``8``
     - Customers User ID
   * - escalation_at
     - ``null``, ``2021-03-24T16:28:38.535Z``
     - Time stamp of the next applicable escalation. One of the following 
       attributes:

          * ``close_escalation_at``
          * ``first_response_escalation_at``
          * ``update_escalation_at``

       **(SLA)**
   * - first_response_at
     - ``null``, ``2021-03-24T16:28:38.303Z``
     - Time stamp of the first communication type reaction to the customer 
       **(SLA)**
   * - first_response_diff_in_min
     - ``null``, ``10``, ``-6``
     - Depends on ``first_response_in_min`` and tells how many minutes the 
       tickets first response took relative to the first response time of your 
       SLA. **(SLA)**
   * - first_response_in_min
     - ``null``, ``11``
     - Value in minutes for how long the first response took based on 
       the business hours. **(SLA)**
   * - group
     - #{group object}
     - | Complete payload of the current tickets group
       | Please see `Group` for more
   * - group_id
     - ``1``
     - ID of the current group
   * - id
     - ``1``, ``111``
     - ID of the Ticket
   * - last_contact_agent_at
     - ``null``, ``2021-03-24T16:28:38.303Z``
     - Time stamp of last communication type contact of any agent
   * - last_contact_at
     - ``null``, ``2021-03-24T16:28:38.303Z``
     - | Time stamp of last communication type contact
       | Depends on ``last_contact_agent_at``, ``last_contact_customer_at`` 
         and "Ticket Last Contact Behaviour" setting
   * - last_contact_customer_at
     - ``null``, ``2021-03-24T16:28:38.303Z``
     - Time stamp of last communication type contact of customer
   * - mention_user_ids
     - ``[3, 5]``
     - Array with mentioned or subscribed users IDs
   * - note
     - ``null``
     - Note of ticket, only set via console or API
   * - number
     - ``1010138``, ``202006231010138``
     - Ticket number
   * - organization
     - ``null``, #{organization object}
     - | Complete Payload of user that owns the ticket
       | Please see `Organization`_ for more
   * - organization_id
     - ``null``, ``2``
     - ID of the customers organization
   * - owner
     - ``null``, #{user object}
     - | Complete Payload of user that owns the ticket
       | Please see `User`_ for more
   * - owner_id
     - ``null``, ``3``
     - User ID of the ticket owner
   * - pending_time
     - ``null``, ``2021-03-24T17:44:06.912Z``
     - Depends on pending states, time stamp for pending time
   * - preferences
     - ``n/a``, special information for internal functions
     - May not be available in your system, contains information for internal 
       system functions
   * - priority
     - #{priority object}
     - | Complete Payload of priority of ticket
       | Please see `Ticket Priority`_ for more
   * - priority_id
     - ``2``
     - Priority ID of the ticket
   * - state
     - #{state object}
     - | Complete Payload of current ticket state
       | Please see `Ticket State`_ for more
   * - state_id
     - ``1``, ``4``
     - ID of current ticket state
   * - tags
     - ``["order", "americano"]``
     - Array with all attached tags
   * - time_unit
     - ``null``, ``15``
     - Accounted time units for ticket (total)
   * - title
     - ``Feedback Form``, ``Need help``
     - Title / Subject of Ticket
   * - type
     - ``null``
     - Ticket type (deprecated)
   * - update_diff_in_min
     - ``null``, ``2021-03-24T16:28:38.303Z``
     - Depends on ``update_in_min`` and tells how many minutes the last ticket 
       update took relatively to the update time setting **(SLA)**
   * - update_escalation_at
     - ``null``, ``2021-03-24T16:28:38.303Z``
     - Time stamp when the ticket would escalate in case update time 
       is violated. **(SLA)**
   * - update_in_min
     - ``null``, ``5``, ``-10``
     - Value in minutes for how long the last ticket update took based on the 
       business hours and update time. **(SLA)**
   * - updated_at
     - ``2021-03-24T16:28:38.303Z``
     - Last ticket update
   * - updated_by
     - #{user object}
     - | Complete Payload of the user that updated the ticket
       | Please see `User`_ for more
   * - updated_by_id
     - ``1``, ``3``
     - User ID that updated the ticket

Ticket Priority
===============

Ticket State
============

Article
=======

+---------------------+--------------------------+----------------------------------------------+
| Field               | Sample Value             | Description                                  |
+=====================+==========================+==============================================+
| attachment.title    | file1.txt                | File name                                    |
+---------------------+--------------------------+----------------------------------------------+
| attachment.content  | Hello world              | File Content                                 |
+---------------------+--------------------------+----------------------------------------------+
| attachment.keywords | keyword                  | File Keywords                                |
+---------------------+--------------------------+----------------------------------------------+
| attachment.content  | Max                      | File Author                                  |
+---------------------+--------------------------+----------------------------------------------+
| body                | :)                       | Content of the article                       |
+---------------------+--------------------------+----------------------------------------------+
| cc                  | null                     | Content of the optional cc field             |
+---------------------+--------------------------+----------------------------------------------+
| content_type        | text/plain               | Content type                                 |
+---------------------+--------------------------+----------------------------------------------+
| created_at          | 2017-08-03T14:21:38.000Z | Article create date (DateTime, UTC)          |
+---------------------+--------------------------+----------------------------------------------+
| created_by          | See User                 | Who has created the article                  |
+---------------------+--------------------------+----------------------------------------------+
| created_by_id       | 13                       | Who (UserID) has created the article         |
+---------------------+--------------------------+----------------------------------------------+
| from                | Christopher Miller via   | Sender address of the article                |
|                     | <order@chrispresso.com>  | Sender address of the article                |
+---------------------+--------------------------+----------------------------------------------+
| id                  | 19                       | internal (DB) article id                     |
+---------------------+--------------------------+----------------------------------------------+
| in_reply_to         | null                     | Content of reply to field                    |
+---------------------+--------------------------+----------------------------------------------+
| internal            | FALSE                    | Is article visible for customer              |
+---------------------+--------------------------+----------------------------------------------+
| message_id          | null                     | Message ID (if article was an email)         |
+---------------------+--------------------------+----------------------------------------------+
| message_id_md5      | null                     | internal message id MD5 Checksum             |
+---------------------+--------------------------+----------------------------------------------+
| origin_by_id        | null                     | For which real user (UserID) the article     |
|                     |                          | creation has been done. For example the      |
|                     |                          | customer which was calling on the phone done |
+---------------------+--------------------------+----------------------------------------------+
| preferences         | { }                      | Hash for additional information              |
+---------------------+--------------------------+----------------------------------------------+
| references          | null                     | Email references header                      |
+---------------------+--------------------------+----------------------------------------------+
| reply_to            | null                     | Content of the reply to field                |
+---------------------+--------------------------+----------------------------------------------+
| sender              | Customer                 | Who is the sender (Customer, Agent)          |
+---------------------+--------------------------+----------------------------------------------+
| sender_id           | 2                        | Which type of user has created the article   |
|                     |                          | (Agent, Customer)                            |
+---------------------+--------------------------+----------------------------------------------+
| subject             | Feedback Form            | Article subject                              |
+---------------------+--------------------------+----------------------------------------------+
| ticket_id           | 19                       | referencing ticket ID                        |
+---------------------+--------------------------+----------------------------------------------+
| to                  | null                     | Content of the to field                      |
+---------------------+--------------------------+----------------------------------------------+
| type                | web                      | Article type (phone, email, web...)          |
+---------------------+--------------------------+----------------------------------------------+
| type_id             | 11                       | Article type id (phone, email, web...)       |
+---------------------+--------------------------+----------------------------------------------+
| updated_at          | 2017-08-03T14:21:38.701Z | Update time of the article (DateTime, UTC)   |
+---------------------+--------------------------+----------------------------------------------+
| updated_by          | See User                 | Who has updated the article                  |
+---------------------+--------------------------+----------------------------------------------+
| updated_by_id       | 13                       | Who (UserID) has updated the article         |
+---------------------+--------------------------+----------------------------------------------+

User
====

+-----------------+--------------------------+-----------------------------------------+
| Field           | Sample Value             | Description                             |
+-----------------+--------------------------+-----------------------------------------+
| active          | TRUE                     | is activ (boolean)                      |
+-----------------+--------------------------+-----------------------------------------+
| address         |                          | User Adress                             |
+-----------------+--------------------------+-----------------------------------------+
| city            |                          | User City                               |
+-----------------+--------------------------+-----------------------------------------+
| country         |                          | User Country                            |
+-----------------+--------------------------+-----------------------------------------+
| created_at      | 2017-07-26T21:21:28.000Z | User creation date (DateTime, UTC)      |
+-----------------+--------------------------+-----------------------------------------+
| created_by_id   | 1                        | ID of user who created the current user |
+-----------------+--------------------------+-----------------------------------------+
| department      |                          | User Department                         |
+-----------------+--------------------------+-----------------------------------------+
| email           | chris@chrispresso.com    | User E-Mail                             |
+-----------------+--------------------------+-----------------------------------------+
| fax             |                          | User Fax                                |
+-----------------+--------------------------+-----------------------------------------+
| firstname       | Christopher              | User Firstname                          |
+-----------------+--------------------------+-----------------------------------------+
| id              | 3                        | Internal id (database, autincrement)    |
+-----------------+--------------------------+-----------------------------------------+
| last_login      | 2017-07-26T21:23:15.019Z | User last login (DateTime, UTC)         |
+-----------------+--------------------------+-----------------------------------------+
| lastname        | Miller                   | User Lastname                           |
+-----------------+--------------------------+-----------------------------------------+
| login           | chris@chrispresso.com    | User Login                              |
+-----------------+--------------------------+-----------------------------------------+
| mobile          |                          | User Mobile                             |
+-----------------+--------------------------+-----------------------------------------+
| note            |                          | internal note                           |
+-----------------+--------------------------+-----------------------------------------+
| organization    | Chrispresso Inc          | Orgnaization name of the current user   |
+-----------------+--------------------------+-----------------------------------------+
| organization_id | 2                        | ID which links to the organization name |
+-----------------+--------------------------+-----------------------------------------+
| phone           |                          | User Phone                              |
+-----------------+--------------------------+-----------------------------------------+
| street          |                          | User Street                             |
+-----------------+--------------------------+-----------------------------------------+
| updated_at      | 2017-07-27T15:04:47.270Z | Last update date (DateTime, UTC)        |
+-----------------+--------------------------+-----------------------------------------+
| updated_by_id   | 3                        | ID of user who updated the current user |
+-----------------+--------------------------+-----------------------------------------+
| verified        | FALSE                    | is verified (boolean)                   |
+-----------------+--------------------------+-----------------------------------------+
| vip             | FALSE                    | Is VIP (boolean)                        |
+-----------------+--------------------------+-----------------------------------------+
| web             |                          | User Web Url                            |
+-----------------+--------------------------+-----------------------------------------+
| zip             |                          | User ZIP                                |
+-----------------+--------------------------+-----------------------------------------+

Organization
============

Group
=====
