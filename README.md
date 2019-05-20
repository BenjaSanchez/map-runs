# map-runs

[![Build Status](https://travis-ci.org/BenjaSanchez/map-runs.svg?branch=master)](https://travis-ci.org/BenjaSanchez/map-runs)

Code for creating an HTML map with all runs mapped with [runkeeper](http://runkeeper.com) (or similar).

## Requirements

* Python (tested for 2.7, 3.4, 3.5, 3.6 & 3.7).
* folium (`pip install folium`) for visualizing the data in a Leaflet map.
* gpxpy (`pip install gpxpy`) for parsing the `.gpx` files.

## Instructions for creating your own map

1. Request your running data from the app you use for tracking runs. In the case of runkeeper, you can do this at https://runkeeper.com/exportData (it takes about a week for them to send you your data).
2. Either clone locally or download this repo. If you would like to have continuous integration set up, create the proper fork and modify the `.travis.yml` accordingly.
3. Place all your `.gpx` files in `./gps-data`. Make sure to remove the preexisting files that are there.
4. Modify the location (variables `lat` & `lon` in `map_runs.py`) to correspond to your hometown.
5. Run `map_runs.py` (make sure you have all requirements installed).
6. Done! your map is now available at `./output-map.html`.
