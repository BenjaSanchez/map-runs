# map-runs

[![Build Status](https://travis-ci.org/BenjaSanchez/map-runs.svg?branch=master)](https://travis-ci.org/BenjaSanchez/map-runs)

Code for creating an HTML map with all runs mapped with [runkeeper](http://runkeeper.com) (or similar).

## Requirements

* Python (tested for 2.7, 3.4, 3.5, 3.6 & 3.7).
* folium (`pip install folium`) for visualizing the data in a Leaflet map.
* gpxpy (`pip install gpxpy`) for parsing the `.gpx` files.

## Instructions for creating your own map

1. Either clone locally or download this repo.
2. Request your running data from the app you use for tracking runs. In the case of runkeeper, you can do this [here](https://runkeeper.com/exportData) (it takes about a week for them to send you your data).
3. Place all your `.gpx` files in `./gps-data`. Make sure to remove any preexisting files.
4. Modify the location (variables `lat` & `lon` in `./scripts/map_runs.py`) to correspond to your hometown.
5. Run locally `./scripts/map_runs.py` (make sure you have all requirements installed).
6. Done! your map is now available at `./output-map.html`.

## Instructions for setting up continuous integration

These steps are only necessary if you would like to update automatically your map as you get new data with continuous integration (CI). You will need both Github and [Travis CI](https://travis-ci.org) accounts.

1. Fork this repo.
2. Trigger CI by Travis for your fork.
3. Get a personal access token from Github with `repo` access (instructions [here](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)).
4. Add said token as an environment variable (with name `GITHUB_TOKEN`) in Travis' settings for your fork.
5. Follow steps 2-3-4 from the previous instructions.
6. Commit+push your changes to the repo.
7. Your map will be available in the `gh-pages` branch, at [`./output-map.html`](https://benjasanchez.github.io/map-runs/output-map.html).
