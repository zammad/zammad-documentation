Software
********

If you want to install Zammad, you need the following software.

1. Ruby Programming Language
============================

Zammad requires Ruby. All required rubygems like ruby on rails are listed in the Gemfile.
The following Ruby version is supported:

* Ruby 2.6.5

.. csv-table:: Zammad/Ruby version compatibility
   :header: "Zammad", "Ruby"
   :widths: 20, 20

   "3.4+", "2.6.5"
   "3.1 - 3.3", "2.5.5"
   "2.5 - 3.0", "2.4.4"

2. Package Dependencies
=======================

The below dependencies need to be installed on your system.
If you're using the package install, the packages below will automatically installed with the Zammad-Package.

.. code-block:: sh

   # Debian 8 & 9, Ubuntu 16.04 & 18.04
   $ apt-get install libimlib2 libimlib2-dev

   # openSUSE
   $ zypper install imlib2 imlib2-devel

   # CentOS 7
   $ yum install imlib2 imlib2-devel


3. Database Server
==================

Zammad will store all content in an RDBMS.
You can choose between the following products:

* MySQL 5.6+
* MariaDB 10.0+
* PostgreSQL 9.1+

.. note:: We tend to recommend PostgreSQL. For the last 10 years we had the best experience with it.

.. warning:: **Required configuration for MySQL/MariaDB:**

   * Use UTF8 encoding. utf8mb4 for example will fail.
   * Set ``max_allowed_packet`` to a value larger than the default of 4 MB (64 MB+ recommended).


4. Reverse Proxy
================

In a typical web environment today, you use a reverse proxy to deliver the static content of your application.
Only the "expensive" app required HTTP requests are forwarded to the application server.

The following reverse proxies are supported:

* Nginx 1.3+
* Apache 2.2+


5. Elasticsearch (optional)
===========================

Zammad uses Elasticsearch to
1) make search faster and
2) support advanced features like reports
or searching by email attachment contents.
This becomes increasingly important
as the number of tickets in your system gets larger and larger.

This dependency is optional but strongly recommended;
Zammad will work without it,
but search performance will be degraded, and some features will be disabled.

.. hint:: 📦 **If you install Zammad via package manager...**

   It’s perfectly safe to manually override the Elasticsearch dependency.
   The appropriate command line flag will depend on your platform
   (*e.g.,* ``--force``, ``--ignore-depends``, ``--skip-broken``);
   check your package manager’s manpage to find out.

.. warning:: Please note that if you do not install and use Elasticsearch, the search will be very limited!
   We recommend using Elasticsearch, as it will boost the usuage of Zammad greatly!


The Elasticsearch support differs on the Elasticsearch and Zammad version you're using:

.. csv-table:: Zammad/Elasticsearch version compatibility
   :header: "Zammad", "Elasticsearch"
   :widths: 20, 20

   "3.4+", "5.5–7.6"
   "3.3", "2.4–7.6"
   "3.2", "2.4–7.5"
   "3.1", "2.4–7.4"
   "2.0–3.0", "2.4–5.6"

An Elasticsearch plugin is required to index the contents of email attachments:

* ``mapper-attachments`` for Elasticsearch 5.5
* ``ingest-attachment`` for Elasticsearch 5.6–7
