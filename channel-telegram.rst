Telegram
*******

It's possible to put your Telegram Bot communication into Zammad. To do so, you need to follow these steps.

Note: Your Zammad instance need to be available via https from public (we use Telegram WebHooks).

Register a Telegram Bot app
====================

Register your Telegram Bot via your Telegram client, see also here: https://core.telegram.org/bots#3-how-do-i-create-a-bot

Got to BotFather

.. image:: images/telegram_bot_start.png
   :alt: inital page

Register a new bot by using "/newbot", definde name and username

.. image:: images/telegram_bot_name_and_username.png
   :alt: /newbot

All done, you will get your Telegram Bot API token

.. image:: images/telegram_bot_finish.png
   :alt: bot is created


Configure Zammad as Telegram Bot
===============================

Go to "Admin -> Channels -> Telegram" and click "Add Bot"

.. image:: images/telegram_admin_new.png
   :alt: Admin -> Channels -> Telegram

Enter your "API Token", enter your "welcome message" and set the incoming group.

.. image:: images/telegram_admin_new_done.png
   :alt: Telegram Bot added

Done, your Zammad is configured as Telegram Bot now.


Start using your new channel
============================

Go to your Telegram client, search for your new Telegram Bot and start writing a message.

.. image:: images/telegram_client_search_bot.png
   :alt: search for bot

.. image:: images/telegram_client_start.png
   :alt: enter a new message

.. image:: images/telegram_client_start_with_first_message.png
   :alt: first message

After a few seconds a new message in Zammad appears.

.. image:: images/telegram_agent_new_message.png
   :alt: A new Ticket - the message - just reply

Just click on reply button (as you do it for emails) to send a reply.

.. image:: images/telegram_agent_reply.png
   :alt: Ticket reply

The message will appear in your Telegram client.

.. image:: images/telegram_client_start_with_messages.png
   :alt: enter a new message
