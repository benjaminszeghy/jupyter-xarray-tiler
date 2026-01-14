# Jupyter MicroGIS

[![Github Actions Status](https://github.com/geojupyter/jupyter-server-titiler/workflows/Build/badge.svg)](https://github.com/geojupyter/jupyter-server-titiler/actions/workflows/build.yml)

> [!IMPORTANT]
> This repository is experimental and in the prototype stage.
> Expect nothing to work.
> Expect it to be broken up in to multiple repositories and for the name to change in
> the future.

A Jupyter extension which provides a barebones read-only GIS experience from Xarray and
GeoPandas objects in a widget.

Inspired by [jupytergis-tiler](https://github.com/geojupyter/jupytergis-tiler) by
[David Brochart](https://github.com/davidbrochart).

Goals:

- Serve users' simplest reasons for leaving JupyterLab for QGIS to make a cloud-only
  workflow more comfortable
- Simple API with usable defaults (`explore(ds, ds, gdf, { data: gdf, symbology: "choropleth"}`)
- Re-arrange, show/hide, change transparency of layers

Stretch goals:

- Data discovery interface to find and visualize public datasets alongside your
  Python data objects
- Simple symbology editing

Non-goals:

- Exporting maps
- Data analysis (use a Notebook!)
- Advanced Symbology

This extension is composed of a Python package named `jupyter_server_titiler`
for the server extension and an NPM package named `jupyter-server-titiler`
for the frontend extension.

## Requirements

- JupyterLab >= 4.0.0

## Install

> [!WARNING]
> This method of installation doesn't work yet, see the dev instuctions for now.

To install the extension, execute:

```bash
pip install jupyter_server_titiler
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyter_server_titiler
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```bash
jupyter labextension list
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
