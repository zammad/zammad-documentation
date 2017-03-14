Console
*******

To open the rails console on the shell you have enter the following commands.

1.) Start Zammads Rails console
=========================================================

If you used a Zammad DEB or RPM package:
----------------------------------------

::

 shell> zammad run rails c

If you compiled Zammad by yoursef just use:
-------------------------------------------

::

 shell> rails c


2.) Delete all tickets
======================

::

 rails> Ticket.destroy_all
