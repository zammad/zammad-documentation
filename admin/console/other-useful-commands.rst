Other useful commands
*********************

.. include:: /admin/console/missing-commands-ask-community.include.rst

Fetch mails
-----------

The below command will do a manual fetch of mail channels.
This will also show errors that might appear within that process.

.. code-block:: ruby

   >> Channel.fetch

Reprocess unprocessable mails
-----------------------------

When Zammad encounters a mail it cannot parse (e.g. due to a parser bug or a
malformed message), it will store the mail in
``var/spool/unprocessable_mail/<ID>.eml``,  give up on attempting to parse the
mail, and will warn on the monitoring page that there are unprocessed mails.

To force Zammad to reattempt to parse those mails, run the following command:

.. code-block:: ruby

   >> Channel::EmailParser.process_unprocessable_mails

In case of a malformed message (e.g. an invalid email address in one of the
header fields), you may need to manually edit the mail before Zammad can process
it.

If Zammad fails to process the message, it will remain in the
``var/spool/unprocessable_mail`` folder; otherwise it will be removed after it
has been parsed successfully.

Add translation
---------------

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

Translating attributes
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

Fill a test system with test data
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
