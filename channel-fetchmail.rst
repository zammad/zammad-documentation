Pipe (Fetchmail)
****************

Maybe you want to add emails via Fetchmail and Procmail to Zammad.

To get this to work you need to pipe your emails to rails.

Command line
==================

::

 su - zammad
 cd /opt/zammad
 cat test/fixtures/mail1.box | rails r 'Channel::Driver::MailStdin.new(trusted: true)'


Fetchmail
=========

Create .fetchmailrc
--------------------

::

 su - zammad
 cd ~
 touch .fetchmailrc
 chmod 0600 .fetchmailrc


vi .fetchmailrc
---------------

 ::

 #
 # zammad fetchmail config
 #
 poll your.mail.server protocol POP3 user USERNAME pass PASSWORD mda "rails r 'Channel::Driver::MailStdin.new(trusted: true)'"


Thats it. Mails now will be directly piped into Zammad.



Using Procmail for advanced features like presorting
=====================================================

If you want to do some more with your emails, like presorting to a Zammad group or filtering spam, you can use Procmail.

Fetchmail config looks slightly different.

vi .fetchmailrc
---------------

::

 #
 # zammad fetchmail config
 #
 poll your.mail.server protocol POP3 user USERNAME pass PASSWORD mda /usr/bin/procmail is zammad here


Create .procmailrc
------------------

::

 su - zammad
 cd ~
 touch .procmailrc

vi .procmailrc
--------------

::

 # --
 # Pipe all emails into Zammad
 # --
 PATH=/opt/zammad/bin:/opt/zammad/vendor/bundle/bin:/sbin:/bin:/usr/sbin:/usr/bin:
 SYS_HOME="/home/zammad"
 RAILS_ENV=production
 GEM_PATH=/opt/zammad/vendor/bundle/ruby/2.3.0/
 LOGFILE="$SYS_HOME/procmail.log"
 #VERBOSE="on"

 :0 :
 | rails r 'Channel::Driver::MailStdin.new(trusted: true)'



Supported email headers for presorting
======================================

Ticket attributes
-----------------

For ticket creation use "X-Zammad-Ticket-Attribute: some value". If you want to change
ticket attributes on follow-up, use "X-Zammad-Ticket-FollowUp-Attribute: some value".


X-Zammad-Ticket-Priority
++++++++++++++++++++++++

* Sets priority of ticket (for available priorities check Zammad's database).
* Example: X-Zammad-Ticket-Priority: (1 low|2 normal|3 high)


X-Zammad-Ticket-Group
+++++++++++++++++++++

* Presorts by group (highest sort priority).
* Example: X-Zammad-Ticket-Group: [one system group]


X-Zammad-Ticket-Owner
+++++++++++++++++++++

* Assigns ticket to agent.
* Example: X-Zammad-Ticket-Owner: [login of agent]


X-Zammad-Ticket-State
+++++++++++++++++++++

* Sets state of ticket (for available states check Zammad's database)! Be careful!
* Example: X-Zammad-Ticket-State: (new|open|...)

X-Zammad-Customer-Email
+++++++++++++++++++++++

* Sets customer via explicit email address.
* Example: X-Zammad-Customer-Email: [email address]


X-Zammad-Customer-Login
+++++++++++++++++++++++

* Sets customer via explicit login.
* Example: X-Zammad-Customer-Login: [login]



Article attributes
------------------

Everytime an article is being created (new ticket or/and follow up) you can use
"X-Zammad-Article-Attribute: some value".


X-Zammad-Article-Sender
+++++++++++++++++++++++

* Info about the sender.
* Example: X-Zammad-Article-Sender: (Agent|System|Customer)


X-Zammad-Article-Type
+++++++++++++++++++++

* Article type (for available types check Zammad's database).
* Example: X-Zammad-Article-Type: (email|phone|fax|sms|webrequest|note|twitter status|direct-message|facebook|...)


X-Zammad-Article-Visibility
+++++++++++++++++++++++++++

* Article visibility.
* Example: X-Zammad-Article-Visibility: (internal|external)

Ignore Header
+++++++++++++

* If you want to ignore an email, just set the "X-Zammad-Ignore" header.
* Example: X-Zammad-Ignore: [yes|true]
