# %%
import geopandas as gpd
import matplotlib.pyplot as plt

# %%
gdf = gpd.read_file('zonas_censitarias_geom.geojson')
gdf.crs

# %%
gdf.plot(column='areametros')
# %%
