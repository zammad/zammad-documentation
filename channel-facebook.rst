Facebook
********

It's possible to put your Facebook Page communication into Zammad. To do so, you need to follow these steps:

Register Facebook app
=====================

Register your Zammad as Facebook app under https://developers.facebook.com.

.. image:: images/developers.facebook.com-create-app.png
   :alt: new app page

Click on "Create New App" and enter app name

.. image:: images/developers.facebook.com-settings-basic.png
   :alt: app settings

You need to do the following:

* Go to Settings -> Basic
* "+ add Platform" -> Website and enter your Zammad URL link http://support.zammad.com
* Fill "App Domains", "Contact Email", "Privacy Policy URL", "Terms of Service URL" and add a app icon

Finally "Save Changes".

In order to read and write on facebook pages we need to get "publish_pages" and "manage_pages" permissions.

Go to "App Review" and request them.

.. image:: images/developers.facebook.com-review-permission.png
   :alt: "publish_pages" and "manage_pages" permissions

Finally go to Settings -> Basic -> "App Secret" -> "Show" and note the "App ID" and "App Secret".


Configure Zammad as Facebook app
================================

Go to "Admin -> Channels -> Facebook"

.. image:: images/zammad_connect_app1.png
   :alt: Admin -> Channels -> Facebook

Click on "Connect Facebook App" and enter your "App ID", "APP Secret" and verify the "Callback URL".

.. image:: images/zammad_connect_app2.png
   :alt: Connect Facebook App, click "Submit"

Done, your Zammad is configured as Facebook App now.


Link your Facebook Page to your Zammad Facebook app
===================================================

Now you need to link your Facebook Page from which you want to get posts and send out comments.

Click on "Add Account", then you will see the authorize app page of Facebook. Click on "authorize app".

.. image:: images/zammad_link_facebook_account.png
   :alt: Click on "Add Account"

.. image:: images/facebook.com_authorize_app.png
   :alt: Facebook authorize app page will appear

You will get redirected back to Zammad. Now you need to configure your search keys, where mentions and direct messages should get routed.

.. image:: images/zammad_linked_facebook_account.png
   :alt: Back in Zammad - settings

After you are done, you will get an overview of all linked Facebook Accounts.

.. image:: images/zammad_linked_facebook_account_done.png
   :alt: Back in Zammad - settings


Start using your new channel
============================

Start and write a post to your page, short time later you will have a new ticket in Zammad.

Just click on reply button (as you do it for emails) to send a comment.
