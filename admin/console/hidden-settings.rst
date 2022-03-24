Advanced customization settings
*******************************

On this page you can find some settings that you won't find within the Zammad
UI. Those settings might come in handy as it can change Zammad's behavior.

.. include:: /admin/console/missing-commands-ask-community.include.rst

Send all outgoing E-Mails to a BCC-Mailbox
------------------------------------------

This option allows you to send all outgoing E-Mails (not notifications) to a
specific mailbox. Please note that this shouldn't be a mailbox you're importing
already! This will apply to all groups and is a global setting.

.. code-block:: ruby

   >> Setting.set('system_bcc', 'alias@domain.tld')

You can easily check the current BCC-Setting by running the following:

.. code-block:: ruby

   >> Setting.get('system_bcc')

Activate counter on grouped overviews
-------------------------------------

This is a hidden setting which you can only set via Command-Line.
This will globally enable a ticket number value in each heading for grouped
elements.

.. code-block:: ruby

   >> Setting.set('ui_table_group_by_show_count', true)  # enable counter on grouped overviews
   >> Setting.set('ui_table_group_by_show_count', false) # disable counter on grouped overviews
   >> Setting.get('ui_table_group_by_show_count')        # get current setting (`nil` is false)

.. image:: /images/console/ui_table_group_by_show_count-example.png

Default Ticket type on creation
-------------------------------

Zammad allows you to define the default article type upon Ticket creation.
By default this will be a incoming phone call.

You can choose between

   * ``phone-in`` (incoming call, **default**),
   * ``phone-out`` (outgoing call) and
   * ``email-out``  (Sending an E-Mail out).

.. code-block:: ruby

   >> Setting.set('ui_ticket_create_default_type', 'email-out')

To check what setting is set currently, simply run:

.. code-block:: ruby

   >> Setting.get('ui_ticket_create_default_type')

Adding a warning to the ticket creation process
-----------------------------------------------

If in case you need to give your agent a note or warning during ticket creation,
you can do so with the below command.

You can use three different warnings for

   * Incoming Calls ``:"phone-in"=>""``,
   * Outgoing Calls ``:"phone-out"=>""`` and
   * Outgoing E-Mails ``:"email-out"=>""``.

.. code-block:: ruby

   >> Setting.set('ui_ticket_create_notes', {
         :"phone-in"=>"You're about to note a incoming phone call.",
         :"phone-out"=>"You're about to note an outgoing phone call.",
         :"email-out"=>"You're going to send out an E-Mail."
      })

.. note::

   You can use those three sub-settings independently, if you e.g. don't need a
   warning on incoming calls, simply leave out ``:"phone-in"=>""`` out of the
   setting. The setting itself is done within an array ( ``{}`` ).


To check what's currently set, you can use:

.. code-block:: ruby

   >> Setting.get('ui_ticket_create_notes')

Sample of the above setting:

.. image:: /images/console/ui_ticket_create_notes.gif

Show Email address of customer on customer selection (ticket creation)
----------------------------------------------------------------------

By default Zammad will not display the E-Mail-Addresses of customers.
The below option allows you to change this behavior.

.. code-block:: ruby

   >> Setting.set('ui_user_organization_selector_with_email', true)

Get the current state of this setting with:

.. code-block:: ruby

   >> Setting.get('ui_user_organization_selector_with_email')

Change font settings for outgoing HTML mails
--------------------------------------------

.. note::

   Some clients (like Outlook) might fallback to other settings while it might
   work for other clients.

The below setting allows you to adjust Zammad's email font setting.
This setting does not require a service restart.

.. code-block:: ruby

   >> Setting.set("html_email_css_font", "font-family:'Helvetica Neue', Helvetica, Arial, Geneva, sans-serif; font-size: 12px;")

If you want to check the current setting, you can simply run the below code.

.. code-block:: ruby

   >> Setting.get('html_email_css_font')
