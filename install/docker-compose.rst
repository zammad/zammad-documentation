Install with Docker-Compose
***************************

.. Warning:: We currently do not support Docker environments in productive use. If you run Zammad on docker, it is fine. But we just support the application!

Docker is a container-based software framework for automating deployment of applications. Compose is a tool for defining and running multi-container Docker applications.
This repo is meant to be the starting point for somebody who likes to use dockerized multi-container Zammad in production.
The Zammad Docker image uses the stable branch of Zammad's Git repo.

The Docker images are hosted on `Dockerhub <https://hub.docker.com/r/zammad/zammad-docker-compose/>`_.

.. Tip:: Never use the "latest" tag. Use a tag which has a version attached.

You need at least 4 GB of RAM to run the containers.

Install Docker Environment
==========================

Your Docker environment needs to be up and running and you need to have docker-compose installed.

Docker
------

* https://docs.docker.com/engine/installation/

Docker-Compose
--------------

* https://docs.docker.com/compose/install/


Getting started with zammad-docker-compose
==========================================

Clone GitHub repo
-----------------

* git clone https://github.com/zammad/zammad-docker-compose.git
* cd zammad-docker-compose

Setting vm.max_map_count for Elasticsearch
------------------------------------------

* sysctl -w vm.max_map_count=262144

.. Tip:: For Mac OS: https://github.com/zammad/zammad-docker/issues/27#issuecomment-455171752


Start Zammad using DockerHub images
-----------------------------------

* docker-compose up


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and invite other agents.


Maintenance
===========

Updating Zammad
---------------

* docker-compose stop
* git pull
* docker-compose pull
* docker-compose up


Start Zammad building Docker images locally with development branch
-------------------------------------------------------------------

* GIT_BRANCH=develop docker-compose -f docker-compose-build.yml up

Recreate locally built images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* GIT_BRANCH=develop docker-compose -f docker-compose-build.yml build --no-cache


Open shell in running Zammad image
----------------------------------

* docker-compose exec zammad /bin/bash

Port compatibility error
------------------------

* The nginx container may have compatibility problems with other machines or services pointing to port 0.0.0.0:80. So to fix this, we'll just have to modify the file `docker-compose.override.yml` and select different ports
