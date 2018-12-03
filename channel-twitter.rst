Twitter
*******

It's possible to put your Twitter communication into Zammad. To do so, you need to follow these steps:

Register Twitter developer account
====================
Register your Twitter developer account under http://developer.twitter.com. After your register the account you get the following welcome screen:

.. image:: images/app.twitter.com_developer_account.png
   :alt: welcome Twitter developer account


Register Twitter app
====================

Register your Zammad as Twitter app under http://developer.twitter.com. It's required to let Zammad read/write tweets and direct messages.

Click on your login name on the right top, then "Apps"

.. image:: images/apps.twitter.com_create_app_screen.png
   :alt: new app page

.. image:: images/apps.twitter.com_create_app_screen2.png
   :alt: new app page

Enter app settings. As "Callback URL" you need to enter "https://zammad_host/api/v1/external_credentials/twitter/callback"

.. image:: images/apps.twitter.com_created_app_screen.png
   :alt: new app is being created

After the app has been created, update the application icon and organization attributes.

.. image:: images/apps.twitter.com_set_permissions.png
   :alt: set permissions to receive and send direct messages

Next we need to set _read, write and access direct messages permissions_ for the app.

.. image:: images/apps.twitter.com_get_credentials.png
   :alt: click on Keys & Access Token, note them

Go to "Keys and Access Token" tab and note the "Consumer Key", "Consumer Secret", "Access token" and "Access token secret".

Next we need to create a "Dev Environment", click on your login name on the right top, then "Dev Environments"

.. image:: images/apps.twitter.com_dev_environment.png
   :alt: setup a new Dev Environment

Rember the "Dev environment label", you need it later.


Configure Zammad as Twitter app
===============================

Go to "Admin -> Channels -> Twitter"

.. image:: images/zammad_connect_twitter_app1.png
   :alt: Admin -> Channels -> Twitter

Click on "Connect Twitter App" and enter your "Consumer Key", "Consumer Secret", "Access token" and "Access token secret", "Dev environment label" and verify the "Callback URL".

.. image:: images/zammad_connect_twitter_app2.png
   :alt: Connect Twitter App, click "Submit"

Done, your Zammad is configured as Twitter App now.


Link your Twitter account to your Zammad Twitter app
====================================================

Now you need to link your Twitter Account from which you want to get tweets and send out tweets.

Click on "Add Account", then you will see the authorize app page of Twitter. Click on "authorize app".

.. image:: images/zammad_link_twitter_account.png
   :alt: Click on "Add Account"

.. image:: images/twitter.com_authorize_app.png
   :alt: Twitter authorize app page will appear

You will get redirected back to Zammad. Now you need to configure your search keys, where mentions and direct messages should get routed.

.. image:: images/zammad_linked_twitter_account.png
   :alt: Back in Zammad - settings

After you are done, you will get an overview of all linked Twitter Accounts.

.. image:: images/zammad_linked_twitter_account_done.png
   :alt: Back in Zammad - settings

Start using your new channel
============================

Start and write a message (direct message or tweet), short time later you will have a new ticket in Zammad.

.. image:: images/zammad_first_tweet_as_ticket.png
   :alt: A new Ticket - the tweet - just reply

Just click on the reply button (as you do it for emails) to send a reply.

.. image:: images/zammad_first_tweet_as_ticket_reply.png
   :alt: Ticket after reply sent out


