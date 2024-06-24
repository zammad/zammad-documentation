Install with Docker
*******************

Zammad can be deployed using Docker-Compose. You can even use
graphical docker front ends like
`Portainer <https://www.portainer.io/>`_.

.. hint::

   We do not provide support in terms of Docker (-Compose) or Portainer specific problems.
   If you choose to run Zammad via Docker, support is only provided for the Zammad application.

   In case you're not too familiar with Docker and the way it works, you may want
   to stick with :doc:`the package installation </install/package/>` instead.

Prerequisites
=============

* This documentation expects you already have a working
  `Docker Compose <https://docs.docker.com/compose/>`_ environment.
* Make sure to have at least 4 GB of RAM to run the containers.
* You're required to adjust your host's settings to run Elasticsearch properly:

   .. code-block:: sh

      $ sysctl -w vm.max_map_count=262144

Deployment with Portainer
=========================

The easiest way to get Zammad running is via a graphical docker UI. We recommend `Portainer <https://www.portainer.io/>`_.
For installation instructions, check out `Portainer's documentation <https://docs.portainer.io/>`_.

Step 1: **Add Stack**
   In the Portainer GUI (e.g. ``https://yourdomain.tld:9443``),
   choose your target environment, select **Stacks** and
   choose **Add stack** as you can see in the screenshot below.

Step 2: **Build From Repository**
   Switch to **Repository** build method and provide the information below:

   - **Name**: enter a desired name of the stack
   - **Repository URL**: ``https://github.com/zammad/zammad-docker-compose``
   - **Repository reference**: ``refs/heads/master``
   - **Compose path**: ``docker-compose.yml`` (default)

   Optional: if you need to provide
   :doc:`environment variables <./docker-compose/environment>`, you can enter
   them in the **Environment variable** section or even upload a ``.env`` file.
   See the `example env template <https://github.com/zammad/zammad-docker-compose/blob/master/.env.dist>`_.

   Zammad runs on port ``8080`` by default. If you want to use another port, you can set it via the variable ``NGINX_EXPOSE_PORT``.

Step 3: **Deploy the Stack**
   After the stack is ready, you can access Zammad via the configured docker host and port, e.g. ``http://localhost:8080/``.

.. figure:: /images/install/docker-compose/portainer/portainer-stacks.png
   :alt: Screenshot showing portainer UI with stacks section and highlighted "Add stack" button

   In the **Stacks** section in Portainer select **Add stack**.

.. figure:: /images/install/docker-compose/portainer/portainer-stack-creation.png
   :alt: Screenshot showing stack creation with necessary information

   Stack creation with provided information in **Repository** screen


Deployment with Docker-Compose
==============================

Step 1: **Clone the GitHub Repo**
   .. code-block:: sh

      $ git clone https://github.com/zammad/zammad-docker-compose.git

   Make sure to run ``git pull`` frequently to fetch updates.
   Alternatively, you can download the files from
   `the releases page <https://github.com/zammad/zammad-docker-compose/releases>`_.

Step 2: **Adjust Environment as Needed**
   In some cases our default environment is not what a docker-compose user is
   looking for. See :doc:`/install/docker-compose/environment` for details on
   which settings can be configured.

   .. note:: If you want to use a ``.env`` file, you can use the provided
      ``.env.dist`` file and copy it to ``.env``. That way it will be picked
      up by Docker-Compose automatically and not overwritten during updates.

   Zammad runs on port ``8080`` by default. If you want to use another port, you can set it via the variable ``NGINX_EXPOSE_PORT``.

Step 3: Start the stack
   .. code-block:: sh

      $ cd zammad-docker-compose
      $ docker compose up -d

   After the stack is ready, you can access Zammad via the configured docker host and port, e.g. ``http://localhost:8080/``.

Customizing the Zammad Stack
============================

Sometimes it's necessary to apply local changes to the Zammad docker stack, e.g. to
include additional services. If you plan to do so, we recommend that you do not change
the ``docker-compose.yml`` file, but instead create a local ``docker-compose.override.yml``
that includes all your modifications. Docker-Compose will
`automatically load this file and merge its changes into your stack <https://docs.docker.com/compose/multiple-compose-files/merge/>`_.

.. toctree::
   :hidden:
   :maxdepth: 1

   /install/docker-compose/environment

How to Run Commands in the Stack
================================

The docker entrypoint script sets up environment variables required by Zammad
to function properly. That is why calling ``rails`` or ``rake`` on the console
should be done via one of the following methods:

.. code-block:: sh

   # Directly execute a specific command:

   $ docker compose run --rm zammad-railsserver rails r '...your rails command here...'

   # Run the interactive rails console to manually enter Rails commands:

   $ docker compose run --rm zammad-railsserver rails c

   # Via 'docker exec':

   $ docker exec zammad-docker-compose-zammad-railsserver-1 /docker-entrypoint.sh rails r '...your rails command here...'

If you need to retrieve information from the rails server, you can place
for example ``pp`` (pretty print) in front of your rails command. This
leads to an output in your terminal.