!pip install folium

import folium

m = folium.Map(location=[37.737234669348055, -122.43491855649619], zoom_start=12)
folium.Marker(location=[37.737234669348055, -122.43491855649619], 
              popup='Seattle',
              icon=folium.Icon(icon='star', color='red')).add_to(m)
folium.Marker(location=[37.744455045847346, -122.48749464989561]).add_to(m)
folium.Marker(location=[37.72008677201449, -122.41236383024616]).add_to(m)
folium.Marker(location=[37.7459351958392, -122.44451758051804]).add_to(m)
folium.Marker(location=[37.73214343805581, -122.39006093596466]).add_to(m)
folium.Marker(location=[37.7782876008788, -122.49513629400617]).add_to(m)
folium.Marker(location=[37.76984972279721, -122.44615959224852]).add_to(m)
folium.Marker(location=[31.4635090543772, -96.06578977766901]).add_to(m)
folium.Marker(location=[37.56571513350493, -85.25325558455908]).add_to(m)



m
