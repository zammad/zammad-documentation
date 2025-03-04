Docker Compose Scenarios
========================

Overview
--------

The following scenarios are supported:

- add-cloudflare-tunnel.yml
- add-external-network-to-nginx.yml
- add-nginx-proxy-manager.yml
- disable-backup-service.yml
- disable-elasticsearch-service.yml

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

.. code-block:: yaml

   docker compose -f docker-compose.yml -f /scenarios/{scenario you want to use}.yml up -d

Replace the part in ``{}`` brackets with the file name of one of the scenario
files. You can even combine the scenarios by adding additional files according
to the example above.

Scenario Details
----------------

Add Cloudflare Tunnel
^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-cloudflare-tunnel.yml``

**Why?**

If you want to publish Zammad in a very easy way and without taking
care about e.g. SSL certificates, you can use a
`Cloudflare <https://www.cloudflare.com/>`_ tunnel.

**How?**

- Use the relevant scenario file
- Provide your Cloudflare token as environment variable (``CLOUDFLARE_TUNNEL_TOKEN``)

Add External Network to Nginx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-external-network-to-nginx.yml``

Add Nginx Proxy Manager
^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/add-nginx-proxy-manager.yml``

**Why?**

If you don't already have a reverse proxy, you can directly deploy it with
the Zammad stack.

**How?**

- Use the relevant scenario file
- Provide your Cloudflare token as environment variable (``CLOUDFLARE_TUNNEL_TOKEN``)

Disable Backup Service
^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/disable-backup-service.yml``


Disable Elasticsearch Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Relevant file: ``/scenarios/disable-elasticsearch-service.yml``