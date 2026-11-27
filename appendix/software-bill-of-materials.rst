Software Bill of Materials
==========================

A software bill of materials (SBOM) lists the third-party components that
ship inside a product: which dependencies, in which versions. Administrators
feed it to vulnerability scanners or hand it out to customers who ask for a
bill of materials of their Zammad installation.

Availability and Format
-----------------------

From Zammad 7.4 on, every DEB/RPM package and every Docker image contains an
SBOM in CycloneDX format at ``/opt/zammad/sbom.cdx.json``. It is generated
during the build of the package or image with
`syft <https://github.com/anchore/syft>`_.

What It Covers
--------------

Zammad's SBOM includes the software that ships inside the package or the
image itself.

The SBOM of a package lists Ruby, the Ruby gems, Node.js with its bundled npm
and pnpm, and the JavaScript dependencies of the frontend. Those only exist
compiled into the assets, so they are merged into the SBOM from the lockfile
at build time.

The SBOM of a Docker image covers the same components plus the Debian
packages of the image, e.g. the bundled nginx. Node.js, npm and pnpm are not
listed there, because the image does not contain them.

The following are out of scope of Zammad's SBOM:

- Source installations. No package or image build takes place, so no
  SBOM is provided for them.
- Services next to Zammad: PostgreSQL, Redis, Elasticsearch, Memcached, the
  web server of a package installation, and the third-party images of the
  Docker Compose stack and the Helm chart.
- Add-on packages that you install later through the admin interface. Docker
  images built with add-on packages in ``packages/install`` do include their
  gems.

Getting the SBOM
----------------

Package installation
   The file is part of the package and lives at
   ``/opt/zammad/sbom.cdx.json``.

Docker image
   Create a container from the image without starting it, copy the file
   out and remove the container again:

   .. code-block:: console

      $ container=$(docker create ghcr.io/zammad/zammad:<version>)
      $ docker cp "$container":/opt/zammad/sbom.cdx.json sbom.cdx.json
      $ docker rm "$container"

Kubernetes
   For a Helm release named ``zammad``:

   .. code-block:: console

      $ kubectl exec deploy/zammad-railsserver -c zammad-railsserver -- \
        cat /opt/zammad/sbom.cdx.json > sbom.cdx.json

Scanning the SBOM
-----------------

Scanners that read CycloneDX take the file as input. `Trivy
<https://trivy.dev/>`_, for example, reports the known vulnerabilities of the
listed components:

.. code-block:: console

   $ trivy sbom sbom.cdx.json

The scan answers what the shipped versions are exposed to. It does not check
the state of a running installation.

Trust
-----

There is no separate signature or checksum for the SBOM. Its origin is
covered by the delivery channel: DEB and RPM packages arrive from a signed
package repository, and Docker images can be pinned by their digest. The digest
identifies the exact content of an image, but it does not verify who published
it. Use a digest obtained from a trusted source, as pinning alone is not proof
of origin.
