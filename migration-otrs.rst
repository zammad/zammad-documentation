from OTRS
*********

Via Browser
===========

After installing Zammad, open http://localhost:3000 with your browser and follow the installation wizard.
From there you're able to start migration from OTRS.

See the Video @ http://days.zammad.org/features/migrator

Via command line
================

If you miss this at the beginning or you want to re-import again you have to use the command line at the moment.

* Install OTRS migration plugin on OTRS

  * OTRS 5:

    * https://portal.znuny.com/api/addon_repos/public/617/latest

  * OTRS 4:

    * https://portal.znuny.com/api/addon_repos/public/383/latest

  * OTRS 3.1 - 3.3:

    * https://portal.znuny.com/api/addon_repos/public/287/latest

* Stop all Zammad processes and switch Zammad to import mode (no events are fired - e. g. notifications, sending emails, ...)

::

 rails c
 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Import::OTRS.start

After the import is done switch Zammad back to non import mode and mark the system initialization as done

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.

**Note: It's currently not possible to import the user passwords. Therefore each user has to go through the reset password procedure!**

