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

 curl -u test@zammad.com:test123 https://xxx.zammad.com/api/v1/tickets/3

Put information::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X PUT -d '{ json: "data" }' https://xxx.zammad.com/api/v1/tickets/3

Post information::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X POST -d '{ json: "data" }' https://xxx.zammad.com/api/v1/tickets/3


Example CURL Requests (for tickets and users)
=============================================

Create a new ticket::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X POST -d '{"title":"Help me!","group": "Users","article":{"subject":"some subject","body":"some message","type":"note","internal":false},"customer":"email_of_existing_customer@example.com","note": "some note"}' https://xxx.zammad.com/api/v1/tickets

Search for tickets (with contains "some message")::

 curl -u test@zammad.com:test123 'https://xxx.zammad.com/api/v1/tickets/search?query=some+message&limit=10&expand=true'

Search for tickets (for tickets with state new and open )::

 curl -u test@zammad.com:test123 'https://xxx.zammad.com/api/v1/tickets/search?query=state:new%20OR%20state:open&limit=10&expand=true'

For more search examples regarding searching, please see `this page <https://user-docs.zammad.org/en/latest/advanced/search.html>`_ .

Create an new user::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X POST -d '{"firstname":"Bob","lastname":"Smith","email":"email_of_customer@example.com","roles":["Customer"],"password":"some_password"}' https://xxx.zammad.com/api/v1/users

Create an new user (with welcome email)::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -X POST -d '{"firstname":"Bob","lastname":"Smith","email":"email_of_customer@example.com","roles":["Customer"],"password":"some_password","invite":true}' https://xxx.zammad.com/api/v1/users

Search for users::

 curl -u test@zammad.com:test123 'https://xxx.zammad.com/api/v1/users/search?query=smith&limit=10&expand=true'

Example CURL Request on behalf of a different user
==========================================

It is possible to do a request on behalf of a different user. If you have your own application and you want to create a ticket for the customer
without the information that the api user has created this ticket then you can transfer the target user with the request to create the ticket on behalf of the customer user::

 curl -u test@zammad.com:test123 -H "Content-Type: application/json" -H "X-On-Behalf-Of: user-login" -X POST -d '{"title":"Help me!","group": "Users","article":{"subject":"some subject","body":"some message","type":"note","internal":false},"customer":"email_of_existing_customer@example.com","note": "some note"}' https://xxx.zammad.com/api/v1/tickets

The value of the header has to contain one of the following values:

* user id
* user login
* user email

The value types will be checked in a cascade and the first detected user by id, login or email will be used for the request action.

This functionality can be used for any type of action.

Requirements for the feature:

* Authenticated user must have **admin.user** permissions
* Feature is available since Zammad version 2.4

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

If you want to retrieve expanded information for a request (e. g. the organization attribute), you just need to add an ``expand=true`` to the request URL.

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

 GET /api/v1/users?expand=true&page=1&per_page=5 HTTP/1.1

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
* .NET Client - https://github.com/Asesjix/Zammad-Client
* Android API-Client - https://github.com/KirkBushman/zammad-android
  .. Note:: Please note that this is a API client only, it's no "ready to use" App.
