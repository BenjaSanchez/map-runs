import os
import re

import folium
import gpxpy


# Location:
lat = 55.760274
lon = 12.541296


class RunMap():

    def __init__(self):
        self.Map = folium.Map(
            location=[lat, lon],
            tiles='Stamen Terrain',
            zoom_start=12
        )
        print("Successfully initialized map")

    
        """Function that adds a run to the map"""

    def add_run(self, file_path):
        file_name = os.path.basename(file_path)
        gpx_file = open(file_name, 'r')
        gpx = gpxpy.parse(gpx_file)
        run = list()
        for track in gpx.tracks:
            activity = re.split("\d", track.name)[0]
            for segment in track.segments:
                for point in segment.points:
                    run.append([point.longitude, point.latitude])

        track_name = activity + "/ " + file_name[:10]
        geojson = folium.GeoJson({'type': 'LineString', 'coordinates': run},
                                style_function=lambda feature: {'color': '#b80f0a', 'opacity': 0.5, 'weight': 3},
                                highlight_function=lambda feature: {'color': '#ffc30b', 'opacity': 1, 'weight': 5},
                                tooltip=track_name)
        geojson.add_to(self.Map)


    def add_all_runs(self, dir_name):

        for file_name in os.listdir(dir_name):
            self.add_run(os.path.join(dir_name, file_name))
        print("Successfully added all runs to map")


    def export(self, file_name):

        self.Map.save(file_name)
        print("Successfully exported map")


def create_run_map():
    """Function that creates an updated map with all runs"""

    # Initialize map:
    run_map = RunMap()

    # Add all runs from ./gps-data:
    run_map.add_all_runs('./gps-data')

    # Export map:
    run_map.export('./output-map.html')


# Call from shell:
if __name__ == '__main__':
    create_run_map()