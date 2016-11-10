Introduction
************

Zammad is a web based open source helpdesk/ticket system with many features
to manage customer communication via several channels like telephone, facebook,
twitter, chat and e-mails.

This chapter describes the Zammad API v1.

The API
=======

The API is a REST/JSON API. Endpoints are documented with the HTTP method for the request and a partial resource.

Example::

 GET /api/v1/users


The full url looks like::

 https://your_zammad/api/v1/users


Curly braces, {}, indicate values you have to supply for the url.

Example::

 GET  /api/v1/users/{id}


Authentication
==============

Zammad supports 3 different authentication methods for the Zammad API.


HTTP Basic Authentication (username/password)
---------------------------------------------

The username/password provided as http header in the http call. The Zammad admin can enable/disable his authentication method in the admin interface. Read more about HTTP Basic Authentication [here](https://en.wikipedia.org/wiki/Basic_access_authentication).

Example::

 curl -u {username}:{password} https://your_zammad/api/v1/users


HTTP Token Authentication (Access Token)
----------------------------------------

The access token provided as http header in the http call. Each user need to create it's own access token in user preferences. The Zammad admin can enable/disable his authentication method in the admin interface.

Example::

 curl -H "Authorization: Token token={your_token}" https://your_zammad/api/v1/users


OAuth2 (Token Access)
---------------------

The Zammad API supports OAuth2 authorization. In order to create OAuth2 tokens by an external application, the Zammad user needs to create an Application in the admin interface first. In your requests, specify the access token in an authorization header as follows:

Example::

 curl -H "Authorization: Bearer {your_token}" https://your_zammad/api/v1/users


Request Format
==============

The Zammad API is a JSON API, so you need to set a "Content-Type: application/json" in each http call. If you do not so, you will get and text/html response.

Example::

 POST /api/v1/users/{id} HTTP/1.1
 Content-Type: application/json
 
 {
  "name":"some name",
  "organization_id": 123,
  "note":"some note"
 }


Response Format
===============

If an response is successful, an HTTP status codes in the 200 or 300 range is returned. If an item got created or updated, all new attributes will be returned (also server site generated attributes like created_at and updated_at).

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

If you want to get reference lookup in response (e. g. the organization attribute will be added at response), you just need to add a ```expand=true``` to the request url.

Example::

 GET /api/v1/users/{id}?expand=true HTTP/1.1

will return a record link this::

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

All resources support a pagination functionality. You can do like this::

 GET /api/v1/users?expand=true&page=1,per_page=5 HTTP/1.1

will return 5 records beginning with first record of all::

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
