Install with Vagrant
********************

Vagrant is a tool for building complete development environments. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases development/production parity, and makes the "works on my machine" excuse a relic of the past.

Let’s begin using Vagrant!
First be sure that a Vagrant provider is installed. You can use "Virtual Box" from https://www.virtualbox.org .

Clone the Vagrant file
======================

::

 git clone git@github.com:zammad/zammad-vagrant.git

Run Vagrant
===========

::

 cd zammad-vagrant
 vagrant up

That’s it! You’re now running Zammad in a Vagrant environment.

Go to http://localhost:3001 and you'll see:
-------------------------------------------

*  "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.
