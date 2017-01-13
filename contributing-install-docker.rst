Install with Docker
*******************

Docker is a container-based software framework for automating deployment of applications. 
Our Docker image is a **single container** based application designed to have Zammad **up and running fast for testing proposes**.

If you like to run Docker in production try our Docker-compose version: https://docs.zammad.org/en/latest/install-docker-compose.html

Your Docker environment needs to be up and running.

You can find the image at https://hub.docker.com/r/zammad/zammad/

Run a Docker Container
======================

Docker run will run a command in a new container, -i attaches stdin and stdout, -t allocates a tty, and we’re using the standard Zammad container.

Set vm.max_map_count for Elasticsearch
--------------------------------------

::

 sysctl -w vm.max_map_count=262144

Run docker container
--------------------

::

 docker run -ti -p 80:80 zammad/zammad


That’s it! You’re now using a bash shell inside of a Zammad docker container using the develop branch of the GitHub repo.

To disconnect or detach from the shell without exiting, use the escape sequence Ctrl-p + Ctrl-q.


Go to http://localhost and you'll see:
======================================

* "Welcome to Zammad!", there you need to create your admin user.
