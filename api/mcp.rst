MCP Server
==========

Zammad answers the *Model Context Protocol* (MCP) on a server of its own, next
to the REST API. An AI client, a chat application or a coding tool for example,
reads, finds, updates and creates tickets through it. The server is part of
every installation, nothing has to be installed or run in addition.

This page describes the tools the server offers and the limits that apply to
them. Switching the server on and the tokens it accepts are described in the
:admin-docs:`API settings </system/api.html>`, connecting a client in the
:user-docs:`user documentation </extras/mcp-server.html>`.

Access
------

The server answers at ``https://{fqdn}/mcp`` over the MCP transport
*Streamable HTTP*, and only to ``POST`` requests. A client has to send a fixed
``Authorization: Bearer {your_token}`` header with every request. Supporting the
transport alone is not enough, a client that cannot set the header stays out.

Requests reach the server only at the **Fully Qualified Domain Name**, the
**Alternative fully qualified domain name** or a loopback address
(``localhost``, ``127.0.0.1``, ``::1``). Requests at another address are
refused, as are browser requests from another origin, which protects the
server against DNS rebinding.

The **MCP server** toggle is off by default. While it is off the server refuses
every request, whatever token the request carries. Clients authenticate with
personal access tokens only: neither a password nor an OAuth2 token gets in,
and neither does a request acting on behalf of another user. The token and its
owner both keep their limits, so a client can do exactly what they may do and
nothing more. Every tool requires the ``ticket.agent`` permission, and a user
without agent permissions, a customer for example, gets no tools at all.

Tools
-----

The client gets the following tools, in an order it decides itself. The access
column names what a tool does with the data: ``read`` changes nothing,
``write`` changes a ticket.

.. list-table::
   :widths: 30 8 62
   :header-rows: 1

   * - Tool
     - Access
     - What it does
   * - ``add_internal_note``
     - write
     - Adds an internal note to a ticket. The customer never sees it.
   * - ``create_article``
     - write
     - Adds an article to a ticket or sends a reply to the customer.
   * - ``create_ticket``
     - write
     - Creates a ticket with a first message from a phone call or an email, or
       as an internal note.
   * - ``get_current_user``
     - read
     - Reads the user the connection works as, with their groups and their
       knowledge base access.
   * - ``get_knowledge_base_answer``
     - read
     - Reads one knowledge base answer in full, in the locale asked for.
   * - ``get_organization``
     - read
     - Reads an organization with its domain, VIP flag, note, custom fields and
       members.
   * - ``get_overview_tickets``
     - read
     - Reads the tickets of an overview, such as "My Assigned Tickets".
   * - ``get_shared_draft``
     - read
     - Reads the shared draft saved for a ticket.
   * - ``get_ticket``
     - read
     - Reads a ticket with its customer, organization, owner, links and
       messages.
   * - ``get_ticket_articles``
     - read
     - Reads the messages of a ticket: an index, a search in them or chosen
       ones with their text.
   * - ``get_ticket_fields``
     - read
     - Lists the fields a ticket has, with the values to choose from.
   * - ``get_ticket_history``
     - read
     - Reads what changed on a ticket, when and by whom or by which automation.
   * - ``get_user``
     - read
     - Reads a user with email, phone, mobile, organizations and custom fields.
   * - ``link_knowledge_base_answer``
     - write
     - Links a knowledge base answer to a ticket.
   * - ``link_tickets``
     - write
     - Links two tickets.
   * - ``list_overviews``
     - read
     - Lists the overviews with their number of tickets.
   * - ``list_tags``
     - read
     - Lists the tags that exist, the most used first.
   * - ``read_attachment``
     - read
     - Reads the text of a file attached to a ticket message. See
       `Limits`_ for which files it reads.
   * - ``save_shared_draft``
     - write
     - Saves a reply as the shared draft of a ticket. Nothing is sent.
   * - ``search_knowledge_base``
     - read
     - Searches the knowledge base by words or by meaning.
   * - ``search_organizations``
     - read
     - Finds organizations by their name or their domain.
   * - ``search_tickets``
     - read
     - Searches tickets by a query, by filters or both.
   * - ``search_users``
     - read
     - Finds users by name, email, login or phone number.
   * - ``send_shared_draft``
     - write
     - Sends the shared draft of a ticket as it is saved.
   * - ``set_ticket_tags``
     - write
     - Adds tags to a ticket and removes tags from it.
   * - ``update_ticket``
     - write
     - Changes state, priority, group, owner, pending time or custom fields of
       a ticket.

The three knowledge base tools, ``get_knowledge_base_answer``,
``link_knowledge_base_answer`` and ``search_knowledge_base``, appear only
where a knowledge base is active.

Limits
------

A tool reads the text of a text file: plain text, logs, CSV, JSON, XML or
HTML, up to 10 MB. Any other file, and a larger one, is not read. The tool then
says why and returns the file's download link, so the client can hand the link
to the user. A long text arrives in parts, one part per call.

Files cannot be sent through the server. ``create_article`` and
``create_ticket`` take text only, a user who wants to send a file adds it to
the message in Zammad itself.

Which messages a client sends without a further approval is described in the
:admin-docs:`API settings </system/api.html>`.
