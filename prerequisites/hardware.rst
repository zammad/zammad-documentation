Hardware
********

The hardware requirements to run Zammad effectively vary depending on several
factors, for example:

- Number of users (especially agents and customers)
- Volume of incoming tickets
- Usage of channels
- Installation type
- Used software which is required to run Zammad

There are even many more factors which have influence on the performance. This
makes it hard to publish general hardware requirements which are fitting
for all use cases. If you don't want to deal with such things, you should
consider our `hosted Zammad setup <https://zammad.com/en/pricing>`_.

However, you can use the following information as a rough guide.

.. tip:: In any case,
   more and better hardware ensures that Zammad runs smoothly and the
   maintenance breaks for updates should be shorter as well.

.. note::

   We can't make any disk space recommendations, as this highly depends on
   how you work. Zammad will always try to recognize the same attachments and
   store it just once.

Minimum Setup
=============

For a minimalistic Zammad deployment with a PostgreSQL database server, you
should not go below the following values:

* 2 CPU cores
* 6 GB of RAM (+4 GB if you want to run Elasticsearch on the same server)

If you run your Elasticsearch instance on a lightweight machine like this and
your RAM got exhausted, you could try a less-than-ideal solution like
`limit the ES heap size <https://www.elastic.co/guide/en/elasticsearch/reference/current/advanced-configuration.html#set-jvm-heap-size>`_.

Example Setup
=============

This is a basic setup for **up to 40 agents**. As mentioned above, it highly
depends on many factors, but this can be a good starting point for dimensioning
your system.

* 4 CPU cores
* 6 GB of RAM (+6 GB if you want to run Elasticsearch on the same server)

Performance Tuning
==================

As the number of active users and/or tickets grows, performance will
eventually degrade. You should have a look at
:ref:`performance tuning section <performance_tuning>` then, or consider upgrade
your setup.
