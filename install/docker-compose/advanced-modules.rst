Advanced Portainer Configuration
================================

KB Custom URL
-------------

If you want to publish Zammad's knowledge base under a different URL than the
default one, you can follow our configuration example using
`NPM (Nginx Proxy Manager) <https://nginxproxymanager.com/>`_ below.

Configure Zammad
^^^^^^^^^^^^^^^^

.. figure:: /images/install/docker-compose/additional-modules/kb-custom-url.png
    :alt: Screenshots shows the custom URL tab in Zammad's KB settings
    :scale: 70%

- Go to "Knowledge Base" in Zammad's admin settings and select the "Custom URL"
  tab
- Add the URL you want to publish your knowledge base under and click the
  **Submit** button
- Click on the **Web Server Configuration** button to get the configuration for
  your NPM. You can already copy the snippet or just leave it open, it is
  needed for the NPM configuration.

.. figure:: /images/install/docker-compose/additional-modules/kb-custom-url-dialog.png
    :alt: Screenshots shows the web server configuration dialog for custom KB URL
    :scale: 70%

Configure NPM
^^^^^^^^^^^^^

In NPM, add a new proxy host with the following parameters:

Details tab
    - **Domain Names**: the domain under which you want to publish your
      knowledge base
    - **Forwarded Hostname / IP**: the host/IP of your Zammad instance
    - **Forward Port**: the port of your Zammad (by default ``8080`` in
      Portainer deployment)

    .. figure:: /images/install/docker-compose/additional-modules/npm-details-tab.png
        :alt: Screenshots shows NPM configuration dialog with details tab
        :scale: 70%

Custom location tab
    - **Define location**: ``/``
    - **Forward Hostname / IP**: Same as above
    - **Forward Port**: Same as above
    - Click on the Cogwheel to open the custom location configuration text field
      and paste ``proxy_set_header X-ORIGINAL-URL $request_uri;`` (the lower
      part of Zammad's snippet)

    .. figure:: /images/install/docker-compose/additional-modules/npm-custom-locations-tab.png
        :alt: Screenshots shows NPM configuration dialog with custom locations tab
        :scale: 70%

Advanced tab
    - **Custom Nginx Configuration**: Add the upper part of Zammad's snippet,
      which should be similar to the following one:

    .. code-block::

        # Add following lines to "server" directive
        if ($host = help.your.domain ) {
        rewrite ^/(api|assets)/(.*)$ /$1/$2 last;
        rewrite ^(.*)$ /help$1 last;
        }

    .. figure:: /images/install/docker-compose/additional-modules/npm-advanced-tab.png
        :alt: Screenshots shows NPM configuration dialog with custom locations tab
        :scale: 70%

After following these steps, your knowledge base should be published under a
custom URL. You can test it by clicking the preview button in your knowledge
base.

