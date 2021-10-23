from configparser import ConfigParser
from pathlib import Path
import os
import re

import folium
import gpxpy

import map_runs


REPO_PATH = Path(os.path.dirname(map_runs.__file__)).parent.absolute()
INIT_FILE_PATH = os.path.join(REPO_PATH, "map-runs.ini")


class RunMap():
    """
    Class that holds the folium map + a few methods to work with the map.
    """

    def __init__(self, init_file_path=INIT_FILE_PATH, verbose=None):
        """
        Initializes the folium map.

        Parameters
        ==========
        init_file_path: str
            Path to .ini file with map parameters.
        verbose: bool
            Weather any output should be printed or not. If not
            specified, it will default to what is indicated in
            map-runs.ini.

        Returns
        =======
        RunMap: object
            Object with a folium.Map attribute + a few other handy
            attributes/methods.
        """

        # Set map parameters:
        config = ConfigParser()
        config.read(init_file_path)
        self.run_color = config["layout-settings"]["run-color"]
        self.run_opacity = float(config["layout-settings"]["run-opacity"])
        self.run_weight = int(config["layout-settings"]["run-weight"])
        self.highlight_color = config["layout-settings"]["highlight-color"]
        self.highlight_opacity = float(config["layout-settings"]["highlight-opacity"])
        self.highlight_weight = int(config["layout-settings"]["highlight-weight"])

        # Parse verbose setting if not defined:
        if verbose is None:
            verbose = bool(config["misc-settings"]["verbose"])

        # Set misc parameters:
        self.verbose = verbose
        self.data_path = config["misc-settings"]["data-path"]
        self.output_path = config["misc-settings"]["output-path"]

        # Create folium.Map object:
        lat = float(config["start-settings"]["starting-latitude"])
        lon = float(config["start-settings"]["starting-longitude"])
        self.Map = folium.Map(
            location=[lat, lon],
            tiles=config["layout-settings"]["terrain"],
            zoom_start=float(config["start-settings"]["starting-zoom"])
        )

        # Print progress (if applicable):
        if verbose:
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
            activity = re.split(r"\d", track.name)[0]
            for segment in track.segments:
                for point in segment.points:
                    run.append([point.longitude, point.latitude])

        # Create a GeoJson object and add it to the map:
        geojson = folium.GeoJson(
            {"type": "LineString", "coordinates": run},
            style_function=lambda feature: {
                "color": self.run_color,
                "opacity": self.run_opacity,
                "weight": self.run_weight
            },
            highlight_function=lambda feature: {
                "color": self.highlight_color,
                "opacity": self.highlight_opacity,
                "weight": self.highlight_weight
            },
            tooltip=activity + "/ " + file_name[:10]
        )
        geojson.add_to(self.Map)

    def add_all_runs(self, folder_path=None):
        """
        Function that adds all runs to the map object.

        Parameters
        ==========
        folder_path: str
            Path to folder where the .gpx files are. If not specified,
            it will default to what is indicated in map-runs.ini.
        """

        # Retrieve folder path if not defined:
        if folder_path is None:
            folder_path = self.data_path

        # Loop through folder and add runs to map:
        for file_name in os.listdir(folder_path):
            self.add_run(os.path.join(folder_path, file_name))

        # Print progress (if applicable):
        if self.verbose:
            print("Successfully added all runs to map")

    def save(self, file_path=None):
        """
        Function that saves the map object as a .html file.

        Parameters
        ==========
        file_path: str
            Path where the .html will be saved. If not specified, it
            will default to what is indicated in map-runs.ini.
        """

        # Retrieve file path if not defined:
        if file_path is None:
            file_path = self.output_path

        # Save file:
        self.Map.save(file_path)

        # Print progress (if applicable):
        if self.verbose:
            print("Successfully exported map")


def create_run_map(init_file_path=INIT_FILE_PATH, data_path=None, output_path=None, verbose=None):
    """
    Function that creates an updated map with all runs.

    Parameters
    ==========
    init_file_path: str
        Path to .ini file with map parameters.
    data_path: str
        Path to folder with all .gpx files. If not specified, it will
        default to what is indicated in map-runs.ini.
    output_path: str
        Path where the .html will be saved. If not specified, it will
        default to what is indicated in map-runs.ini.
    verbose: bool
        Weather any output should be printed or not. If not specified,
        it will default to what is indicated in map-runs.ini.
    """

    # Initialize map:
    run_map = RunMap(init_file_path, verbose)

    # Add all runs:
    run_map.add_all_runs(data_path)

    # Export map:
    run_map.save(output_path)


# Call from shell:
if __name__ == "__main__":
    create_run_map(init_file_path=INIT_FILE_PATH)
