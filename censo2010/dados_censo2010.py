# %%
import pandas as pd

# %% [markdown]
# # dados censo 2010

# %%[markdown]
# ## planilha Domicilio02_SC.csv
# cod | descr
# --- | ---
# Cod_setor | Código do setor censitário
# V001 | Moradores em domicílios particulares e domicílios coletivos
# V002 | Moradores em domicílios particulares permanentes
# V003 | Moradores em domicílios particulares permanentes do tipo casa
# V004 | Moradores em domicílios particulares permanentes do tipo casa de vila ou em condomínio
# V005 | Moradores em domicílios particulares permanentes do tipo apartamento
# V006 | Moradores em domicílios particulares permanentes próprios e quitados
# V007 | Moradores em domicílios particulares permanentes próprios e em aquisição
# V008 | Moradores em domicílios particulares permanentes alugados
# V009 | Moradores em domicílios particulares permanentes cedidos por empregador
# V010 | Moradores em domicílios particulares permanentes cedidos de outra forma
# V011 | Moradores em domicílios particulares permanentes com outra condição de ocupação (não são próprios, alugados, nem cedidos)

# %%
Domicilio02_SC = pd.read_csv('dados/Domicilio02_SC.csv',
                             sep=';')
Domicilio02_SC = Domicilio02_SC[['Cod_setor',
                                 'V001',
                                 'V002',
                                 'V003',
                                 'V004',
                                 'V005',
                                 'V006',
                                 'V007',
                                 'V008',
                                 'V009',
                                 'V010',
                                 'V011']]

Domicilio02_SC.rename(columns={
    'V001': 'domi1V001',
    'V002': 'domi1V002',
    'V003': 'domi1V003',
    'V004': 'domi1V004',
    'V005': 'domi1V005',
    'V006': 'domi1V006',
    'V007': 'domi1V007',
    'V008': 'domi1V008',
    'V009': 'domi1V009',
    'V010': 'domi1V010',
    'V011': 'domi1V011'},
    inplace=True)

Domicilio02_SC.iloc[:, 1:] = Domicilio02_SC.iloc[:, 1:].apply(
    pd.to_numeric, errors='coerce').fillna(0).astype(int)

# %%
pd.DataFrame(Domicilio02_SC).to_csv(
    'Domicilio02_SC.csv', index=False)

# %% [markdown]
# ## Domicilio01_SC.csv
# cod | descr
# --- | ---
# Cod_setor | Código do setor censitário
# V050 | Domicílios particulares permanentes com 1 morador
# V051 | Domicílios particulares permanentes com 2 moradores
# V052 | Domicílios particulares permanentes com 3 moradores
# V053 | Domicílios particulares permanentes com 4 moradores
# V054 | Domicílios particulares permanentes com 5 moradores
# V055 | Domicílios particulares permanentes com 6 moradores
# V056 | Domicílios particulares permanentes com 7 moradores
# V057 | Domicílios particulares permanentes com 8 moradores
# V058 | Domicílios particulares permanentes com 9 moradores
# V059 | Domicílios particulares permanentes com 10 ou mais moradores

# %%
Domicilio01_SC = pd.read_csv('dados/Domicilio01_SC.csv',
                             sep=';')
Domicilio01_SC = Domicilio01_SC[['Cod_setor',
                                 'V050',
                                 'V051',
                                 'V052',
                                 'V053',
                                 'V054',
                                 'V055',
                                 'V056',
                                 'V057',
                                 'V058',
                                 'V059']]

Domicilio01_SC.rename(columns={
    'V050': 'domi2V050',
    'V051': 'domi2V051',
    'V052': 'domi2V052',
    'V053': 'domi2V053',
    'V054': 'domi2V054',
    'V055': 'domi2V055',
    'V056': 'domi2V056',
    'V057': 'domi2V057',
    'V058': 'domi2V058',
    'V059': 'domi2V059'},
    inplace=True)

Domicilio01_SC.iloc[:, 1:] = Domicilio01_SC.iloc[:, 1:].apply(
    pd.to_numeric, errors='coerce').fillna(0).astype(int)

# %%
pd.DataFrame(Domicilio01_SC).to_csv(
    'Domicilio01_SC.csv', index=False)

