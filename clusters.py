# %%
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.cluster import KMeans

# %%
df = pd.read_csv('dados_selecionados_join.csv')

# %%
df.set_index('ncod', inplace=True)
df.head()

# %%
df.describe()

# %%
# df.corr()

# %%
# df.hist()

# %%
# sns.pairplot(df)

# %%
# sns.boxplot(data=df, orient="h")

# %%
df.shape

# %%[markdown]
# ## Aplicando a clusterização

# %%
# Carregar os dados:
array = df.values

# Separar array em componentes de input e output:
x = array[:, 0:45]

# Criação do modelo
modelo = KMeans(n_clusters=10)
modelo.fit(x)

out = modelo.predict(x)

# %%[markdown]
# ## Entendendo a saída do modelo

# %%
saida = pd.DataFrame(out)
saida['cluster'] = saida[0]
grupos = saida.groupby(["cluster"]).count()
grupos
df['cluster'] = out

# %%
df
df.to_csv('censo_clusters.csv')
