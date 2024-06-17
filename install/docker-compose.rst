Install with Docker
*******************

Zammad can be deployed using Docker-Compose. You can even use
`Portainer <https://www.portainer.io/>`_.
See the sections below for details.

.. warning::

   Be aware that we can't support in terms of Docker (-Compose) or Portainer
   specific problems.
   It's no problem if you run Zammad via Docker, however, support is only
   provided for Zammad as application!

   If you're not too familiar with Docker and the way it works, you may want
   to stick with :doc:`the package installation </install/package/>` instead.

Prerequisites
=============

Docker-Compose Environment
   This documentation expects you already have a working Docker Compose
   environment. You can find the required documentations for these steps here:

      * `Docker Engine <https://docs.docker.com/engine/installation/>`_
      * `Docker Compose <https://docs.docker.com/compose/install/>`_

Hardware Requirements
   Make sure to have at least 4 GB of RAM to run the containers.

Setting ``vm.max_map_count`` for Elasticsearch
   Even with running Elasticsearch in a container, you're required to adjust your
   host's settings to run Elasticsearch properly:

   .. code-block:: sh

      $ sysctl -w vm.max_map_count=262144

Deployment with Portainer
=========================

The easiest way to get Zammad running is via Portainer's management UI.
If you already have a running Portainer instance, head over to
:ref:`portainer-deploying-zammad`.

Install Portainer
-----------------

Make sure to meet the
`requirements and prerequisites <https://docs.portainer.io/start/requirements-and-prerequisites>`_
and follow their official installation instructions
(`Community Edition <https://docs.portainer.io/start/install-ce/server>`_ or
`Business Edition <https://docs.portainer.io/start/install>`_).

After following these steps, you should be able to access the Portainer UI via
browser.

.. _portainer-deploying-zammad:

Deploying Zammad
----------------

1. Head over to your Portainer GUI (e.g. ``https://yourdomain.tld:9443``)
   and log in.
2. Select your environment in which you want to deploy Zammad
3. Select **Stacks** and choose **Add stack** as you can see in the following
   screenshot
4. Switch to **Repository** build method and provide the below listed
   information:

     - **Name**: enter a desired name of the stack
     - **Repository URL**: ``https://github.com/zammad/zammad-docker-compose``
     - **Repository reference**: ``refs/heads/master``
     - **Compose path**: ``docker-compose.yml`` (default)

5. Optional: if you need to provide
   :doc:`environment variables <./docker-compose/environment>`, you can enter
   them in the **Environment variable** section.
6. Finally, click on **Deploy the stack**

.. figure:: /images/install/docker-compose/portainer/portainer-stacks.png
   :alt: Screenshot showing portainer UI with stacks section and highlighted "Add stack" button

   In the **Stacks** section in Portainer select **Add stack**.

.. figure:: /images/install/docker-compose/portainer/portainer-stack-creation.png
   :alt: Screenshot showing stack creation with necessary information

   Stack creation with provided information in **Repository** screen


Deployment with Docker-Compose
==============================

.. toctree::
   :hidden:
   :maxdepth: 1

   /install/docker-compose/environment

Step 1: Clone GitHub Repo
-------------------------

.. warning::

   If you're updating Zammad, below commands will cause values set in ``.env``
   and ``docker-compose.override.yml`` to be lost. You're expected to check
   if the ``docker-compose.yml`` has changed and if so to adjust it accordingly.

.. code-block:: sh

   $ git clone https://github.com/zammad/zammad-docker-compose.git
   $ cd zammad-docker-compose

.. hint::

   If cloning is too much of a hassle, you can also download the files from
   https://github.com/zammad/zammad-docker-compose/releases. This will make sure
   file permissions are preserved.


Step 2: Adjust Environment as needed
------------------------------------

In some cases our default environment is not what a docker-compose user is
looking for. To remove complexity from this page, we outsourced information on
this topic.

See :doc:`/install/docker-compose/environment`

Step 3: Start Zammad by running containers
------------------------------------------

.. warning::

   Before starting your containers ensure to not use default login data for
   your Zammad database!

.. code-block:: sh

   $ docker compose up -d

.. hint:: **🔧 How to run rails/rake commands in containers**

   The docker entrypoint script sets up environment variables required by Zammad
   to function properly. That is why calling ``rails`` / ``rake`` on the console
   should be done via one of the following methods:

   .. code-block:: sh

      $ docker compose run --rm zammad-railsserver rails r '...your rails command here...'

   This will run the command via the docker entrypoint and is recommended.

   Alternatively, you can run the rails console interactively by running:

   .. code-block:: sh

      $ docker compose run --rm zammad-railsserver rails c

   In case you require the use of ``docker exec``, you can use the following
   command:

   .. code-block:: sh

      $ docker exec zammad-docker-compose-zammad-railsserver-1 /docker-entrypoint.sh rails r '...your rails command here...'

   This will manually invoke the docker entrypoint and pass the desired command
   to it for execution in the proper environment.

   If you need to retrieve information from the rails server, you can place
   for example ``pp`` (pretty print) in front of your rails command. This
   leads to an output in your terminal.

.. include:: /install/includes/next-steps.rst
