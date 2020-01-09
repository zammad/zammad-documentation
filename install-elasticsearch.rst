.. _install_elasticsearch:

Set up Elasticsearch
********************

We use Elasticsearch for the awesome search in Zammad.

Currently we support:

* Elasticsearch 5.5.x with mapper-attachments plugin
* Elasticsearch 5.6.x, 6.x, 7.x with ingest-attachment plugin

.. Warning:: Please note that we will be dropping Elasticsearch support prior 5.5.x on future releases.

This manual uses the ``zammad run`` command which is only available if you installed Zammad from one of our package repos.
If you're using a source code based install, simply leave that part away and just run ``rails ...`` or ``rake ...`` where ever neded.


Install Elasticsearch and its Attachment plugin
===============================================

Generic install Elasticsearch 5.6, 6.x, 7.x (ingest-attachment):
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Download and install via https://www.elastic.co/downloads/elasticsearch (5.6, 6.x or 7.x)
* Install the Attachment plugin

::

 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

* Setting vm.max_map_count for Elasticsearch

::

 sysctl -w vm.max_map_count=262144
 
 
.. Tip:: On Mac OS you also have to do: https://www.elastic.co/guide/en/elasticsearch/reference/5.6/docker.html#docker-cli-run-prod-mode
 
 
* Start elasticsearch


The most current repository installation path can be found `here <https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html>`_.

CentOS 7:
+++++++++

::

 rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
 echo "[elasticsearch-7.x]
 name=Elasticsearch repository for 7.x packages
 baseurl=https://artifacts.elastic.co/packages/7.x/yum
 gpgcheck=1
 gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
 enabled=1
 autorefresh=1
 type=rpm-md"| sudo tee /etc/yum.repos.d/elasticsearch-7.x.repo
 yum install -y java-1.8.0-openjdk elasticsearch
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
 systemctl start elasticsearch
 systemctl enable elasticsearch


Debian 8:
+++++++++

::

 apt-get install apt-transport-https sudo wget
 echo "deb http://ftp.debian.org/debian jessie-backports main" | sudo tee -a /etc/apt/sources.list.d/debian-backports.list
 echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install -t jessie-backports openjdk-8-jre
 apt-get install elasticsearch
 sudo /var/lib/dpkg/info/ca-certificates-java.postinst configure
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Debian 9:
+++++++++

::

 apt-get install apt-transport-https sudo wget
 echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install openjdk-8-jre elasticsearch
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Ubuntu 16.04 & 18.04:
+++++++++++++++++++++

::

 apt-get install apt-transport-https sudo wget
 echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install openjdk-8-jre elasticsearch
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment
 systemctl restart elasticsearch
 systemctl enable elasticsearch

Adjust default settings of Elasticsearch
++++++++++++++++++++++++++++++++++++++++

.. Note:: The we found the below settings to work good with Zammad. Please note that this is only suggestion that can affect your local environment.

To ensure an optimal performance of Zammad together with elasticsearch, you might want to increase the maximum possible 
content length for http requests by adding the following to your ``/etc/elasticsearch/elasticsearch.yml``:

::
  
  http.max_content_length: 400mb

.. Note:: The following step is only necessary starting with elasticsearch 7 and newer.


To enable Zammad to search for many values at the same time (to speed up your search), you'll also need to add the followingf option to your ``/etc/elasticsearch/elasticsearch.yml``:

::
  
  indices.query.bool.max_clause_count: 2000

Above setting is necessary, as the default value is ``1024`` which is too low. 
elasticsearch 6.x will only throw a deprecation warning, so you might want to adjust it with above as well.

Configure Zammad to work with Elasticsearch
*******************************************

First of all we need to tell Zammad where it can find elasticsearch. 

::

 zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"

If you need to use authentication for your elasticsearch installation or specific indice namings, please take a look at 
`Optional settings`_.

Create Elasticsearch index
==========================

After you have configured Zammad for using Elasticsearch, you need to rebuild the index with the following command:

::

 zammad run rake searchindex:rebuild

Optional settings for Elasticsearch
***********************************

Elasticsearch with HTTP basic auth
==================================

If you're using another elasticsearch instance, you might need to authenticate against it.
Below options help you with that.
::

 zammad run rails r "Setting.set('es_user', 'elasticsearch')"
 zammad run rails r "Setting.set('es_password', 'zammad')"


