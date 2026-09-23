Troubleshooting and FAQ
=======================

This guide will discuss frequently asked questions and how to resolve common
problems with Elasticsearch.

.. note:: 🤓 Troubleshooting unsuccessful or issue not described?

   If you can't solve your issue using the provided troubleshooting steps or
   can't find your particular issue described here, feel free to
   `ask the community <https://community.zammad.org>`_ for technical assistance.

Data Missing From the Web-UI / Search Data Missing or Incomplete
----------------------------------------------------------------

A commonly reported issue is data missing from the Web-UI.
This could be tickets, articles, users or anything else
:doc:`indexed by Elasticsearch </install/elasticsearch/indexed-attributes>`
and can be caused by missing or incomplete indexes.

If you are experiencing this issue and installed Elasticsearch according to
:doc:`/install/elasticsearch`, please follow these steps to make sure
Elasticsearch is working correctly.

Verify Elasticsearch is running
   Check Elasticsearch status:

   .. code-block:: console

      $ systemctl status elasticsearch

   This should output something like the following, make sure it says
   ``Active: active (running)``:

   .. code-block:: text
      :emphasize-lines: 3

      ● elasticsearch.service - Elasticsearch
         Loaded: loaded (/lib/systemd/system/elasticsearch.service; enabled; vendor preset: enabled)
         Active: active (running) since Tue 2021-07-20 09:38:21 UTC; 1h 4min ago
         Docs: https://www.elastic.co
         Main PID: 1790 (java)

   Otherwise, try starting it and check again:

   .. code-block:: console

      $ sudo systemctl restart elasticsearch

   .. code-block:: console

      $ sudo systemctl status elasticsearch

   .. warning::

      | If this fails, your Elasticsearch installation is probably broken.
      | Try completely purging and reinstalling Elasticsearch according
         to :doc:`/install/elasticsearch`

Verify Zammad can access Elasticsearch and rebuild the indexes
   Without specifying CPU cores to use:

   .. code-block:: console

      $ zammad run rake zammad:searchindex:rebuild

   With specifying the amount of CPU cores to use (example: 8):

   .. code-block:: console

      $ zammad run rake zammad:searchindex:rebuild[8]

   This should start rebuilding the indexes and output it's progress:

   .. code-block:: text
      :class: no-copybutton

      Dropping indexes... done.
      Deleting pipeline... done.
      Creating indexes... done.
      Creating pipeline... done.
      Reloading data...
         - Chat::Session...
            done in 0 seconds.
         - Cti::Log...
            done in 0 seconds.

      [...]

   Depending on the system performance and amount of data, this can take
   a while to complete. Please let this task finish completely and wait until
   it drops you back to the console.

   If this fails or throws an error, there might be something else
   wrong with your installation.
   Make sure you followed the complete Elasticsearch set up and
   integration procedure according to :doc:`/install/elasticsearch`.

.. tip::

   In many situations where you're not successful with above steps,
   you may want to check Elasticsearch's log file:
   ``/var/log/elasticsearch/elasticsearch.log``.

| After completing these steps, you should have verified your Elasticsearch
  installation is running and rebuilt the indexes. If this does not resolve your
  issue, feel free to `ask the community <https://community.zammad.org>`_.
