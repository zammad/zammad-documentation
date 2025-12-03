Proxy and Connections
======================

If you want to route Zammad's traffic over a proxy, you can find information
about it on this page.

Proxy Variables
---------------

The following environment variables can be used to configure proxy settings.
Set it the way you want and adjust the values to your use case:

.. code-block:: sh

   export HTTP_PROXY="http://127.0.0.1:8080"

.. code-block:: sh

   export HTTPS_PROXY="http://127.0.0.1:8080"

.. code-block:: sh

   export ES_JAVA_OPTS="-Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=8080 -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=8080"

Download Dependencies
---------------------

During installation and operation of Zammad, some connections to online services
are required. Depending on your installation method and Zammad configuration,
a connection to the following services is made:

.. csv-table::
   :header: "Address", "Comment"
   :widths: 40, 70

   "artifacts.elastic.co",  "Download of the ingest plugin (only ES < 8)"
   "dl.packager.io",        "Download of OS package (package installation)"
   "go.packager.io",        "As above; new package hosting service"
   "geo.zammad.com",        "Used for geo data"
   "google.com",            "Download of feast days for the calendar"
   "index.rubygems.org",    "Download of gems for ruby"
   "registry.npmjs.org",    "Download of js dependencies"

Test Script
-----------

You can use a script to check the connection state of your system. Run it either
by fetching it from the Zammad repository or by executing the local version on
your Zammad machine:

Remote:

.. code-block:: sh

   curl -fsSL https://raw.githubusercontent.com/zammad/zammad/refs/heads/stable/contrib/packager.io/test_download_dependencies_connection.sh | sh

Local:

.. code-block:: sh

   /opt/zammad/contrib/packager.io/test_download_dependencies_connection.sh