# %% [markdown]
# ## DomicilioRenda_SC.csv
# cod | descr
# --- | ---
# Cod_setor | Código do setor censitário
# V001 | Total de domicílios particulares improvisados
# V002 | Total do rendimento nominal mensal dos domicílios particulares
# V003 | Total do rendimento nominal mensal dos domicílios particulares permanentes
# V004 | Total do rendimento nominal mensal dos domicílios particulares improvisados
# V005 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de até 1/8 salário mínimo
# V006 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1/8 a 1/4 salário mínimo
# V007 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1/4 a 1/2 salário mínimo
# V008 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1/2 a 1 salário mínimo
# V009 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1 a 2 salários mínimos
# V010 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 2 a 3 salários mínimos
# V011 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 3 a 5 salários mínimos
# V012 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 5 a 10 salários mínimos
# V013 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 10 salários mínimos
# V014 | Domicílios particulares sem rendimento nominal mensal domiciliar per capita

# %%
DomicilioRenda_SC = pd.read_csv('dados/DomicilioRenda_SC.csv',
                                sep=';')
DomicilioRenda_SC = DomicilioRenda_SC[['Cod_setor',
                                       'V001',
                                       'V002',
                                       'V003',
                                       'V004',
                                       'V005',
                                       'V006',
                                       'V007',
                                       'V008',
                                       'V009',
                                       'V010',
                                       'V011',
                                       'V012',
                                       'V013',
                                       'V014']]

DomicilioRenda_SC.rename(columns={
    'V001': 'rendaV001',
    'V002': 'rendaV002',
    'V003': 'rendaV003',
    'V004': 'rendaV004',
    'V005': 'rendaV005',
    'V006': 'rendaV006',
    'V007': 'rendaV007',
    'V008': 'rendaV008',
    'V009': 'rendaV009',
    'V010': 'rendaV010',
    'V010': 'rendaV011',
    'V010': 'rendaV012',
    'V010': 'rendaV013',
    'V011': 'rendaV014'},
    inplace=True)

DomicilioRenda_SC.iloc[:, 1:] = DomicilioRenda_SC.iloc[:, 1:].apply(
    pd.to_numeric, errors='coerce').fillna(0).astype(int)

# %%
pd.DataFrame(DomicilioRenda_SC).to_csv(
    'DomicilioRenda_SC.csv', index=False)

