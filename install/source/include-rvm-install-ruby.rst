.. code-block:: sh

   # Add zammad user to RVM group
   $ usermod -a -G rvm zammad

   # Install Ruby 3.0.4
   $ su - zammad
   $ rvm install ruby-3.0.4

   # Install bundler, rake and rails
   $ rvm use 3.0.4
   $ gem install bundler rake rails
