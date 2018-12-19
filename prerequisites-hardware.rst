Hardware
********

You can run Zammad on bare metal or on a virtual machine. Choose what you prefer.

For Zammad and a database server like PostgreSQL we recommend at least:
=======================================================================

* 2 CPU cores
* 2 GB of RAM (+2 GB if you want to run Elasticsearch on the same server)

For optimal performance up to 40 agents:
========================================

* 4 CPU cores
* 4 GB of RAM (+4 GB if you want to run Elasticsearch on the same server)

Of course at the end it depends on acutal load of concurent agents and data traffic.

.. Note:: We can't suggest any disk space recommendations, as this highly depends on how you work. Zammad will always try to recognize the same attachments and store it just once. 
