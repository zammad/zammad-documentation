List of Indexed Attributes
**************************

Below is a comprehensive list of all object attributes indexed by
Elasticsearch. In other words, if you wish to find a ticket, article, or user
via the Zammad search box, Elasticsearch can match on any (or all) of the
fields below.

.. contents:: Table of content
   :local:
   :depth: 1

.. note::

   These fields may vary if you created custom fields (objects) in the admin interface.

.. hint:: **Below you can find some hints:**

      * **(SLA)**: Attributes marked as SLA attribute are only set if the ticket is
        affected by SLA calculation. Please note that some attributes may
        not be set if specific conditions are not met.

        Also note that some attributes may be reset to ``null`` if no
        longer applicable.
      * ``note`` **attribute**: Note attributes usually are empty if not
        specified via console or API.
      * **Timestamps**: All timestamps provided by Zammad are UTC by default.
        This also applies to times provided by Elasticsearch

Ticket
======

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_ticket``

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
       | Please see `Group`_ for more
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

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_ticket_priority``

.. list-table:: Ticket Priority-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - active
     - ``true``, ``false``
     - Defines if the priority is active (available)
   * - created_at
     - ``2021-03-03T14:50:20.724Z``
     - Creation date of priority
   * - created_by_id
     - ``1``
     - User that created priority
   * - default_create
     - ``false``, ``true``
     - Defines if priority is default priority upon ticket creation
   * - id
     - ``3``
     - ID of priority
   * - name
     - ``3 high``
     - Priority name
   * - note
     - ``null``
     - Note for priority that has been set via console or API
   * - ui_color
     - ``null``, ``high-priority``
     - CSS class for tickets of priority
   * - ui_icon
     - ``null``, ``important``
     - CSS class for ticket icons of priority
   * - updated_at
     - ``2021-03-03T14:50:20.724Z``
     - Date of last change
   * - updated_by_id
     - ``1``
     - User ID of user last updating the priority

Ticket State
============

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_ticket_state``

.. list-table:: Ticket State-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - active
     - ``true``, ``false``
     - Defines if state is active (available)
   * - created_at
     - ``2021-03-03T14:50:20.694Z``
     - Creation date
   * - created_by_id
     - ``1``
     - User ID that created state
   * - default_create
     - ``false``, ``true``
     - Defines if the state is the default state upon ticket creation
   * - default_follow_up
     - ``false``, ``true``
     - Defines if the state is the default follow up state on ticket follow ups
   * - id
     - ``7``
     - State ID
   * - ignore_escalation
     - ``false``, ``true``
     - Defines if SLA calculation is generally ignored for this state
   * - name
     - ``pending close``
     - State name
   * - next_state
     - ``n/a``, #{state object}
     - Contains all follow up state information if applicable,
       may not be available depending on the state type
   * - next_state_id
     - ``null``, ``4``
     - State ID of follow up state
   * - note
     - ``null``
     - Note that has been set via console or API
   * - state_type
     - Contains these attributes:
          * created_at: ``2021-03-03T14:50:20.582Z``
          * created_by_id: ``1``
          * id: ``4``
          * name: ``pending action``
          * note: ``null``
          * updated_at: ``2021-03-03T14:50:20.582Z``
          * updated_by_id: ``1``
     - Contains all available information of the states type
   * - state_type_id
     - ``4``
     - ID of the state type
   * - updated_at
     - ``2021-03-03T14:50:20.694Z``
     - Last update of state
   * - updated_by_id
     - ``1``
     - User ID that updated state last

Article
=======

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_ticket``

.. note::

   Articles are part of the ticket index.
   To reduce complexity we decided to provide it in its own table. 🙏