Extra Elasticsearch index name space
====================================

If you're running several Zammad instances (or other services using ES) with a central elasticsearch server, 
you might want to specify which index Zammad should use.
::

 zammad run rails r "Setting.set('es_index', Socket.gethostname.downcase + '_zammad')"

Ignore certain file extensions for indexing
===========================================

Some attachments might be troublesome when indexing or simply not needed within the search index.
You can tell Zammad to ignore those attachments by specifying their file extension so it won't post it to elasticsearch.
::

 zammad run rails r "Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

Maximum attachment size which is used for indexing
==================================================

.. Note:: By default Zammad will limit indexing to attachments to 50 MB.

Limiting the maximum size of attachments (for indexing) might be usefull, you can set it like so:
::

 zammad run rails r "Setting.set('es_attachment_max_size_in_mb', 50)"


Using elasticsearch on another server
=====================================

elasticsearch also allows you to use authentication via X-Pack to run it on another system as the one Zammad runs on.
Please note that the configuration of this functionality is out of scope of this documentation.

Elastic provides a great documentation on `how to set up X-Pack <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-xpack.html>`_.


Versions prior elasticsearch 6.3
++++++++++++++++++++++++++++++++

.. Note:: Depending on the elasticsearch version it can provide authentication. There are also subscription based authentication features you can get from the elastic-team.
  
  `You can find an Nginx reverse proxy config here <https://github.com/zammad/zammad/blob/develop/contrib/nginx/elasticsearch.conf>`_


List of fields being stored in Elasticsearch
********************************************

Ticket
======

Please note that these fields may vary if you created custom fields (objects) in the admin interface.

