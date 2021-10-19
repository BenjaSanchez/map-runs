from configparser import ConfigParser
from pathlib import Path
from shutil import copyfile
import os

import pytest

from map_runs.map_runs import create_run_map


repo_path = Path(__file__).parents[2].absolute()


@pytest.fixture
def tmp_output_path(tmp_path):
    """Fixture for getting the temporal output path of the map."""

    return os.path.join(tmp_path, "output.html")


def assert_run_map_results(capsys, tmp_output_path, verbose):
    """
    Helper function to check things worked.

    Parameters
    ==========
    capsys: fixture
        Pytest fixture that provides access to all printed output.
    tmp_output_path: str
        Temporal output path of the map.
    verbose: bool
        Weather any output should be printed or not.
    """

    # Check if file was created in the proper place:
    assert os.path.isfile(tmp_output_path)
    assert not os.path.isfile(os.path.join(repo_path, "output.html"))

    # Check verbosity:
    assert verbose == (capsys.readouterr().out != "")


def test_create_run_map_default(capsys, tmp_output_path):
    """Test function with default parameters."""

    create_run_map(output_path=tmp_output_path)
    assert_run_map_results(capsys, tmp_output_path, True)


def test_create_run_map_alt_ini(capsys, tmp_path, tmp_output_path):
    """Test function with a different .ini file."""

    # Create new map-runs.ini file from old one:
    config = ConfigParser()
    config.read(os.path.join(repo_path, "map-runs.ini"))
    config["start-settings"]["starting-longitude"] = "10"
    config["layout-settings"]["highlight-color"] = "#b80f0a"
    config["misc-settings"]["output-path"] = tmp_output_path
    tmp_ini_file = os.path.join(tmp_path, "map-runs.ini")
    with open(tmp_ini_file, "w") as configfile:
        config.write(configfile)

    create_run_map(init_file_path=tmp_ini_file)
    assert_run_map_results(capsys, tmp_output_path, True)


def test_create_run_map_alt_data(capsys, tmp_path, tmp_output_path):
    """Test function with data in a different path."""

    # Create smaller dataset:
    data_path = os.path.join(repo_path, "gps-data")
    tmp_data_path = os.path.join(tmp_path, "gps-data")
    os.mkdir(tmp_data_path)
    for file_name in os.listdir(data_path):
        if file_name.startswith("2017-07"):
            copyfile(
                os.path.join(data_path, file_name),
                os.path.join(tmp_data_path, file_name)
            )

    create_run_map(data_path=tmp_data_path, output_path=tmp_output_path)
    assert_run_map_results(capsys, tmp_output_path, True)


def test_create_run_map_no_verbose(capsys, tmp_output_path):
    """Test function without printing anything."""

    create_run_map(output_path=tmp_output_path, verbose=False)
    assert_run_map_results(capsys, tmp_output_path, False)
