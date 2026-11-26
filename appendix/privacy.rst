Privacy & Data Retention
========================

How long does Zammad hold onto user data? How can I manage its user data
retention behavior?

Zammad stores operational and personal data in its database. Some of it
is removed automatically by built-in cleanup jobs after a fixed period.
Most core data, like tickets and users, stays until you delete it.

Automatic Deletion
------------------

The data below is deleted by scheduled cleanup jobs. The retention
column states how old the data may get before removal, measured from
the point in time noted with each entry. The interval column says how
often Zammad checks for entries to delete, so actual removal can lag
the retention period by up to one interval.

These cleanups are built-in. They don't appear under *Manage →
Scheduler*, which only lists jobs you create yourself, and
neither the periods nor the intervals can be changed through settings.
Adjusting or deactivating a built-in task requires the Rails console.

.. list-table::
   :header-rows: 1
   :widths: 30 45 25

   - - Data
     - Retention
     - Cleanup runs
   - - Activity stream entries
     - 3 months after creation
     - daily
   - - API tokens that aren't personal access tokens
     - 30 days after creation, or immediately after they expire
     - daily
   - - Audit log entries
     - 12 months after the change
     - daily
   - - Chat sessions, once marked **closed**
     - 12 months after the last update
     - every 5 days
   - - CTI caller log
     - 12 months after the call
     - monthly
   - - Data privacy tasks
     - 12 months after creation
     - daily
   - - HTTP logs
     - 1 month after the request
     - daily
   - - MCP confirmation tokens for AI agents
     - until they expire
     - daily
   - - Mobile taskbar entries
     - 1 day after the app was last in contact
     - every 10 minutes
   - - Online notifications
     - 9 months after creation, or shortly after being seen
     - every 2 hours
   - - Recent views and recent closes
     - 3 months after last use
     - daily
   - - Sessions
     - 2 hours of inactivity (non-persistent) and 60 days at most
       (all)
     - every 12 hours
   - - Statistics data
     - 12 months after the last update
     - every 31 days
   - - Upload cache (draft attachments that were never submitted)
     - 1 month, except files belonging to an open draft
     - monthly

Some of these entries deserve a closer look:

HTTP logs
   Zammad records the HTTP calls it performs for integrations here.
   They appear as **Recent Logs** on the related admin pages, e.g. for
   webhooks, LDAP, SAML or WhatsApp. AI provider requests are logged
   too and show up under *AI → Feedback & Logs*.
   HttpLog masks specific credential patterns in the stored request
   and response content: Bearer, Basic and DeepL-Auth-Key
   Authorization headers, ``*-token`` headers such as
   ``PRIVATE-TOKEN``, cookie values, and access_token, api_key and
   secret values in query parameters and inline text. The masking is
   pattern-based and not exhaustive. Other Authorization schemes,
   including ``Token``, and credentials in other formats stay in the
   clear, and the request URL itself is stored unmasked, query string
   included. Request and response content can still include ticket
   and user data, and because the cleanup runs daily, removal can lag
   the one-month period by another day.

Audit log
   Records changes to administrative objects such as settings,
   groups, roles and channels. Entries name the acting user and store
   the source IP address. See :admin-docs:`audit logs
   </system/audit-logs.html>` for the full field list.

Chat sessions
   When a closed chat is deleted, the stored IP address, geographic
   location and reverse DNS name disappear with it. To remove that
   data while keeping the chat contents, use the
   :doc:`console recipe for chat logs </admin/console/working-on-chat>`.
   The recipe only processes chats that have been closed and unchanged
   for seven days. Data in recently closed or still open chats is
   left untouched and needs another run once that delay has passed.

Sessions
   Zammad keeps one session per logged-in client, holding the IP
   address, browser and location derived from the IP. A session is
   also deleted when the user logs out. Administrators can view and
   delete sessions under *System → Sessions*, and
   users can do so for their own devices in their profile settings.

Data Without Automatic Deletion
-------------------------------

The following data stays in the database until you remove it or delete
the object it belongs to.

