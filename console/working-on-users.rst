Working on user information
***************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Find user
---------

In order to work on user information or to check for specific information, you'll need to find it first.
::

 User.find(4)				# We already know the ID of the user
 User.find_by(email: 'your@email')	# Searching for the user by his E-Mail-Address
 User.find_by(login: 'john.doe')	# Searching for the user by his login


Re-activate a locked user account
---------------------------------

It sometimes happens that a user locks himself out by wildly trying the wrong password multiple times.
Depending on your maximum failing login count (`default: 10 times`), Zammad might lock the account. 
The user can't login any more (forever) if he doesn't change the password or you reset the counter.
::

  u=User.find(**USERID**)
  u.login_failed=0
  u.save!

You can also double check if the account is locked by running the following (result needs to be 1 above your limit, so `11` for the default of 10 failing logins)
::

 User.find(**USERID**).login_failed


Change / Update E-Mail-Adress of User
-------------------------------------

If needed, you can simply change the E-Mail-Address of the user.

.. Note:: Please note that the login attribute is not affected by this and Zammad thus might show different information within the UI.
::

 u=User.find(**USERID**)
 u.email = 'user@exmaple.com'
 u.save!
  
  
You need to find the User-ID of the user first for this.
  
  
Change / Update Login name of User
----------------------------------

Change the user name of the user (e.g. if you want to login with a shorter username instead of a mail address)
::

 u=User.find(**USERID**)
 u.login = 'user@exmaple.com'
 u.save!
  
  
You need to find the User-ID of the user first for this.


Set admin rights for user
-------------------------

Don't have access to Zammad anymore? Grant yourself or another user administrative rights.
::

 u = User.find_by(email: 'you@example.com')
 u.roles = Role.where(name: ['Agent', 'Admin'])
 u.save!


Set password for user
---------------------

You or the user did forget his password? No problem! Simply reset it by hand if needed.
::

 User.find_by(email: 'you@example.com').update!(password: 'your_new_password')

