# %%[markdown]
# Dados dos CNAEs de Santa Catarina separados por cidade

# %%
import pandas as pd
import os

# %%
wpath = os.getcwd()
path = f'{wpath}/dados_receita_sc/'
print(path)
get_ipython().run_line_magic('ls', '{path}')

# %%
files = os.listdir(path)

dados_csv = []

for x in files:
    if '.csv' in x:
        print(x)
        data = pd.read_csv(f'{path}{x}')
        dados_csv.append(data)
dados_csv = pd.concat(dados_csv)

# %%
dados_csv['grupo_cnae'] = dados_csv['cod_classe'].str.slice(0, 2)

# %%
santa_catarina_ccivil = dados_csv[[
    'codigo_ibge',
    'grupo_cnae']]

# %%
# 41 = Construção de edifícios
# 42 = Obras de Infraestrutura
# 43 = Serviços especializados para construção
santa_catarina_ccivil = santa_catarina_ccivil.pivot_table(index='codigo_ibge',
                                                          columns='grupo_cnae',
                                                          aggfunc=len).reset_index()

# %%
# pd.DataFrame(santa_catarina_ccivil).to_csv(
#    'cnaes_municipios.csv', index=False)

# %%
