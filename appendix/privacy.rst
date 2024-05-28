Privacy & Data Retention
************************

How long does Zammad hold onto user data? How can I manage its user data retention behavior?

On-Premises Data
================

The following kinds of data are stored locally on the production system:

Tickets and users
   By default, Zammad never automatically deletes tickets or users.

   To enable **automatic** deletion of tickets after a given interval,
   :admin-docs:`use the scheduler </manage/scheduler.html>`.

   To **manually** delete users and all their associated tickets
   (*e.g.* in compliance with a “Right to Forget” request under the GDPR),
   you can use the
   :admin-docs:`data privacy functions </system/data-privacy.html>`
   in the admin panel or
   :doc:`use the console </admin/console/dangerzone-for-experts>`.

Chat sessions
   Once a chat session has been marked **closed**,
   it is scheduled for automatic deletion 12 months later.

   IP address logs for chat sessions can be manually deleted
   by :doc:`following the directions here </admin/console/working-on-chat>`.

CTI caller log
   The caller log shows only the 60 most recent entries.
   Each entry in the caller log is automatically deleted after 12 months.

Log files
   Zammad writes log files to disk (typically under ``/opt/zammad/log/``).

   Package installations will set up a separate system utility called
   ``logrotate`` to rename and archive (or *rotate*) log files on a nightly
   basis and remove old logs after 14 days.

   If installing from source, it is strongly recommended to configure ``logrotate``
   or a similar log management utility; Zammad will not purge old logs on its own.

User sessions
   Zammad maintains session information about every user currently logged in.

   This information is automatically purged when a user logs out,
   and can be viewed or manually deleted via the admin panel (under **System → Sessions**).
   Users may also delete their own session information
   via the user preferences menu, under **Device**.

   Session information includes IP address (and possibly geographic location), browser,
   time of original login, and time of last visit.

Data Privacy Tasks
   Each entry in the data privacy task list is automatically deleted after 12 months.

External Services
=================

Zammad utilizes third-party web services for certain functions,
meaning that user data may occasionally be sent or exposed to third parties.
These functions can be individually disabled in the admin panel
under **Settings → System → Services**.

.. note:: By default, the third-party services that Zammad relies on
   are mostly ones hosted and managed by the Zammad Foundation itself,
   but Zammad can be extended to interface with other services instead.

   The source code for these third-party service integrations can be found
   `here <https://github.com/zammad/zammad/tree/develop/lib/service>`_.

Images
   No private images or personally-identifying information are stored on images.zammad.com.

   The Images service caches publicly-available images from sources like Gravatar
   and serves them to the Zammad application as user avatars and organization logos.
   These images are discovered using MD5 digests of user email addresses and organization domain names.
   User avatars are cached for 7 days; organization logos are cached for 30 days.

GeoCalendar
   No user information is stored or cached on geo.zammad.com.

   As part of its service-level agreement (SLA) functionality,
   Zammad requires detailed, localized calendar information
   (*e.g.,* to set the time zone and
   accommodate national holidays and daylight savings time).
   The GeoCalendar service is used to retrieve this information.

GeoIP
   No user information is stored or cached on geo.zammad.com.

   One of Zammad's security features is to track user sessions
   based on the user's browser and country of origin.
   Suspicious login activity from a different browser or country may trigger Zammad
   to dispatch an alert email to the affected user.
   The GeoIP service is used to associate IP addresses to a geographic origin.

Geolocation
   Zammad's geolocation service relies on OpenStreetMap (OSM) unless you turned
   it off. If you provide an address (or parts of an address) in a user
   object, there is a lookup of coordinates from OSM which are stored in
   Zammad's database. Have a look at their
   `privacy policy <https://osmfoundation.org/wiki/Privacy_Policy>`_ for
   more information.

