.. code-block:: sh

   # Set rails environment specific things
   $ echo "export RAILS_ENV=production" >> /opt/zammad/.bashrc
   $ echo "export RAILS_SERVE_STATIC_FILES=true" >> /opt/zammad/.bashrc
   $ echo "rvm --default use 2.7.3" >> /opt/zammad/.bashrc

   # Debian, CentOS & OpenSuSE
   $ echo "source /usr/local/rvm/scripts/rvm" >> /opt/zammad/.bashrc
   # Ubuntu
   $ echo "source /usr/share/rvm/scripts/rvm" >> /opt/zammad/.bashrc
