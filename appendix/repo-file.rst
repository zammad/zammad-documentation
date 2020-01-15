Package Repo Files
******************

Recently (24 Jul 2017) our packaging service provider (packager.io: http://www.packager.io/) improved its package distribution which makes it necessary that you update your Zammad repo file (e. g. /etc/apt/sources.list.d/zammad.list or /etc/yum.repos.d/zammad.repo) on your operating system.

If you're using an old repo file, you will not be able to update Zammad.

For more background information see: https://blog.packager.io/posts/24-change-of-repository-urls

Please use the following commands to update your Zammad repo file:


CentOS 7
=============

::

 sudo yum -y install epel-release wget
 sudo wget -O /etc/yum.repos.d/zammad.repo https://dl.packager.io/srv/zammad/zammad/stable/installer/el/7.repo
 sudo yum install zammad


Debian 8
=============

::

 sudo apt-get install wget
 wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
 sudo wget -O /etc/apt/sources.list.d/zammad.list https://dl.packager.io/srv/zammad/zammad/stable/installer/debian/8.repo
 sudo apt-get update
 sudo apt-get install zammad


Debian 9
=============

::

 sudo apt-get install wget
 wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
 sudo wget -O /etc/apt/sources.list.d/zammad.list https://dl.packager.io/srv/zammad/zammad/stable/installer/debian/9.repo
 sudo apt-get update
 sudo apt-get install zammad


Ubuntu 16.04
=============

::

 sudo apt-get install wget
 wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
 sudo wget -O /etc/apt/sources.list.d/zammad.list https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/16.04.repo
 sudo apt-get update
 sudo apt-get install zammad


Ubuntu 18.04
=============

::

 sudo apt-get install wget
 wget -qO- https://dl.packager.io/srv/zammad/zammad/key | sudo apt-key add -
 sudo wget -O /etc/apt/sources.list.d/zammad.list \
   https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/18.04.repo
 sudo apt-get update
 sudo apt-get install zammad


SLES 12
=============

::

 sudo zypper install wget
 sudo wget -O /etc/zypp/repos.d/zammad.repo https://dl.packager.io/srv/zammad/zammad/stable/installer/sles/12.repo
 sudo zypper install zammad


Note
=============
If you're using an old repo file, you will get error messages like these:

::

 E: Failed to fetch https://deb.packager.io/gh/zammad/zammad/dists/xenial/stable/binary-amd64/Packages  Writing more data than expected (7831 > 1153)
 E: Some index files failed to download. They have been ignored, or old ones used instead.

::

 Paket zammad-1.5.0-1500965473.2be861e2.centos7.x86_64.rpm not signed
