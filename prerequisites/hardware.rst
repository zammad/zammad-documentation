Hardware
********

You can run Zammad on bare metal or on a virtual machine. Choose what you prefer.

For Zammad and a database server like PostgreSQL we recommend at least:
=======================================================================

* 2 CPU cores
* 4 GB of RAM (+4 GB if you want to run Elasticsearch on the same server)

For optimal performance up to 40 agents:
========================================

* 4 CPU cores
* 6 GB of RAM (+6 GB if you want to run Elasticsearch on the same server)

Of course at the end it depends on acutal load of concurent agents and data traffic.

.. note:: We can't suggest any disk space recommendations, as this highly depends on how you work. Zammad will always try to recognize the same attachments and store it just once.

Performance Tuning
==================

As the number of active users on your system grows,
performance will eventually degrade, leading to:

   * delays for outgoing email,
   * long loading times when viewing or creating tickets,
   * stale or out-of-sync search results, or
   * stale or out-of-sync ticket overviews.

You may see modest improvements by
:doc:`setting certain environment variables > Performance Tuning </appendix/configure-env-vars#performance-tuning>`,
such as ``$WEB_CONCURRENCY`` or ``$ZAMMAD_SESSION_JOBS_CONCURRENT``.
