.. code-block:: sh

   # Add zammad user to RVM group
   $ usermod -a -G rvm zammad

   # Install Ruby 3.2.8
   $ su - zammad
   $ rvm install ruby-3.2.8

   # Install bundler, rake and rails
   $ rvm use ruby-3.2.8
   $ gem install bundler rake rails
