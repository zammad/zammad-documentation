Docker Compose Scenarios
========================

Overview
--------

If the "vanilla" Zammad stack doesn't cover your use-case, you can use one of
the pre-defined scenarios. We don't recommend to change the Compose files
locally, because it will be hard to keep track of upstream changes for the stack
then. This is why you should either use Portainer's repository build method or
clone the repository and update it regularly, when using Docker Compose.

The following scenarios are supported and explained further below:

- :ref:`Making the stack available via HTTPS <stack-https>`

  - Add a Cloudflare tunnel service to the stack
  - Add a Nginx Proxy Manager (NPM) to the stack
  - Add an external Docker network to Nginx

- :ref:`Using external services <external-services>`

  - Disable Elasticsearch service

- :ref:`Making services externally available <external-availability>`

  - Add an external Docker network to Elasticsearch
  - Add an host port to Elasticsearch

- :ref:`Additional scenarios <additional-scenarios>`

  - Disable the backup service
  - Add an Ollama instance to the stack
  - Add a LibreTranslate instance to the stack
  - Limit hardware resources of the stack

You can find the files in the
`Zammad Docker Compose repository <https://github.com/zammad/zammad-docker-compose>`_.

.. _general-usage-scenarios:

General Usage
-------------

.. tabs::

  .. tab::

    Docker Compose

    To use a scenario, list its compose file in the environment variable
    ``COMPOSE_FILE``. Either create a ``.env`` file or copy and rename the
    ``.env.dist`` in the cloned repository folder. The main compose file
    must be specified first, followed by one or more scenarios, separated by a
    colon (``:``). The files are applied in the order given. Replace the
    placeholder in curly brackets with the filename of the scenario you want
    to use.

    **Example with two scenario placeholders:**

    .. code-block:: console

       COMPOSE_FILE=docker-compose.yml:scenarios/{scenario you want to use}.yml:scenarios/{another scenario you want to use}.yml

    After specifying the scenarios, start the stack with
    ``docker compose up -d``.

    .. note::
       When using the ``COMPOSE_FILE`` variable, the
       ``docker-compose.override.yml``  is not automatically picked up. If you
       want to use it, make sure to append it to the environment variable's
       list.

  .. tab::

    Portainer

    Follow the
    :doc:`general deployment guide <../docker-compose>`
    and apply the following changes.

    Below the "Compose path" field, click on the ``Add file`` button. This opens
    the "Additional paths" section where you can specify the scenario you want to
    use. Add ``scenarios/{scenario you want to use}.yml`` and replace the last
    part in ``{}`` brackets with the name of one of the scenario files. You can
    even combine the scenarios by adding additional paths.

    .. figure:: /images/install/docker-compose/additional-scenarios/portainer-additional-paths.png
        :alt: Screenshot shows where to add additional paths in Portainer
        :scale: 70%

.. _stack-https:

Making the Stack Available via HTTPS
------------------------------------

If you set up Zammad for production use, it needs to be secured by using an
HTTPS connection. There are different scenarios for achieving this, which have
one thing in common:

The scenarios below publish Zammad through a reverse proxy that terminates TLS
and forwards plain HTTP to Zammad. Zammad's own Nginx overwrites the
``X-Forwarded-Proto`` header with the scheme of the connection it receives, so
the scenarios set the environment variable ``NGINX_SERVER_SCHEME`` to
``https``. Without it, Zammad does not write its session cookie and login
fails with a CSRF token verification error. The default from the scenario
files is usually correct, see :doc:`environment variables
</appendix/environment-variables>` if you need to change it.

Add Cloudflare Tunnel
^^^^^^^^^^^^^^^^^^^^^

If you want to publish Zammad in a very convenient way, you can use a
`Cloudflare <https://www.cloudflare.com/>`_ tunnel.

- Use the scenario file ``scenarios/add-cloudflare-tunnel.yml`` for deployment
- Add a sub-domain to an already existing domain in your Cloudflare dashboard
- Create a tunnel for this subdomain and configure it to forward traffic
  to your zammad-nginx service with ``http://zammad-nginx:8080``
