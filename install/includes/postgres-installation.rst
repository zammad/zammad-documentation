.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: console

         $ sudo apt update

      .. code-block:: console

         $ sudo apt install postgresql postgresql-contrib

      .. code-block:: console

         $ sudo systemctl start postgresql

      .. code-block:: console

         $ sudo systemctl enable postgresql

   .. tab:: CentOS

      .. code-block:: console

         $ sudo yum install postgresql-server postgresql-contrib

      .. code-block:: console

         $ sudo postgresql-setup initdb

      .. code-block:: console

         $ sudo systemctl start postgresql


      .. code-block:: console

         $ sudo systemctl enable postgresql

   .. tab:: OpenSUSE / SLES

      .. code-block:: console

         $ sudo zypper refresh

      .. code-block:: console

         $ sudo zypper install postgresql postgresql-server postgresql-contrib

      openSuSE 15 also requires:

      .. code-block:: console

         $ sudo zypper install postgresql-server-devel

      .. code-block:: console

         $ sudo systemctl start postgresql

      .. code-block:: console

         $ sudo systemctl enable postgresql
