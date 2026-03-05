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

Detailled Steps
---------------

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
    
            $ sudo yum upgrade --exclude zammad

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

Add New Repository
""""""""""""""""""

In case the repository key has changed, add the new one. Otherwise skip this
step and go on by changing the repository configuration to point to the new
package version fitting your operating system. Depending on where your
operating system expects the repository configuration, you might
need to move or recreate the repository configuration file.

.. include:: /install/package.rst
   :start-after: .. repo-start:
   :end-before: .. repo-end:

Remove Old Repository
"""""""""""""""""""""

This is only needed in case you added a **new** repository instead adjusting
the old. Remove the old repository configuration file or disable/delete the
old repository in your package manager.

Update Zammad
^^^^^^^^^^^^^

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
   
         $ sudo yum upgrade zammad

.. note::

   If there is a new Zammad version available and you updated to it, check the
   `release notes <https://zammad.com/en/product/releases>`_ for any required
   additional steps.

Start Zammad
^^^^^^^^^^^^

.. code-block:: bash

   sudo systemctl start zammad
