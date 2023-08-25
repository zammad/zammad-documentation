[![Documentation Status](https://readthedocs.org/projects/zammad/badge/?version=pre-release)](https://docs.zammad.org/en/pre-release/?badge=pre-release) (pre-release)

[![Documentation Status](https://readthedocs.org/projects/zammad/badge/?version=latest)](https://docs.zammad.org/en/latest/?badge=latest) (latest)

# Zammad Documentation

Source files for [Zammad’s
documentation][docs].

## Contributing

If you would like to improve the docs,
simply:

1. fork the repo,
2. edit the appropriate `.rst` files (see [Markup Format](#restructuredtext-markup) below), and
3. submit a pull request.

Thanks! ❤ ❤ ❤
   The Zammad Team

### ReStructuredText Markup

If you like to edit the docs, use the
ReStructuredText markup language.
Information about this markup language
can be found at:

- http://www.sphinx-doc.org/en/stable/
rest.html
- https://docutils.sourceforge.io/rst.
html

### Versioning

This documentation provides versions:

- ``pre-release`` can contain develop,
not yet released functions and changes
- ``main`` is the ``latest`` (and
stable) version of the repository
- ``stable-x.x`` is the old back port
for an earlier version
  - These branches do not receive
further updates and serve as
historic help
    for administrators

## Notes on Documentation Branches and Pull Requests

Please note that this repository uses
protected branches.
The most current version is
**always**  ``pre-release`` - if you
create
Pull Requests, please use
``pre-release`` as destination Branch.

This will ensure that your changes are
available upon merge.

## Compilation

### Dependencies

* sphinx

  ```
  $ pip install -r requirements.txt
  ```

### Example for a local HTML build

```
make html
```

[docs]: https://docs.zammad.org/en/latest/
