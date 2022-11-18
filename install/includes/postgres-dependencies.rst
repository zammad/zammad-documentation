Install PostgreSQL Dependencies
    .. tabs::

        .. tab:: Ubuntu / Debian

            .. code-block:: sh

                $ apt install libpq-dev

        .. tab:: CentOS

            .. code-block:: sh

                # CentOS 7
                $ yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
                $ yum install postgresql13-libs postgresql13-devel

                # CentOS 8
                $ yum install postgresql-libs postgresql-devel

        .. tab:: OpenSuSE

            .. code-block:: sh

                $ zypper install postgresql-devel

Install Gems for Zammad
    .. code-block:: sh

        $ su - zammad
        $ bundle config set without "test development mysql"
        $ bundle install

        # CentOS 7 users - above command might fail, run the following
        # command and repeat above bundle install.
        # Adjust pg_config path according to your environment
        $ gem install pg -v '0.21.0' -- --with-pg-config=/usr/pgsql-13/bin/pg_config
