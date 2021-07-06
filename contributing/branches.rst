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

* We're supporting the current stable branch for security fixes and minor bugfixes.
* Let's say you're on version `1.2.0` and the next release will be `1.3.0`. In that case we'd provide a stable backport of mayor bug fixes that won't interfere with the old code base to `stable-1.2.1` - this also applies for security fixes *if the code base supports it*. The old stable version will be switched to `stable-1.2.0` (from `stable`) and stable version `1.3.0` will be the new `stable` branch.

