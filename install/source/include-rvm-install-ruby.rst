.. code-block:: sh

   # Add zammad user to RVM group
   $ sudo usermod -a -G rvm zammad
   
   # Install Ruby 2.6.6
   $ su - zammad
   $ rvm install ruby-2.6.6

   # Install bundler, rake and rails
   $ rvm use 2.6.6
   $ gem install bundler rake rails
