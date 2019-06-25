Welcome to Zammad's documentation!
==================================
The Zammad documentation consists of three parts:

- Zammad system installation and configuration (this documentation)

- Zammad administration (https://admin-docs.zammad.org)

- Zammad user documentation (https://user-docs.zammad.org)

This system documentation for Zammad is organized into a couple of sections:

* :ref:`about-docs`
* :ref:`prerequisites-docs`
* :ref:`install-docs`
* :ref:`getting-started-docs`
* :ref:`migration-docs`
* :ref:`admin-console`
* :ref:`contributing-docs`
* :ref:`rest-api-docs`
* :ref:`appendix`


.. _about-docs:

.. toctree::
   :maxdepth: 2
   :caption: About

   about-zammad


.. _prerequisites-docs:

.. toctree::
   :maxdepth: 2
   :caption: Prerequisites

   prerequisites-software
   prerequisites-hardware


.. _install-docs:

.. toctree::
   :maxdepth: 2
   :caption: Installation & Update

   install-source
   install-centos
   install-debian
   install-ubuntu
   install-suse
   install-elasticsearch
   install-docker-compose
   install-kubernetes
   install-univention
   install-update


.. _getting-started-docs:

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   getting-started-first-steps


.. _migration-docs:

.. toctree::
   :maxdepth: 2
   :caption: Migration

   migration-otrs
   migration-zendesk


.. _admin-webfrontend:

.. toctree::
   :maxdepth: 3
   :glob:
   :caption: Administration via webfrontend

   Admin-Documentation <https://admin-docs.zammad.org/>


.. _admin-console:

.. toctree::
  :maxdepth: 2
  :glob:
  :caption: Administration via console

  admin-console


.. _contributing-docs:

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Contributing / Development

   contributing-start
   contributing-branches
   contributing-packages
   contributing-ci
   contributing-code-quality
   contributing-install-docker
   contributing-install-vagrant


.. _rest-api-docs:

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: REST API

   api-intro
   api-user
   api-organization
   api-group
   api-ticket
   api-ticket-state
   api-ticket-priority
   api-ticket-article
   api-notification
   api-object
   api-tags
   api-user_access_token


.. _cti-api-docs:

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: CTI API

   cti-api-intro
   cti-api-push


.. _appendix:

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Appendix


   appendix-backup-and-restore
   appendix-configure-env-vars
   appendix-repo-file
   appendix-privacy
