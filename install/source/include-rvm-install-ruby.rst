.. code-block:: sh

   # Add zammad user to RVM group
   $ usermod -a -G rvm zammad
   
   # Install Ruby 2.6.8
   $ su - zammad
   $ rvm install ruby-2.6.8

   # Install bundler, rake and rails
   $ rvm use 2.6.8
   $ gem install bundler rake rails
