Search Cheat Sheet
******************

Tickets, articles (with attachments), users and organizations are indexed by default.

A simple search for all objects can be: "something". If you want to search for objects with certain attributes you can use "attribute: something".

* For example: "customer: some name"

With complex searches you can use conditions with () and AND/OR options.

* For example: "state: open AND (from:me OR from:somebody else)"

Note: In general you can use Elasticsearch queries for search (https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html).

Examples
========

For a more detailed list of available attributes please see:
[https://docs.zammad.org/en/latest/install-elasticsearch.html#list-of-values-which-are-stored-in-elasticsearch]

* number:1118566
* title:"some words with spaces" # exact phrase / without quotation marks " an AND search for the words will be performed (in Zammad 1.5 and lower an OR search will be performed)
* title:"some wor*" # exact phrase beginning with "some wor*" will be searched
* created_at:[2017-01-01 TO 2017-12-31] # a time range
* created_at:>now-1h # created within last hour
* state:new OR state:open
* (state:new OR state:open) OR priority:"3 normal"
* (state:new OR state:open) AND customer.lastname:smith
* state:(new OR open) AND title:(full text search) # state: new OR open & title: full OR text OR search
* tag: sometag
* tag: "some tag"
* owner.email: "bod@example.com" AND state: (new OR open OR pending*) # show all open tickets of a certain agent
* state:closed AND _missing_:tag # all closed objects without tags
* article_count: [1 TO 5] # tickets with 1 to 5 articles
* article:count: [10 TO *] # tickets with 10 or more articles
* article.from: *bob* # also article.from can be used
* article.body: heat~ # using the fuzzy operator will also find terms that are similar, in this case also "head"
* article.body: /joh?n(ath[oa]n)/ # using regular expressions

Ticket attributes
=================

* number: string
* title: string
* group: string
* priority: string
* state: string
* organization: string
* owner: object (owner.firstname, owner.lastname, owner.email, ...)
* customer: object (customer.firstname, customer.lastname, customer.email, ...)
* first_response_at: timestamp
* first_response_in_min: integer (business min till first response)
* close_at: timestamp
* close_in_min: integer (business min till close)
* last_contact_at: timestamp (last contact by customer or agent)
* last_contact_agent_at: timestamp (last contact by agent)
* last_contact_customer_at: timestamp (last contact by customer)
* create_article_type: string (email|phone|web|...)
* create_article_sender: string (Customer|Agent|System)
* article_count: integer
* escalation_at: timestamp
* pending_time: timestamp

Article attributes
==================

* article.from: string
* article.to: string
* article.cc: string
* article.subject: string
* article.body: string
* article.attachment._name: string (filename of attachment)
* article.attachment._content: string (content of attachment)

