Jinja
=====

This action library provides integration with [Jinja], "[...] a full featured template engine for Python [...]" .

---

[Jinja]: http://jinja.pocoo.org/

Features
--------
The following features are available:

- Produce content using Jinja template
    - Per item content
    - Multiple item content


Requirements
------------
```sh
    pip install openpipe --user
    pip install Jinja2 --user
```

## How to test

```bash
openpipe install-action-lib jinja
openpipe test transform from jinja
```

## How to use

Check the [test file](test.yaml) for usage examples and configuration options.