+------------------------------+--------------------------+---------------------------------------------------------------+
| Field                        | Sample Value             | Description                                                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| article                      | Article                  | Article Hash, which includes all articles stored on a ticket  |
+------------------------------+--------------------------+---------------------------------------------------------------+
| article_count                | 1                        | Count of articles                                             |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_at                     | null                     | First close time, after create                                |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_diff_in_min            | null                     | Business hours in minutes within or above the specified SLA   |
|                              |                          | for closing the ticket.                                       |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_escalation_at          | null                     | Time stamp of the escalation if the SLA of the closing time   |
|                              |                          | has been violated. (DateTime, UTC)                            |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_in_min                 | null                     | Business hours in minutes it took to close the ticket.        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_sender        | Customer                 | Who has created the first article (Agent,Customer)            |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_sender_id     | 2                        | Sender id of the first article (Agent|Customer)               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_type          | web                      | Article type for the first article (note, email, phone...)    |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_type_id       | 11                       | Article type ID for the first article (note, email, phone...) |
+------------------------------+--------------------------+---------------------------------------------------------------+
| created_at                   | 2017-08-03T14:21:38.701Z | Created timestamp (DateTime, UTC)                             |
+------------------------------+--------------------------+---------------------------------------------------------------+
| created_by                   | User                     | User details of the user who created the ticket               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| created_by_id                | 13                       | User id of user who created the ticket                        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| customer                     | User                     | Customer details                                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| customer_id                  | 13                       | User id of the current customer (assigned to ticket)          |
+------------------------------+--------------------------+---------------------------------------------------------------+
| escalation_at                | null                     | Next first escalation date (nearest close_escalation_at,      |
|                              |                          | first_response_escalation_at or update_escalation_at          |
|                              |                          | (DateTime, UTC)                                               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_at            | null                     | Time stamp of the first reaction to the customer              |
|                              |                          | (DateTime, UTC)                                               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_diff_in_min   | null                     | Business hours in minutes within or above the specified SLA   |
|                              |                          | for the first reaction to the customer.                       |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_escalation_at | null                     | Time stamp of the escalation if the SLA of the first reaction |
|                              |                          | time has been violated. (DateTime, UTC)                       |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_in_min        | null                     | Business hours in minutes it took to send inital response to  |
|                              |                          | customer.                                                     |
+------------------------------+--------------------------+---------------------------------------------------------------+
| group                        | Sales                    | Current ticket group (Sales, Support...)                      |
+------------------------------+--------------------------+---------------------------------------------------------------+
| group_id                     | 1                        | Current ticket group id                                       |
+------------------------------+--------------------------+---------------------------------------------------------------+
| id                           | 19                       | Ticket id                                                     |
+------------------------------+--------------------------+---------------------------------------------------------------+
| last_contact_agent_at        | null                     | Last contact to customer from agent, timestamp (DateTime, UTC)|
+------------------------------+--------------------------+---------------------------------------------------------------+
| last_contact_at              | 2017-08-03T14:21:38.701Z | Last contact timestamp (DateTime, UTC)                        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| last_contact_customer_at     | 2017-08-03T14:21:38.701Z | Last contact from a customer, timestamp (DateTime, UTC)       |
+------------------------------+--------------------------+---------------------------------------------------------------+
| note                         | null                     | Internal note for ticket                                      |
+------------------------------+--------------------------+---------------------------------------------------------------+
| number                       | 61019                    | The uniq ticket number                                        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| organization_id              | null                     | Id of the organization of a given customer                    |
+------------------------------+--------------------------+---------------------------------------------------------------+
| owner                        | User                     | Current owner (agent)                                         |
+------------------------------+--------------------------+---------------------------------------------------------------+
| owner_id                     | 1                        | User id of owner                                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| pending_time                 | null                     | Current pending time (DateTime, UTC)                          |
+------------------------------+--------------------------+---------------------------------------------------------------+
| preferences                  |                          | Sub Hash for special information                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| priority                     | 2 normal                 | Ticket priority                                               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| priority_id                  | 2                        | ID of the currently set priority                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| state                        | new                      | Ticket state (new, open...)                                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| state_id                     | 1                        | Ticket state id for available ticket states (new, open...)    |
+------------------------------+--------------------------+---------------------------------------------------------------+
| time_unit                    | null                     | Accounted time units for this ticket                          |
+------------------------------+--------------------------+---------------------------------------------------------------+
| title                        | Feedback Form            | Ticket title                                                  |
+------------------------------+--------------------------+---------------------------------------------------------------+
| type                         | null                     | Ticket Type (deprecated)                                      |
+------------------------------+--------------------------+---------------------------------------------------------------+
| update_diff_in_min           | null                     | Business hours in minutes within or above the specified SLA   |
|                              |                          | for updating the ticket.                                      |
+------------------------------+--------------------------+---------------------------------------------------------------+
| update_escalation_at         | null                     | Time stamp of the last update reaction to the customer        |
|                              |                          | (DateTime, UTC)                                               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| update_in_min                | null                     | Business hours in minutes it took to send the last update     |
|                              |                          | response to customer                                          |
+------------------------------+--------------------------+---------------------------------------------------------------+
| updated_at                   | 2017-08-03T14:21:38.701Z | Last update timestamp (DateTime, UTC)                         |
+------------------------------+--------------------------+---------------------------------------------------------------+
| updated_by                   | User                     | User who updated the ticket                                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| updated_by_id                | 13                       | User id of user who updated the ticket                        |
+------------------------------+--------------------------+---------------------------------------------------------------+

Article
=======

+---------------------+------------------------------------------------+--------------------------------------------------------------+
| Field               | Sample Value                                   | Description                                                  |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| attachment.title    | file1.txt                                      | File name                                                    |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| attachment.content  | Hello world                                    | File Content                                                 |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| attachment.keywords | keyword                                        | File Keywords                                                |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| attachment.content  | Max                                            | File Author                                                  |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| body                | :)                                             | Content of the article                                       |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| cc                  | null                                           | Content of the optional cc field                             |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| content_type        | text/plain                                     | Content type                                                 |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| created_at          | 2017-08-03T14:21:38.000Z                       | Article create date (DateTime, UTC)                          |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| created_by          | See User                                       | Who has created the article                                  |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| created_by_id       | 13                                             | Who (UserID) has created the article                         |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| from                | Christopher Miller via <order@chrispresso.com> | Sender address of the article                                |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| id                  | 19                                             | internal (DB) article id                                     |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| in_reply_to         | null                                           | Content of reply to field                                    |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| internal            | FALSE                                          | Is article visible for customer                              |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| message_id          | null                                           | Message ID (if article was an email)                         |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| message_id_md5      | null                                           | internal message id MD5 Checksum                             |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| origin_by_id        | null                                           | For which real user (UserID) the article creation has been   |
|                     |                                                | done. For example the customer which was calling on the phone|
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| preferences         | { }                                            | Hash for additional information.                             |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| references          | null                                           | Email references header.                                     |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| reply_to            | null                                           | Content of the reply to field                                |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| sender              | Customer                                       | Who is the sender (Customer, Agent)                          |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| sender_id           | 2                                              | Which type of user has created the article (Agent, Customer) |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| subject             | Feedback Form                                  | Article subject                                              |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| ticket_id           | 19                                             | referencing ticket ID                                        |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| to                  | null                                           | Content of the to field                                      |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| type                | web                                            | Article type (phone, email, web...)                          |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| type_id             | 11                                             | Article type id (phone, email, web...)                       |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| updated_at          | 2017-08-03T14:21:38.701Z                       | Update time of the article (DateTime, UTC)                   |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| updated_by          | See User                                       | Who has updated the article                                  |
+---------------------+------------------------------------------------+--------------------------------------------------------------+
| updated_by_id       | 13                                             | Who (UserID) has updated the article                         |
+---------------------+------------------------------------------------+--------------------------------------------------------------+

