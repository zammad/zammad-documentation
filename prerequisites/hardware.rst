Hardware
********

The hardware requirements to run Zammad effectively vary depending on several
factors, for example:

- Number of users (especially agents and customers)
- Volume of incoming tickets
- Usage of channels
- Installation type
- Used software which is required to run Zammad

There are even more factors which have influence on the performance. This
makes it hard to publish general hardware requirements which are fitting
for all use cases. If you don't want to deal with such things, you should
consider our `hosted Zammad setup <https://zammad.com/en/pricing>`_.

However, you can use the following information as a rough guide. In any case,
more and better hardware ensures that Zammad runs smoothly and the maintenance
breaks for updates should be shorter as well.

Minimum Setup
=============

For a minimalistic Zammad deployment with a PostgreSQL database server, you
should not go below the values below:

* 2 CPU cores
* 4 GB of RAM (+4 GB if you want to run Elasticsearch on the same server)

Recommended Setup
=================

This is a basic setup for up to 40 agents.

* 4 CPU cores
* 6 GB of RAM (+6 GB if you want to run Elasticsearch on the same server)

.. note::

   We can't suggest any disk space recommendations, as this highly depends on
   how you work. Zammad will always try to recognize the same attachments and
   store it just once.

Performance Tuning
==================

As the number of active users on your system grows,
performance will eventually degrade, leading to:

 * delays for outgoing email,
 * long loading times when viewing or creating tickets,
 * stale or out-of-sync search results, or
 * stale or out-of-sync ticket overviews.

You may see modest improvements by
:ref:`setting certain environment variables for Performance Tuning <performance_tuning>`,
such as ``$WEB_CONCURRENCY`` or ``$ZAMMAD_SESSION_JOBS_CONCURRENT``.