- Provide your Cloudflare tunnel token to the Zammad stack by using the
  environment variable ``CLOUDFLARE_TUNNEL_TOKEN``

Add Nginx Proxy Manager
^^^^^^^^^^^^^^^^^^^^^^^

A very common setup of publishing web services is to use a reverse proxy, which
handles the SSL termination. One common tool is the Nginx Proxy Manager (NPM),
which can be configured via UI quite simply. If you don't have a reverse
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
this scenario is helpful. It adds an external Docker network to Zammad's
included Nginx service to be able to access it from a reverse proxy that is not part
of the Zammad stack's network.

- Use the scenario file ``scenarios/add-external-network-to-nginx.yml`` for deployment
- Provide the name of your external network by using the environment
  variable ``ZAMMAD_NGINX_EXTERNAL_NETWORK``

.. _external-services:

Using External Services
-----------------------

Disable Elasticsearch Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do you have an Elasticsearch instance already running and want to use it for
Zammad, too? Then you can disable the Elasticsearch service in the Zammad stack
to save resources.

- Use the scenario file ``scenarios/disable-elasticsearch-service.yml`` for
  deployment - this will turn off the built-in service for Elasticsearch
- Use the following environment variables to provide information about the
  connection to your existing Elasticsearch instance:

  - ``ELASTICSEARCH_SCHEMA``
  - ``ELASTICSEARCH_HOST``
  - ``ELASTICSEARCH_PORT``
  - ``ELASTICSEARCH_USER``
  - ``ELASTICSEARCH_PASS``

.. _external-availability:

Making Services Externally Available
------------------------------------

These scenarios are meant to connect from external applications to Zammad
services. Depending on where your external service is hosted, you can use one
of the following scenarios.

.. danger:: When exposing Elasticsearch outside the stack, make sure
   to set the variable ``ELASTICSEARCH_PASS`` to a custom value first!
   Otherwise this is a big security issue because the Elasticsearch index
   contains most of Zammad's data.

.. hint:: If you want to use TLS, you have to connect to Elasticsearch via
   reverse proxy.

Add External Docker Network to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A common use case for this is to use a reporting/visualization tool like Grafana
on the same host in another stack. Because such tools need to access the
Elasticsearch index, the network of the other stack has to be added to Zammad's
Elasticsearch container.

- Use the scenario file ``scenarios/add-external-network-to-elasticsearch.yml``
  for deployment
- Provide the name of your external network by using the environment
  variable ``ZAMMAD_ELASTICSEARCH_EXTERNAL_NETWORK``

Add Host Port to Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case you want to expose the Elasticsearch service of the Zammad stack in the
network, you can assign a host port to the container. This is useful if you need to
access the Elasticsearch container from a different host.

- Use the scenario file ``scenarios/add-hostport-to-elasticsearch.yml`` for
  deployment
- The default port for Elasticsearch is ``9200``. Change it to another
  port by using the environment variable ``ELASTICSEARCH_EXPOSE_HTTP_PORT``

.. _additional-scenarios:

Additional Scenarios
--------------------

Disable Backup Service
^^^^^^^^^^^^^^^^^^^^^^

In case you want to handle backups in a different way, you can disable the
built in backup service in the stack to save resources.

You can do so by just using the scenario file
``scenarios/disable-backup-service.yml`` for deployment.

Add Ollama
^^^^^^^^^^

You can spin up an additional `Ollama <https://ollama.com/>`_ container to use
:admin-docs:`Zammad's AI features </ai/features.html>` on your machine.

.. hint:: This is intended for development or testing purposes as running a
   productive LLM stack is complex.

To deploy an Ollama container inside the Zammad stack, use the scenario file
``scenarios/add-ollama.yml``. This creates an Ollama container which
automatically pulls and serves ``Llama3.2`` to be ready to use/test AI features
out of the box.

