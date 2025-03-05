Docker Compose Scenarios
========================

Overview
--------

If the "vanilla" Zammad stack doesn't cover your use-case, you can use one of
the pre-defined scenarios. We don't recommend to change the compose files
locally because upstream changes for the stack aren't reflected automatically
then. This is why you should either use Portainer's repository build method or
clone the repository and update it regularly, when using docker compose.

The following scenarios are supported:

- Making the stack available via HTTPS

  - Add a Cloudflare tunnel service to the stack
  - Add a Nginx Proxy Manager (NPM) to the stack
  - Add an external docker network to Nginx

- Using external services

  - Disable Elasticsearch service

- Making services externally available

  - Add an external docker network to Elasticsearch
  - Add an host port to Elasticsearch

- Additional scenarios

  - Disable the backup service

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

   docker compose -f docker-compose.yml -f scenarios/{scenario you want to use}.yml up -d

Replace the part in ``{}`` brackets with the file name of one of the scenario
files. You can even combine the scenarios by adding additional files according
to the example above.


Making the Stack Available via HTTPS
------------------------------------

If you set up Zammad for production use, it needs to be secured by using an
HTTPS connection. Because this can be achieved in different ways, we added 3
different scenarios.

Add Cloudflare Tunnel
^^^^^^^^^^^^^^^^^^^^^

If you want to publish Zammad in a very easy way and without taking
care about e.g. SSL certificates, you can use a
`Cloudflare <https://www.cloudflare.com/>`_ tunnel.

- Use the scenario file ``scenarios/add-cloudflare-tunnel.yml`` for deployment
- Add a sub-domain to an already existing domain in your Cloudflare dashboard
- Forward it to your Zammad Nginx instance with port ``8080``
- Create a tunnel. This is where you get your token for the next step
- Provide your Cloudflare token by using the environment variable
  ``CLOUDFLARE_TUNNEL_TOKEN``

Add Nginx Proxy Manager
^^^^^^^^^^^^^^^^^^^^^^^

A very common setup of publishing web services is to use a reverse proxy, which
handles the SSL termination. One common tool is the Nginx Proxy Manager (NPM),
which can be configured via UI quite simple. If you don't have a reverse
proxy already, this might be a useful scenario for you. If you already have a
running reverse proxy, head over to the next section.

- Use the scenario file ``scenarios/add-nginx-proxy-manager.yml`` for deployment
- Provide your FQDN for Zammad by using the environment variable ``ZAMMAD_FQDN``
- Configure your DNS. The chosen Zammad FQDN should point to the IP address of
  the NPM host
- Configure a new proxy host in your NPM and follow the steps to get an SSL
  certificate

Add External Docker Network to Nginx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you already have a reverse proxy which takes care about the SSL termination,
this scenario is helpful. It adds an external docker network to Zammad's
included Nginx service to be able to access it from a separated reverse proxy.

- Use the scenario file ``scenarios/add-external-network-to-nginx.yml`` for deployment
- Provide the name of your external network by using the environment
  variable ``ZAMMAD_NGINX_EXTERNAL_NETWORK``

Using External Services
-----------------------

Disable Elasticsearch Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do you have an Elasticsearch instance already running and want to use it for
Zammad too? Then you can disable the Elasticsearch service in the Zammad stack
to save resources.

- Use the scenario file ``scenarios/disable-elasticsearch-service.yml`` for
  deployment
- Use the following environment variables to provide information about the
  connection to your existing Elasticsearch instance:

  - ``ELASTICSEARCH_SCHEMA``
  - ``ELASTICSEARCH_HOST``
  - ``ELASTICSEARCH_PORT``
  - ``ELASTICSEARCH_USER``
  - ``ELASTICSEARCH_PASS``

Making Services Externally Available
------------------------------------

Add External Docker Network to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-external-network-to-elasticsearch.yml``

Why?
   If you need to connect your Zammad stack to another network on your
   docker compose / Portainer instance where your Elasticsearch is running.

How?
   - Use the relevant scenario file
   - Provide the name of your external network by using the environment
     variable ``ZAMMAD_ELASTICSEARCH_EXTERNAL_NETWORK``

Add Host Port to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/add-hostport-to-elasticsearch.yml``

Why?
   If you want to expose the Elasticsearch service of this stack, e.g. to
   access it from an external Grafana instance.

How?
   - Use the relevant scenario file
   - Your ES service is now accessible under port ``9200``

Additional Scenarios
--------------------

Disable Backup Service
^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``scenarios/disable-backup-service.yml``

Why?
   If you want to do the backups in a different way, you can disable the backup
   service in the stack to save resources.

How?
   Just use the relevant scenario file.

Other use cases
^^^^^^^^^^^^^^^

- suggest a new scenario…

- or customize locally:

Sometimes it's necessary to apply local changes to the Zammad docker stack, e.g. to
include additional services. If you plan to do so, we recommend that you do not change
the ``docker-compose.yml`` file, but instead create a local ``docker-compose.override.yml``
that includes all your modifications. Docker-Compose will
`automatically load this file and merge its changes into your stack <https://docs.docker.com/compose/multiple-compose-files/merge/>`_.
