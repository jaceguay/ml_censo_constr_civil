# %%
import pandas as pd
import geopandas as gpd

# %%
shp_zonas = gpd.read_file('dados/sc_setores_censitarios/42SEE250GC_SIR.shp')
shp_zonas.crs

# %%
# área em m²
shp_zonas['areametros'] = (shp_zonas.area).astype(int)

# %%
# transformar crs para wgs84 (google mercator)
shp_zonas = shp_zonas.to_crs(epsg: 4326)

# %%
# shp_zonas[['CD_GEOCODI',
#            'NM_MUNICIP',
#            'areametros',
#            'geometry']].to_file('zonas_censitarias.geojson',
#                                 driver='GeoJSON')
# %%
