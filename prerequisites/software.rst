Software
********

If you want to install Zammad, you need the following software.

1. Ruby Programming Language
============================

| Zammad requires Ruby. All required rubygems like ruby on rails are listed in
  the Gemfile.
| The following Ruby version is supported:
| ``Ruby 2.6.6``

.. csv-table:: Zammad/Ruby version compatibility
   :header: "Zammad", "Ruby"
   :widths: 20, 20

   "3.4.1+", "2.6.6"
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
   "OpenSuSE / SLES", "Leap 42.3 / 12"
   "Ubuntu", "16.04, 18.04 & 20.04"

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

5. Reverse Proxy
================

In a typical web environment today, you use a reverse proxy to deliver the
static content of your application. Only the "expensive" app required HTTP
requests are forwarded to the application server.

The following reverse proxies are supported:

* Nginx 1.3+
* Apache 2.2+

6. Elasticsearch (optional)
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

   "4.0+", "6.5-7.12"
   "3.4-3.6", "5.5–7.9"
   "3.3", "2.4–7.6"
   "3.2", "2.4–7.5"
   "3.1", "2.4–7.4"
   "2.0–3.0", "2.4–5.6"

An Elasticsearch plugin is required to index the contents of email attachments:
``ingest-attachment``.
