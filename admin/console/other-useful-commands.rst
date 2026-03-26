Other Useful Commands
=====================

.. include:: /admin/console/missing-commands-ask-community.include.rst

Remove AI Feature
-----------------

Zammad's AI feature is completely optional and requires a configuration before
any AI request is made. However, if you don't want to see the feature, you can
do so by setting the permission to inactive.

Disable any AI provider, in case you already configured it:

.. code-block:: irb

   >> Setting.set('ai_provider', false)

Disable permission to hide the settings from UI:

.. code-block:: irb

   >> Permission.where("name LIKE 'admin.ai%'").update!(active: false)

To re-enable it, set the ``active`` flag to ``true``.

Fetch Emails
------------

The below command will do a manual fetch of mail channels.
This will also show errors that might appear within that process.

.. code-block:: irb

   >> Channel.fetch

Reprocess Failed Emails
-----------------------

When Zammad fetches a mail it cannot parse (e.g. due to a parser bug or a
malformed message), it will store the mail in the database and warn in
the monitoring section about it.

In case of a malformed message (e.g. an invalid email address in one of the
header fields), you may need to manually edit the mail before Zammad can process
it. To do so, follow the steps below:

Export all Failed Emails to a Local Folder
   Execute ``rake zammad:email_parser:failed_email:export_all``. You can find
   the location of the exported email in the output of your console.
   Every time you perform an export of failed (unprocessable) emails, it
   creates one folder containing all failed emails at the time of execution.

Edit the Email
   The email has been exported in the step above. Now you can have a look at it
   and try to repair it. Make sure to leave the file name untouched, as the
   import will otherwise fail.

Import and Reprocess Locally Modified Email
   After editing the email, run
   ``rake zammad:email_parser:failed_email:import path/to/your/email.eml``
   to apply your changes from the file to the database. You can also pass
   the entire folder as argument, so all ``.eml`` files in it will we imported
   and reprocessed. If the reprocessing of the email was successful, the file(s)
   will be deleted, and the empty folder removed.

   .. hint::

      Make sure to run these commands only from the main Zammad folder ``/opt/zammad``.
      There may be problems if you try to run it from within the generated subfolder.

Delete Unwanted Emails
   In case of unwanted emails such as spam, you can delete them from the
   database after exporting them with the command
   ``rake zammad:email_parser:failed_email:delete path/to/your/email.eml``.
   If you pass the export folder as argument instead, all contained emails will
   be removed from the database, their files deleted and finally the empty folder
   removed.

Show and Retry Failed Data Privacy Jobs
---------------------------------------

In rare cases, Zammad's data privacy jobs might fail. To show them, you can use
the following rake command:

.. code-block:: console

   $ rake zammad:data_privacy:failed:show

To retry failed data privacy jobs, you can use the following command. However,
without changing the underlying issue that caused the failure, the job will fail
again. So make sure to check the logs for the root cause of the failure and fix
it before retrying the job.

.. code-block:: console

   $ rake zammad:data_privacy:failed:retry

Fill a Test System With Test Data
---------------------------------

.. danger::

   Don't run this in a productive environment! This can slow down Zammad and is
   hard to revert if you create much!

The below command will add ``50`` agents, ``1000`` customers, ``20`` groups,
``40`` organizations, ``5`` new overviews and ``100`` tickets.
You can always use ``0`` to not create specific items.
Zammad will create random data which make no logical sense.

.. code-block:: irb

   >> FillDb.load(agents: 50,customers: 1000,groups: 20,organizations: 40,overviews: 5,tickets: 100,)
