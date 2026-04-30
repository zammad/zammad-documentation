Proxy and Connections
=====================

Proxy
-----

This section covers the proxy configuration via environment variables. As an
alternative, the proxy configuration is also possible via Zammad UI. You can
find more information about that in the
:admin-docs:`network section of the admin documentation </settings/system/network.html>`.

.. csv-table:: Proxy configuration comparison
   :header: "", "GUI configuration", "Environment variable"
   :widths: 40, 30, 30

   "Host OS access required",                   "No",  "Yes"
   "Automatically excluded loopback addresses", "Yes", "No"
   "Configuration check",                       "Yes", "Manually via test script"
   "Exceptions",                                "Yes", "No"

The following environment variables can be used to configure proxy settings.
Adjust the values according to your environment.

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
   Expects a comma separated list of addresses and supports wildcards. Use
   a leading ``.`` as wildcard for subdomains, e.g. ``.example.com`` would match
   example.com and all of its subdomains. Make sure to include loopback addresses
   to exclude them from being routed via proxy.
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
