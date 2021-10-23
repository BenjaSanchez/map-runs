#!/usr/bin/env python

from setuptools import setup, find_packages


with open("requirements.txt") as reqs:
    requirements = reqs.read().splitlines()

setup(
    name="map-runs",
    description="Map GPS runs in a single map",
    packages=find_packages(),
    install_requires=requirements,
    tests_require="pytest",
    data_files=[("map_runs", ["map_runs/map-runs.ini"])],
)
