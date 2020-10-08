Due to a `issue <https://github.com/crohr/pkgr/issues/165>`_ with packager.io 
you'll need to correct file permissions for public files.

.. code-block:: sh

   chown -R 644 /opt/zammad/public/
   chmod -R +x /opt/zammad/public/