To use it in Zammad, add the service name and port (``http://ollama:11434``) to
the :admin-docs:`provider configuration </ai/provider.html>`.

Add LibreTranslate
^^^^^^^^^^^^^^^^^^

You can run an additional `LibreTranslate <https://libretranslate.com/>`_
container to power Zammad's article translation on your own hardware. For
details on the integration itself, see the :admin-docs:`translation services
documentation </system/integrations/translation-services.html>`.

To deploy a LibreTranslate container inside the Zammad stack, use the scenario
file ``scenarios/add-libretranslate.yml``. The service doesn't publish any
ports to the host; Zammad reaches it inside the stack network as
``http://libretranslate:5000``.

.. hint:: The first start takes a while, as the container downloads the
   language models before the service becomes available. The models are kept
   in a Docker volume, so they survive stack restarts.

The scenario supports the following environment variables:

LT_LOAD_ONLY
   Comma-separated list of languages to load, e.g. ``en,de,fr``. If unset, all
   language models are downloaded, which can take minutes on cold starts.

LT_UPDATE_MODELS
   Set to ``true`` to check for updated language models on every stack
   startup. Only models with a newer available version are redownloaded.
   Without it, the models are downloaded on the first start only.

LT_API_KEYS
   Set to ``true`` to enable API key support. Each key carries its own
   allowed requests per minute. To issue a key, start the service and run:

   .. code-block:: console

      $ docker compose exec libretranslate ltmanage keys add 120

   The number is the allowed requests per minute for this key. The command
   prints the generated key, which is a UUID created by LibreTranslate itself.
   You can also provide your own key with the ``--key`` option instead.

LT_REQUIRE_API_KEY_SECRET
   Set to ``true`` to make API keys mandatory for all requests. Requires
   ``LT_API_KEYS=true``.

.. note:: LibreTranslate supports many more options. They are described in
   the `official documentation <https://docs.libretranslate.com/>`_, which
   also lists the environment variables the container accepts.

Once the stack is up, configure the service under
*System > Integrations > Translation services*: point the URL to
``http://libretranslate:5000`` and provide an API key if your instance
requires one.

Limit Resources
^^^^^^^^^^^^^^^

If you want to limit the hardware resources the Zammad stack is allowed to use,
use the ``scenarios/apply-resource-limits.yml`` scenario. Default values for CPU
and memory usage for each container in the stack are applied then. You can find
these default values in the ``.env.dist`` file. Provide the changed variables
you want to use as environment variables and deploy the stack.

Other Use Cases
^^^^^^^^^^^^^^^

Your scenario is not covered yet? Feel free to suggest your use case.
We plan to add more common use cases to the stack in future.

.. _customize-stack-locally:

Customize the Stack Locally
---------------------------

The default stack fits most environments, but sometimes you need to adapt it:
add another service, change settings or use your own files. Whichever applies,
don't change ``docker-compose.yml`` itself. Keeping your changes in separate
files lets ``git pull`` update the stack without conflicts.

How you do this depends on what you want to achieve:

**Change settings of the existing services**
   Create a ``docker-compose.override.yml`` file. Docker Compose
   `automatically loads this file and merges its changes into your stack
   <https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/>`_.
   The stack repository ships an inactive example file you can copy and
   adjust:

   .. code-block:: console

      $ cp docker-compose.override.yml.dist docker-compose.override.yml

   The override file is for changing settings of the services that the main
   compose file already defines. Loading scenarios is not supported. To load
   a scenario, use the ``COMPOSE_FILE`` variable in your ``.env`` file, as
   described in the :ref:`general usage <general-usage-scenarios>` section
   above.

**Add your own files**
   If you deployed the stack with Docker Compose by cloning the repository,
   you can store files that belong only to your instance in the stack's
   ``local/`` directory, e.g. configuration snippets, custom scenario files,
   scripts, notes or certificates. Git ignores the directory's contents
   except for README.md, so ``git pull`` neither reports nor changes these
   files.

   Files in ``local/`` are not loaded automatically. To use a custom Compose
   file, reference it from the override file or from ``COMPOSE_FILE`` in
   your .env file, using a path such as ``./local/my-file``. Keep in mind
   that setting ``COMPOSE_FILE`` turns off the automatic pickup of the
   override file, see the :ref:`general usage <general-usage-scenarios>`
   section above. Docker Compose resolves relative paths against the
   directory containing the main compose file, including paths used by
   custom scenario files in ``local/``.
