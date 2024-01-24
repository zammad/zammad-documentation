Helper scripts
**************

.. danger:: **☠️ The following scripts are potentially destructive ☠️**

   You should **never** run scrips which scopes you don't understand.
   Below scripts potentially can make things worse which is why you should
   evaluate them *before hand*.

   You're running these scripts at your own risk.

If we found a script is helping you more than 30 lines of new documentation,
we may have added a helper script.

.. _reset_db_password:

Database Helper: (re)set password
---------------------------------

   Limitations
      * This script is working for PostgreSQL installations only.
      * Only local database servers are supported (script changes user).
      * This script requires to be run as ``root`` or similar privileged user!

   Scopes
      Mostly the following installation types will be affected / relevant:

         * package installations (especially CentOS & SUSE)
         * possibly source code installations

   Functionality
      The script will do the following actions depending on the situation
      automatically for you. It will double tab by asking for your confirmation
      up front.

         * If ``database.yml`` contains an empty password line, a new password
           will be generated, and set for the database user of Zammad, and
           saved to the configuration file.
         * If ``database.yml`` contains a password, it will be used to set
           the password of the Zammad database user.
         * Please note that the script will automatically stop and start Zammad!

   Usage
      Run ``/opt/zammad/contrib/backup/zammad_db_user_helper.sh`` and follow
      the instructions. No specific configurations are required.

      If errors occur the script will try to bring Zammad back online before
      exitting. Please ensure that your service is running.
