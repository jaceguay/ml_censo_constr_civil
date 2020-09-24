# %%
import pandas as pd

# %%
df1 = pd.read_csv('cnaes_municipios.csv')
df2 = pd.read_csv('Domicilio01_SC.csv')
df3 = pd.read_csv('Domicilio02_SC.csv')
df4 = pd.read_csv('DomicilioRenda_SC.csv')
df5 = pd.read_csv('Pessoa13_SC.csv')
df6 = pd.read_csv('zonas_censitarias_area.csv')

# %%
df_lists = [df1, df2, df3, df4, df5, df6]

# %%
joined = pd.concat(df_lists, join='outer', axis=1).fillna(0)

joined['poptotal'] = joined[['0a17',
                             '18a24',
                             '25a39',
                             '40a59',
                             '60mais']].sum(axis=1)

joined['densidade'] = joined['areametros'] / joined['poptotal']

# %%
pd.DataFrame(joined[['Cod_setor',
                     '41',
                     '42',
                     '43',
                     'domi2V050',
                     'domi2V051',
                     'domi2V052',
                     'domi2V053',
                     'domi2V054',
                     'domi2V055',
                     'domi2V056',
                     'domi2V057',
                     'domi2V058',
                     'domi2V059',
                     'domi1V001',
                     'domi1V002',
                     'domi1V003',
                     'domi1V004',
                     'domi1V005',
                     'domi1V006',
                     'domi1V007',
                     'domi1V008',
                     'domi1V009',
                     'domi1V010',
                     'domi1V011',
                     'rendaV001',
                     'rendaV002',
                     'rendaV003',
                     'rendaV004',
                     'rendaV005',
                     'rendaV006',
                     'rendaV007',
                     'rendaV008',
                     'rendaV009',
                     'rendaV013',
                     'rendaV014',
                     'V012',
                     'V013',
                     'V014',
                     '0a17',
                     '18a24',
                     '25a39',
                     '40a59',
                     '60mais',
                     'areametros',
                     'poptotal',
                     'densidade']]).to_csv(
    'dados_selecionados_join.csv', index=False)

# %%
