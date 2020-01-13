Install with Docker
*******************

Docker is a container-based software framework for automating deployment of applications.
Our Docker image is a **single container** based application designed to have Zammad **up and running fast for testing purposes**.

Please note that this is a non persistent storage container and **all Zammad data is lost** when you're stopping the container.

If you like to run Docker in production environment try our Docker-compose version: :ref:`install_docker_compose` .

Your Docker environment needs to be up and running.

You can find the image at https://hub.docker.com/r/zammad/zammad/

You need at least 4 GB of RAM to run the container.

Run the Docker Container
========================

Docker run will run a command in a new container, -i attaches stdin and stdout, -t allocates a tty.

Set vm.max_map_count for Elasticsearch
--------------------------------------

::

 sysctl -w vm.max_map_count=262144

.. Tip:: For Mac OS: https://github.com/zammad/zammad-docker/issues/27#issuecomment-455171752

Run docker container
--------------------

::

 docker container run -ti --rm --name zammad -p 80:80 zammad/zammad


That’s it! You’re now using a bash shell inside of a Zammad docker container using the develop branch of the GitHub repo.

To disconnect or detach from the shell without exiting, use the escape sequence Ctrl-p + Ctrl-q.


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user.
