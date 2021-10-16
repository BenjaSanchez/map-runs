import os
import re

import folium
import gpxpy


# Location:
lat = 55.760274
lon = 12.541296


class RunMap():
    """
    Class that holds the folium map + a few methods to work with the map.
    """

    def __init__(self):
        """
        Initializes the folium map.

        Returns
        =======
        RunMap: object
            Map: folium.Map
                Map with predefined settings.
        """

        self.Map = folium.Map(
            location=[lat, lon],
            tiles='Stamen Terrain',
            zoom_start=12
        )

        print("Successfully initialized map")

    
    def add_run(self, file_path):
        """
        Function that adds a run to the map object.
        
        Parameters
        ==========
        file_path: str
            Path to a .gps file.
        """

        # Parse the gps file:
        file_name = os.path.basename(file_path)
        gpx_file = open(file_path, "r")
        gpx = gpxpy.parse(gpx_file)

        # Append all data related to a single activity to a list:
        run = list()
        for track in gpx.tracks:
            activity = re.split("\d", track.name)[0]
            for segment in track.segments:
                for point in segment.points:
                    run.append([point.longitude, point.latitude])

        # Create a GeoJson object and add it to the map:
        geojson = folium.GeoJson(
            {"type": "LineString", "coordinates": run},
            style_function=lambda feature: {"color": "#b80f0a", "opacity": 0.5, "weight": 3},
            highlight_function=lambda feature: {"color": "#ffc30b", "opacity": 1, "weight": 5},
            tooltip=activity + "/ " + file_name[:10]
        )
        geojson.add_to(self.Map)


    def add_all_runs(self, folder_path="./gps-data"):
        """
        Function that adds all runs to the map object.
        
        Parameters
        ==========
        folder_path: str
            Path to folder where the .gps files are.
        """

        for file_name in os.listdir(folder_path):
            self.add_run(os.path.join(folder_path, file_name))
        print("Successfully added all runs to map")


    def save(self, file_path="./output-map.html"):
        """
        Function that saves the map object as a .html file.
        
        Parameters
        ==========
        file_path: str
            Path where the .html will be saved.
        """

        self.Map.save(file_path)
        print("Successfully exported map")


def create_run_map(
    data_path="./gps-data",
    output_path="./output-map.html"
    ):
    """
    Function that creates an updated map with all runs.

    Parameters
    ==========
    data_path: str
        Path to folder with all .gps files.
    output_path: str
        Path where the .html will be saved.
    """

    # Initialize map:
    run_map = RunMap()

    # Add all runs:
    run_map.add_all_runs(data_path)

    # Export map:
    run_map.save(output_path)


# Call from shell:
if __name__ == "__main__":
    repo_path = os.path.join(os.path.dirname(__file__), "..") #TODO: make nicer
    create_run_map(
        data_path=os.path.join(repo_path, "gps-data"),
        output_path=os.path.join(repo_path, "output-map.html")
    )
