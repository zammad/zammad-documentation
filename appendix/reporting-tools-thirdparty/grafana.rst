Grafana
=======

Grafana allows you to query, visualize and alert on metrics your Zammad
installation stores within the Elasticsearch indexes.

.. figure:: /images/appendix/reporting-tools/grafana/grafana-dashboard-several-metas.png
   :alt: Sample Dashboard with metrics from a Zammad instance.
   :width: 90%
   :align: center

.. include:: include-limitations.rst

Overview
--------

**Quickly jump to...**
   * `Setting up required data sources`_
   * `The Dashboards`_

You will need
   * A Grafana 10.3+ instance (hosted or self hosted)

.. include:: include-requirements.rst

Setting up required data sources
--------------------------------

.. hint:: **🤓 You may not need all data sources**

**Before we start:** The data sources always follow the same scheme. We reduced
below information to ``name``, ``time field name`` and ``index name``.
Everything else relies on your environment and is out of our scope.

   .. note::

      Please replace ``zammad_production_`` with your fitting prefix.

ES - Chat Sessions:
   | Index name: ``zammad_production_chat_session``
   | Time field name: ``created_at``

ES - CTI Log:
   | Index name: ``zammad_production_cti_log``
   | Time field name: ``start_at``

ES - Ticket Articles:
   | Index name: ``zammad_production_ticket``
   | Time field name: ``article.created_at``

ES - Tickets by closed_at:
   | Index name: ``zammad_production_ticket``
   | Time field name: ``close_at``

ES - Tickets by created_at:
   | Index name: ``zammad_production_ticket``
   | Time field name: ``created_at``

ES - Tickets by first_response_at:
   | Index name: ``zammad_production_ticket``
   | Time field name: ``first_response_at``

With above data sources you basically have everything you need to start
building your own dashboards. 🎉

   .. tip:: **🤓 Not sure about your index names?**

      Querying your elasticsearch like this and replace ``localhost:9200`` with
      the IP/URL of your setup:

      .. code-block:: console

         $ curl http://localhost:9200/_aliases?pretty=true

      This will return a list that looks similar to the following:

      .. code-block:: json

         {
           "zammad_production_knowledge_base_translation" : {
             "aliases" : { }
           },
           "zammad_production_ticket_priority" : {
             "aliases" : { }
           },
           "zammad_production_stats_store" : {
             "aliases" : { }
           },
           "zammad_production_organization" : {
             "aliases" : { }
           },
           "zammad_production_cti_log" : {
             "aliases" : { }
           },
           "zammad_production_group" : {
             "aliases" : { }
           },
           "zammad_production_knowledge_base_answer_translation" : {
             "aliases" : { }
           },
           "zammad_production_ticket" : {
             "aliases" : { }
           },
           "zammad_production_ticket_state" : {
             "aliases" : { }
           },
           "zammad_production_chat_session" : {
             "aliases" : { }
           },
           "zammad_production_user" : {
             "aliases" : { }
           },
           "zammad_production_knowledge_base_category_translation" : {
             "aliases" : { }
           }
         }

The Dashboards
--------------

If you want to get inspired, you can also use our sample dashboards as
mentioned below. These dashboards can also be found on
`GitHub <https://github.com/zammad/grafana-dashboards>`_.

Importing an existing Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to **➕ → Import** and either upload the json file you received or
use the grafana.com ID. During importing you can provide a dashboard name
and folder. You'll also be asked to map the data sources to your environment.
If you used our data source names above, you can simply search for the same name.

   .. figure:: /images/appendix/reporting-tools/grafana/import-existing-dashboard.gif
      :alt: Screencast showing how to import existing dashboards by grafana.com ID
      :width: 90%
      :align: center

      Importing existing dashboards by ID

Ticket statistics
^^^^^^^^^^^^^^^^^

   .. tip:: **🤓 Grafana.com ID:** ``14222``

   .. figure:: /images/appendix/reporting-tools/grafana/dashboard/tickets.png
      :width: 80%
      :align: center
      :alt: Screenshot showing the Ticket dashboard with demo data.

This dashboard provides graphs for:
   * ticket opening and closing [2]_
   * created articles
   * ticket SLA (in time *and* violation) per type [2]_ [3]_

It also contains specific ticket and article meta information:
   * ticket group distribution
   * sender ratio (e.g. Customer / Agent) [1]_
   * article type ratio (e.g. email, phone) [1]_
   * article content type
   * escalation ratios [2]_
   * average first response, update time and close time [3]_
   * top 10

      * organization of ticket customer [2]_
      * ticket customers [2]_
      * ticket owners [2]_
      * average accounted time on ticket
      * ticket tags [2]_
   * last 10 escalated tickets

Required data sources:
   * ``ES - Ticket Articles``
   * ``ES - Tickets by created_at``
   * ``ES - Tickets by closed_at``

.. [1] Specific reference IDs are not the same on every instance and thus the
       panel may not work or show incorrect data. Check the panels description
       on how to find our the relations on your system.
.. [2] Some values are not available as time series information.
       This means we can only display the *last* value of the field in question.
.. [3] Requires SLA function to be active.
       Negative values indicate SLA violations.

Chat-Session statistics
^^^^^^^^^^^^^^^^^^^^^^^

   .. tip:: **🤓 Grafana.com ID:** ``14224``

   .. figure:: /images/appendix/reporting-tools/grafana/dashboard/chat-sessions.png
      :width: 80%
      :align: center
      :alt: Screenshot showing the Chat dashboard with demo data.

This dashboard provides graphs for:
   * Chat session creations

It also contains specific chat session meta information:
   * top 10

      * chat tags
      * chat agents
      * chat exit pages
      * city origins
   * chat topic ratio
   * average number of messages within chat-sessions
   * average chatting time
   * World map with chat origin countries

Required data sources:
   * ``ES - Chat Sessions``

CTI-Log statistics
^^^^^^^^^^^^^^^^^^

   .. tip:: **🤓 Grafana.com ID:** ``14223``

   .. figure:: /images/appendix/reporting-tools/grafana/dashboard/calls.png
      :width: 80%
      :align: center
      :alt: Screenshot showing the CTI dashboard with demo data.

This dashboard provides graphs for:
   * number of calls per direction (in / out)

It also contains specific chat session meta information:
   * call ratio (in / out)
   * average waiting time
   * average talking time
   * top 10

      * callers (in)
      * call answerers (in)

Required data sources:
   * ``ES - CTI Log``
