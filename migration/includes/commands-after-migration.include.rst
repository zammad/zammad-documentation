After the import has finished, run the following commands
   .. code-block:: ruby
      :force:

      $ Setting.set('import_mode', false)
      $ Setting.set('system_init_done', true)
      $ Rails.cache.clear
