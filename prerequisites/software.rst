Software
========

.. include:: /install/includes/hosted-services.rst

1. Client Requirements
----------------------

Please note that, while Zammad being a web application, there's some
requirements for your clients. This ensures that Zammad works as expected.

1.1 Supported Browsers
^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Zammad/Browser version compatibility
   :header-rows: 1
   :widths: 20, 30

   * - Browser
     - Remarks
   * - Firefox 78+
     - (ESR)
   * - (Google) Chrome 83+
     - This also applies for all Chromium based Browsers like Microsoft Edge
   * - Opera 69+
     - (based on Chromium 83)
   * - Microsoft Internet Explorer 11
     - ⚠️ Deprecated, will be removed with Zammad 7
   * - Safari 14.1+
     -

.. danger:: ⚠️ Deprecation warning ⚠️

   Zammad 7 will no longer support Internet Explorer 11 environments.
   Users using IE will be forced to use a different browser.

Please note that Zammad heavily uses Javascript which makes it a hard
requirement. Some browser addons that hook into page content may interfere with
Zammads function which is not a bug.
For example the Google Chrome translation module is known to do odd things,
especially to state names. Use Zammads internal translations instead.

1.2 Network Requirements
^^^^^^^^^^^^^^^^^^^^^^^^

Zammad uses web sockets. Some application firewalls may filter these
connections. This may lead to decreased browser performance.

There's a fallback to Ajax which causes a higher application server load
and thus should be avoided.

In case you're having issues with field selection, you can activate the
:admin-docs:`AJAX Mode for "Core Workflows" </settings/system/frontend.html>`
separately.

2. Server Requirements
----------------------

If you want to install Zammad, you need the following software.

.. note::

   Most of the software versions listed below (unless stated as specific
   version)  are minimum requirements of Zammad. We strongly encourage you to
   use most current possible versions that *are not end of life*.

   Docker and Kubernetes are shipping all dependencies and services by default!

2.1 Supported Distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zammad provides binary packages for the most recent two stable /
long-term-support releases of the supported Linux distributions, until they
reach their end-of-life or until they can no longer provide the technical
requirements for Zammad. Using of the latest supported stable /
long-term-support version is generally recommended.

Below you can find all distributions Zammad provides packages for.

.. csv-table:: Supported operating system matrix
   :header: "Distribution", "Versions"
   :widths: 20, 20

   "CentOS / RHEL", "8 & 9"
   "Debian", "11 & 12"
   "OpenSUSE / SLES", "Leap 15.x / 15"
   "Ubuntu", "20.04, 22.04 & 24.04"

.. warning:: ⚠️ SuSE Tumbleweed **does not** meet Zammad requirements and thus
   **is not** supported!

.. note:: **🤓 What about my specific distribution?! It's so cool!**

   If you distribution is not listed, you can still install Zammad.
   For this you can either use :doc:`Docker-Compose </install/docker-compose>`
   or :doc:`kubernetes </install/kubernetes>` installation.

   We try to provide all current distributions that are supported by
   `Packager.io <https://packager.io/>`_. This means that we can't always
   provide support for your favorite system.

.. _package_dependencies:

2.2 Package Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

The dependencies below need to be installed on your system.
If you're using the package installation method, these packages will
automatically be installed with the Zammad-Package.

.. code-block:: sh

   # Debian & Ubuntu
   $ apt install libimlib2

   # openSUSE
   $ zypper install imlib2

   # CentOS
   $ yum install epel-release
   $ yum install imlib2

.. note::

   | ``libimlib2-dev`` **or** ``imlib2-devel`` are no longer required.
   | *However:* If you have to use ``bundle install`` for e.g. custom Gems or
     development, you'll need to install it!

2.3 Database Server
^^^^^^^^^^^^^^^^^^^

Zammad stores its content in a database. The supported database system is
`PostgreSQL <https://www.postgresql.org/>`_ 10 or newer.

If no PostgreSQL server could be detected, it will be installed automatically
during the package installation.

.. note::
   If you use database connection pooling software like PgBouncer, make sure
   to use a pooling mode that is fully compatible with PostgreSQL. Typically
   this is called "session connection pooling". Transaction-based connection
   pooling is not supported and may lead to errors during database migrations.

2.4 Reverse Proxy
^^^^^^^^^^^^^^^^^

In a typical web environment today, you use a reverse proxy to deliver the
static content of your application. Only the "expensive" app required HTTP
requests are forwarded to the application server.

The following reverse proxies are supported:

* Nginx 1.3+
* Apache 2.2+

.. hint::

   Some configuration is required, please see :doc:`/getting-started/configure-webserver`.

2.5 Redis
^^^^^^^^^

Starting with Zammad 6.0, `Redis <https://redis.io/>`_ is required for
realtime communication via web socket.

The installation and configuration is out of scope of this documentation.
Please follow the official guides and ensure to set it up in a secure way.

.. _prerequisites_elasticsearch:

2.6 Elasticsearch (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zammad uses Elasticsearch to

   1) make the search faster
   2) support advanced features like reports
   3) search for content of email attachments

This becomes increasingly important the higher the number of tickets in your
system gets.

.. warning::
   This dependency is optional but **strongly recommended**!

   Zammad will work without it, but search performance will be degraded and
   the search will be very limited. We recommend using Elasticsearch, as it will
   boost the usage of Zammad greatly!

.. hint:: 📦 **If you install Zammad via package manager...**

   It's perfectly safe to manually override the Elasticsearch dependency.
   The appropriate command line flag will depend on your platform
   (e.g. ``--force``, ``--ignore-depends``, ``--skip-broken``);
   check your package manager's manpage to find out.

.. csv-table:: Zammad/Elasticsearch version compatibility
   :header: "Zammad", "Elasticsearch"
   :widths: 20, 20

   "5.2+", ">= 7.8, < 9"
   "5.0 - 5.1", ">= 7.8, < 8"
   "4.0-4.1", ">= 6.5, <= 7.12"
   "3.4-3.6", ">= 5.5, <= 7.9"
   "3.3", ">= 2.4, <=7.6"
   "3.2", ">= 2.4, <=7.5"
   "3.1", ">= 2.4, <=7.4"
   "2.0-3.0", ">= 2.4, <=5.6"

An Elasticsearch plugin is required for version 7 or older to index the
contents of email attachments: ``ingest-attachment``. Starting with
Elasticsearch 8, it is included by default.

2.7 Memcached
^^^^^^^^^^^^^

Zammad heavily relies on caching to improve performance. This cache can be stored
in the file system without relying on externals services. However, this is only possible
if all services of Zammad are running on the same file system!

In all other cases like deploying Zammad via containers (Docker or Kubernetes) or on separate cluster nodes, a
`Memcached <https://memcached.org/>`_ service is required to store the cache and serve it to all Zammad instances.
The Docker and Kubernetes stacks already include this service.

However, even local file system installations may benefit from Memcached's performance improvements.
You might want to have a look at our :ref:`performance_tuning` section too.

The installation and configuration is out of scope of this documentation.
In case you have to install Memcached manually, please follow the
`official documentation of Memcached <https://docs.memcached.org/>`_.

2.8 GnuPG (optional)
^^^^^^^^^^^^^^^^^^^^
If you want to use the PGP integration for sending and receiving signed and
encrypted emails, you need to install the GnuPG-Tool.
Please have a look at the official `GnuPG website`_.

.. _GnuPG website: https://www.gnupg.org/index.html
