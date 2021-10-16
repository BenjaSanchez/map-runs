# map-runs

[![Build Status](https://github.com/benjasanchez/map-runs/actions/workflows/github-actions.yml/badge.svg)](https://github.com/BenjaSanchez/map-runs/actions/workflows/github-actions.yml)

Code for creating an HTML map with all runs mapped with [runkeeper](http://runkeeper.com) (or similar). It uses:

* [gpxpy](https://pypi.org/project/gpxpy) for parsing the `.gpx` files.
* [folium](https://pypi.org/project/folium) for visualizing the data in a Leaflet map.

## Installation

In a Python environment (created with e.g. [Conda](https://docs.conda.io/en/latest/)) and from the repository's root, run:

```bash
pip install .
```

**NB:** Tested for Python 3.5, 3.6, 3.7 & 3.8.

## Usage

### Instructions for creating your own map

1. Either clone locally or download this repo.
2. Request your running data from the app you use for tracking runs. In the case of runkeeper, you can do this [here](https://runkeeper.com/exportData) (it takes about a week for them to send you your data the first time).
3. Place all your `.gpx` files in `./gps-data`. Make sure to remove any preexisting files.
4. Modify the location (variables `lat` & `lon` in `./map_runs/map_runs.py`) to correspond to your hometown.
5. Follow the [installation instructions](#installation) if you have not done so yet.
6. Run locally `./map_runs/map_runs.py`.
7. Done! your map is now available at `./output-map.html`.

### Instructions for keeping your map up to date

These steps are only necessary if you would like to update automatically your map as you get new data with continuous integration (CI). You will need a local Git client + a Github account.

1. Fork this repo.
2. Follow steps 2-3-4 from the previous instructions.
3. Commit+push your changes to the repo.
4. Your map will be available in the `gh-pages` branch, at [`./output-map.html`](https://benjasanchez.github.io/map-runs/output-map.html).

## Credits

Thanks to Jörg R Schumacher ([@eHanseJoerg](https://github.com/eHanseJoerg)) for [this](https://nbviewer.jupyter.org/github/eHanseJoerg/folium/blob/master/examples/Highlight_Function.ipynb) useful jupyter notebook for plotting routes using the geoJSON format.
