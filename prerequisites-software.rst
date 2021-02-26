Software
********

If you want to install Zammad, you need the following software.

1. Ruby Programming Language
============================

Zammad requires Ruby. All required rubygems like ruby on rails are listed in the Gemfile.
The following Ruby version is supported:

* Ruby 2.5.5

.. Warning:: We changed our Ruby dependency with Zammad 3.1. Earlier Zammad-Versions require Ruby 2.4.4.

2. Package Dependencies
=======================

The below dependencies need to be installed on your system.
If you're using the package install, the packages below will automatically installed with the Zammad-Package.

.. Note:: The below package dependency was added with Zammad 2.9 which improves image previews.

.. Warning:: Please note that upgrading from Zammad 2.8 and earlier might fail, because your system does not satisfy the new dependencies. 
  Below installation commands will help you out (you can update normally afterwards)

Debian 8 & 9, Ubuntu 16.04 & 18.04
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  apt-get install libimlib2 libimlib2-dev


OpenSuSe
^^^^^^^^

::

  zypper install imlib2 imlib2-devel


CentOS 7
^^^^^^^^

::

  yum install imlib2 imlib2-devel


MacOS
^^^^^

* Install via Homebrew

::

 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
 brew install imlib2


3. Database Server
==================

Zammad will store all content in an RDBMS.
You can choose between the following products:

* MySQL 5.6+
* MariaDB 10.0+
* PostgreSQL 9.1+

.. Note:: We tend to recommend PostgreSQL. For the last 10 years we had the best experience with it.

.. Warning:: **Required configuration for MySQL/MariaDB:**

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

.. Note:: Package install will insist on installing elasticsearch, you can break dependencies during install if needed.

.. Warning:: Please note that if you do not install and use Elasticsearch, the search will be very limited!
  We recommend using Elasticsearch, as it will boost the usuage of Zammad greatly!

For excellent search performance we use Elasticsearch.
The following Elasticsearch versions are supported:

* Elasticsearch 2.4 up to 5.5 with ``mapper-attachments`` plugin
* Elasticsearch 5.6, 6.x & 7.x with ``ingest-attachment`` plugin

.. Warning:: Please note that Elasticsearch 6.x and 7.x support came with Zammad 3.1.
  If you try to use Elasticsearch newer than 5.6.x on Zammad 3.0 and earlier, your search index will **not work**.
