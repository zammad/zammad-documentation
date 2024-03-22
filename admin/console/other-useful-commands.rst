Other Useful Commands
*********************

.. include:: /admin/console/missing-commands-ask-community.include.rst

Fetch Mails
-----------

The below command will do a manual fetch of mail channels.
This will also show errors that might appear within that process.

.. code-block:: ruby

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
   and reprocessed. If the reprocessing of the mail was successful, the file(s)
   will be deleted, and the empty folder removed.

   .. hint::

      Make sure to run these commands only from the main Zammad folder ``/opt/zammad``.
      There may be problems if you try to run it from within the generated subfolder.

Delete Unwanted Email
   In case of unwanted emails such as SPAM, you can delete them from the
   database after exporting them with the command
   ``rake zammad:email_parser:failed_email:delete path/to/your/email.eml``.
   If you pass the export folder as argument instead, all contained emails will
   be removed from the database, their files deleted and finally the empty folder
   removed.

Add Translation
---------------

.. warning::

   Although the procedure described below still works, it is not recommended for usage any more.

   Since Zammad version 6.3 it's possible to customize any translation via graphical UI. All coupled with handy
   suggestions for all translatable custom objects in the local system. For more information, see the documentation for the :admin-docs:`translations screen </system/translations.html>`.

This comes in handy if you e.g. added a new state that you need to translate
for several languages.

.. code-block:: ruby

   >> Translation.create_if_not_exists(:locale => 'de-de', :source => "New", :target => "Neu", created_by_id: 1, updated_by_id: 1)

.. warning::

   While Zammad knows further attributes for the Translation model, please
   *do not* set them manually. Doing so may interfere with our `Weblate`_
   translation process and cause you loosing your custom translations.

   If you want to translate code base strings that are available within standard
   code, please use `Weblate`_ instead.

.. _Weblate: https://translations.zammad.org/

Translating Attributes
~~~~~~~~~~~~~~~~~~~~~~

By default Zammad will not translate custom attributes.
With the following code you can enable translation.
This will translate the attribute display name and the display names of values
(if it's a value field). For this to work, just replace ``{attribute-name}``
with the name of your attribute.

.. code-block:: ruby

   >> attribute = ObjectManager::Attribute.find_by(name: '{attribute-name}')
   >> attribute.data_option[:translate] = true  # set this to false to disable
                                                # translation again
   >> attribute.save!

.. note::

   Translating value display names works for the following attribute types:

   * Boolean
   * Select
   * Tree Select

   If you're translating the display name of e.g. an Integer-attribute,
   this works as well!

Fill a Test System With Test Data
---------------------------------

.. danger::

   Don't run this in a productive environment! This can slow down Zammad and is
   hard to revert if you create much!

The below command will add ``50`` agents, ``1000`` customers, ``20`` groups,
``40`` organizations, ``5`` new overviews and ``100`` tickets.
You can always use ``0`` to not create specific items.
Zammad will create random data which make no logical sense.

.. code-block:: ruby

   >> FillDb.load(agents: 50,customers: 1000,groups: 20,organizations: 40,overviews: 5,tickets: 100,)
