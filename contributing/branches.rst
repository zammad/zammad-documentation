Branches
********

The Zammad main repo at https://github.com/zammad/zammad has several branches

Master
======

* Current unreleased development state of next stable minor release
* Bug fixes of current stable version are added here
* Is the branch where features work correctly
* Could be used for production environment by experienced users
* If current stable version is 1.1.0 this will become 1.1.1


Develop
=======

* Default GitHub branch
* Current unreleased development state of next major release
* Is the first instance where all features are being developed
* This branch will have open issues
* If current stable version is 1.1.0 this will become 1.2.0
* Unstable!
* Should not be used in production environment!

Stable
======

* Current stable release
* Can be used for production
* Stable bugfixes will be merged from master when new stable minor version will be released


Stable-X.x
==========

* Each minor and major version will have a stable branch (stable-x.x).
* We are supporting the current develop and stable branch for security fixes and minor bugfixes
* The latest downloadble version on https://zammad.org/ is based on the stable branch
* If your version is older and e.g. equals version 1.2.0 then the name of the branch is stable-1.2 and there also would be stable-1.1 and stable-1.0
