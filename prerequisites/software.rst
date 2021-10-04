Software
********

If you want to install Zammad, you need the following software.

.. note::

   Most of below software versions (unless stated as specific version) 
   are minimum requirements of Zammad. We strongly encourage you to use 
   most current possible versions that *are not end of life*.

1. Ruby Programming Language
============================

| Zammad requires Ruby. All required rubygems like ruby on rails are listed in
  the Gemfile.
| The following Ruby version is supported:
| ``Ruby 2.7.4``

.. csv-table:: Zammad/Ruby version compatibility
   :header: "Zammad", "Ruby"
   :widths: 20, 20

   "5.0+", "2.7.4"
   "3.4.1 - 4.1", "2.6.6"
   "3.4.0", "2.6.5"
   "3.1 - 3.3", "2.5.5"
   "2.5 - 3.0", "2.4.4"

2. Supported distributions
==========================

Below you can find all distributions Zammad provides packages for.

.. csv-table:: Supported operating system matrix
   :header: "Distribution", "Versions"
   :widths: 20, 20

   "CentOS", "7 & 8"
   "Debian", "9 & 10"
   "⚠ OpenSuSE / SLES", "Leap 42.3 / 12"
   "Ubuntu", "16.04, 18.04 & 20.04"

.. warning:: **⚠ SuSE users be aware**

   Due to the age of SLES12 / Leap 42.3 you may no longer be able to satisfy
   all (soft) dependencies of Zammad.

   If you're not running a docker-compose or package installation please
   consider changing to a different distribution that's supported.

.. note:: **🤓 What about my specific distribution?! It's so cool!**

   If you distribution is not listed, you can still install Zammad.
   For this you can either use :doc:`Docker-Compose </install/docker-compose>`
   or :doc:`Source </install/source>` installation.

   We try to provide all current distributions that are supported by
   `Packager.io <https://packager.io/>`_. This means that we can't always
   provide support for your favorite system.

.. _package_dependencies:

3. Package Dependencies
=======================

The below dependencies need to be installed on your system.
If you're using the package install, the packages below will automatically
installed with the Zammad-Package.

.. code-block:: sh

   # Debian 9 & 10, Ubuntu 16.04, 18.04 & 20.04
   $ apt install libimlib2

   # openSUSE
   $ zypper install imlib2

   # CentOS 7 & 8
   $ yum install epel-release
   $ yum install imlib2

.. note::

   | ``libimlib2-dev`` **or** ``imlib2-devel`` are no longer required.
   | *However:* If you have to use ``bundle install`` for e.g. custom Gems or
     development, you'll need to install it!

4. Database Server
==================

Zammad will store all content in a Database.
You can choose between the following database servers:

* MySQL 5.7+
* MariaDB 10.3+
* PostgreSQL 9.3+

.. note::

   We tend to recommend PostgreSQL. For the last 10 years we had the best
   experience with it.

   **Zammad requires UTF-8 for its database.**

.. warning:: **Required configuration for MySQL/MariaDB:**

   * Use ``UTF-8`` encoding - ``utf8mb4`` for example will fail!
   * Set ``max_allowed_packet`` to a value larger than the default of 4 MB
     (64 MB+ recommended).

5. Node.js
==========

.. note:: This soft dependency was introduced with Zammad 5.0.

Node.js 10+ is required for asset compiling.

.. hint:: **🔨 No changes to JS or CSS files?**

   If you don't require to change any javascript or stylesheed files you'll
   be fine without this package. It's only required if you have to run
   ``rake assets:precompile`` on your system.

   .. warning:: Node.js **is** required on source code installations.

.. csv-table:: Zammad/Node.js version compatibility
   :header: "Zammad", "Node.js"
   :widths: 20, 20

   "5.0+", "10.0+"

6. Reverse Proxy
================

In a typical web environment today, you use a reverse proxy to deliver the
static content of your application. Only the "expensive" app required HTTP
requests are forwarded to the application server.

The following reverse proxies are supported:

* Nginx 1.3+
* Apache 2.2+

7. Elasticsearch (optional)
===========================

Zammad uses Elasticsearch to

   1) make search faster
   2) support advanced features like reports
   3) searching by email attachment contents

This becomes increasingly important as the number of tickets in your system
gets larger and larger.

This dependency is optional but strongly recommended;
Zammad will work without it,
but search performance will be degraded, and some features will be disabled.

.. hint:: 📦 **If you install Zammad via package manager...**

   It’s perfectly safe to manually override the Elasticsearch dependency.
   The appropriate command line flag will depend on your platform
   (*e.g.,* ``--force``, ``--ignore-depends``, ``--skip-broken``);
   check your package manager’s manpage to find out.

.. warning::

   Please note that if you do not install and use Elasticsearch, the search
   will be very limited! We recommend using Elasticsearch, as it will boost the
   usage of Zammad greatly!

.. note::

   Starting with Zammad 4.0 you can decide if you want to use
   ``elasticsearch`` or ``elasticsearch-oss``. Please note that CentOS
   **requires** ``elasticsearch``.


.. csv-table:: Zammad/Elasticsearch version compatibility
   :header: "Zammad", "Elasticsearch"
   :widths: 20, 20

   "5.0+", "7.8+"
   "4.0-4.1", "6.5-7.12"
   "3.4-3.6", "5.5–7.9"
   "3.3", "2.4–7.6"
   "3.2", "2.4–7.5"
   "3.1", "2.4–7.4"
   "2.0–3.0", "2.4–5.6"

An Elasticsearch plugin is required to index the contents of email attachments:
``ingest-attachment``.

8. Optional tools of improved caching and distribution
======================================================

.. note:: **Below support was introduced by Zammad 5.0**

   These tools are optional and may make a lot of sense in big
   environments even if you decide against distributed use cases.

   We consider this topic as :ref:`performance_tuning`.


8.1 Redis
~~~~~~~~~

   Using `Redis <https://redis.io/>`_ allows you to store all web socket
   information in Redis instead of your file system.

      .. note::

         Configuration and installation is out of our scope.
         Please follow the official vendor guides and ensure to have a
         tight security on your installation.

8.2 Memcached
~~~~~~~~~~~~~

   Instead of storing Zammads cache files within your filesystem, you can also
   do so in `Memcached <https://memcached.org/>`_. This can allow you to restrict
   the size of your cache directories to improve performance.

      .. note::

         Configuration and installation is out of our scope.
         Please follow the official vendor guides and ensure to have a
         tight security on your installation.
