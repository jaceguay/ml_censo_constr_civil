# %%
import geopandas as gpd

# %%
shp_zonas = gpd.read_file('dados/sc_setores_censitarios/42SEE250GC_SIR.shp')
shp_zonas.crs

# %%
# área em m²
shp_zonas['areametros'] = (shp_zonas.area).astype(int)

# %%
# transformar crs para wgs84 (google mercator)
shp_zonas = shp_zonas.to_crs(4326)
shp_zonas.crs

# %%
# shp_zonas[['CD_GEOCODI',
#            'NM_MUNICIP',
#            'areametros',
#            'geometry']].to_file('zonas_censitarias.geojson',
#                                 driver='GeoJSON')
# %%
import pandas as pd
pd.DataFrame(shp_zonas[['CD_GEOCODI',
                         'NM_MUNICIP',
                         'areametros']]).to_csv(
    'area_zonas.csv', index=False)

# %%
