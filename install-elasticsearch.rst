Set up Elasticsearch
********************

We use Elasticsearch for the awesome search in Zammad.

Currently we support:

* Elasticsearch 2.4.x to 5.5.x with mapper-attachments plugin
* Elasticsearch 5.6.x with ingest-attachment plugin

This manual uses the "zammad" command which is only available if you installed Zammad from one of our package repos.

Install Elasticsearch and its Attachment plugin
===============================================

Generic install Elasticsearch 2.4 (mapper-attachments):
++++++++++++++++++++++++++++++++++

* Download and install via https://www.elastic.co/downloads/elasticsearch (2.4.x)
* Install the Attachment plugin

::

 cd /usr/share/elasticsearch
 bin/plugin install mapper-attachments

* Start elasticsearch

Generic install Elasticsearch 5.0-5.5 (mapper-attachments):
++++++++++++++++++++++++++++++++++

* Download and install via https://www.elastic.co/downloads/elasticsearch (5.0-5.5)
* Install the Attachment plugin

::

 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments

* Setting vm.max_map_count for Elasticsearch

::

 sysctl -w vm.max_map_count=262144


* Start elasticsearch

Generic install Elasticsearch 5.6 (ingest-attachment):
++++++++++++++++++++++++++++++++++

* Download and install via https://www.elastic.co/downloads/elasticsearch (5.6)
* Install the Attachment plugin

::

 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-attachment

* Setting vm.max_map_count for Elasticsearch

::

 sysctl -w vm.max_map_count=262144


* Start elasticsearch

CentOS 7:
+++++++++

::

 rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
 echo "[elasticsearch-5.x]
 name=Elasticsearch repository for 5.x packages
 baseurl=https://artifacts.elastic.co/packages/5.x/yum
 gpgcheck=1
 gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
 enabled=1
 autorefresh=1
 type=rpm-md"| sudo tee /etc/yum.repos.d/elasticsearch-5.x.repo
 yum install -y java-1.8.0-openjdk elasticsearch-5.5.3-1
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments
 systemctl start elasticsearch
 systemctl enable elasticsearch


Debian 8:
+++++++++

::

 apt-get install apt-transport-https sudo wget
 echo "deb http://ftp.debian.org/debian jessie-backports main" | sudo tee -a /etc/apt/sources.list.d/debian-backports.list
 echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install -t jessie-backports openjdk-8-jre
 apt-get install elasticsearch=5.5.3
 sudo /var/lib/dpkg/info/ca-certificates-java.postinst configure
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Debian 9:
+++++++++

::

 apt-get install apt-transport-https sudo wget
 echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install openjdk-8-jre elasticsearch
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Ubuntu 16.04:
+++++++++++++

::

 echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install openjdk-8-jre elasticsearch=5.5.3
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Configure Zammad to work with Elasticsearch
===========================================

::

 zammad run rails r "Setting.set('es_url', 'http://localhost:9200')"


Create Elasticsearch index
==========================

After you have configured Zammad for using Elasticsearch, you need to rebuild the index with the following command:

::

 zammad run rake searchindex:rebuild


Optional settings
=================

Elasticsearch with HTTP basic auth
----------------------------------

::

 zammad run rails r "Setting.set('es_user', 'elasticsearch')"
 zammad run rails r "Setting.set('es_password', 'zammad')"

Extra Elasticsearch index name space (optional)
----------------------------------------------

::

 zammad run rails r "Setting.set('es_index', Socket.gethostname + '_zammad')"

Ignore certain file extensions for indexing (optional)
------------------------------------------------------

::

 zammad run rails r "Setting.set('es_attachment_ignore', [ '.png', '.jpg', '.jpeg', '.mpeg', '.mpg', '.mov', '.bin', '.exe', '.box', '.mbox' ] )"

Maximum attachment size which is used for indexing, default is 50 MB (optional)
-------------------------------------------------------------------------------

::

 zammad run rails r "Setting.set('es_attachment_max_size_in_mb', 50)"


Using Elasticsearch on another server
=====================================

Elasticsearch can also be installed on another server but you have to know that this is insecure out of the box because Elasticsearch has no authentication.
For this reason you should run elasticsearch on 127.0.0.1 and use a reverse proxy with authentication to access it from Zammad.

You can find an Nginx reverse proxy config here:

* https://github.com/zammad/zammad/blob/develop/contrib/nginx/elasticsearch.conf

List of values which are stored in ElasticSearch
================================================

