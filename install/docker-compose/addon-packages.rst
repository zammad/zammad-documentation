.. Copyright (C) 2012-2026 Zammad Foundation, https://zammad-foundation.org/

Addon Packages in Docker Images
===============================

Zammad 7.2 and later can include addon packages (``.zpm`` files) in a custom
Docker image. Use packages compatible with the Zammad release you are building.
The package's maintainer is responsible for its compatibility.

Package installation and removal through the web interface are disabled in
containers. Copying code into a running container changes only that container
and loses the changes when it is replaced. Other services, such as the scheduler
and websocket server, also need the same addon code.

The image contains the package code and compiled assets. PostgreSQL stores
package registration and migration state. The ``/opt/zammad/storage`` volume
stores uploaded files; it does not persist addon code. Keep the database and
storage volumes when replacing containers, and include them in your
:doc:`backup procedure </appendix/backup-and-restore/docker-compose>`.

Build the Image
---------------

Build from a complete checkout of the Zammad source for your target release.
This example uses Zammad 7.2.0. Replace the release, package filename and image
tag as appropriate:

.. code-block:: console

   $ git clone --branch 7.2.0 --depth 1 https://github.com/zammad/zammad.git zammad-custom
   $ cd zammad-custom
   $ mkdir -p packages/install packages/uninstall
   $ cp /path/to/my-addon.zpm packages/install/
   $ docker build --build-arg COMMIT_SHA="$(git rev-parse HEAD)" \
       --build-arg BUILD_LABEL=addons -t zammad-custom:7.2.0-addons-1 .

The source Dockerfile unpacks staged packages, installs any additional gems,
regenerates the GraphQL API and compiles assets before creating the runtime
image. ``COMMIT_SHA`` is required; ``BUILD_LABEL`` is optional.
Copying packages into an image derived from the stock runtime image does not
perform these build steps.

Build on the Docker host that will run the stack, or push the image to a registry
accessible to that host. Keep the package files with your build inputs so you
can rebuild the image for a Zammad update.

Deploy with Docker Compose
--------------------------

In your ``zammad-docker-compose`` checkout, set the following variables in
``.env``, keeping your other settings:

.. code-block:: console

   IMAGE_REPO=zammad-custom
   VERSION=7.2.0-addons-1

For a registry image, use its repository path as ``IMAGE_REPO``. The standard
Compose configuration uses these variables for all Zammad services, including
``zammad-init``. Check that local overrides do not select a different image for
any of those services:

.. code-block:: console

   $ docker compose config --images

For an existing installation, take a backup and stop the application services
before applying the new image and its package migrations. Run these commands
from the Compose checkout:

.. code-block:: console

   $ docker compose stop zammad-nginx zammad-railsserver zammad-scheduler zammad-websocket
   $ docker compose run --rm zammad-init
   $ docker compose up -d

For a new installation, ``docker compose up -d`` starts the init service as part
of the normal setup.

The init service processes ``packages/uninstall/`` first, then registers
``packages/install/`` and runs their migrations. It uses the code already built
into the image. Other application services wait for staged packages to be
applied before starting. Check the init output for errors before restoring
access to the application.

Verify Installation
-------------------

Check the running images and init logs:

.. code-block:: console

   $ docker compose ps
   $ docker compose logs zammad-init
   $ docker compose exec zammad-railsserver bundle exec rails r 'pp Package.all.pluck(:name, :version)'

The explicit ``docker compose run --rm zammad-init`` command prints its logs
directly; those logs disappear with that one-off container.
Confirm that the expected package names and versions are registered, and test
the addon's functionality in the application. If registration is missing, check
that the packages were staged before building and that init used the same image
as the application services.

Update Zammad or an Addon
-------------------------

For every Zammad update, build a new image from the new release's source with
compatible packages in ``packages/install/``. Set ``VERSION`` to a new image tag
and repeat the deployment steps above. Retaining database registration does not
put addon code into a new stock image. Do not mount an old application directory
over the new image.

To update an addon, replace its staged file with the new package version and
rebuild using a new image tag. Staged packages with the same or an older version
than the installed package are skipped; this workflow does not downgrade a
package. Test compatibility and migrations before updating production.

Remove an Addon
---------------

Keep the installed version of the package for the removal build. Remove it from
``packages/install/`` and place it in ``packages/uninstall/`` instead. Include
any dependent packages that must also be removed. Build a new image with a new
tag and repeat the deployment steps. The init service uninstalls staged packages
in reverse dependency order and executes their down migrations.

Verify that the package is no longer registered and that removal completed
successfully. In a subsequent image build, omit the removed package from both
staging directories. Simply dropping its files from the image leaves its
database registration and migration state behind.