User
====

Please note that these fields may vary if you created custom fields (objects) in the admin interface.

+-----------------+--------------------------+-----------------------------------------+
| Field           | Sample Value             | Description                             |
+-----------------+--------------------------+-----------------------------------------+
| active          | TRUE                     | is activ (boolean)                      |
+-----------------+--------------------------+-----------------------------------------+
| address         |                          | User Adress                             |
+-----------------+--------------------------+-----------------------------------------+
| city            |                          | User City                               |
+-----------------+--------------------------+-----------------------------------------+
| country         |                          | User Country                            |
+-----------------+--------------------------+-----------------------------------------+
| created_at      | 2017-07-26T21:21:28.000Z | User creation date (DateTime, UTC)      |
+-----------------+--------------------------+-----------------------------------------+
| created_by_id   | 1                        | ID of user who created the current user |
+-----------------+--------------------------+-----------------------------------------+
| department      |                          | User Department                         |
+-----------------+--------------------------+-----------------------------------------+
| email           | chris@chrispresso.com    | User E-Mail                             |
+-----------------+--------------------------+-----------------------------------------+
| fax             |                          | User Fax                                |
+-----------------+--------------------------+-----------------------------------------+
| firstname       | Christopher              | User Firstname                          |
+-----------------+--------------------------+-----------------------------------------+
| id              | 3                        | Internal id (database, autincrement)    |
+-----------------+--------------------------+-----------------------------------------+
| last_login      | 2017-07-26T21:23:15.019Z | User last login (DateTime, UTC)         |
+-----------------+--------------------------+-----------------------------------------+
| lastname        | Miller                   | User Lastname                           |
+-----------------+--------------------------+-----------------------------------------+
| login           | chris@chrispresso.com    | User Login                              |
+-----------------+--------------------------+-----------------------------------------+
| mobile          |                          | User Mobile                             |
+-----------------+--------------------------+-----------------------------------------+
| note            |                          | internal note                           |
+-----------------+--------------------------+-----------------------------------------+
| organization    | Chrispresso Inc          | Orgnaization name of the current user   |
+-----------------+--------------------------+-----------------------------------------+
| organization_id | 2                        | ID which links to the organization name |
+-----------------+--------------------------+-----------------------------------------+
| phone           |                          | User Phone                              |
+-----------------+--------------------------+-----------------------------------------+
| street          |                          | User Street                             |
+-----------------+--------------------------+-----------------------------------------+
| updated_at      | 2017-07-27T15:04:47.270Z | Last update date (DateTime, UTC)        |
+-----------------+--------------------------+-----------------------------------------+
| updated_by_id   | 3                        | ID of user who updated the current user |
+-----------------+--------------------------+-----------------------------------------+
| verified        | FALSE                    | is verified (boolean)                   |
+-----------------+--------------------------+-----------------------------------------+
| vip             | FALSE                    | Is VIP (boolean)                        |
+-----------------+--------------------------+-----------------------------------------+
| web             |                          | User Web Url                            |
+-----------------+--------------------------+-----------------------------------------+
| zip             |                          | User ZIP                                |
+-----------------+--------------------------+-----------------------------------------+


