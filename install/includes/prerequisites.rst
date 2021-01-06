Setup Elasticsearch
-------------------

Elasticsearch is a dependency of Zammad and needs to be provided before 
installing Zammad. Please take a look at the following page: 
:doc:`/install/elasticsearch`.

Ensure correct locale
---------------------

For Zammad to function correctly, your system has to use the correct locales.

.. tabs::

   .. tab:: Ubuntu / Debian

      List your current locale settings.

      .. code-block:: sh

         $ locale |grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ sudo apt-get install locales
         $ sudo locale-gen en_US.UTF-8
         $ sudo echo "LANG=en_US.UTF-8" > /etc/default/locale

   .. tab:: CentOS

      List your current locale settings.

      .. code-block:: sh

         $ locale |grep "LANG="

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ localectl set-locale LANG=en_US.utf8

   .. tab:: OpenSUSE / SLES

      List your current locale settings.

      .. code-block:: sh

         $ localectl status |grep "LC_CTYPE"

      .. include:: /install/includes/include-utf-8-clause.rst

      .. code-block:: sh

         $ localectl set-locale LC_CTYPE=en_US.UTF-8

      .. hint:: 

         By default OpenSUSE uses ``POSIX`` as ``LANG`` value for the root 
         user. Learn more about this within the `OpenSUSE documentation 
         <https://doc.opensuse.org/documentation/leap/startup/html/book-opensuse-startup/cha-yast-lang.html#pro-yast-lang-additional>`_.

         This does not affect other users and thus can be ignored.
