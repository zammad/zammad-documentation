Install PostgreSQL Dependencies
    .. tabs::

        .. tab:: Ubuntu / Debian

            .. code-block:: sh

                $ apt install libpq-dev

        .. tab:: CentOS

            .. code-block:: sh

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
