Reporting Tools (Third party)
=============================

This guide will discuss how to set up third party reporting tools with Zammad.

.. figure:: /images/appendix/reporting-tools/grafana-sample-dashboard-with-graphs.png
   :alt: Screenshot showing a Grafana dashboard fed from Zammad data.
   :align: center
   :width: 80%

   Use third party reporting tools to boost your reporting capabilities.

.. IGNORE THE NEXT BLOCK - This functionality is not yet available.
   .. note:: **💰 Availability**

      The following information require either a self-hosted installation or
      a hosted instance with **PLUS** package. If you're a Hosted user, please
      also check :admin-docs:`the Elasticsearch integration </system/integrations/elasticsearch.html>`
      page for information on how to hook your tool to the index.

.. note:: **🚧 Limitations 🚧**

   Please note that this guide expects all requirements to be up and running.
   We will not cover core configurations of each tool. Please also note that
   we can't support you with configuration of your specific third party tool.

   **🤓 Specific use cases**

   You may have specific use cases which we can't cover in this documentation.
   The following sub pages and also our
   :doc:`/install/elasticsearch/indexed-attributes` should provide enough
   information to help you!

Getting Started
---------------

You will need

   * An instance of the reporting tool of your choice (hosted or self-hosted)

.. include:: reporting-tools-thirdparty/include-requirements.rst

Third Party Reporting Tools Known to be Working
-----------------------------------------------

.. toctree::
   :maxdepth: 1

   /appendix/reporting-tools-thirdparty/grafana

.. note::

   **Want to use another tool?**

   Don't worry, if it does support Elasticsearch Indexes, you may be good to go!
   See :doc:`/install/elasticsearch/indexed-attributes` for available indexes.
