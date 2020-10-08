.. note:: **🤓 required packages**
   
   If not installed already, please install ``wget apt-transport-https gnupg`` before hand.

Debian 9
--------

.. code-block:: sh

   $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
   $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/debian/9.repo

Debian 10
---------

.. code-block:: sh

   $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
   $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/debian/10.repo