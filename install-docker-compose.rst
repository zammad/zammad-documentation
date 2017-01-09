Install with Docker-compose
***************************

Docker is a container-based software framework for automating deployment of applications. Compose is a tool for defining and running multi-container Docker applications.
This repo is meant to be the starting point for somebody who likes to use dockerized multi-container Zammad in production.
The Zammad Docker image uses the stable branch of Zammads GIT repo.

The Docker images are hosted on Dockerhub:

* https://hub.docker.com/r/zammad/zammad-docker-compose/

Your Docker environment needs to be up and running and you need to have docker-compose installed.

Install Docker-compopse
=======================

* https://docs.docker.com/compose/install/

Getting started with zammad-docker-compose
==========================================

Clone GitHub repo
-----------------

* git clone git@github.com:zammad/zammad-docker-compose.git
* cd zammad-docker-compose

Setting vm.max_map_count for Elasticsearch
------------------------------------------

* sysctl -w vm.max_map_count=262144

Using DockerHub images
----------------------

* docker-compose up

Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user and you need to invite other agents.

Maintenance
===========

Updating Zammad
---------------

* docker-compose pull
* docker-compose up


Building Docker images locally with development branch
------------------------------------------------------

* GIT_BRANCH=develop docker-compose -f docker-compose-build.yml up

Recreate locally build images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* GIT_BRANCH=develop docker-compose -f docker-compose-build.yml build --no-cache

Open shell in running Zammad image
----------------------------------

* docker-compose exec zammad /bin/bash
