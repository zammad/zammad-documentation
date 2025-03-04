Docker Compose Scenarios
========================

Overview
--------

The best way to deploy Zammad with Docker Compose or Portainer is by using
the repository build method. With this, your Zammad can be updated regularly
and you are using the default compose file of the repository. This might be
good as default, but your situation may differ. This is why you can set
:doc:`environment variables for docker <environment>` and/or even use our
pre-defined scenarios.

The following scenarios are supported:

- **Add a Cloudflare tunnel service to the stack** (add-cloudflare-tunnel.yml)
- **Add an external network to Elasticsearch** (add-external-network-to-elasticsearch.yml)
- **Add an external network to Nginx** (add-external-network-to-nginx.yml)
- **Add an host port to Elasticsearch** (add-hostport-to-elasticsearch.yml)
- **Add a Nginx Proxy Manager (NPM) to the stack** (add-nginx-proxy-manager.yml)
- **Disable the backup service** (disable-backup-service.yml)
- **Disable Elasticsearch service** (disable-elasticsearch-service.yml)

You can find the files in the
`Zammad-Docker-Compose repository <https://github.com/zammad/zammad-docker-compose>`_.

Usage with Portainer
--------------------

Follow the
:doc:`general deployment guide <../docker-compose>`
and apply the following changes.

Below the "Compose path" field, click on the **Add file** button. This opens
the "Additional paths" section where you can specify the scenario you want to
use. Add ``/scenarios/{scenario you want to use}.yml`` and replace the last
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

Relevant file: ``/scenarios/add-cloudflare-tunnel.yml``

Why?
   If you want to publish Zammad in a very easy way and without taking
   care about e.g. SSL certificates, you can use a
   `Cloudflare <https://www.cloudflare.com/>`_ tunnel.

How?
   - Use the relevant scenario file
   - Provide your Cloudflare token by using the environment variable
     ``CLOUDFLARE_TUNNEL_TOKEN``

Add External Network to Nginx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-external-network-to-nginx.yml``

Why?
   If you need to connect your Zammad stack to another network on your
   docker compose / Portainer instance where your NPM is running.

How?
   - Use the relevant scenario file
   - Provide the name of your external network by using the environment
     variable ``ZAMMAD_NGINX_EXTERNAL_NETWORK``

Add External Network to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-external-network-to-elasticsearch.yml``

Why?
   If you need to connect your Zammad stack to another network on your
   docker compose / Portainer instance where your Elasticsearch is running.

How?
   - Use the relevant scenario file
   - Provide the name of your external network by using the environment
     variable ``ZAMMAD_ELASTICSEARCH_EXTERNAL_NETWORK``


Add Nginx Proxy Manager
^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-nginx-proxy-manager.yml``

Why?
   If you don't have a reverse proxy already, you can directly deploy it with
   the Zammad stack.

How?
  - Use the relevant scenario file
  - Provide your FQDN for Zammad by using the environment variable ``ZAMMAD_FQDN``
  - After deploying the stack, go to the NPM UI by accessing the IP of your
    deployment and the port ``81`` (e.g. ``172.20.0.5:81``)
  - Log in with ``admin@example.com`` (user) and ``changeme`` (password)
  - You have to change the email address and the password after the log in
  - Go to *Hosts > Proxy hosts* and select **Add Proxy Host**.
  - Configure it according to your needs and make sure to set up a proper
    SSL certificate
  - Configure your DNS. The chosen Zammad FQDN should point to the NPM IP/host.

Add Host Port to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-hostport-to-elasticsearch.yml``

Why?
   If you want to expose the Elasticsearch service of this stack, e.g. to
   access it from an external Grafana instance.

How?
   Just use the relevant scenario file.

Disable Backup Service
^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/disable-backup-service.yml``

Why?
   If you want to do the backups in a different way, you can disable the backup
   service in the stack to save resources.

How?
   Just use the relevant scenario file.


Disable Elasticsearch Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/disable-elasticsearch-service.yml``

Why?
   If you have an Elasticsearch instance already and want to use it for Zammad
   too, you can disable the Elasticsearch service in the stack to save
   resources.

How?
   - Use the relevant scenario file
   - Use the environment variable ``ELASTICSEARCH_ENABLED`` and set it to
     ``false``