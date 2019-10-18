Working on chat based information
*********************************

.. Note:: Please note that this is not a full command list, if you're missing commands, feel free to ask over at our `Community <https://community.zammad.org>`_.

Removing IP information from Chat-Sessions
------------------------------------------

In some cases you might need or want to remove IP information from closed Chat-Sessions. 
The below exmaple will remove all IP information if the Chat-Session was last updated 7 days ago and is closed.
::
  
  Chat::Session.where(state: 'closed').where('updated_at < ?', 7.days.ago).each do |session|
    session.preferences.delete('geo_ip')
    session.preferences.delete('remote_ip')
    session.save!
  end