Tickets and users
   By default, Zammad never deletes tickets or users.

   To delete them automatically, create a scheduler job under
   *Manage → Scheduler*. Pick **Ticket** or **User**
   as the object, add conditions that select the records to remove
   (e.g. a state and an age) and choose an action:
   **Delete immediately** removes tickets without a trace, while
   **Add a data privacy deletion task** runs the deletion through the
   :admin-docs:`data privacy panel </system/data-privacy.html>`, where
   it is visible and reviewable. For users, only the data privacy
   task is offered. See :admin-docs:`the scheduler
   </manage/scheduler.html>` for job details.

   To **manually** delete users and all their associated tickets
   (e.g. in compliance with a "Right to Forget" request under
   the GDPR), you can use the
   :admin-docs:`data privacy functions </system/data-privacy.html>`
   in the admin settings or
   :doc:`use the console </admin/console/dangerzone-for-experts>`.

Ticket history
   Entries shown on a ticket's history tab are kept as long as the
   ticket exists and are deleted with it. They are not purged on
   their own.

Web form data in tickets
   Tickets created through a ticket form store the submitter's IP
   address and an MD5 hash of their browser fingerprint inside the
   ticket. This data lives and dies with the ticket.

Devices
   Zammad records one entry per login device, holding the IP address
   and browser fingerprint plus a location derived from the IP. There
   is no
   automatic deletion. Users can remove entries in their profile
   settings under **Devices**. Deleting the user also removes their
   device entries.

Imports
   Imported tickets are regular tickets with no separate retention.
   The import job itself, including its error data, stays in the
   system until you delete it.

AI feedback and analytics
   Ratings, free-text comments on AI results and the run data behind
   them are stored without an end date. They appear under
   *AI → Feedback & Logs* and can be exported from
   there as a report. Ratings and comments are removed when their
   author is deleted, nothing else is.

Log Files
---------

Zammad writes log files to disk (typically under ``/opt/zammad/log/``).
Package installations set up a separate system utility called
``logrotate`` to rename and archive (or *rotate*) log files on a
nightly basis and remove old logs after 14 days.

Container and Kubernetes installations usually write log output to
stdout instead. There, retention is decided by your container runtime
and logging stack, not by Zammad.

External Services
-----------------

Zammad utilizes third party web services for certain functions,
meaning that user data may occasionally be sent or exposed to third
parties. These functions can be individually disabled in the admin
settings under *System → Services*.

.. note:: By default, the third party services that Zammad relies on
   are mostly ones hosted and managed by the Zammad Foundation itself,
   but Zammad can be extended to interface with other services instead.

   The source code for these third party service integrations can be
   found
   `here <https://github.com/zammad/zammad/tree/develop/lib/service>`_.

Images
   The Images service caches publicly-available images from sources
   like Gravatar and serves them to the Zammad application as user
   avatars and organization logos. To find an image, Zammad sends the
   user's email address and the organization's domain name in plain
   text to images.zammad.com. User avatars are cached for 7 days,
   organization logos for 30 days.

GeoCalendar
   No user information is stored or cached on geo.zammad.com.

   As part of its service-level agreement (SLA) functionality,
   Zammad requires detailed, localized calendar information
   (e.g. to set the time zone and accommodate national holidays
   and daylight savings time). The GeoCalendar service is used to
   retrieve this information.

GeoIP
   No user information is stored or cached on geo.zammad.com.

   One of Zammad's security features is to track user sessions
   based on the user's browser and country of origin. Suspicious
   login activity from a different browser or country may trigger
   Zammad to dispatch an alert email to the affected user. The GeoIP
   service is used to associate IP addresses to a geographic origin.

Geolocation
   Zammad's geolocation service relies on OpenStreetMap (OSM) unless
   you turned it off. If you provide an address (or parts of an
   address) in a user object, there is a lookup of coordinates from
   OSM which are stored in Zammad's database. They are replaced only
   when the address changes and the lookup returns a result. Clearing
   the address or editing other user data leaves the old coordinates
   in place, and they are removed only with the user. Have a look at
   their `privacy policy <https://osmfoundation.org/wiki/Privacy_Policy>`_
   for more information.

AI providers
   If AI features are enabled, Zammad sends content to the configured
   (e.g. ticket text for summaries or translation. How
   long the provider keeps that data is governed by the provider's
   own policies, which Zammad can't influence. On the Zammad side,
   the requests fall under the HTTP log retention described above, so
   they exist for about a month after the call, plus the daily
   cleanup delay.
