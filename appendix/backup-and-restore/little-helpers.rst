Helper scripts
**************

Warning
=======

A script can potentially be destructive!
You should **never** run scrips which scopes you don't understand.

Be aware that you are running these scripts at your own risk.

.. _reset_db_password:

Database Helper: (re)set password
=================================

Limitations
   * This script is working for PostgreSQL installations only.
   * Only local database servers are supported (script changes user).
   * This script requires to be run as ``root`` or similar privileged user.
   * Be aware that the script will automatically stop and start Zammad!

Scopes
   Mostly the following installation types will be affected / relevant:

      * package installations (especially CentOS & SUSE)
      * possibly source code installations

Functionality
   The script will do the following actions automatically for you, depending
   on the situation. It will ask for your confirmation before performing
   actions.

      * If ``database.yml`` contains an empty password line, a new password
        will be generated and set for the database user of Zammad. It will also
        be saved to the configuration file.
      * If ``database.yml`` contains a password, it will be used to set
        the password of the Zammad database user.

Usage
   Run ``/opt/zammad/contrib/backup/zammad_db_user_helper.sh`` and follow
   the instructions. No specific configurations are required.

   If errors occur, the script will try to bring Zammad back online before
   exiting.