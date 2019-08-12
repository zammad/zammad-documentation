Issues you might encounter
==========================

Below we have gathered information to problems that might occur in combination with Univention.

Zammad can't communicate with external systems
----------------------------------------------

In rare cases (sometimes even right after installation), Zammad won't be able to communicate with e.g. external 
e-mail servers. Simply restart the Zammad app in the App Center module in the UCS management system and it should be enough to get it back working.


Zammad communicates a wrong URL within the notifications
--------------------------------------------------------

This issue rises because of how the "Getting Started"-Wizard in Zammad works.
Even though the wizard reports the correct FQDN-Setting (and we manually set it), it will overwrite the setting after sanitizing what it recognized.

This is an application level issue and a subject to change - you can find more information about this in `Issue 2651 <https://github.com/zammad/zammad/issues/2651>`_.
To solve this, just go into the Univention App-Settings (for Zammad-App) and apply the settings **after** finishing the wizard.


Customers can't click on the "Knowledge base"-URL within the customer portal
---------------------------------------------------------------------------

This currently can't be fixed, as Zammad is available via one Port only.
The issue is described within `Issue 2628 <https://github.com/zammad/zammad/issues/2628>`_ and a subject to fix.

