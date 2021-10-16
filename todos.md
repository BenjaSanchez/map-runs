* new features:
  * keep run highlighted when clicked on (not possible afaik with folium atm)
  * display basic stats of the run when clicked on
* performance issues:
  * switch to better rendering (folium is slow)
  * skip build if no data is added
* misc:
  * add tests
  * update links to folium & gpxpy homepages + terrain customizations in readme
  * find proper way of getting parent directory
  * make command line tool: `map-runs ./gps-folder -o output.html -v`. Allow `.ini` parameters as input
  * index in PyPI
  * organize versions
  * history file
