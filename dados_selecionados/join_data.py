# %%
import pandas as pd

# %%
df1 = pd.read_csv('cnaes_municipios.csv', dtype={'Cod_setor': 'string'})
df2 = pd.read_csv('Domicilio01_SC.csv', dtype={'Cod_setor': 'string'})
df3 = pd.read_csv('Domicilio02_SC.csv', dtype={'Cod_setor': 'string'})
df4 = pd.read_csv('DomicilioRenda_SC.csv', dtype={'Cod_setor': 'string'})
df5 = pd.read_csv('Pessoa13_SC.csv', dtype={'Cod_setor': 'string'})
df6 = pd.read_csv('zonas_censitarias_area.csv', dtype={'Cod_setor': 'string'})

# %%
df2['cod_cidade'] = df2['Cod_setor'].str.slice(0, 7)
dfa = df2.merge(df1,
                left_on='cod_cidade',
                right_on='Cod_setor',
                how='left').fillna(0)
dfa['ncod'] = dfa['Cod_setor_x']
# %%
dfb = dfa.merge(df3,
                left_on='ncod',
                right_on='Cod_setor',
                how='left').fillna(0)

# %%
dfc = dfb.merge(df4,
                left_on='ncod',
                right_on='Cod_setor',
                how='left').fillna(0)

# %%
dfd = dfc.merge(df5,
                left_on='ncod',
                right_on='Cod_setor',
                how='left').fillna(0)

# %%
joined = dfd.merge(df6,
                   left_on='ncod',
                   right_on='Cod_setor',
                   how='left').fillna(0)
# %%

joined['poptotal'] = joined[['0a17',
                             '18a24',
                             '25a39',
                             '40a59',
                             '60mais']].sum(axis=1)

joined['densidade'] = joined['areametros'] / joined['poptotal']

# %%
pd.DataFrame(joined[['ncod',
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
