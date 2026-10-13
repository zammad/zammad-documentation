Reporting Tools (Third party)
=============================

Zammad stores its data in Elasticsearch, which opens it up to a wide range
of third party reporting and visualization tools.

.. figure:: /images/appendix/reporting-tools/grafana-sample-dashboard-with-graphs.png
   :alt: Screenshot showing a Grafana dashboard fed from Zammad data.
   :align: center
   :width: 80%

   Use third party reporting tools to boost your reporting capabilities.

Both self-hosted and Zammad SaaS (hosted) customers can connect reporting
tools to their instance. The only requirement is access to your
Elasticsearch index: self-hosted customers have it by default, while hosted
customers can enable it via the
:admin-docs:`Elasticsearch (SaaS) integration
</system/integrations/elasticsearch.html>` (Plus or Ultimate plans).

Getting started
---------------

You need:

- An instance of the reporting tool of your choice (hosted or self-hosted)
- Read access to your Elasticsearch index

.. warning::

   Never expose Elasticsearch to the public if you're not sure how to do it.
   Especially **never** without authentication! Zammad stores **very
   sensitive** information within the Elasticsearch index.

We will not cover core configurations of each tool and can't support you
with the configuration of your specific third party tool. For a deeper
insight, have a look at our
:doc:`/install/elasticsearch/indexed-attributes`.

Known to be working
-------------------

.. toctree::
   :maxdepth: 1

   /appendix/reporting-tools-thirdparty/grafana

.. note::

   **Want to use another tool?**

   Don't worry, if it does support Elasticsearch indexes, you may be good to
   go! See :doc:`/install/elasticsearch/indexed-attributes` for available
   indexes.
