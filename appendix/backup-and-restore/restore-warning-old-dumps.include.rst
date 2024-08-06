Be aware that restoring backups can overwrite your ``database.yml``.
You can check that by looking into the ``[...]_zammad_files.tar.gz`` file.
If there is a ``database.yml`` in the directory *config > database*, ensure
to save the original version **before restoring**.

In case it has been overwritten already, you can try the
:ref:`reset_db_password`.
