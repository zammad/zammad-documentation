.. code-block:: sh

   # Add zammad user to RVM group
   $ usermod -a -G rvm zammad

   # Install Ruby 3.2.3
   $ su - zammad
   $ rvm install ruby-3.2.3

   # Install bundler, rake and rails
   $ rvm use ruby-3.2.3
   $ gem install bundler rake rails