+------------------------------+--------------------------+---------------------------------------------------------------+
| Field                        | sample value             | Description                                                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| note                         | null                     | Internal note for ticket (deprecated)                         |
+------------------------------+--------------------------+---------------------------------------------------------------+
| owner_id                     | 1                        | User id of owner                                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| last_contact_agent_at        | null                     | Last contact to customer from agent, timestamp (datetime utc) |
+------------------------------+--------------------------+---------------------------------------------------------------+
| created_at                   | 2017-08-03T14:21:38.701Z | Created timestamp (datetime utc)                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_sender_id     | 2                        | Sender id of the first article (agent|customer)               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| title                        | Feedback Form            | Ticket title                                                  |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_diff_in_min   | null                     | First response time, after create, in minutes                 |
+------------------------------+--------------------------+---------------------------------------------------------------+
| pending_time                 | null                     | Current pending time (datetime utc)                           |
+------------------------------+--------------------------+---------------------------------------------------------------+
| type                         | null                     | Ticket Type (deprecated)                                      |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_diff_in_min            | null                     | First close time, after create                                |
+------------------------------+--------------------------+---------------------------------------------------------------+
| number                       | 61019                    | Ticket number                                                 |
+------------------------------+--------------------------+---------------------------------------------------------------+
| priority_id                  | 2                        | ID of the currently set priority                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| last_contact_at              | 2017-08-03T14:21:38.701Z | Last contact timestamp (datetime utc)                         |
+------------------------------+--------------------------+---------------------------------------------------------------+
| updated_at                   | 2017-08-03T14:21:38.701Z | Last update timestamp (datetime utc)                          |
+------------------------------+--------------------------+---------------------------------------------------------------+
| article_count                | 1                        | Count of articles                                             |
+------------------------------+--------------------------+---------------------------------------------------------------+
| escalation_at                | null                     | Next escalation date (dateime utc)                            |
+------------------------------+--------------------------+---------------------------------------------------------------+
| time_unit                    | null                     | Stored time units                                             |
+------------------------------+--------------------------+---------------------------------------------------------------+
| update_in_min                | null                     | Escalation update time in minutes                             |
+------------------------------+--------------------------+---------------------------------------------------------------+
| id                           | 19                       | Ticket id                                                     |
+------------------------------+--------------------------+---------------------------------------------------------------+
| state_id                     | 1                        | Ticket state id for available ticket states (new, open...)    |
+------------------------------+--------------------------+---------------------------------------------------------------+
| state                        | new                      | Ticket state (new, open...)                                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| last_contact_customer_at     | 2017-08-03T14:21:38.701Z | Last contact from a customer, timestamp (datetime utc)        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| group                        | Sales                    | Current ticket group (Sales, Support...)                      |
+------------------------------+--------------------------+---------------------------------------------------------------+
| owner                        | User                     | Current owner (agent)                                         |
+------------------------------+--------------------------+---------------------------------------------------------------+
| preferences                  |                          | Sub Hash for special information                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_escalation_at | null                     | Escalation first response time (datetime, utc)                |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_in_min        | null                     | Escalation first response time (in minutes)                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_sender        | Customer                 | Who has created the first article (Agent,Customer)            |
+------------------------------+--------------------------+---------------------------------------------------------------+
| first_response_at            | null                     | First Response time, after create (Datetime, utc)             |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_escalation_at          | null                     | Escalation close time (datetime, utc)                         |
+------------------------------+--------------------------+---------------------------------------------------------------+
| priority                     | 2 normal                 | Ticket priority                                               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_in_min                 | null                     |                                                               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| created_by                   | User                     | User details of the user who created the ticket               |
+------------------------------+--------------------------+---------------------------------------------------------------+
| Article                      | Article                  | Article Hash, which includes all articles stored on a ticket  |
+------------------------------+--------------------------+---------------------------------------------------------------+
| update_escalation_at         | null                     | Escalation update time (datetime, utc)                        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| group_id                     | 1                        | Current ticket group id                                       |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_type          | web                      | Article type for the first article (Note, Mail, Phone...)     |
+------------------------------+--------------------------+---------------------------------------------------------------+
| organization_id              | null                     | Id of the organization of a given customer                    |
+------------------------------+--------------------------+---------------------------------------------------------------+
| create_article_type_id       | 11                       | Article type ID for the first article (Note, Mail, Phone...)  |
+------------------------------+--------------------------+---------------------------------------------------------------+
| updated_by                   | User                     | User who updated the ticket                                   |
+------------------------------+--------------------------+---------------------------------------------------------------+
| close_at                     | null                     | First close time, after create                                |
+------------------------------+--------------------------+---------------------------------------------------------------+
| updated_by_id                | 13                       | User id of user who updated the ticket                        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| created_by_id                | 13                       | User id of user who created the ticket                        |
+------------------------------+--------------------------+---------------------------------------------------------------+
| customer_id                  | 13                       | User id of the current customer (assigned to ticket)          |
+------------------------------+--------------------------+---------------------------------------------------------------+
| update_diff_in_min           | null                     | (Deprecated)?                                                 |
+------------------------------+--------------------------+---------------------------------------------------------------+
| customer                     | User                     | Customer details                                              |
+------------------------------+--------------------------+---------------------------------------------------------------+
