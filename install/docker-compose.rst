Install with Docker
===================

.. include:: /install/includes/hosted-services.rst

Zammad can be deployed using Docker-Compose. You can even use
graphical docker front ends like
`Portainer <https://www.portainer.io/>`_.

.. hint::

   We do not provide support in terms of Docker (-Compose) or Portainer specific
   problems. If you choose to run Zammad via Docker, support is only provided
   for the Zammad application.

Prerequisites
-------------

* This documentation expects you already have a working
  `Docker Compose <https://docs.docker.com/compose/>`_ environment.
* Make sure to have at least 4 GB of RAM to run the containers.
* Adjust your host's settings to run Elasticsearch properly:

   .. code-block:: sh

      sysctl -w vm.max_map_count=262144

Deployment with Portainer
-------------------------

The easiest way to get Zammad running is via a graphical docker UI. We recommend
`Portainer <https://www.portainer.io/>`_.
For installation instructions, check out
`Portainer's documentation <https://docs.portainer.io/>`_.

Step 1: Add Stack
   In the Portainer GUI (e.g. ``https://yourdomain.tld:9443``),
   choose your target environment, select **Stacks** and
   choose **Add stack** as you can see in the screenshot below.

.. figure:: /images/install/docker-compose/portainer/portainer-stacks.png
   :alt: Screenshot showing portainer UI with stacks section and highlighted "Add stack" button

Step 2: Build From Repository
   Switch to **Repository** build method and provide the information below:

   - **Name**: enter a desired name of the stack
   - **Repository URL**: ``https://github.com/zammad/zammad-docker-compose``
   - **Repository reference**: ``refs/heads/master``
   - **Compose path**: ``docker-compose.yml`` (default)

   In some cases, our default environment is not what a Docker-Compose user is
   looking for. You can customize the stack using pre-defined scenarios and
   adjust environment variables. Jump to the
   :ref:`the customization section <customizing-stack>` below to find more
   information.

.. figure:: /images/install/docker-compose/portainer/portainer-stack-creation.png
   :alt: Screenshot showing stack creation with necessary information

Step 3: Deploy the Stack
   Finally, click the **Deploy the stack** button. The first time, it may take
   some time until the Docker images are fetched.

   After the stack is ready, you can access Zammad via the configured docker
   host and port, e.g. ``http://localhost:8080/``.


Deployment with Docker-Compose
------------------------------

Step 1: Clone the GitHub Repo
   .. code-block:: sh

      git clone https://github.com/zammad/zammad-docker-compose.git

   Make sure to run ``git pull`` frequently to fetch updates.
   Alternatively, you can download the files from
   `the releases page <https://github.com/zammad/zammad-docker-compose/releases>`_.

Step 2: Adjust Environment as Needed
   In some cases, our default environment is not what a docker-compose user is
   looking for. You can customize the stack using pre-defined scenarios and
   adjust environment variables. Jump to the
   :ref:`customization section <customizing-stack>` below to find more
   information.

Step 3: Start the stack
   .. code-block:: sh

      cd zammad-docker-compose
      docker compose up -d

   Optional: Use an additional ``.yml`` file to use a pre-defines scenario.
   Read on in the :ref:`Customizing the Zammad Stack <customizing-stack>`
   section.

   After the stack is ready, you can access Zammad via the configured docker
   host and port, e.g. ``http://localhost:8080/``.

Exposing the Stack via HTTPS
----------------------------

To publish a Zammad stack on the internet, it needs be secured via the HTTPS
protocol. To achieve that without modifying the Zammad stack, you can:

- Use a reverse proxy like Nginx Proxy Manager (NPM). It has a GUI that provides
  an easy `Letsencrypt <https://letsencrypt.org/>`_ integration.
- Use a cloudflare tunnel, which provides SSL termination.

Both scenarios are covered in the
:doc:`Docker compose scenarios section <docker-compose/docker-compose-scenarios>`.

.. _customizing-stack:

Customizing the Zammad Stack
----------------------------

The Zammad stack can be customized by loading additional scenario files for
common use cases. For example, you can deploy the stack with an included Nginx
Proxy Manager (NPM) or with disabled Postgres or Elasticsearch services, in case
you already have these services running.

Please see the :doc:`Docker compose scenarios section <docker-compose/docker-compose-scenarios>`.

To adjust the stack and settings, use
:doc:`docker specific environment variables </install/docker-compose/environment>`.

.. toctree::
   :hidden:
   :maxdepth: 1

   /install/docker-compose/environment
   /install/docker-compose/docker-compose-scenarios


How to Run Commands in the Stack
--------------------------------

The docker entrypoint script sets up environment variables required by Zammad
to function properly. That is why calling ``rails`` or ``rake`` on the console
should be done via one of the following methods:

.. tabs::

   .. tab:: Via Portainer GUI

      In your Portainer GUI, go to the container view and select the running
      rails container from your Zammad stack. Click on the **Exec Console**
      icon in the "Quick Actions" column.

      .. figure:: /images/install/docker-compose/portainer/portainer-exec-console.png
         :alt:
         :width: 70%

      In the "Execute" dialog, select the "rails console" entry point as you
      can see in the screenshot:

      .. figure:: /images/install/docker-compose/portainer/portainer-execute-command.png
         :alt:
         :width: 70%

   .. tab:: Via console

      Directly execute a specific command:

      .. code-block:: sh

         docker compose run --rm zammad-railsserver rails r '...your rails command here...'

      Run the interactive rails console to manually enter Rails commands:

      .. code-block:: sh

         docker compose run --rm zammad-railsserver rails c

      Via ``docker exec``:

      .. code-block:: sh

         docker exec zammad-docker-compose-zammad-railsserver-1 /docker-entrypoint.sh rails r '...your rails command here...'

      If you need to retrieve information from the rails server, you can place
      for example ``pp`` (pretty print) in front of your rails command. This
      leads to an output in your terminal.
