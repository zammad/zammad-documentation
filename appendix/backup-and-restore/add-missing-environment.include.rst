If you've set any environmental settings like higher web concurrency
due to required performance tuning via
`environment variables </appendix/environment-variables>`, please re-apply your
settings now.

If not already done, please install Elasticsearch now (if you want to use it).
Follow :ref:`configure_zammad_with_elasticsearch` to reconfigure your
installation for Elasticsearch use and rebuild the search index.

You are now ready to continue your work.
The rebuild of your search index can safely run during your work, but will
cause a degraded search performance and may lead to temporarily not found
data.
