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
         $ yum install postgresql14-server postgresql14-contrib
         $ postgresql13-setup initdb
         $ systemctl start postgresql14
         $ systemctl enable postgresql14

         # CentOS 8
         $ yum install postgresql-server postgresql-contrib
         $ postgresql-setup initdb
         $ systemctl start postgresql
         $ systemctl enable postgresql

   .. tab:: OpenSUSE / SLES

      .. code-block:: sh

         $ zypper refresh
         $ zypper install postgresql postgresql-server postgresql-contrib
         $ systemctl start postgresql
         $ systemctl enable postgresql
