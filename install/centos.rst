Install on CentOS via RPM
*************************

.. note:: Currently we support RHEL7 & CentOS7.

Prerequisites
=============

.. include:: /install/includes/prerequisites.rst

Add Repository and install Zammad
=================================

.. include:: /install/includes/repo_centos.rst

Now you can install the Zammad package.

.. code-block:: sh

   $ sudo yum -y install zammad

SELinux & Firewalld
-------------------

On CentOS SELinux & Firewalld are possibly enabled.
To get everything work you have to use the following commands:

.. code-block:: sh

   $ setsebool httpd_can_network_connect on -P
   $ firewall-cmd --zone=public --add-service=http --permanent
   $ firewall-cmd --zone=public --add-service=https --permanent
   $ firewall-cmd --reload

.. include:: /install/includes/centos-public-folder.rst

.. include:: /install/includes/adjust-webserver-configuration.rst

.. include:: /install/includes/manage-services.rst