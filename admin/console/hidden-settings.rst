Advanced Customization Settings
===============================

On this page you can find some settings that you won't find within the Zammad
UI. Those settings might come in handy as it can change Zammad's behavior.

.. include:: /admin/console/missing-commands-ask-community.include.rst

Send All Outgoing Emails to a BCC-Mailbox
------------------------------------------

This option allows you to send all outgoing emails (not notifications) to a
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

   - ``phone-in`` (incoming call, **default**),
   - ``phone-out`` (outgoing call) and
   - ``email-out``  (Sending an email out).

.. code-block:: irb

   >> Setting.set('ui_ticket_create_default_type', 'email-out')

To check what setting is set currently, simply run:

.. code-block:: irb

   >> Setting.get('ui_ticket_create_default_type')

Show a Note During Article Creation
-----------------------------------

If you need to give your agents a note or warning with important information
during the article creation, you can create such a static note for different
article types. Be aware that there are two settings: one for ticket creation and
the other for article creation in an existing ticket. Adjust the commands below
to use it for the desired article types and replace the text with yours. In case
you don't want a warning for all article types, simply omit these types.

.. figure:: /images/console/article-creation-warning.png
   :alt: Screenshot shows the article editor with a warning above.
   :align: center

Ticket creation
   .. code-block:: irb

      >> Setting.set('ui_ticket_create_notes', {
            "phone-in"  => "You're about to note an incoming phone call.",
            "phone-out" => "You're about to note an outgoing phone call.",
            "email-out" => "You're going to send out an email."
         })

Append article in existing tickets
   .. code-block:: irb

      >> Setting.set('ui_ticket_add_article_hint', {
            "note-internal"  => "You are writing an |internal note|, only people of your organization will see it.",
            "note-public"    => "You are writing a |public note|.",
            "phone-internal" => "You are writing an |internal phone note|, only people of your organization will see it.",
            "phone-public"   => "You are writing a |public phone note|.",
            "email-internal" => "You are writing an |internal email|, only people of your organization will see it.",
            "email-public"   => "You are writing a |public email|."
         })

Check what's currently set
   .. code-block:: irb

      >> Setting.get('ui_ticket_create_notes')

   .. code-block:: irb

      >> Setting.get('ui_ticket_add_article_hint')

Markup options
   To apply text formatting, use the following markup:

   - ``||italic||``
   - ``|bold|``
   - ``_underline_``
   - ``//strikethrough//``
   - ``§key§`` (renders a keyboard key like :kbd:`key`)
   - ``¶`` (newline)
   - ``[link text](/example.com)``

Show Email Address of Customer on Customer Selection (Ticket Creation)
----------------------------------------------------------------------

By default Zammad will not display the email addresses of customers.
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
