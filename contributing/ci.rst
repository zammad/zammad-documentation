Continuous integration
**********************

All pushes to our main repo at https://github.com/zammad/zammad will trigger build tests.
We use internal build tests on internal and external continuous integration platforms.

Internal
========

* Done on our private continuous integration platform

External
========

Travis-CI
---------

* You can find the build test results at https://travis-ci.org/zammad/zammad
* If you fork the Zammad repo you're able to also use travis-ci.org to get your builds tested
* Just change the file ".travis.yml" to fit your needs
* Current build test status is:

.. image:: https://travis-ci.org/zammad/zammad.svg?branch=develop
   :target: https://travis-ci.org/zammad/zammad

Local
=====

RSpec
-----

To run tests locally in the test environment, you need to first ensure the test DB is in the expected state:

::

  RAILS_ENV=test bundle exec rake db:drop db:create zammad:ci:test:prepare


For tests that use compiled front end assets, make sure the latest state of the code is considered:

::

  RAILS_ENV=test bundle exec rake assets:precompile


Finally, running a single test can be done via the following command:

::

  bundle exec rspec spec/system/ticket/zoom_spec.rb


Note that it's also possible to run a specific test case by including the line number in the command:

::

  bundle exec rspec spec/system/ticket/zoom_spec.rb:1070
