Docker Compose Scenarios
========================

Overview
--------

If the "vanilla" Zammad stack doesn't cover your use-case, you can use one of
the pre-defined scenarios. We don't recommend to change the compose files
locally because upstream changes for the stack aren't reflected automatically
then. This is why you should either use Portainer's repository build method or
clone the repository and update it regularly.

The following scenarios are supported:

- Making the stack available via HTTPS

  - Add a Cloudflare tunnel service to the stack(add-cloudflare-tunnel.yml)
  - dd a Nginx Proxy Manager (NPM) to the stack (add-nginx-proxy-manager.yml)
  - Add an external docker network to Nginx (add-external-network-to-nginx.yml)

- Using external services

  - Disable Elasticsearch service (disable-elasticsearch-service.yml)

- Making services externally available

  - Add an external docker network to Elasticsearch (add-external-network-to-elasticsearch.yml)
  - Add an host port to Elasticsearch (add-hostport-to-elasticsearch.yml)

- Additional scenarios

  - Disable the backup service (disable-backup-service.yml)

You can find the files in the
`Zammad-Docker-Compose repository <https://github.com/zammad/zammad-docker-compose>`_.

Usage with Portainer
--------------------

Follow the
:doc:`general deployment guide <../docker-compose>`
and apply the following changes.

Below the "Compose path" field, click on the **Add file** button. This opens
the "Additional paths" section where you can specify the scenario you want to
use. Add ``scenarios/{scenario you want to use}.yml`` and replace the last
part in ``{}`` brackets with the name of one of the scenario files. You can
even combine the scenarios by adding additional paths.

.. figure:: /images/install/docker-compose/additional-scenarios/portainer-additional-paths.png
    :alt: Screenshot shows where to add additional paths in Portainer
    :scale: 70%

Usage with Docker Compose
-------------------------

Follow the first 2 steps of the
:doc:`general deployment guide <../docker-compose>`. To start the stack with
one or more additional scenarios, use the following command for step 3 in
the cloned repository folder instead:

.. code-block:: sh

   docker compose -f docker-compose.yml -f /scenarios/{scenario you want to use}.yml up -d

Replace the part in ``{}`` brackets with the file name of one of the scenario
files. You can even combine the scenarios by adding additional files according
to the example above.

Scenario Details
----------------

Add Cloudflare Tunnel
^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-cloudflare-tunnel.yml``

Why?
   If you want to publish Zammad in a very easy way and without taking
   care about e.g. SSL certificates, you can use a
   `Cloudflare <https://www.cloudflare.com/>`_ tunnel.

How?
   - Use the relevant scenario file
   - Add a sub-domain to an already existing domain
   - Forward it to your Zammad Nginx instance with port ``8080``
   - Create a tunnel. This is where you get your token for the next step
   - Provide your Cloudflare token by using the environment variable
     ``CLOUDFLARE_TUNNEL_TOKEN``

Add External Docker Network to Nginx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-external-network-to-nginx.yml``

Why?
   If you need to connect your Zammad stack to another network on your
   docker compose / Portainer instance where your NPM is running.

How?
   - Use the relevant scenario file
   - Provide the name of your external network by using the environment
     variable ``ZAMMAD_NGINX_EXTERNAL_NETWORK``

Add External Docker Network to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-external-network-to-elasticsearch.yml``

Why?
   If you need to connect your Zammad stack to another network on your
   docker compose / Portainer instance where your Elasticsearch is running.

How?
   - Use the relevant scenario file
   - Provide the name of your external network by using the environment
     variable ``ZAMMAD_ELASTICSEARCH_EXTERNAL_NETWORK``


Add Nginx Proxy Manager
^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-nginx-proxy-manager.yml``

Why?
   If you don't have a reverse proxy already, you can directly deploy it with
   the Zammad stack.

How?
  - Use the relevant scenario file
  - Provide your FQDN for Zammad by using the environment variable ``ZAMMAD_FQDN``
  - Configure your DNS. The chosen Zammad FQDN should point to the IP address of the NPM host.
  - Configure a new proxy host in your NPM and follow their steps to get an SSL certificate.


Add Host Port to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-hostport-to-elasticsearch.yml``

Why?
   If you want to expose the Elasticsearch service of this stack, e.g. to
   access it from an external Grafana instance.

How?
   - Use the relevant scenario file
   - Your ES service is now accessible under port ``9200``

Disable Backup Service
^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/disable-backup-service.yml``

Why?
   If you want to do the backups in a different way, you can disable the backup
   service in the stack to save resources.

How?
   Just use the relevant scenario file.


Disable Elasticsearch Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/disable-elasticsearch-service.yml``

Why?
   If you have an Elasticsearch instance already and want to use it for Zammad
   too, you can disable the Elasticsearch service in the stack to save
   resources.

How?
   - Use the relevant scenario file
   - Use the environment following environment variables to provide information
     about your external ES:

      - ``ELASTICSEARCH_SCHEMA``
      - ``ELASTICSEARCH_HOST``
      - ``ELASTICSEARCH_PORT``
      - ``ELASTICSEARCH_USER``
      - ``ELASTICSEARCH_PASS``

Other use cases
^^^^^^^^^^^^^^^

- suggest a new scenario…

- or customize locally:

Sometimes it's necessary to apply local changes to the Zammad docker stack, e.g. to
include additional services. If you plan to do so, we recommend that you do not change
the ``docker-compose.yml`` file, but instead create a local ``docker-compose.override.yml``
that includes all your modifications. Docker-Compose will
`automatically load this file and merge its changes into your stack <https://docs.docker.com/compose/multiple-compose-files/merge/>`_.
