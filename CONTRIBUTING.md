# Contributing

## Development install

First, clone the repo to your local environment and change directory to the
newly cloned repo.
Then, install the package in development mode.

Recommended:

```bash
uv sync --group dev --group test
```

For simplicity, the following instructions will be written for `uv` users.

You can also create, activate, and manage your virtual environment manually with `venv`
and `pip` if you prefer, but it's more complicated!

## Development process

Double-check the server extension is properly installed:

```bash
uv run jupyter server extension list
```

Start JupyterLab:

```bash
uv run jupyter lab
```

Remember that changes won't immediately be reflected in the running instance of
JupyterLab.
Depending on what you've changed, you may need to restart the server (CTRL+C and start
JupyterLab again), or restart the kernel in the JupyterLab UI.

## Development uninstall

```bash
uv remove jupyter-xarray-tiler
```

## Testing the extension

This extension is using [Pytest](https://docs.pytest.org/) for Python code testing.

To execute tests, run:

```sh
uv run pytest --cov
```

## Packaging the extension

See [RELEASE.md](RELEASE.md)
