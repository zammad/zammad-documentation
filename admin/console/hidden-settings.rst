Advanced Customization Settings
===============================

On this page you can find some settings that you won't find within the Zammad
UI. Those settings might come in handy as it can change Zammad's behavior.

.. include:: /admin/console/missing-commands-ask-community.include.rst

Send All Outgoing E-Mails to a BCC-Mailbox
------------------------------------------

This option allows you to send all outgoing E-Mails (not notifications) to a
specific mailbox. Please note that this shouldn't be a mailbox you're importing
already! This will apply to all groups and is a global setting.

.. code-block:: irb

   >> Setting.set('system_bcc', 'alias@domain.tld')

You can easily check the current BCC-Setting by running the following:

.. code-block:: irb

   >> Setting.get('system_bcc')

Activate Counter on Grouped Overviews
-------------------------------------

This is a hidden setting which you can only set via console.
This will globally enable a ticket number value in each heading for grouped
elements.

Enable counter on grouped overviews:

.. code-block:: irb

   >> Setting.set('ui_table_group_by_show_count', true)

Disable counter on grouped overviews:

.. code-block:: irb

   >> Setting.set('ui_table_group_by_show_count', false)

Get current setting (``nil`` is false):

.. code-block:: irb

   >> Setting.get('ui_table_group_by_show_count')

.. image:: /images/console/ui_table_group_by_show_count-example.png

Default Ticket Type on Creation
-------------------------------

Zammad allows you to define the default article type upon ticket creation.
By default this will be a incoming phone call.

You can choose between

   * ``phone-in`` (incoming call, **default**),
   * ``phone-out`` (outgoing call) and
   * ``email-out``  (Sending an E-Mail out).

.. code-block:: irb

   >> Setting.set('ui_ticket_create_default_type', 'email-out')

To check what setting is set currently, simply run:

.. code-block:: irb

   >> Setting.get('ui_ticket_create_default_type')

Adding a Warning to the Ticket Creation Process
-----------------------------------------------

If in case you need to give your agent a note or warning during ticket creation,
you can do so with the below command.

You can use three different warnings for

   * Incoming Calls ``:"phone-in"=>""``,
   * Outgoing Calls ``:"phone-out"=>""`` and
   * Outgoing E-Mails ``:"email-out"=>""``.

.. code-block:: irb

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

.. code-block:: irb

   >> Setting.get('ui_ticket_create_notes')

Sample of the above setting:

.. image:: /images/console/ui_ticket_create_notes.gif

Adding a Warning to the Article Reply Process
---------------------------------------------

In case you need to give your agent a warning during the ticket article reply,
you can do that with the command below.

You can provide different warnings for different channels and article visibility

   * Internal Notes ``:"note-internal"=>""``,
   * Public Notes ``:"note-public"=>""``,
   * Internal Calls ``:"phone-internal"=>""``,
   * Public Calls ``:"phone-public"=>""``,
   * Internal Emails ``:"email-internal"=>""`` and
   * Public Emails ``:"email-public"=>""``.

.. code-block:: irb

   >> Setting.set('ui_ticket_add_article_hint', {
         :"note-internal"=>"You are writing an |internal note|, only people of your organization will see it.",
         :"note-public"=>"You are writing a |public note|.",
         :"phone-internal" => "You are writing an |internal phone note|, only people of your organization will see it.",
         :"phone-public"=>"You are writing a |public phone note|.",
         :"email-internal" => "You are writing an |internal Email|, only people of your organization will see it.",
         :"email-public"=>"You are writing a |public Email|."
      })

.. note::

   You can use example sub-settings above independently, if you e.g. don't need
   a warning on internal calls, simply leave out ``:"phone-internal"=>""`` out
   of the setting. The setting itself is in a form of an array ( ``{}`` ).


To check what's currently set, you can use:

.. code-block:: irb

   >> Setting.get('ui_ticket_add_article_hint')

Sample of the above setting:

.. image:: /images/console/ui_ticket_add_article_hint-example.gif

Show Email Address of Customer on Customer Selection (Ticket Creation)
----------------------------------------------------------------------

By default Zammad will not display the E-Mail-Addresses of customers.
The below option allows you to change this behavior.

.. code-block:: irb

   >> Setting.set('ui_user_organization_selector_with_email', true)

Get the current state of this setting with:

.. code-block:: irb

   >> Setting.get('ui_user_organization_selector_with_email')

Change Font Settings for Outgoing HTML Emails
---------------------------------------------

.. note::

   Some clients (like Outlook) might fallback to other settings while it might
   work for other clients.

The below setting allows you to adjust Zammad's email font setting.
This setting does not require a service restart.

.. code-block:: irb

   >> Setting.set("html_email_css_font", "font-family:'Helvetica Neue', Helvetica, Arial, Geneva, sans-serif; font-size: 12px;")

If you want to check the current setting, you can simply run the below code.

.. code-block:: irb

   >> Setting.get('html_email_css_font')

Highlight Customer's Open Ticket Count
--------------------------------------

This option enhances the selected customer's open tickets count. It highlights
the count in different colors if they hit a threshold.

.. code-block:: irb

   >> Setting.set('ui_sidebar_open_ticket_indicator_colored', true)

Sample of the above setting:

.. image:: /images/console/ui_sidebar_open_ticket_indicator_colored.png

Above settings has specific thresholds as follows. You cannot adjust these
thresholds.

   .. list-table:: Situational threshold list for open ticket indication
      :widths: 30, 20, 20, 20
      :header-rows: 1

      * - Situation / View
        - no indication
        - warning (orange)
        - danger (red)
      * - **Ticket Zoom**
        - < 2
        - 2
        - >= 3
      * - **New Ticket dialog**
        - 0
        - 1
        - >= 2

Activate Attachment Tab in Sidebar
----------------------------------

This option activates a new tab in the right sidebar in the ticket view
which shows all attachments of the currently viewed ticket.

.. code-block:: irb

   >> Setting.set('ui_ticket_zoom_sidebar_article_attachments', 'true')

Sample of the above setting:

.. figure:: /images/console/attachment-tab.png
   :align: center
   :scale: 80%

Time Period for Showing Customer Profile on New Calls
-----------------------------------------------------

Zammad shows the customer profile dialog when a call of this customer is
incoming and there is an existing ticket of this customer in this time period.
The default time period is 30 days. If there is no ticket in this period, the
customer dialog is not shown automatically.

.. code-block:: irb

   >> Setting.set('cti_customer_last_activity', '90') # set the time period to 90 days
