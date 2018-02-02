Software
********

If you want to install Zammad, you need the following software.

1. Ruby Programming Language
============================

Zammad requires Ruby. All required rubygems like ruby on rails are listed in the Gemfile.
The following Ruby version is supported:

* Ruby 2.4.2


2. Database Server
==================

Zammad will store all content in an RDBMS.
You can choose between the following products:

* MySQL 5.6+
* MariaDB 10.0+
* PostgreSQL 9.1+

Side note: We tend to recommend PostgreSQL. For the last 10 years we had the best experience with it.


3. Reverse Proxy
================

In a typical web environment today, you use a reverse proxy to deliver the static content of your application.
Only the "expensive" app required HTTP requests are forwarded to the application server.

The following reverse proxies are supported:

* Nginx 1.3+
* Apache 2.2+


4. Elasticsearch
================

For excellent search performance we use Elasticsearch.
The following Elasticsearch versions are supported:

* Elasticsearch 2.4 up to 5.5 with mapper-attachments plugin
* Elasticsearch 5.6 with ingest-attachment plugin
