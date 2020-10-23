from OTRS
*********

Install plugins on OTRS
=======================

.. Note:: Currently only passwords of OTRS >= 3.3 can be reused in Zammad! Passwords that were stored in another format than the default SHA2 are not possible to use. Users then have to use the password reset procedure.

Install Znuny4OTRS-Repo
-----------------------

This is a dependency of the OTRS migration plugin

* On OTRS 6:

  *  https://addons.znuny.com/api/addon_repos/public/1029/latest

* On OTRS 5:

  *  https://addons.znuny.com/api/addon_repos/public/615/latest

* On OTRS 4:

  *  https://addons.znuny.com/api/addon_repos/public/309/latest
  
* On OTRS 3:

  *  https://addons.znuny.com/api/addon_repos/public/142/latest


Install OTRS migration plugin
-----------------------------

* OTRS 6:

  * https://addons.znuny.com/api/addon_repos/public/1085/latest

* OTRS 5:

  * https://addons.znuny.com/api/addon_repos/public/617/latest

* OTRS 4:

  * https://addons.znuny.com/api/addon_repos/public/383/latest

* OTRS 3.1 - 3.3:

  * https://addons.znuny.com/api/addon_repos/public/287/latest


Import via Browser
==================

.. Note:: If your OTRS installation is rather huge, you might want to consider using the command line version of this feature.

After installing Zammad, open http://localhost:3000 with your browser and follow the installation wizard.
From there you're able to start the migration from OTRS.

See the Video at `this site <https://days.zammad.org/features/migrator>`_ .


Import via command line
=======================

If you miss this at the beginning or you want to re-import again you have to use the command line at the moment.

Stop all Zammad processes and switch Zammad to import mode (no events are fired - e. g. notifications, sending emails, ...)


If you installed the Zammad DEB or RPM package
----------------------------------------------

::

 zammad run rails c


If you installed from source
----------------------------

::

 su zammad
 cd /opt/zammad
 rails c


Extending import time for big installations (optional)
------------------------------------------------------

Optional, if you're having a bigger installation or running in timeouts like:
``Delayed::Worker.max_run_time is only 14400 seconds (4 hours)`` you need to do the following:

For importing via console
^^^^^^^^^^^^^^^^^^^^^^^^^

* open the file ``config/initializers/delayed_jobs_settings_reset.rb`` and add the following at the end of it:
  :: 
    
    Delayed::Worker.max_run_time = 7.days

* Restart the Zammad-Service (``systemctl restart zammad``)

For importing via browser (not recommended on big installations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run below in a Zammad console and ensure to not close it during import:
  :: 
    
    Delayed::Worker.max_run_time = 7.days


.. Note:: The above setting is only valid for the lifetime of the Zammad rails console.
  If you close the console, the change is reset to the default value.
 
Enter the following commands in the rails console
-------------------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Import::OTRS.start


After the import is done switch Zammad back to non-import mode and mark the system initialization as done.

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.

Importing a diff
================

.. Note:: This is only possible after finishing an earlier OTRS import **successful**.

In some cases it might be desirable to update the already imported data from OTRS. This is possible with the following commands.

Enter the following commands in the rails console
-------------------------------------------------

::

 Setting.set('import_otrs_endpoint', 'http://xxx/otrs/public.pl?Action=ZammadMigrator')
 Setting.set('import_otrs_endpoint_key', 'xxx')
 Setting.set('import_mode', true)
 Setting.set('system_init_done', false)
 Import::OTRS.diff_worker

After the import is done switch Zammad back to non-import mode and mark the system initialization as done.

::

 Setting.set('import_mode', false)
 Setting.set('system_init_done', true)

Start all Zammad processes again. Done.


Restarting from scratch
=======================

First make sure all Zammad processes are stopped. After that reset your database.

If you installed the Zammad DEB or RPM package
----------------------------------------------

::

 zammad run rake db:drop
 zammad run rake db:create
 zammad run rake db:migrate
 zammad run rake db:seed


If you installed from source
----------------------------

::

 rake db:drop
 rake db:create
 rake db:migrate
 rake db:seed

After that your DB is reset and you can start the import right over.


Debug
=======================

In case of fail/error during import process or network error that stop import process in the middle of big OTRS instance this debug script can be used.


1.) Create a file called `debug_1349.rb` in your Zammad directory (usually `/opt/zammad`)

