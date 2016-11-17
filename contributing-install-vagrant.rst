Install with Vagrant
********************

Vagrant is a tool for building complete development environments. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases development/production parity, and makes the "works on my machine" excuse a relic of the past.

Be aware that Vagrant is meaned for developers and therefore uses our unstable packages from the "develop" branch on GitHub.

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
===========================================

*  "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.


SSH into the machine
====================

After "vagrant up"

::

 vagrant ssh


Problems to start the VM?
=========================

Iy you get errors like:

::

 A VirtualBox machine with the name 'Zammad' already exists.
 Please use another name or delete the machine with the existing
 name, and try again.


Use the following commands to fix it:

::

 vboxmanage controlvm Zammad poweroff
 vboxmanage unregistervm Zammad
 
