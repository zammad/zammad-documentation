.. note:: **🤓 required packages**
   
   If not installed already, please install ``wget apt-transport-https gnupg`` before hand.

Ubuntu 16.04
------------

.. code-block:: sh

   $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
   $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/16.04.repo

Ubuntu 18.04
------------

.. code-block:: sh

   $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
   $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/18.04.repo

Ubuntu 20.04
------------

.. code-block:: sh

   $ wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
   $ sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/20.04.repo