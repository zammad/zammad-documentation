Ensure locale
-------------

Ensure your system uses UTF-8 encoding. 
Use the following command and look for ``LANG=``.

.. code-block:: sh

   $ locale

.. tip:: You can correct the locate like so:

   .. code-block:: sh

      $ sudo apt-get install locales
      $ sudo locale-gen en_US.UTF-8
      $ sudo echo "LANG=en_US.UTF-8" > /etc/default/locale