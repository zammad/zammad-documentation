Host Upgrade and Repository Migration
=====================================

.. include:: includes/hosted-services.rst

This page covers the required steps for a host upgrade and to switch to Zammad's
new package repositories. If you just want to update Zammad itself, please refer
to :doc:`update`. To just switch to the new repositories without a host upgrade,
skip the host upgrade steps.

Zammad packages are being built with a new toolchain and are hosted under
another URL. The old toolchain is no longer in use, so the packages in the old
repositories no longer receive updates. This means you need to add a new
repository key and change your repository configuration.

The repository channel in the URL selects the release line: ``stable`` contains
the current stable release, while release lines that are out of support have a
channel of their own, for example ``stable-6.5``.

.. warning:: Always make sure to have a
    :doc:`backup </appendix/backup-and-restore/index>` of your data before
    performing an upgrade.

.. TODO: remove this warning box with the next Zammad release (added for the
   6.5.5 emergency release).

.. warning::

   Zammad 6.5.5 is an emergency release that fixes a security issue. Zammad 6.5
   is out of support and its packages are only available in the ``stable-6.5``
   channel. See `Update an Out-of-Support Release`_ below for the steps.

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

Remove Old Repository Key
^^^^^^^^^^^^^^^^^^^^^^^^^

Remove the old repository key from your system. Depending on your operating
system and version, the location or method differs.

.. tabs::

   .. group-tab:: Ubuntu

      .. code-block:: console

         $ sudo rm /etc/apt/keyrings/pkgr-zammad.gpg

   .. group-tab:: Debian

      .. code-block:: console

         $ sudo rm /etc/apt/trusted.gpg.d/pkgr-zammad.gpg

   .. group-tab:: OpenSUSE / SLES

      List the keys of your system:

      .. code-block:: console

         $ rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'

      Delete the key(s) related to Zammad (and only those!), replace
      ``<key-name>`` with the actual key ID:

      .. code-block:: console

         $ sudo rpm -e <key-name>

   .. group-tab:: CentOS / RHEL

      List the keys of your system:

      .. code-block:: console

         $ rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'

      Delete the key(s) related to Zammad (and only those!), replace
      ``<key-name>`` with the actual key ID:

      .. code-block:: console

         $ sudo rpm -e <key-name>

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

.. TODO: remove this section with the next Zammad release (added for the 6.5.5
   emergency release).

Update an Out-of-Support Release
--------------------------------

Zammad 6.5.5 is an emergency release that fixes a security issue. Zammad 6.5
has been out of support for some time and no longer receives security updates,
so updating to the current stable release is the recommended action. Follow the
steps below only if you cannot update to a supported release right now.

Zammad builds 6.5.5 packages for Ubuntu 20.04, 22.04 and 24.04, Debian 11 and
12, CentOS/RHEL 8 and 9, and OpenSUSE Leap/SLES 15.

Add the 6.5 Repository
^^^^^^^^^^^^^^^^^^^^^^

Remove the old repository and its key first, as described in Adjust Package
Repository above. Otherwise your package manager keeps reading the old
repository, which offers packages of a newer release line.

Add the new repository with the ``stable-6.5`` channel:

.. tabs::

   .. group-tab:: Ubuntu

      Add repository key:

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/deb/zammad/zammad/gpg-key.gpg" \
             -o /usr/share/keyrings/zammad.gpg && sudo chmod 644 /usr/share/keyrings/zammad.gpg

      Add repository (Ubuntu 20.04):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/ubuntu/20.04.list" \
             -o /etc/apt/sources.list.d/zammad.list

      Add repository (Ubuntu 22.04):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/ubuntu/22.04.list" \
             -o /etc/apt/sources.list.d/zammad.list

      Add repository (Ubuntu 24.04):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/ubuntu/24.04.list" \
             -o /etc/apt/sources.list.d/zammad.list

   .. group-tab:: Debian

      Add repository key:

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/deb/zammad/zammad/gpg-key.gpg" \
             -o /usr/share/keyrings/zammad.gpg && sudo chmod 644 /usr/share/keyrings/zammad.gpg

      Add repository (Debian 11):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/debian/11.list" \
             -o /etc/apt/sources.list.d/zammad.list

      Add repository (Debian 12):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/debian/12.list" \
             -o /etc/apt/sources.list.d/zammad.list

   .. group-tab:: OpenSUSE / SLES

      Add repository (OpenSUSE/SLES 15):

      .. code-block:: console

         $ sudo curl -o /etc/zypp/repos.d/zammad.repo \
             "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/sles/15.repo"

   .. group-tab:: CentOS / RHEL

      Add repository key:

      .. code-block:: console

         $ sudo rpm --import https://go.packager.io/srv/rpm/zammad/zammad/gpg-key.asc

      Add repository (CentOS/RHEL 8):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/el/8.repo" \
             -o /etc/yum.repos.d/zammad.repo

      Add repository (CentOS/RHEL 9):

      .. code-block:: console

         $ sudo curl -fsSL "https://go.packager.io/srv/zammad/zammad/stable-6.5/installer/el/9.repo" \
             -o /etc/yum.repos.d/zammad.repo

Update Zammad to 6.5.5
^^^^^^^^^^^^^^^^^^^^^^

Stop Zammad:

.. code-block:: console

   $ sudo systemctl stop zammad

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

Start Zammad:

.. code-block:: console

   $ sudo systemctl start zammad
