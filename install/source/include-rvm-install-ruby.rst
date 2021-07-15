.. code-block:: sh

   # Add zammad user to RVM group
   $ usermod -a -G rvm zammad

   # Install Ruby 2.7.4
   $ su - zammad
   $ rvm install ruby-2.7.4

   # Install bundler, rake and rails
   $ rvm use 2.7.4
   $ gem install bundler rake rails