.. list-table:: Article-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - body
     - ``Hi,\n\nplease send me:\n1 [...] \n75007 Paris\n\nDavid Bell``
     - Article body in plain text
   * - cc
     - ``null``, ``alias@domain.tld``
     - EMail-Addresses set as CC (String)
   * - content_type
     - ``text/html``
     - Content type of article
   * - created_at
     - ``2021-03-22T03:47:59.290Z``
     - Time stamp of article creation
   * - created_by_id
     - ``10``
     - User ID that created the article
   * - from
     - ``David Bell <david@example.com>``
     - From field of article creator
   * - id
     - ``16``
     - Internal article ID
   * - in_reply_to
     - ``null``
     - In-Reply-To Header from emails if applicable
   * - internal
     - ``false``, ``true``
     - Defines if article is internal
   * - message_id
     - ``null``
     - Message ID of Email if applicable
   * - origin_by_id
     - ``null``
     - User ID or original creator if created on behalf another user
   * - preferences
     - ``{}``
     - Internal preferences, may be empty, mainly for delivery states
   * - references
     - ``null``
     - Contains message references
   * - reply_to
     - ``null``
     - Contains reply to header if applicable
   * - sender_id
     - ``2``
     - ID of sender type (Customer, System, Agent)
   * - subject
     - ``My amazing subject``
     - Article subject
   * - ticket_id
     - ``9``
     - Ticket ID the article belongs to
   * - to
     - ``support@example.com``
     - EMail address from TO-Header
   * - type_id
     - ``1``
     - ID of articles Type (phone, email, web, ...)
   * - updated_at
     - ``2021-03-22T03:47:59.290Z``
     - Last update
   * - updated_by_id
     - ``10``
     - User that updated article

User
====

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_user``

.. list-table:: User-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - active
     - ``true``, ``false``
     - Defines if user is active
   * - address
     - ``""``, ``Bennelong Point\nSydney NSW 2000``
     - Address string
   * - city
     - ``""``, ``Berlin``
     - City string
   * - country
     - ``""``, ``Germany``
     - Country string
   * - created_at
     - ``2021-03-22T12:47:56.460Z``
     - Creation date of user
   * - created_by_id
     - ``1``
     - User ID that created the user
   * - department
     - ``""``, ``IT``
     - Department string
   * - email
     - ``""``, ``alias@domain.tld``
     - EMail Address of user, if applicable
   * - fax
     - ``""``, ``1234``
     - Fax number
   * - firstname
     - ``null``, ``John``
     - Users first name
   * - id
     - ``8``
     - Internal User ID
   * - last_login
     - ``null``, ``2021-03-23T12:47:56.460Z``
     - Updated upon every user login
   * - lastname
     - ``null``, ``Doe``
     - Users last name
   * - login
     - ``auto-1234567``, ``jdoe``
     - Login name, always set and unique, can differ from ``email``
   * - mobile
     - ``""``, ``1232``
     - Mobile phone number
   * - note
     - ``""``
     - Note being available via web, console and API
   * - organization
     - #{organization object}
     - | Complete Payload of the organization the user is member of
       | Please see `Organization`_ for more
   * - organization_id
     - ``3``
     - ID of organization the user is member of
   * - out_of_office
     - ``false``, ``true``
     - Defines if user has activated out of office function
   * - out_of_office_end_at
     - ``null``, ``2021-03-26``
     - Ending date out of office
   * - out_of_office_replacement_id
     - ``null``, ``3``
     - User ID that replaces this user during out of office period
   * - out_of_office_start_at
     - ``null``, ``2021-03-24``
     - Begin date out of office
   * - permissions
     - ``(Array)``
     - Array with all permissions of the user
   * - phone
     - ``""``, ``0061 2 1234 7777``
     - Phone number of user
   * - preferences
     - ``{}``, #{several preference attributes}
     - Depends on user and situation, may contain ``notification_config``,
       ``locale`` and other internal system information
   * - role_ids
     - ``(Array)``, ``[1, 2]``
     - Contains array with role IDs assigned to the user
   * - street
     - ``""``
     - Street
   * - updated_at
     - ``2021-03-25T00:27:52.308Z``
     - Time stamp of last update
   * - updated_by_id
     - ``3``
     - User ID that updated this entry
   * - verified
     - ``false``, ``true``
     - Defines if the user has verified the account
   * - vip
     - ``false``, ``true``
     - Defines if user has VIP state
   * - web
     - ``""``, ``https://zammad.org``
     - Web URL of User
   * - zip
     - ``""``, ``10123``
     - ZIP code

