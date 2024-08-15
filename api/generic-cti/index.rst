Generic CTI
===========

This page describes the generic CTI API scopes and functionalities.

.. include:: /api/generic-cti/cti-endpoint-limitations.include.rst

Features
   Here's a small condensed list of the possibilities this CTI API provides.

   Inbound
      * :user-docs:`Caller log functions </extras/caller-log.html>` for your
        agents.
      * Blocking of CallerIDs during signaling.

   Outbound
      * :user-docs:`Caller log functions </extras/caller-log.html>` for your
        agents.
      * Set outbound caller IDs depending on the caller ID target.

Endpoint
   The endpoint can be found in the generic CTI integration and contains a
   unique token which acts as authentication. Make sure to keep this endpoint
   URL safe.

   .. hint::

      Generic CTI configuration and the correct endpoint can be found in your
      Zammad integration settings and are documented in our
      :admin-docs:`admin documentation </system/integrations/cti/generic.html>`.

      | Please also note the there listed requirements and limitations.
      | All options that require returns (e.g. blocking, manipulating
        outgoing caller IDs) rely on configurations within the Zammad CTI
        integration page.

Events
   There are several events in terms of an ongoing call.
   These actions always come from your PBX system and may be:

      * :doc:`"newCall" event <newcall-event>` (initiation of a call)
      * :doc:`"hangup" event <hangup-event>` (call ending)
      * :doc:`"answer" event <answer-event>` (aka picking up the phone)

   In some situations Zammad may provide a return on your PBX calls
   (e.g. a reject) if you blocked a specific caller. Zammad will never initiate
   specific actions with your PBX. Zammad is a passive component in all
   described cases.

.. toctree::
   :hidden:

   /api/generic-cti/newcall-event
   /api/generic-cti/hangup-event
   /api/generic-cti/answer-event
