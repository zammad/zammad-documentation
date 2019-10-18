Privacy
*******

Zammads related information
===========================

Ticket and user storage times
-----------------------------

Tickets and users are stored forever in Zammad. However, if needed, you can use the `Scheduler <https://admin-docs.zammad.org/en/latest/manage-scheduler.html>`_ to automatically remove tickets after a specific time. 
If you need to delete user and ticket data ("Right to forget"), you currently can use the `Console <https://docs.zammad.org/en/latest/console/dangerzone-for-experts.html>`_.


Chat-Sessions
-------------

Chat-Sessions will be removed after 3 months, as long as they're in closed-state. 
Please note that Chat-Sessions also contain IP address information that you `might want to cleanup earlier <https://docs.zammad.org/en/latest/console/working-on-chat.html#removing-ip-information-from-chat-sessions>`_.


CTI Caller-Log
--------------

The caller log shows the last 60 entries. 
Zammad will remove all CTI Caller-Log information after 12 months.

Logfiles
--------

Zammad writes logfiles (normally in ``/opt/zammad/log/``) which are not changed or deleted by Zammad after wards. 
We suggest using logrotation here. Package installations will by default rotate log files nightly and remove the oldest one after 14 days.

User-Sessions
-------------

As long as the user is authenticated, Zammad will hold Session information (including Location (if applicable), IP address, Browser, creation date and last update) for the time the session is active. These information can be either deleted by the admin via UI or at the moment the user log outs.

Please note that the user can, if logging out every time, remove the session by himself at any point.
Also, users can delete their Session information via the "Device" preference menu.


External services
=================

What information is stored exactly on images.zammad.com, and for how long?
--------------------------------------------------------------------------

* We use images.zammad.com to serve user avatars (based on email address fetched from e. g. gravatar) and organization logo (based on domain used for Zammad login page after initial admin account creation).

  * images.zammad.com is only a proxy for images (e. g. found on public resources like gravatar)
  * md5 sums of email addresses are used to cache images for 7 days
  * md5 sums of domains are used to cache images for 30 days

Which other parts of the system do send data?
---------------------------------------------

* Zammad uses 4 online services
* you can enabled/disable all of them via Admin → System → Services

**Note: You can also create and set up your own backends/services for this, if you want.**

* Image: To serve user avatars (based on email address fetched from e. g. gravatar) and organization logo (based on domain used for Zammad login page after initial admin account creation).

  * images.zammad.com is only a proxy for images
  * md5 sums of email addresses are used to cache images for 7 days
  * md5 sums of domains are used to cache images for 30 days

* GeoCalendar: Zammad can handle SLAs, for SLAs calendars (time zone, working hours and vacation days are important). This GeoCalendar service is executed after initial admin account creation to automatically configure the calendar of the admin (time zone, vacation days, ...).

  * GeoCalendar - No information is stored or cached on geo.zammad.com

* GeoIp: Zammad has a security feature to track user sessions based on the user's browser and country. So if your session or password is used (maybe stolen) on a new browser or from a different country, Zammad will inform the Agent about the new use of password/session via email.

  * GeoIp - No information is stored or cached on geo.zammad.com

* GeoLocation: A ticket overview will not only be shown in a regular table, but on a map. For this map we need to know the geo location of certain items.

  * GeoLocation - Currently there is only a google maps backend to lookup geo locations

* The source code of this services is available at:

  * https://github.com/zammad/zammad/tree/develop/lib/service
