Setup Elasticsearch
-------------------

Elasticsearch is a dependency of Zammad and needs to be provided before installing Zammad.
Please take a look at the following page: :doc:`/install/elasticsearch`.

Additional software dependencies
--------------------------------

In addition to already mentioned :ref:`Package dependencies <package_dependencies>`, 
some operating systems may require additional packages if not already installed.

.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh
      
         $ apt install wget apt-transport-https gnupg

   .. tab:: CentOS

      .. code-block:: sh

         $ yum install wget epel-release


Ensure correct locale
---------------------

For Zammad to function correctly, your system has to use the correct locales.

.. tabs::

   .. tab:: Ubuntu / Debian

      List your current locale settings.

      .. code-block:: sh

         $ locale |grep "LANG="

      If above does not return ``<lang_code>.UTF-8`` you can correct this issue as follows.

      .. code-block:: sh

         $ sudo apt-get install locales
         $ sudo locale-gen en_US.UTF-8
         $ sudo echo "LANG=en_US.UTF-8" > /etc/default/locale

   .. tab:: CentOS

      List your current locale settings.

      .. code-block:: sh

         $ locale |grep "LANG="

      If above does not return ``<lang_code>.utf8`` you can correct this issue as follows.

      .. code-block:: sh

         $ localectl set-locale LANG=en_US.utf8

   .. tab:: OpenSUSE / SLES

      List your current locale settings.

      .. code-block:: sh

         $ localectl status |grep "LC_CTYPE"

      If above does not return ``<lang_code>.UTF-8`` you can correct this issue as follows.

      .. code-block:: sh

         $ localectl set-locale LC_CTYPE=en_US.UTF-8

      .. hint:: By default OpenSUSE uses ``POSIX`` as ``LANG`` value for the root user. Learn more about this 
         within the `OpenSUSE documentation 
         <https://doc.opensuse.org/documentation/leap/startup/html/book-opensuse-startup/cha-yast-lang.html#pro-yast-lang-additional>`_.

         This does not affect other users and thus can be ignored.