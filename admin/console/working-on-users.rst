Working on User Information
===========================

.. include:: /admin/console/missing-commands-ask-community.include.rst

Find User
---------

In order to work on user information or to check for specific information,
you'll need to find it first.

.. code-block:: ruby

   >> User.find(4)                       # We already know the ID of the user
   >> User.find_by(email: 'your@email')  # Searching for the user by his Email address
   >> User.find_by(login: 'john.doe')    # Searching for the user by his login

Unlock a Locked User Account
----------------------------

.. tip::

   Unlocking a locked user account is also supported by Zammad's web UI.
   Please refer to the :admin-docs:`admin documentation </manage/users/via-the-admin-panel.html>`
   for more information.

It sometimes happens that a user locks himself out by wildly trying the wrong
password multiple times. Depending on your maximum failing login count
(`default: 10 times`), Zammad might lock the account.

The user can't login any more (forever) if he doesn't change the password or
you reset the counter.

.. code-block:: ruby

   >> u=User.find(**USERID**)
   >> u.login_failed=0
   >> u.save!

You can also double check if the account is locked by running the following
(result needs to be 1 above your limit, so `11` for the default of 10 failing
logins)

.. code-block:: ruby

   >> User.find(**USERID**).login_failed

Change / Update Email Address of User
-------------------------------------

If needed, you can simply change the Email address of the user.

.. note::

   Please note that the login attribute is not affected by this and Zammad thus
   might show different information within the UI.

.. code-block:: ruby

   >> u = User.find(**USERID**)
   >> u.email = 'user@exmaple.com'
   >> u.save!


You need to find the user ID of the user first for this.

Change / Update Login Name of User
----------------------------------

Change the user name of the user (e.g. if you want to login with a shorter
username instead of a mail address)

.. code-block:: ruby

   >> u = User.find(**USERID**)
   >> u.login = 'user@exmaple.com'
   >> u.save!


You need to find the user ID of the user first for this.

Set Admin Rights for User
-------------------------

Don't have access to Zammad anymore? Grant yourself or another user
administrative rights.

.. code-block:: ruby

   >> u = User.find_by(email: 'you@example.com')
   >> u.roles = Role.where(name: ['Agent', 'Admin'])
   >> u.save!

Set Password for User
---------------------

You or the user did forget his password? No problem! Simply reset it by hand
if needed.

.. code-block:: ruby

   >> User.find_by(email: 'you@example.com').update!(password: 'your_new_password')
