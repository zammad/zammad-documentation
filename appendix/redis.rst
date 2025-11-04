Redis Configuration
===================

Zammad requires Redis to work. During package installation, it is installed
automatically unless there is a Redis installation on the host already. In the
Docker Compose stack, there is a Redis Service included. Both scenarios work out
of the box and should not require adjustments unless your setup differs or you
want to explicitly make adjustments.

Redis Standard Setup
--------------------

For a Redis standard deployment, you can provide one variable: ``REDIS_URL``.
This variable can include IP/URL, a port, a username and password.
Examples:

- ``redis://redis.example.com:1234``
- ``redis://user:password@redis.example.com``

Redis Sentinel Setup
--------------------

The variables in the table don't have default values set. In case you want to
connect Zammad to a Redis Sentinel cluster, only ``REDIS_SENTINELS`` variable is
mandatory, the others are optional.

.. csv-table::
   :header: "Variable", "Explanation", "Example"
   :widths: 15, 20, 30

   ``REDIS_SENTINELS``,         "Mandatory to use Sentinel setup; comma separated IPs/URLs; optional port",     "``sentinel1.example.com:26380``, ``sentinel2.example.com``"
   ``REDIS_SENTINEL_NAME``,     "Name of Sentinel setup; fallback to ``mymaster`` if not provided",             "``custommaster``"
   ``REDIS_SENTINEL_USERNAME``, "Username for Sentinel",                                                        "``sentineluser``"
   ``REDIS_SENTINEL_PASSWORD``, "Password for Sentinel",                                                        "``sentinelpass``"
   ``REDIS_USERNAME``,          "Username for Redis",                                                               "``user``"
   ``REDIS_PASSWORD``,          "Password for Redis",                                                               "``pass``"
