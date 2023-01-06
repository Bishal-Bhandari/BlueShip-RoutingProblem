from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from Algorithm.pathfinder import *

fig = plt.figure(figsize=(10, 8))

map = Basemap(projection='mill',
              llcrnrlat=10,
              urcrnrlat=60,
              llcrnrlon=-80,
              urcrnrlon=10,
              resolution='l')

map.drawcoastlines()

map.drawparallels(np.arange(-90, 90, 10), labels=[0, 1, 0, 1])
map.drawmeridians(np.arange(-180, 180, 10), labels=[0, 0, 0, 1])

lons = [-18.957707699807273, -19.957707699807273, -57.38221644849669, -58.38221644849669, -15.15, -20,
        -16.840600000000002]
lats = [34.999678, 34.999678, 34.999678, 34.999678, 32.56, 35, 34.999678]
x, y = map(lons, lats)
map.scatter(x, y, marker='D', color='m')

lons_l = [-10, -20, -25, -10, 0, 10]
lats_l = [40, 30, 10, 0, 0, -5]
xl, yl = map(lons_l, lats_l)
map.plot(xl, yl, marker=None, color='r')

# Naming the x axis and including the info of generations
plt.xlabel(' ' + '\nLatitude' + '\nGeneration: ')

# naming the y axis
plt.ylabel('Longitude')

plt.title('Blue Ship Routing Problem', fontsize=20)

plt.show()