.. code-block:: ruby

  otrs_url = 'http://your.domain.tld'
  key      = '*YourKeyHere*'

  require 'import/otrs'
  require 'import/otrs/article'
  require 'import/otrs/article/attachment_factory'


  module Import
    module OTRS
      class Article
        module AttachmentFactory

      def import_single(local_article, attachment)
            decoded_filename = Base64.decode64(attachment['Filename'])
            decoded_content  = Base64.decode64(attachment['Content'])
            # TODO: should be done by a/the Storage object
            # to handle fingerprinting
            sha = Digest::SHA256.hexdigest(decoded_content)

            retries = 3
            begin
              queueing(sha, decoded_filename)

              log "Ticket #{local_article.ticket_id}, Article #{local_article.id}, Attachment ContentType #{attachment['ContentType']} - Starting import for fingerprint #{sha} (#{decoded_filename})... Queue: #{@sha_queue[sha]}."
              ActiveRecord::Base.transaction do
                Store.add(
                  object:        'Ticket::Article',
                  o_id:          local_article.id,
                  filename:      decoded_filename.force_encoding('utf-8'),
                  data:          decoded_content,
                  preferences:   {
                    'Mime-Type'           => attachment['ContentType'],
                    'Content-ID'          => attachment['ContentID'],
                    'content-alternative' => attachment['ContentAlternative'],
                  },
                  created_by_id: 1,
                )
              end
              log "Ticket #{local_article.ticket_id}, Article #{local_article.id} - Finished import for fingerprint #{sha} (#{decoded_filename})... Queue: #{@sha_queue[sha]}."
            rescue ActiveRecord::RecordNotUnique, ActiveRecord::StatementInvalid => e
              log "Ticket #{local_article.ticket_id} - #{sha} - #{e.class}: #{e}"
              sleep rand 3
              retry if !(retries -= 1).zero?
              raise
            rescue => e
              log "Ticket #{local_article.ticket_id} - #{sha} - #{e}: #{attachment.inspect}"
              raise
            ensure
              queue_cleanup(sha)
            end
          end
        end
      end
    end
  end

  endpoint = "#{otrs_url}/otrs/public.pl?Action=ZammadMigrator"

  Setting.set('import_otrs_endpoint', endpoint)
  Setting.set('import_otrs_endpoint_key', key)
  Setting.set('import_mode', true)
  Setting.set('system_init_done', false)

  Import::OTRS.start({threads: 1, limit:50, offset: 7500})

You can easy modify:

- `threads` - How many threads to use during import. (This is not limited to CPU threads)

- `limit` - How many tickets to get with one request from OTRS (Keep this relevantly small to not overkill your OTRS server)
- `offset` - From what offset to start import. This is very usefully in case of fail of last import. To found right offset just execute:

::

  `tail -500 /var/log/zammad/production.log | grep PARAMS` 
  
and determinate point around your last improt stop. Because of multi thread default behavior it is good to remove ~500 offset so to be sure that you will not miss anything. (Tickets will not get dublicated in Zammad!)


2.) Run the file from your Zammad directory via:

::

 $ zammad run rails r debug_1349.rb 
 
 # or (as zammad user, depending on your installation source (package/source))
 $ rails r debug_1349.rb 



.. Note:: You can overwrite origin functions (we give example with import_single() where we add `Attachment ContentType #{attachment['ContentType']}`) and modify behavior. May be you want/need more debug info - go edit the script and add what you need!