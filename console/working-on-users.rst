Working on user information
***************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Find user
---------

::

 rails> User.find(4)
 rails> User.find_by(email: 'your@email')


Change / Update E-Mail-Adress of User
-------------------------------------

::

 rails> u=User.find(**USERID**)
 rails> u.email = 'user@exmaple.com'
 rails> u.save!
  
  
You need to find the User-ID of the user first for this.
  
  
Change / Update Login name of User
----------------------------------

::

 rails> u=User.find(**USERID**)
 rails> u.login = 'user@exmaple.com'
 rails> u.save!
  
  
You need to find the User-ID of the user first for this.


Set admin rights for user
-------------------------

::

 rails> u = User.find_by(email: 'you@example.com')
 rails> u.roles = Role.where(name: ['Agent', 'Admin'])
 rails> u.save!


Set password for user
---------------------

::

 rails> User.find_by(email: 'you@example.com').update!(password: 'your_new_password')

