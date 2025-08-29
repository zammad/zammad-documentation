After the import has finished, run the following commands:
   .. code-block:: irb

      >> Setting.set('import_mode', false)

   .. code-block:: irb

      >> Setting.set('system_init_done', true)

   .. code-block:: irb

      >> Rails.cache.clear
