Install with Vagrant
********************

Vagrant is a tool for building complete development environments. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases development/production parity, and makes the "works on my machine" excuse a relic of the past.

Be aware that Vagrant is meant for developers and therefore uses our unstable packages from the "develop" branch on GitHub.

Let’s begin using Vagrant!
First be sure that a Vagrant provider is installed. You can use "Virtual Box" from https://www.virtualbox.org .

Clone the Vagrant file
======================

::

 git clone git@github.com:zammad/zammad-vagrant.git
 cd zammad-vagrant


Run Vagrant
===========


For stable branch package
-------------------------

::

 PACKAGER_REPO=stable vagrant up --provision

For develop branch package
--------------------------

::

 vagrant up --provision



That’s it! You’re now running Zammad in a Vagrant environment.

Go to http://localhost:8080 and you'll see:
===========================================

*  "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.


SSH into the machine
====================

After "vagrant up"

::

 vagrant ssh


After this you can switch to root user via:

::

 sudo -i


Problems starting the VM?
=========================

If you get errors like:

::

 Bringing machine 'default' up with 'virtualbox' provider...
 ==> default: Checking if box 'centos/7' is up to date...
 ==> default: VirtualBox VM is already running.


Use the following commands to fix it:

::

 vboxmanage controlvm Zammad poweroff


