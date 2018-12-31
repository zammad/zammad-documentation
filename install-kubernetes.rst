Install on Kubernetes via Helm
******************************

.. Warning:: We currently do not support Kubernetes installations in productive use.

Kubernetes_ (k8s) is an open-source system for automating deployment, scaling, and management of containerized applications.

.. _Kubernetes: https://kubernetes.io

Helm_ is the package manager for Kubernetes.

.. _Helm: https://helm.sh

This repo is meant to be the starting point for somebody who likes to use dockerized multi-container Zammad on Kubernetes.
The Zammad Docker image uses the stable branch of Zammad's Git repo.

The used Docker images are hosted on Dockerhub:

* https://hub.docker.com/r/zammad/zammad-docker-compose/

You need the Helm binary installed / initialized and at least 4 GB of free RAM in the Kubernetes cluster run the containers.


Add Helm repo
=============

::

 helm repo add zammad https://zammad.github.io


Install / Upgrade Zammad
========================

::

 helm upgrade --install zammad zammad/zammad --namespace=zammad
