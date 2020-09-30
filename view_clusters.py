# %%
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# %%
# geometria
gdf = gpd.read_file('dados_selecionados/zonas_censitarias_geom.geojson')
gdf.crs

# %%
# clusters
clusters = pd.read_csv('censo_clusters.csv',
                       dtype={'ncod': 'str'})
clusters.head()

# %%
df = gdf.merge(clusters[['ncod', 'cluster']],
               left_on='CD_GEOCODI',
               right_on='ncod')

# %%
df.plot(column='cluster',
        figsize=(25, 10))
#plt.xlim(-54.4851, -29.2752)
#plt.ylim(-47.9792, -25.8102)
plt.title('Clusters', fontsize=20)
plt.show()

# %%
# df.to_file('clusters.geojson',
#            driver='GeoJSON')

# %%[markdown]
# SQL QGIS
# select
#     count(clusters.cluster) as num,
#     clusters.NM_MUNICIP
# from
#     clusters
# where
# 	clusters.cluster = 0
# group by
#     clusters.NM_MUNICIP