Install with Docker Compose
***************************

.. warning::

   We currently do not support Docker environments in productive use.
   It's no problem if you run Zammad on docker, however, support is only
   provided for Zammad as application!

.. note::

   Docker Compose environments require deeper system know how.
   If you're not too familiar with Docker and the way it works, you may want
   to stick with :doc:`the package installation </install/package/>` instead.

Docker is a container-based software framework for automating deployment of
applications. Compose is a tool for defining and running multi-container Docker
applications.

Zammads docker images are hosted on `Dockerhub`_.

.. _Dockerhub:
   https://hub.docker.com/r/zammad/zammad-docker-compose/

.. warning::

   Never use the ``latest`` tag. Use a tag which has a version attached.

   You need at least 4 GB of RAM to run the containers.

Install Docker Environment
==========================

This documentation expects you already have a working Docker Compose
environment. You can find the required documentations for these steps below:

   * `Docker Engine <https://docs.docker.com/engine/installation/>`_
   * `Docker Compose <https://docs.docker.com/compose/install/>`_

Getting started with zammad-docker-compose
==========================================

.. toctree::
   :hidden:
   :maxdepth: 1

   /install/docker-compose/environment

Step 1: Clone GitHub repo
-------------------------

.. warning::

   If you're updating Zammad, below commands will cause values set in ``.env``
   and ``docker-compose.override.yml`` to be lost. You're expected to check
   if the ``docker-compose.yml`` has changed and if so to adjust it accordingly.

.. code-block:: sh

   $ git clone https://github.com/zammad/zammad-docker-compose.git
   $ cd zammad-docker-compose

.. hint::

   If cloning is too much of a hassle, it's also enough to get the files
   ``docker-compose.yml`` and ``.env``.

Step 2: Setting vm.max_map_count for Elasticsearch
--------------------------------------------------

Even with running Elasticsearch in a container, you're required to adjust your
host's settings to ensure a clean runtime.

.. code-block:: sh

   $ sysctl -w vm.max_map_count=262144

Step 3: Adjust Environment as needed
------------------------------------

In some cases our default environment is not what a docker-compose user is
looking for. To remove complexity from this page, we outsourced information on
this topic.

See :doc:`/install/docker-compose/environment`

Step 4: Start Zammad using DockerHub images
-------------------------------------------

.. warning::

   Before starting your containers ensure to not use default login data for
   your Zammad database! See Step 3!

.. code-block:: sh

   $ docker compose up -d

.. hint:: **🔧 How to run rails/rake commands in containers**

   The docker entrypoint script sets up environment variables required by Zammad to function properly.
   That is why calling ``rails`` / ``rake`` on the console should be done via one of the following methods:

   .. code-block:: sh

      $ docker compose run --rm zammad-railsserver rails r '...your rails command here...'

   This will run the command via the docker entrypoint and is recommended. In case you require the use of ``docker exec``, you can use the following command:

   .. code-block:: sh

      $ docker exec zammad-docker-compose-zammad-railsserver-1 /docker-entrypoint.sh rails r '...your rails command here...'

   This will manually invoke the docker entrypoint and pass the desired command to it for execution in the proper environment.

.. include:: /install/includes/next-steps.rst
