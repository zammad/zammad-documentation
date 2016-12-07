Privacy
*******

What information is stored exactly on images.zammad.com, and for how long?
==========================================================================

* We use images.zammad.com to serve user avatars (based on email address fetched from e. g. gravatar) and organization logo (based on domain used for Zammad login page after initial admin account creation).

  * images.zammad.com is only a proxy for images (e. g. found on public resources like gravatar)
  * md5 sums of email addresses are used to cache images for 7 days
  * md5 sums domains are used to cache images for 30 days

Which other parts of the system do leak data?
=============================================

* Zammad use 4 online services 
* you can enabled/disable all of them via Admin → System → Services

**Note: You als can create and setup your own backends/services for this, if you want.**

* Image: To serve user avatars (based on email address fetched from e. g. gravatar) and organization logo (based on domain used for Zammad login page after initial admin account creation).

  * images.zammad.com is only a proxy for images
  * md5 sums of email addresses are used to cache images for 7 days
  * md5 sums domains are used to cache images for 30 days

* GeoCalendar: Zammad can handle SLAs, for SLAs calendars (timezone, working hours and vacation days are important). This GeoCalendar service is executed after initial admin account creation to automatically configure the calendar of the admin (timezone, vacation days, ...).

  * GeoCalendar - No information is stored or cached on geo.zammad.com

* GeoIp: Zammad has a security feature to track user sessions based on users browser and users country. So if your session or password is used (maybe stolen) on a new browser or from a different country, Zammad will inform the Agent about the new use of password/session via a new browser/country.

  * GeoIp - No information is stored or cached on geo.zammad.com

* GeoLocation: Zammad has modern features. One new feature will be a ticket overview not in a regular table, but on a map. For this map we need to know the geo location of certain items.

  * GeoLocation - Currently there is only a google maps backend to lookup geo locations

* The source code of this services is available under: 

  * https://github.com/zammad/zammad/tree/develop/lib/service
