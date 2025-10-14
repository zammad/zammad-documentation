Elasticsearch
=============

.. include:: /install/includes/hosted-services.rst

Zammad's search function can be powered by Elasticsearch (which is **highly
recommended**).

The order for a package installation of Zammad is like this:

1. :doc:`Install Elasticsearch (version 9 recommended) <elasticsearch/install-elasticsearch-9>`
2. :doc:`Install Zammad <./package>`
3. :doc:`Connect and configure Elasticsearch <elasticsearch/connect-configure-elasticsearch>`

.. hint:: For a transition period, there is also a
   :doc:`installation guide for Elasticsearch 7 <elasticsearch/install-elasticsearch-7>` available.

.. toctree::
   :maxdepth: 0
   :hidden:

   elasticsearch/install-elasticsearch-7
   elasticsearch/install-elasticsearch-9
   elasticsearch/connect-configure-elasticsearch
