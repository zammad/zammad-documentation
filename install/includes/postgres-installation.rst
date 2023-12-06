.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ apt update
         $ apt install postgresql postgresql-contrib
         $ systemctl start postgresql
         $ systemctl enable postgresql

   .. tab:: CentOS

      .. code-block:: sh

         # CentOS 8
         $ yum install postgresql-server postgresql-contrib
         $ postgresql-setup initdb
         $ systemctl start postgresql
         $ systemctl enable postgresql

   .. tab:: OpenSUSE / SLES

      .. code-block:: sh

         $ zypper refresh
         $ zypper install postgresql postgresql-server postgresql-contrib
         # openSuSE 15 also requires:
         $ zypper install postgresql-server-devel
         $ systemctl start postgresql
         $ systemctl enable postgresql
