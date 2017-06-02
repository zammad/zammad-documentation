Set up Elasticsearch
********************

We use Elasticsearch for the awesome search in Zammad.
This manual uses the "zammad" command which is only available if you installed Zammad from one of our package repos.

Install Elasticsearch and its Attachment plugin
===============================================

Generic install Elasticsearch 2.4:
++++++++++++++++++++++++++++++++++

* Download and install via https://www.elastic.co/downloads/elasticsearch (2.4.x)
* Install the Attachment plugin

::

 cd /usr/share/elasticsearch
 bin/plugin install mapper-attachments

* Start elasticsearch

Generic install Elasticsearch 5.0:
++++++++++++++++++++++++++++++++++

* Download and install via https://www.elastic.co/downloads/elasticsearch (5.0.x)
* Install the Attachment plugin

::

 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments


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
 yum install -y java-1.8.0-openjdk elasticsearch
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
 apt-get install elasticsearch
 sudo /var/lib/dpkg/info/ca-certificates-java.postinst configure
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Ubuntu 16.04:
+++++++++++++

::

 echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
 wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
 apt-get update
 apt-get install openjdk-8-jre elasticsearch
 sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-attachments
 systemctl restart elasticsearch
 systemctl enable elasticsearch


Configure Zammad to work with Elasticsearch
===========================================

::

 zammad run rails r "Setting.set('es_url', 'http://127.0.0.1:9200')"


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
