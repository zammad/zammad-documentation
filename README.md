[![Documentation Status](https://readthedocs.org/projects/zammad/badge/?version=pre-release)](https://docs.zammad.org/en/pre-release/?badge=pre-release) (pre-release)

[![Documentation Status](https://readthedocs.org/projects/zammad/badge/?version=latest)](https://docs.zammad.org/en/latest/?badge=latest) (latest)

# Zammad Documentation

Source files for [Zammad’s documentation](https://docs.zammad.org/en/latest/).

## Contributing

Please see [the Contributing section in this manual](https://docs.zammad.org/en/latest/contributing/start.html).

## Compilation

### Dependencies

Either install the dependencies on your machine or use a devcontainer, see next section.

* sphinx

  ```
  $ pip install -r requirements.txt
  ```
### Devcontainer

If you can't or don't want to install the dependencies on your system, you can use a devcontainer. The repo
is prepared so you just need a supported editor (e.g. VS Code) and a Docker installation on your system.

Simply open the cloned repo in a supported editor and it should ask you to open the folder in a container. After it got
set up, you can compile the docs with your changes locally.

For more information, check these resources:

- https://github.com/devcontainers/
- https://containers.dev/

### Example for a local HTML build

```
make html
```