Organization
============

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_organization``

.. list-table:: Organization-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - active
     - ``true``, ``false``
     - Defines if organization is active
   * - created_at
     - 2021-03-22T12:47:54.807Z
     - Creation date
   * - created_by
     - #{user object}
     - | Complete Payload of the user that created the organzation
       | Please see `User`_ for more
   * - created_by_id
     - ``1``
     - User ID that created the organization
   * - domain
     - ``null``, ``example.com``
     - Organizations domain
   * - domain_assignment
     - ``false``, ``true``
     - Domain assignment depends on ``domain``
   * - id
     - ``1``
     - Organization ID
   * - members
     - #{array of user objects}
     - | Array with complete Payload of the users being member of the
         organization
       | Please see `User`_ for more
   * - name
     - ``Chrispresso Inc.``
     - Organization name
   * - note
     - ``Manufacturer of individual coffee products.``
     - Note being available via web, console and API
   * - shared
     - ``true``, ``false``
     - Defines if the organization is a sharing one
   * - updated_at
     - ``2021-03-22T12:47:54.807Z``
     - Last update time
   * - updated_by
     - #{user object}
     - | Complete Payload of the user that updated the organization
       | Please see `User`_ for more
   * - updated_by_id
     - ``1``
     - User ID that updated the organization
   * - vip
     - ``true``, ``false``
     - Defines if the organization has VIP state

Group
=====

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_group``

.. list-table:: Group-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - active
     - ``true``, ``false``
     - Defines if group is active (available)
   * - assignment_timeout
     - ``null``, ``30``
     - Time in minutes an agent can be inactive until the owner ship is removed
   * - created_at
     - ``2021-03-24T23:55:06.980Z``
     - Time stamp of group creation
   * - created_by_id
     - ``1``
     - User ID that created the group
   * - email_address
     - Contains these attributes:
          * active: ``true``
          * channel_id: ``3``
          * created_at: ``2021-03-24T23:54:58.187Z``
          * created_by_id: ``3``
          * email: ``alias@domain.tld``
          * id: ``1``
          * note: ``null``
          * realname: ``Zammad GmbH``
          * updated_at: ``2021-03-24T23:54:58.187Z``
          * updated_by_id: ``3``
          * preferences: ``null``
     - Contains all available information of the groups email address
   * - email_address_id
     - ``3``
     - ID of email address
   * - follow_up_assignment
     - ``true``, ``false``
     - Defines if owners are still assigned after follow ups
   * - follow_up_possible
     - ``yes``, ``no``
     - Defines if following up on a closed ticket is possible
   * - id
     - ``1``
     - Group ID
   * - name
     - ``Users``, ``Sales``
     - Group name
   * - note
     - ``null``
     - Notes for the group available via web, console and API
   * - signature
     - Contains these attributes:
          * active: ``true``
          * body: ``<br>  #{user.firstname} #{user.lastname}<br>--<br>That Inc``
          * created_at: ``2021-03-03T14:50:19.775Z``
          * created_by_id: ``1``
          * id: ``1``
          * name: ``default``
          * note: ``null``
          * updated_at: ``2021-03-03T14:50:19.775Z``
          * updated_by_id: ``1``
     - Contains all available information of the groups signature
   * - signature_id
     - ``1``
     - Signature ID
   * - updated_at
     - ``2021-03-24T23:55:06.980Z``
     - Time stamp of last group update
   * - updated_by_id
     - ``3``
     - User ID that updated group

CTI Log
=======

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_cti_log``

