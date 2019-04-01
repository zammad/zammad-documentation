Working on user information
***************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Find user
---------

::

 User.find(4)
 User.find_by(email: 'your@email')


Change / Update E-Mail-Adress of User
-------------------------------------

::

 u=User.find(**USERID**)
 u.email = 'user@exmaple.com'
 u.save!
  
  
You need to find the User-ID of the user first for this.
  
  
Change / Update Login name of User
----------------------------------

::

 u=User.find(**USERID**)
 u.login = 'user@exmaple.com'
 u.save!
  
  
You need to find the User-ID of the user first for this.


Set admin rights for user
-------------------------

::

 u = User.find_by(email: 'you@example.com')
 u.roles = Role.where(name: ['Agent', 'Admin'])
 u.save!


Set password for user
---------------------

::

 User.find_by(email: 'you@example.com').update!(password: 'your_new_password')

