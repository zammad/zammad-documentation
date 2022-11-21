Software
********

1. Client requirements
======================

Please note that, while Zammad being a web application, there's some
requirements for your clients. This ensures that Zammad works as expected.

1.1. Supported Browsers
-----------------------

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
   * - Safari 11
     -

.. danger:: ⚠️ Deprecation warning ⚠️

   Zammad 7 will no longer support Internet Explorer 11 environments.
   Users using IE will be forced to use a different browser.

.. note::

   | Zammad heavily uses Javascript which makes it a hard requirement.
   |
   | Browser addons that hook into page content may interfere with Zammads function
     which is not a bug.
   | Google Chromes translation module is known to do
     odd things to especially state names. Use Zammads internal translations
     instead.

1.2. Network requirements
-------------------------

Zammad uses web sockets. Some application firewalls may filter these
connections. This may lead to decreased browser performance.

There's a fallback to Ajax which  causes a higher application server load
and thus should be avoided.

   .. note::

      The "Core workflows" feature of Zammad comes with an `Ajax Mode`_ which
      can be activated separately in case you're having issues with field
      selections.

.. _Ajax Mode:
   https://admin-docs.zammad.org/en/latest/settings/system/frontend.html

2. Server requirements
======================

If you want to install Zammad, you need the following software.

.. note::

   Most of the software versions listed below (unless stated as specific
   version)  are minimum requirements of Zammad. We strongly encourage you to
   use most current possible versions that *are not end of life*.

2.1. Ruby Programming Language
------------------------------

.. hint:: **🤓 Only relevant for source code installations**

   Docker and package installations provide the required ruby dependencies!

| Zammad requires Ruby. All required rubygems like ruby on rails are listed in
  the Gemfile.
| The following Ruby version is supported:
| ``Ruby 3.0.4``

.. csv-table:: Zammad/Ruby version compatibility
   :header: "Zammad", "Ruby"
   :widths: 20, 20

   "5.2+", "3.0.4"
   "5.0 - 5.1", "2.7.4"
   "3.4.1 - 4.1", "2.6.6"
   "3.4.0", "2.6.5"
   "3.1 - 3.3", "2.5.5"
   "2.5 - 3.0", "2.4.4"

2.2. Supported distributions
----------------------------

Below you can find all distributions Zammad provides packages for.

.. csv-table:: Supported operating system matrix
   :header: "Distribution", "Versions"
   :widths: 20, 20

   "CentOS / RHEL", "7 & 8"
   "Debian", "9, 10 & 11"
   "⚠ OpenSuSE / SLES", "Leap 42.3 / 12"
   "Ubuntu", "16.04, 18.04 & 20.04"

.. warning:: **⚠ SuSE users be aware**

   Due to the age of SLES12 / Leap 42.3 you may no longer be able to satisfy
   all (soft) dependencies of Zammad.

   If you're not running a docker-compose or package installation please
   consider changing to a different distribution that's supported.

.. danger:: **☠️ Incompatibility warning for Ubuntu 22.04 LTS ☠️**

   Please note that due to Ubuntu's dependencies, Zammad currently **is not**
   compatible to Ubuntu 22. This affects *all installation types* except
   for docker style installations!

.. note:: **🤓 What about my specific distribution?! It's so cool!**

   If you distribution is not listed, you can still install Zammad.
   For this you can either use :doc:`Docker-Compose </install/docker-compose>`
   or :doc:`Source </install/source>` installation.

   We try to provide all current distributions that are supported by
   `Packager.io <https://packager.io/>`_. This means that we can't always
   provide support for your favorite system.

.. _package_dependencies:

2.3. Package Dependencies
-------------------------

The below dependencies need to be installed on your system.
If you're using the package install, the packages below will automatically
installed with the Zammad-Package.

.. code-block:: sh

   # Debian 9, 10 & 11, Ubuntu 16.04, 18.04 & 20.04
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

2.4. Database Server
--------------------

Zammad will store all content in a Database.
You can choose between the following database servers:

* PostgreSQL 9.3+
* MySQL 5.7+ / MariaDB 10.3+ (⚠️ deprecated with Zammad 7.0+)

.. danger::

   .. include:: /appendix/includes/mysql-deprication-note.rst

   .. include:: /appendix/includes/mysql-deprication-link.rst

.. warning:: **Required configuration for MySQL/MariaDB:**

   * Use ``UTF-8`` encoding - ``utf8mb4`` for example will fail!
   * Set ``max_allowed_packet`` to a value larger than the default of 4 MB
     (64 MB+ recommended).

   You may also want to consider the following settings for your MySQL server::

      innodb_file_format = Barracuda
      innodb_file_per_table = on
      innodb_default_row_format = dynamic
      innodb_large_prefix = 1
      innodb_file_format_max = Barracuda

2.5. Node.js
------------

.. note::

   | This soft dependency was introduced with Zammad 5.0.
   | Package installations come pre-bundled with the correct NodeJS version.
     Unless you require NodeJS on your machine for other projects, a manual
     installation *is not* required.

Node.js is required for asset compiling.

.. hint:: **🔨 No changes to JS or CSS files?**

   If you don't require to change any javascript or stylesheed files you'll
   be fine without this package. It's only required if you have to run
   ``rake assets:precompile`` on your system.

   .. warning:: Node.js **is** required on source code installations.

.. csv-table:: Zammad/Node.js version compatibility
   :header: "Zammad", "Node.js"
   :widths: 20, 20

   "5.2+", "16.0+"
   "5.0 - 5.1", "10.0+"

2.6. Reverse Proxy
------------------

In a typical web environment today, you use a reverse proxy to deliver the
static content of your application. Only the "expensive" app required HTTP
requests are forwarded to the application server.

The following reverse proxies are supported:

* Nginx 1.3+
* Apache 2.2+

2.7. Elasticsearch (optional)
-----------------------------

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

   "5.2+", ">= 7.8, < 9"
   "5.0 - 5.1", ">= 7.8, < 8"
   "4.0-4.1", ">= 6.5, <= 7.12"
   "3.4-3.6", ">= 5.5, <= 7.9"
   "3.3", ">= 2.4, <=7.6"
   "3.2", ">= 2.4, <=7.5"
   "3.1", ">= 2.4, <=7.4"
   "2.0–3.0", ">= 2.4, <=5.6"

An Elasticsearch plugin is required to index the contents of email attachments:
``ingest-attachment``.

2.8. Optional tools of improved caching and distribution
--------------------------------------------------------

.. note:: **The features / integrations below were introduced by Zammad 5.0**

   These tools are optional and may make a lot of sense in big
   environments even if you decide against distributed use cases.

   We consider this topic as :ref:`performance_tuning`.


2.8.1 Redis
~~~~~~~~~~~

   Using `Redis <https://redis.io/>`_ allows you to store all web socket
   information in Redis instead of your file system.

      .. note::

         Configuration and installation is out of our scope.
         Please follow the official vendor guides and ensure to have a
         tight security on your installation.

2.8.2 Memcached
~~~~~~~~~~~~~~~

   Instead of storing Zammads cache files within your filesystem, you can also
   do so in `Memcached <https://memcached.org/>`_. This can allow you to restrict
   the size of your cache directories to improve performance.

      .. note::

         Configuration and installation is out of our scope.
         Please follow the official vendor guides and ensure to have a
         tight security on your installation.
