Proxy and Connections
=====================

Proxy
-----

In addition to the proxy configuration via environment variables, Zammad also
includes a proxy configuration via GUI which you can find in the
:admin-docs:`system settings section of the admin docs </settings/system/network.html>`.
Make sure to avoid a conflicting configuration.

Important Information
^^^^^^^^^^^^^^^^^^^^^

- Use the environment variables configuration to cover connections for used
  Ruby gems.
- Use the UI configuration in Zammad to cover connections from Zammad itself.
- If in doubt, set both accordingly.
- There are parts in Zammad which disregard any proxy configuration:

   - WhatsApp
   - Massenversand
   - Zendesk Migrator

Variables
^^^^^^^^^

The following environment variables can be used to configure proxy settings.
Adjust the example values so they fit your environment.

HTTP_PROXY
   Variable for HTTP traffic. Set it to the address of your proxy server,
   including the port. Example:

   .. code-block:: sh

      export HTTP_PROXY="http://127.0.0.1:8080"

HTTPS_PROXY
   Variable for HTTPS traffic. Set it to the address of your proxy server,
   including the port. Example:

   .. code-block:: sh

      export HTTPS_PROXY="http://127.0.0.1:8080"

NO_PROXY
   Variable for addresses that should be accessed directly and without proxy.
   It supports wildcards as well. Provide a comma separated list of addresses.
   Example:

   .. code-block:: sh

      export NO_PROXY="localhost,127.0.0.1,.example.com"

ES_JAVA_OPTS
   Variable for setting a proxy for Elasticsearch. By default, Elasticsearch
   does not communicate to external systems during the operation. However,
   there can be cases where this is needed, for example when downloading the
   ingest plugin for Elasticsearch versions below 8. Example:

   .. code-block:: sh

      export ES_JAVA_OPTS="-Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=8080 -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=8080"

.. hint::
   Depending on your environment, you might want to use the lower case variants
   of the variables as well. If in doubt, set both variants by additionally
   specifying them with the values of the upper case variants, for example:

   .. code-block:: sh

      export http_proxy=$HTTP_PROXY

External Connections
--------------------

Download Dependencies
^^^^^^^^^^^^^^^^^^^^^

During installation and operation of Zammad, some connections to online services
are required. Depending on your installation method and Zammad configuration,
a connection to the following services is made (maybe also helpful for firewall
configuration):

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
^^^^^^^^^^^

You can use a script to check the connection state of your system.
It tries to connect to the services mentioned above and shows the
result. If every connection was successful, it displays a checkmark for each
contacted service. Run it either by fetching it from the Zammad repository or
by executing the local version on your Zammad machine.

Fetch script from remote
   .. code-block:: sh

      curl -fsSL https://raw.githubusercontent.com/zammad/zammad/refs/heads/stable/contrib/packager.io/test_download_dependencies_connection.sh | sh

Use local script
   .. code-block:: sh

      /opt/zammad/contrib/packager.io/test_download_dependencies_connection.sh
