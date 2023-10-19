.. code-block:: sh

   # Add zammad user to RVM group
   $ usermod -a -G rvm zammad

   # Install Ruby 3.1.3
   $ su - zammad
   $ rvm install ruby-3.1.3

   # Install bundler, rake and rails
   $ rvm use ruby-3.1.3
   $ gem install bundler rake rails
