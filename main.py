import matplotlib as mt
import pandas as pd
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
x = world.plot()
print(x)