.. list-table:: CTI Log-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - call_id
     - ``00006``
     - Unique Call ID
   * - comment
     - ``""``
     - Optional comment
   * - created_at
     - ``2021-03-22T11:48:01.703Z``
     - Creation date of Call
   * - direction
     - ``in``, ``out``
     - Call direction
   * - done
     - ``true``, ``false``
     - Defines if call displays as "to do" within UI
   * - duration_talking_time
     - ``27``
     - Call duration in seconds
   * - duration_waiting_time
     - ``77``
     - Duration in seconds the caller was waiting for answer
   * - end_at
     - ``2021-03-25T08:49:40.647Z``
     - Time stamp of call end
   * - from
     - ``493055571600``
     - Calling number
   * - from_comment
     - ``null``, ``John, Doe``
     - Display name of calling number if applicable
   * - from_pretty
     - ``+49 30 55571600``
     - Pretty version of ``from``
   * - id
     - ``8``
     - Internal ID of entry
   * - initialized_at
     - 2021-03-25T08:47:56.753Z
     - Time stamp of call initialization, usually matches ``created_at``
   * - preferences
     - ``(Array)``
     - Contains internal information if required
   * - queue
     - ``null``, ``491711234567890``
     - Queue the call was answered in
   * - start_at
     - ``2021-03-25T08:49:13.050Z``
     - Time stamp the call was answered
   * - state
     - ``hangup``, ``voicemail``
     - Last state of call
   * - to
     - ``491711234567890``
     - Dialed number
   * - to_comment
     - ``null``, ``John, Doe``
     - Display name of called number if applicable
   * - to_pretty
     - ``+491711234567890``
     - Pretty version of ``to``
   * - updated_at
     - ``2021-03-25T08:49:40.647Z``
     - Last update of entry

Chat Session
============

.. tip::

   🤓 The following indice contains below mentioned information:
   ``*_chat_session``

.. list-table:: Chat Session-Index
   :widths: 10 15 15
   :header-rows: 1

   * - Field
     - Sample Value
     - Description
   * - chat
     - Contains these attributes:
          * active: ``true``
          * block_country: ``null``
          * block_ip: ``null``
          * created_at: ``2021-03-03T14:50:22.607Z``
          * created_by_id: ``1``
          * id: ``1``
          * max_queue: ``5``
          * name: ``default``
          * note: ``""``
          * preferences: ``{}``
          * public: ``false``
          * updated_at: ``2021-03-03T14:50:22.607Z``
          * updated_by_id: ``1``
          * whitelisted_websites: ``null``
     - Contains various preferences of the chat topic in charge
   * - chat_id
     - ``1``
     - ID of Chat topic
   * - created_at
     - ``2021-03-25T10:26:24.376Z``
     - Time stamp of chat creation
   * - created_by_id
     - ``null``
     - User that created the chat, place holder, currently always ``null``
   * - id
     - ``1``
     - ID of Chat Session
   * - messages
     - ``(Array)`` - Array entries contain these attributes:
          * chat_session_id: ``1``
          * content: ``Hello dear customer``
          * created_at: ``2021-03-25T10:26:35.977Z``
          * created_by_id: ``null``, ``3``
          * id: ``1``
          * updated_at: ``2021-03-25T10:26:35.977Z``
     - Array with all messages of chat
   * - name
     - ``null``, ``John Doe``
     - Name agent set for chat user, if applicable
   * - preferences
     - Contains these attributes:
          * dns_name: ``host.domain.tld``
          * geo_ip: ``{}``
          * participants: ``Array``, ``["47118371175780", "47118371850300"]``
          * remote_ip: ``192.168.2.19``
          * url: ``https://zammad.com/en/company/contact``
     - Various internal Meta data of the session_id
   * - session_id
     - ``92f2909631f1ad5ff4d5d1e046952be8``
     - Unique Session ID
   * - state
     - ``closed``
     -  Current state of chat session
   * - tags
     - ``(Array)``, ``["order"]``
     - Tags applied to Chat Session by agent, if applicable
   * - updated_at
     - ``2021-03-25T10:27:03.341Z``
     - Last update
   * - updated_by_id
     - ``null``, ``3``
     - User ID that last updated session, may be ``null``
   * - user
     - #{user object}
     - | Complete Payload of the chat agemt
       | Please see `User`_ for more
   * - user_id
     - ``3``
     - User ID of chat agent
