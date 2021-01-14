Install with Docker Compose
***************************

.. warning:: 

   We currently do not support Docker environments in productive use. 
   If you run Zammad on docker, it is fine. But we just support the application!

.. note::

   Docker Compose environments require deeper system know how. 
   If you're not too familiar with Docker and the way it works, you may want 
   to stick with :doc:`the package installation </install/package/>` instead.

Docker is a container-based software framework for automating deployment of 
applications. Compose is a tool for defining and running multi-container Docker 
applications.

This repo is meant to be the starting point for somebody who likes to use 
dockerized multi-container Zammad in production. The Zammad Docker image uses 
the stable branch of Zammad's Git repo.

The Docker images are hosted on `Dockerhub <https://hub.docker.com/r/zammad/zammad-docker-compose/>`_.

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

.. code-block:: sh

   $ git clone https://github.com/zammad/zammad-docker-compose.git
   $ cd zammad-docker-compose

Step 2: Setting vm.max_map_count for Elasticsearch
--------------------------------------------------

.. code-block:: sh

   $ sysctl -w vm.max_map_count=262144

.. tip:: 

   Mac OS users please also have a look on 
   `Issue 27 <https://github.com/zammad/zammad-docker/issues/27#issuecomment-455171752>`_

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

   $ docker-compose up

.. include:: /install/includes/next-steps.rst
