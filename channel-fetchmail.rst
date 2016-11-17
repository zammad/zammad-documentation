Pipe (Fetchmail)
****************

Maybe you want to add mails via Fetchmail & Procmail.

To get this work you need to pipe your mail to rails.

On the Commandline
==================

::

 su - zammad
 cd /opt/zammad
 cat test/fixtures/mail1.box | rails r 'Channel::Driver::MailStdin.new(trusted: true)'


Fetchmail
=========

Create .ftechmail.rc
--------------------

::

 su - zammad
 cd ~
 touch .fetchmailrc


vi .fetchmailrc
---------------

::

 #
 # zammad fetchmail config
 #
 poll your.mail.server protocol POP3 user USERNAME pass PASSWORD mda /usr/bin/procmail is zammad here



Procmail
========

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

 :0 :
 | rails r 'Channel::Driver::MailStdin.new(trusted: true)'



Supported mail header for presorting
====================================

Ticket-Attributes
-----------------

For ticket creation use "X-Zammad-Ticket-Attribute: some value", if you want to change
ticket attributes on follow up, use "X-Zammad-Ticket-FollowUp-Attribute: some value".


X-Zammad-Ticket-Priority
++++++++++++++++++++++++

* Set priority of ticket (for whole list check your database).
* Example: X-Zammad-Ticket-Priority: (1 low|2 normal|3 high)


X-Zammad-Ticket-Group
+++++++++++++++++++++

* Presort of group (highest sort priority).
* Example: X-Zammad-Ticket-Group: [one system group]


X-Zammad-Ticket-Owner
+++++++++++++++++++++

* Assign ticket to agent.
* Example: X-Zammad-Ticket-Owner: [login of agent]


X-Zammad-Ticket-State
+++++++++++++++++++++

* Set state of ticket (for whole list check your database)! Be careful!
* Example: X-Zammad-Ticket-State: (new|open|...)

X-Zammad-Customer-Email
+++++++++++++++++++++++

* Set customer via explicit email.
* Example: X-Zammad-Customer-Email: [email address]


X-Zammad-Customer-Login
+++++++++++++++++++++++

* Set customer via explicit login.
* Example: X-Zammad-Customer-Login: [login]



Article-Attributes
------------------

Every time if an article is created (new ticket or/and follow up) you can use
"X-Zammad-Article-Attribute: some value".


X-Zammad-Article-Sender
+++++++++++++++++++++++

* Info about the sender.
* Example: X-Zammad-Article-Sender: (Agent|System|Customer)


X-Zammad-Article-Type
+++++++++++++++++++++

* Article type (for whole list check your database).
* Example: X-Zammad-Article-Type: (email|phone|fax|sms|webrequest|note|twitter status|direct-message|facebook|...)


X-Zammad-Article-Visibility
+++++++++++++++++++++++++++

* Article visibility.
* Example: X-Zammad-Article-Visibility: (internal|external)

Ignore Header
+++++++++++++

* If you want to ignore whole email, just set the "X-Zammad-Ignore" header.
* Example: X-Zammad-Ignore: [yes|true]


