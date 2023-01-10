Working with chat logs
**********************

.. include:: /admin/console/missing-commands-ask-community.include.rst

Removing IP address logs
------------------------

Use the following command to remove all IP address records
from **closed chats that haven’t been updated in the last seven days**:

.. code-block:: ruby

   >> Chat::Session.where(state: 'closed').where('updated_at < ?', 7.days.ago).each do |session|
        next if session.preferences['remote_ip'].blank?

        session.preferences.delete('geo_ip')
        session.preferences.delete('remote_ip')
        session.save!(touch: false)
      end