# %% [markdown]
# ## Pessoa13_SC.csv
# cod | descr
# --- | ---
# Cod_setor | Código do setor censitário
# V022 | Pessoas com menos de 1 ano de idade
# V023 | Pessoas com menos de 1 mês de idade
# V024 | Pessoas com 1 mês de idade
# V025 | Pessoas com 2 meses de idade
# V026 | Pessoas com 3 meses de idade
# V027 | Pessoas com 4 meses de idade
# V028 | Pessoas com 5 meses de idade
# V029 | Pessoas com 6 meses de idade
# V030 | Pessoas com 7 meses de idade
# V031 | Pessoas com 8 meses de idade
# V032 | Pessoas com 9 meses de idade
# V033 | Pessoas com 10 meses de idade
# V034 | Pessoas com 11 meses de idade
# V035 | Pessoas de 1 ano de idade
# V036 | Pessoas com 2 anos de idade
# V037 | Pessoas com 3 anos de idade
# V038 | Pessoas com 4 anos de idade
# V039 | Pessoas com 5 anos de idade
# V040 | Pessoas com 6 anos de idade
# V041 | Pessoas com 7 anos de idade
# V042 | Pessoas com 8 anos de idade
# V043 | Pessoas com 9 anos de idade
# V044 | Pessoas com 10 anos de idade
# V045 | Pessoas com 11 anos de idade
# V046 | Pessoas com 12 anos de idade
# V047 | Pessoas com 13 anos de idade
# V048 | Pessoas com 14 anos de idade
# V049 | Pessoas com 15 anos de idade
# V050 | Pessoas com 16 anos de idade
# V051 | Pessoas com 17 anos de idade
# V052 | Pessoas com 18 anos de idade
# V053 | Pessoas com 19 anos de idade
# V054 | Pessoas com 20 anos de idade
# V055 | Pessoas com 21 anos de idade
# V056 | Pessoas com 22 anos de idade
# V057 | Pessoas com 23 anos de idade
# V058 | Pessoas com 24 anos de idade
# V059 | Pessoas com 25 anos de idade
# V060 | Pessoas com 26 anos de idade
# V061 | Pessoas com 27 anos de idade
# V062 | Pessoas com 28 anos de idade
# V063 | Pessoas com 29 anos de idade
# V064 | Pessoas com 30 anos de idade
# V065 | Pessoas com 31 anos de idade
# V066 | Pessoas com 32 anos de idade
# V067 | Pessoas com 33 anos de idade
# V068 | Pessoas com 34 anos de idade
# V069 | Pessoas com 35 anos de idade
# V070 | Pessoas com 36 anos de idade
# V071 | Pessoas com 37 anos de idade
# V072 | Pessoas com 38 anos de idade
# V073 | Pessoas com 39 anos de idade
# V074 | Pessoas com 40 anos de idade
# V075 | Pessoas com 41 anos de idade
# V076 | Pessoas com 42 anos de idade
# V077 | Pessoas com 43 anos de idade
# V078 | Pessoas com 44 anos de idade
# V079 | Pessoas com 45 anos de idade
# V080 | Pessoas com 46 anos de idade
# V081 | Pessoas com 47 anos de idade
# V082 | Pessoas com 48 anos de idade
# V083 | Pessoas com 49 anos de idade
# V084 | Pessoas com 50 anos de idade
# V085 | Pessoas com 51 anos de idade
# V086 | Pessoas com 52 anos de idade
# V087 | Pessoas com 53 anos de idade
# V088 | Pessoas com 54 anos de idade
# V089 | Pessoas com 55 anos de idade
# V090 | Pessoas com 56 anos de idade
# V091 | Pessoas com 57 anos de idade
# V092 | Pessoas com 58 anos de idade
# V093 | Pessoas com 59 anos de idade
# V094 | Pessoas com 60 anos de idade
# V095 | Pessoas com 61 anos de idade
# V096 | Pessoas com 62 anos de idade
# V097 | Pessoas com 63 anos de idade
# V098 | Pessoas com 64 anos de idade
# V099 | Pessoas com 65 anos de idade
# V100 | Pessoas com 66 anos de idade
# V101 | Pessoas com 67 anos de idade
# V102 | Pessoas com 68 anos de idade
# V103 | Pessoas com 69 anos de idade
# V104 | Pessoas com 70 anos de idade
# V105 | Pessoas com 71 anos de idade
# V106 | Pessoas com 72 anos de idade
# V107 | Pessoas com 73 anos de idade
# V108 | Pessoas com 74 anos de idade
# V109 | Pessoas com 75 anos de idade
# V110 | Pessoas com 76 anos de idade
# V111 | Pessoas com 77 anos de idade
# V112 | Pessoas com 78 anos de idade
# V113 | Pessoas com 79 anos de idade
# V114 | Pessoas com 80 anos de idade
# V115 | Pessoas com 81 anos de idade
# V116 | Pessoas com 82 anos de idade
# V117 | Pessoas com 83 anos de idade
# V118 | Pessoas com 84 anos de idade
# V119 | Pessoas com 85 anos de idade
# V120 | Pessoas com 86 anos de idade
# V121 | Pessoas com 87 anos de idade
# V122 | Pessoas com 88 anos de idade
# V123 | Pessoas com 89 anos de idade
# V124 | Pessoas com 90 anos de idade
# V125 | Pessoas com 91 anos de idade
# V126 | Pessoas com 92 anos de idade
# V127 | Pessoas com 93 anos de idade
# V128 | Pessoas com 94 anos de idade
# V129 | Pessoas com 95 anos de idade
# V130 | Pessoas com 96 anos de idade
# V131 | Pessoas com 97 anos de idade
# V132 | Pessoas com 98 anos de idade
# V133 | Pessoas com 99 anos de idade
# V134 | Pessoas com 100 anos ou mais de idade
#
# ### Polulação por grupo de idade:
# 0 a 17 anos
# 18 a 24 anos
# 25 a 39 anos
# 40 a 59 anos
# 60 anos ou mais

# %%
Pessoa13_SC = pd.read_csv('dados/Pessoa13_SC.csv',
                          sep=';')

Pessoa13_SC.iloc[:, 23:] = Pessoa13_SC.iloc[:, 23:].apply(
    pd.to_numeric, errors='coerce').fillna(0).astype(int)

# %%
Pessoa13_SC['0a17'] = Pessoa13_SC.iloc[:, 23:53].sum(axis=1)
Pessoa13_SC['18a24'] = Pessoa13_SC.iloc[:, 53:60].sum(axis=1)
Pessoa13_SC['25a39'] = Pessoa13_SC.iloc[:, 60:75].sum(axis=1)
Pessoa13_SC['40a59'] = Pessoa13_SC.iloc[:, 75:95].sum(axis=1)
Pessoa13_SC['60mais'] = Pessoa13_SC.iloc[:, 95:136].sum(axis=1)

# %%
Pessoa13_SC = Pessoa13_SC[['Cod_setor',
                           '0a17',
                           '18a24',
                           '25a39',
                           '40a59',
                           '60mais']]

# %%
pd.DataFrame(Pessoa13_SC).to_csv(
    'Pessoa13_SC.csv', index=False)
