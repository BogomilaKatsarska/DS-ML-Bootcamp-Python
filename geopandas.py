'''
geopandas
descartes
'''
import geopandas as gpd
import matplotlib.pyplot as plt

districts = gpd.read_file('Districts.shp')
districts.plot(
    # color='green',
    cmap='jet', #cmap==colormap
    column='district', #specify the colour by the values of the district column
    egdecolor='white',
)

area_of_interest = gpd.read_file('area_of_interest.shp')
area_of_interest.plot()
atms = gpd.read_file('atms.shp')
atms.plot()

#plot figures side by side
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 8))
districts.plot(ax=ax1, cmap='jet', edgecolor='white', column='district')
area_of_interest.plot(ax=ax2)

#plot figures on top of each other(multiple layers)
fig, ax = plt.subplots(figsite=(10, 8))
districts.plot(ax=ax, cmap='jet', edgecolor='white', column='district')
area_of_interest.plot(ax=ax, color='none', edgecolor='black')
atms.plot(ax=ax, color='black', markersize=14)

#reprojecting GeoPandas GeoDataFrames
districts = districts.to_crs(epsg=32629)
districts.plot(figsize = (10, 8))

#how to intersect 2different layers
districts_in_area_of_interest = gpd.overlay(districts, area_of_interest, how='intersection')
districts_in_area_of_interest.plot(edgecolor='red')
#calculating the area of intersected layer
districts_in_area_of_interest['area'] = districts_in_area_of_interest.area/1000000 #to convert it to km2
#exporting geoPandas GeoData into shapefile
districts_in_area_of_interest.to_file('updated_districts.shp', driver='ESRI Shapefile')
