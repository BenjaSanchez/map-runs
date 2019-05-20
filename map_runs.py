
# Import required packages:
import os
import folium
import gpxpy

# Location:
lat = 57.6885178
lon = 11.9830906

# Initialize map:
run_map = folium.Map(
    location=[lat, lon],
    tiles='Stamen Terrain',
    zoom_start=12)


# Function that adds a run to the map:
def add_run(base_map, file_name):
    gpx_file = open(file_name, 'r')
    gpx = gpxpy.parse(gpx_file)
    run = list()
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                run.append([point.latitude, point.longitude])
    
    folium.vector_layers.PolyLine(
        locations=run,
        tooltip=file_name[:10],
        color='#b80f0a',
        opacity=0.5).add_to(base_map)


# Add all runs in ./gps-data:
os.chdir('./gps-data')
for file in os.listdir('.'):
    add_run(run_map, file)
os.chdir('./..')

# Export map:
run_map.save('output-map.html')
