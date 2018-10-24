Email
*****

Basic
=====

If you want to fetch emails via POP3 or IMAP, you have to create a mail channel in system settings "#channels/email".

**If you're using an Office365 Mailbox, please ensure that it's a real usermailbox and not a shared mailbox!**

Just follow these steps:

* Click "New"
* Enter "Organization & Department Name"
* Enter "Email address"
* Enter "Password"
* Enter "Destination Group"

Zammad tries to detect the POP3, IMAP and SMTP server settings automatically.
This should work most of the time. If it doesn't, use the "Experts" button to configure it by yourself.

Advanced
========

.. toctree::
   :maxdepth: 1

   channel-email/fetchmail
   channel-email/sendmail
