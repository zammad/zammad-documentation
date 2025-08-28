.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: console

         $ apt update
         $ apt install postgresql postgresql-contrib
         $ systemctl start postgresql
         $ systemctl enable postgresql

   .. tab:: CentOS

      .. code-block:: console

         $ yum install postgresql-server postgresql-contrib
         $ postgresql-setup initdb
         $ systemctl start postgresql
         $ systemctl enable postgresql

   .. tab:: OpenSUSE / SLES

      .. code-block:: console

         $ zypper refresh
         $ zypper install postgresql postgresql-server postgresql-contrib
         # openSuSE 15 also requires:
         $ zypper install postgresql-server-devel
         $ systemctl start postgresql
         $ systemctl enable postgresql
