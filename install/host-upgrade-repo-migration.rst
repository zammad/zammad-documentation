Host Upgrade and Repository Migration
=====================================

.. include:: includes/hosted-services.rst

This page covers the required steps for a host upgrade and to switch to Zammad's
new package repositories. If you just want to update Zammad itself, please refer
to :doc:`update`. If you just want to switch to the new repositories without
upgrading your host system, skip the host upgrade steps after stopping Zammad.

Starting with Zammad 7, packages are being built using a new toolchain and
hosted under another URL. The packages are being built via old toolchain as well
(except for Debian 13) for some time, but we encourage you to switch to the new
repositories in a timely manner. This means you need to add a new repository key
and change your repository configuration.

.. warning:: Always make sure to have a
    :doc:`backup </appendix/backup-and-restore/index>` of your data before
    performing an upgrade.

The following operating systems are supported:

.. include:: /prerequisites/software.rst
   :start-after: .. supported-os-table-start:
   :end-before: .. supported-os-table-end:

Stop Zammad
-----------

.. code-block:: console

   $ sudo systemctl stop zammad

Host Upgrade Steps
------------------

Disable Updates for Zammad
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tabs::

    .. group-tab:: Ubuntu

        .. code-block:: console

            $ sudo apt-mark hold zammad

    .. group-tab:: Debian

        .. code-block:: console

            $ sudo apt-mark hold zammad

    .. group-tab:: OpenSUSE / SLES

        .. code-block:: console

            $ sudo zypper addlock zammad

    .. group-tab:: CentOS / RHEL

        .. code-block:: console

            $ sudo dnf upgrade --exclude zammad

Perform Host Upgrade
^^^^^^^^^^^^^^^^^^^^

Perform the host upgrade according to the documentation of your operating
system. Because this is an advanced task, we don't provide detailed steps here.
After upgrading your operating system, proceed with the next steps.

Reboot Host
^^^^^^^^^^^

In case you did not reboot your system after the upgrade, make sure to reboot
your system now. Afterwards, check if everything is running as expected.
In case Zammad starts automatically, stop it again before proceeding with the
next steps.

Adjust Package Repository
-------------------------

Remove Old Repository
^^^^^^^^^^^^^^^^^^^^^

Remove the old repository configuration file or disable/delete the old
repository in your package manager.

.. tabs::

      .. group-tab:: Ubuntu

         Ubuntu 20.04
            .. code-block:: console

                  $ sudo rm /etc/apt/sources.list.d/zammad.sources

         Ubuntu 22.04
            .. code-block:: console

                  $ sudo rm /etc/apt/sources.list.d/zammad.list

      .. group-tab:: Debian

            .. code-block:: console

                  $ sudo rm /etc/apt/sources.list.d/zammad.list

      .. group-tab:: OpenSUSE / SLES

         .. code-block:: console

               $ sudo rm /etc/zypp/repos.d/zammad.repo

      .. group-tab:: CentOS / RHEL

         .. code-block:: console

               $ sudo rm /etc/yum.repos.d/zammad.repo

Add New Repository
^^^^^^^^^^^^^^^^^^

.. include:: /install/package.rst
   :start-after: .. repo-start:
   :end-before: .. repo-end:

Update Zammad
-------------

.. hint::

   If there is a new Zammad version available and you want to update to it,
   check the `release notes <https://zammad.com/en/product/releases>`_ for any
   required additional steps.

Re-enable updates for Zammad (in case you disabled it) and update Zammad to the
latest version available for your operating system.

.. tabs::

   .. group-tab:: Ubuntu

      Update package index:
         .. code-block:: console

            $ sudo apt update

      Re-enable updates for Zammad:
         .. code-block:: console

            $ sudo apt-mark unhold zammad

      Update Zammad:
         .. code-block:: console

            $ sudo apt upgrade zammad

   .. group-tab:: Debian

      Update package index:
         .. code-block:: console

            $ sudo apt update

      Re-enable updates for Zammad:
         .. code-block:: console

            $ sudo apt-mark unhold zammad

      Update Zammad:
         .. code-block:: console

            $ sudo apt upgrade zammad

   .. group-tab:: OpenSUSE / SLES

      Update package index:
         .. code-block:: console

            $ sudo zypper refresh

      Re-enable updates for Zammad:
         .. code-block:: console

            $ sudo zypper removelock zammad

      Update Zammad:
         .. code-block:: console

            $ sudo zypper update zammad

   .. group-tab:: CentOS / RHEL

      .. code-block:: console

         $ sudo dnf upgrade zammad

Start Zammad
------------

.. code-block:: console

   $ sudo systemctl start zammad
