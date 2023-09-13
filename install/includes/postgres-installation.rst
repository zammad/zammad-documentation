.. tabs::

   .. tab:: Ubuntu / Debian

      .. code-block:: sh

         $ apt update
         $ apt install postgresql postgresql-contrib
         $ systemctl start postgresql
         $ systemctl enable postgresql

   .. tab:: CentOS

      .. code-block:: sh

         # CentOS 7
         $ yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
         $ yum install postgresql15-server postgresql15-contrib
         $ postgresql-15-setup initdb
         $ systemctl start postgresql-15
         $ systemctl enable postgresql-15

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
