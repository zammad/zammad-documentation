Reporting with Grafana
======================

Grafana is a third party analytics/visualization application you can connect
to Zammad (precisely: Elasticsearch). It can access the Elasticsearch index
and visualize your Zammad data. If you don't want to start from scratch,
Zammad provides ready-made sample dashboards that you can import into your
Grafana instance within minutes.

Prerequisites
-------------

- A running instance of Grafana (hosted or self hosted) in version 10.3 or
  higher
- Read access to your Elasticsearch index

.. warning::

   Never expose Elasticsearch to the public if you're not sure how to do it.
   Especially **never** without authentication! Zammad stores **very
   sensitive** information within the Elasticsearch index.

This guide expects all requirements to be up and running. For a deeper
insight, have a look at our :doc:`/install/elasticsearch/indexed-attributes`
and the `documentation of Grafana <https://grafana.com/docs/>`_.

Setup
-----

Data sources are Grafana's connection settings for external data providers
and are managed under *Connections > Data sources*. A data source is a
prerequisite to have a dashboard showing you numbers.

Add a data source of type *Elasticsearch* and provide the following information:

- URL: the URL of your Elasticsearch instance, e.g. ``http://localhost:9200``
- Authentication: select the correct method and provide your credentials
- Index name: ``zammad_production_*`` (replace the prefix to match your
  installation, see note below)
- Time field name: ``created_at`` (required by Grafana, but overridden per
  panel by the dashboards below, so any valid field name works)

After configuring it, click on ``Save & test``. If everything is fine, you
should see a message like "Elasticsearch data source is healthy".

The dashboards pick their own index fields and time stamps, so no further data
source tuning is required. All sample dashboards below work with a single
Elasticsearch data source. If you build your own dashboards and want
separate data sources per index, feel free to do so.

.. note:: **Not sure about your index prefix?**

   The default prefix is ``zammad_production``. It only differs if the index
   namespace was changed after installation, e.g. to separate multiple
   Zammad instances on a single Elasticsearch server.

   To double check, query your Elasticsearch instance (replace
   ``http://localhost:9200`` with the HTTP type and URL of your setup):

   .. code-block:: console

      $ curl http://localhost:9200/_aliases?pretty=true

   This returns a list of your indexes, which looks similar to the
   following:

   .. code-block:: json

      {
        "zammad_production_ticket" : {
          "aliases" : { }
        },
        "zammad_production_ticket_state" : {
          "aliases" : { }
        }
      }

Dashboards
----------

A dashboard can be imported to Grafana in different ways. You can copy/paste
raw JSON content, upload a JSON file or fetch it by its ID (easiest way).
You can find the dashboard templates for Zammad in
`GitHub <https://github.com/zammad/grafana-dashboards>`_ or grafana.com.

To import a dashboard, click the **➕** icon in the top right corner of your
Grafana instance and choose **Import dashboard**. You can either upload the
json file you downloaded from GitHub or enter the grafana.com ID given
below. Grafana then fetches the dashboard and shows a settings page where
you can provide a name and target folder before importing.

Below the name settings, Grafana lists the data sources the dashboard
requires. Just assign your created data source to every entry. The names in
this list are placeholders from the dashboard creation, so the mapping (not
the names) decides which data your panels show.

Empty panels after import usually mean a mapped data source doesn't match or
your instance has no data of that kind yet: an unmatched mapping imports
fine, but every affected panel stays empty. You can fix the mapping any time
via the panel's edit dialog.

Tickets
^^^^^^^

Grafana.com ID: ``14222``

.. figure:: /images/appendix/reporting-tools/grafana/dashboard/tickets.png
   :align: center
   :alt: Screenshot showing the Ticket dashboard with demo data.

Provides ticket opening and closing rates, created articles, ticket and
article meta information as well as SLA insights (the latter requires the
SLA function to be active).

Chats
^^^^^

Grafana.com ID: ``14224``

.. figure:: /images/appendix/reporting-tools/grafana/dashboard/chat-sessions.png
   :align: center
   :alt: Screenshot showing the Chat dashboard with demo data.

Provides chat session statistics, e.g. session creations, chat tags, agents
and origins as well as average chatting time.

CTI log
^^^^^^^

Grafana.com ID: ``14223``

.. figure:: /images/appendix/reporting-tools/grafana/dashboard/calls.png
   :align: center
   :alt: Screenshot showing the CTI dashboard with demo data.

Provides call statistics, e.g. calls per direction, average waiting and
talking times as well as top callers and answerers.
