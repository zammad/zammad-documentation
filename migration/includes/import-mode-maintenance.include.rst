.. warning::

   Import mode also enables the :admin-docs:`maintenance mode
   </system/maintenance.html>`, for as long as import mode is enabled. Zammad
   then denies every request of a user without the ``admin.maintenance``
   permission. Turn import mode off again before letting users work in the
   instance.
