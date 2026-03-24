Host Upgrade
============

.. include:: includes/hosted-services.rst

If you installed Zammad via :doc:`package manager <package>` and need to
upgrade your host operating system, make sure to read the steps below. Some
additional steps are required compared to just updating Zammad itself.

.. warning:: Always make sure to have a
    :doc:`backup </appendix/backup-and-restore/index>` of your data before
    performing an upgrade.

The following operating systems are supported:

.. include:: /prerequisites/software.rst
   :start-after: .. supported-os-table-start:
   :end-before: .. supported-os-table-end:

General
-------

The general steps, no matter which operating system you are using, are:

#. Stop Zammad
#. Disable updates for Zammad
#. Perform host upgrade
#. Reboot host
#. Adjust package repository
#. Update Zammad
#. Start Zammad

Detailed Steps
--------------

Stop Zammad
^^^^^^^^^^^

.. code-block:: bash

   sudo systemctl stop zammad

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
^^^^^^^^^^^^^^^^^^^^^^^^^

Remove Old Repository
"""""""""""""""""""""

Remove the old repository configuration file or disable/delete the old
repository in your package manager.

.. tabs::

      .. group-tab:: Ubuntu

         Ubuntu 22.04
            .. code-block:: console

                  $ sudo rm /etc/apt/sources.list.d/zammad.list

         Ubuntu 20.04
            .. code-block:: console

                  $ sudo rm /etc/apt/sources.list.d/zammad.sources

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
""""""""""""""""""

If the repository key is different for the old and new version your distribution
or your distribution expects it in a different location, add the new one.
Otherwise, you can add the new repository configuration directly.

.. include:: /install/package.rst
   :start-after: .. repo-start:
   :end-before: .. repo-end:

Update Zammad
^^^^^^^^^^^^^

.. hint::

   If there is a new Zammad version available and you want to update to it,
   check the `release notes <https://zammad.com/en/product/releases>`_ for any
   required additional steps.

Re-enable updates for Zammad and update Zammad to the latest version available
for your operating system.

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
^^^^^^^^^^^^

.. code-block:: bash

   sudo systemctl start zammad
