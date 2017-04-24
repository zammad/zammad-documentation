Introduction
************

Zammad is a web based open source helpdesk/ticket system with many features
to manage customer communication via several channels like telephone, facebook,
twitter, chat and e-mails.

This chapter describes the Zammad API v1.

The API
=======

Zammad provides a REST/JSON API. Its endpoints are documented with the HTTP method for the request and a partial resource.

Example::

 GET /api/v1/users


The full URL looks like::

 https://your_zammad/api/v1/users


Curly braces {} indicate values you have to supply for the URL.

Example::

 GET  /api/v1/users/{id}


Authentication
==============

Zammad supports three different authentication methods for API.


HTTP Basic Authentication (username/password)
---------------------------------------------

The username/password must be provided as HTTP header in the HTTP call. The Zammad admin can enable/disable the authentication method in the admin interface. Read more about HTTP basic authentication [here](https://en.wikipedia.org/wiki/Basic_access_authentication).

Example::

 curl -u {username}:{password} https://your_zammad/api/v1/users


HTTP Token Authentication (access token)
----------------------------------------

The access token must be provided as HTTP header in the HTTP call. Each user needs to create its own access token in the user preferences. The Zammad admin can enable/disable the authentication method in the admin interface.

Example::

 curl -H "Authorization: Token token={your_token}" https://your_zammad/api/v1/users


OAuth2 (token access)
---------------------

The Zammad API supports OAuth2 authorization. In order to create OAuth2 tokens for an external application, the Zammad user needs to create an application in the admin interface. The access token then has to be given within the HTTP header:

Example::

 curl -H "Authorization: Bearer {your_token}" https://your_zammad/api/v1/users


Request Format
==============

Zammad uses JSON for its API, so you need to set a "Content-Type: application/json" in each HTTP call. Otherwise the response will be text/html.

Example::

 POST /api/v1/users/{id} HTTP/1.1
 Content-Type: application/json

 {
  "name":"some name",
  "organization_id": 123,
  "note":"some note"
 }

Example CURL Requests
=====================

Get information::

 curl -u test@zammad.com:test123 https://xxx.zammad.com/api/v1/users/3

Put information::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X PUT -d '{ json: 'data' }' https://xxx.zammad.com/api/v1/tickets/3

Post information::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X POST -d '{ json: 'data' }' https://xxx.zammad.com/api/v1/users/3

Post file and form data::

 curl -u test@zammad.com:test123 -X POST --form form_id=740354910 --form File=@/workspace/test.jpg https://xxx.zammad.com/api/v1/ticket_attachment_upload

Response Format
===============

If a response is successful, an HTTP status code in the 200 or 300 range will be returned. If an item has been created or updated, all new attributes will be returned (also server side generated attributes like created_at and updated_at).

Example::

 Status: 201 Created
 Content-Type:application/json; charset=utf-8

 {
  "id": 123,
  "name":"some name",
  "organization_id": 123,
  "note":"some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Response Format (expanded)
==========================

If you want to retrieve expanded information for a request (e. g. the organization attribute), you just need to add an ```expand=true``` to the request URL.

Example::

 GET /api/v1/users/{id}?expand=true HTTP/1.1

will return the following structure, expanded by "organization"::

 Status: 200 Ok
 Content-Type:application/json; charset=utf-8

 {
  "id": 123,
  "name":"some name",
  "organization_id": 123,
  "organization": "Some Organization Name",
  "note":"some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
 }


Pagination
==========

All resources support pagination::

 GET /api/v1/users?expand=true&page=1,per_page=5 HTTP/1.1

will return five records beginning with first record of all::

 Status: 200 Ok
 Content-Type:application/json; charset=utf-8

 [
  {
    "id": 1,
    "name":"some name 1",
    "organization_id": 123,
    "organization": "Some Organization Name",
    "note":"some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 2,
    "name":"some name 2",
    "organization_id": 345,
    "organization": "Some Other Organization Name",
    "note":"some note",
    "updated_at": "2016-08-17T07:55:42.221Z",
    "created_at": "2016-08-16T09:112:42.221Z"
  },
  ...
 }


API clients
===========

* Ruby Client - https://github.com/zammad/zammad-api-client-ruby
* PHP Client - https://github.com/zammad/zammad-api-client-php
