Troubleshooting and FAQ
***********************

This guide will discuss frequently asked questions and how to resolve common problems with Zammad.


Data missing from the Web-UI
============================

A commonly reported issue is data missing from the Web-UI.
This could be Tickets, Articles, Users or anything else :doc:`indexed by Elasticsearch </install/elasticsearch/indexed-attributes>` and can be caused by missing or incomplete indexes.

If you are experiencing this issue and installed Elasticsearch according to :doc:`/install/elasticsearch`, please follow these steps to make sure Elasticsearch is working correctly.

Step 1: Verify Elasticsearch is running
   .. code-block:: sh

      # check elasticsearch status
      $ systemctl status elasticsearch

   .. note:: 
      This should output something like the following, make sure it says ``Active: active (running)``:

      .. code-block:: sh
         :emphasize-lines: 3

         ● elasticsearch.service - Elasticsearch
            Loaded: loaded (/lib/systemd/system/elasticsearch.service; enabled; vendor preset: enabled)
            Active: active (running) since Tue 2021-07-20 09:38:21 UTC; 1h 4min ago
            Docs: https://www.elastic.co
            Main PID: 1790 (java)

      Otherwise, try starting it and check again:

      .. code-block:: sh

         # restart elasticsearch and check status
         $ systemctl restart elasticsearch
         $ systemctl status elasticsearch

      .. warning::
         | If this fails, your Elasticsearch installation is probably broken.
         | Try completely purging and reinstalling Elasticsearch according to :doc:`/install/elasticsearch`


Step 2: Verify the ingest-attachment plugin is installed correctly
   .. code-block:: sh

      # list installed elasticsearch plugins
      $ /usr/share/elasticsearch/bin/elasticsearch-plugin list

   .. note:: 
      The output should include ``ingest-attachment``.

      Otherwise, try reinstalling the ``ingest-attachment`` plugin and check again:

      .. code-block:: sh
      
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin remove ingest-attachment
         $ /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

         $ systemctl restart elasticsearch

         $ /usr/share/elasticsearch/bin/elasticsearch-plugin list

Step 3: Verify Zammad can access Elasticsearch and rebuild the indexes
   .. code-block:: sh

      # force zammad to drop and rebuild the elasticsearch indexes
      $ zammad run rake searchindex:rebuild

   .. note:: 
      This should start rebuilding the indexes and output it's progress:

      .. code-block:: sh

         drop indexes...done
         delete pipeline (pipeline)... done
         create indexes...done
         create pipeline (pipeline)... done
         reload data...
            reload User
               - started at 2021-07-20 11:18:12 UTC

         [...]

      | Depending on the system performance and amount of data, this can take a while to complete.
      | Please let this task finish completely and wait until it drops you back to the console.

      .. warning::
         | If this fails or throws an error, there might be something else wrong with your installation.
         | Make sure you followed the complete Elasticsearch set up and integration procedure according to :doc:`/install/elasticsearch`

| After completing these steps, you should have verified your Elasticsearch installation is running and rebuilt the indexes.
| If this does not resolve your issue, please see :ref:`troubleshooting-unsuccessful`.

.. _troubleshooting-unsuccessful:

Troubleshooting unsuccessful or issue not described
===================================================

If you can't solve your issue using the provided troubleshooting steps or can't find your particular issue described here, feel free to `ask the community <https://community.zammad.org>`_ for technical assistance.