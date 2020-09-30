

## 1. Definição do problema pelo cliente.

O perfil é uma empresa de construção civil, no ramo de construção de edificações, estabelecido na região de Itajaí.

## 2. Que dados do cliente você deve coletar?

- Enquadramento no CNAES em que se encontra seu CNPJ, 41.20-4-00 Construção de edifícios

- Faixa etária e renda média dos clientes que possuí.

## 3. Que dados externos você pode usar para enriquecer o estudo?

### [Dados públicos CNPJ](https://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj)

- Selecionados os seguintes grupos de CNAEs em Santa Catarina:
    - 41 = Construção de edifícios
    - 42 = Obras de Infraestrutura
    - 43 = Serviços especializados para construção

### [Dados do Censo 2010 IBGE](https://downloads.ibge.gov.br/)

- Selecionadas as seguintes tabelas:
    - Domicilio01_SC.csv
    - Domicilio02_SC.csv
    - DomicilioRenda_SC.csv
    - Pessoa13_SC.csv
        - 0 a 17 anos
        - 18 a 24 anos
        - 25 a 39 anos
        - 40 a 59 anos
        - 60 anos ou mais
    - 42SEE250GC_SIR.shp (geometria)
        - área (m²)
        - totalpop

## 4. Quais softwares vai usar?

O trabalho foi desenvolvido utilizando python e as biblioteca pandas e geopandas.

## 5. Desenvolvimento do projeto.

A primeira etapa foi a extração dos CNAES de Santa Catarina, o conjunto de dados disponibilizados pela Receita Federal compreende todos os CNPJs do Brasil, são 21 arquivos em 'Fixed width format', um arquivo de [layout](http://200.152.38.155/CNPJ/LAYOUT_DADOS_ABERTOS_CNPJ.pdf) acompanha o conjunto para orientar a extração.

```python
dados = []
for i, r in enumerate(arq_unico):
    line = r.decode("iso-8859-1")
    tipo_registro = line[0:1]  # tipo empresa
    situacao = line[223:225]  # empresas ativas
    nm_estado = line[682:684]  # santa catarina
    if tipo_registro == '1' and nm_estado == 'SC' and situacao == '02':
        dados.append([
            line[684:688],
            line[375:382]])
arq_unico.close()

import pandas as pd
santa_catarina = pd.DataFrame(dados)
santa_catarina.rename(columns={
    0: 'end_cod_mun',
    1: 'cod_cnae'
}, inplace=True)
```

Na sequência foi feito a união com a tabela de cnaes e filtrados os grupos de interesse.

```python
import pandas as pd
cnaes = pd.read_csv('tabelas/cnae.csv',
                    dtype={'cod_cnae': 'string'})

# CNAEs selecionados grupos: 41xxxxx, 42xxxxx, 43xxxxx
cnaes_ccivil = cnaes.loc[(cnaes['cod_classe']
                          .str.slice(0, 2)
                          .str.contains("41|42|43")) == True][
                              ['cod_classe', 'cod_cnae', 'nm_grupo']]
```

Por fim foi necessário adicionar a coluna que contêm o código da cidade pelo IBGE, uma vez que a receita utiliza outra codificação (siafi).

```python
# tabela municípios código IBGE x código Receita
import pandas as pd
municipios_ibge = pd.read_csv('tabelas/codigo_municipios.csv',
                              sep='#',
                              dtype={'codigo_siafi': 'string'})

santa_catarina = santa_catarina.merge(municipios_ibge[['codigo_siafi',
                                                       'codigo_ibge',
                                                       'descricao']],
                                      left_on='end_cod_mun',
                                      right_on='codigo_siafi')
```

Os dados das zonas censitárias foram divididos em tabulares, oriundos dos arquivos .csv do censo de 2010 e shapefile, que contêm a geometria com delimitações de cada setor.

A partir do arquivo .shp foi possível obter a área de cada setor.

```python
import geopandas as gpd
shp_zonas = gpd.read_file('dados/sc_setores_censitarios/42SEE250GC_SIR.shp')

# área em m²
shp_zonas['areametros'] = (shp_zonas.area).astype(int)
```

Para as tabelas do censo foram aplicados nos arquivos .csv os filtros para as colunas:

### - Domicilio02_SC.csv

cod | descr
--- | ---
Cod_setor | Código do setor censitário
V001 | Moradores em domicílios particulares e domicílios coletivos
V002 | Moradores em domicílios particulares permanentes
V003 | Moradores em domicílios particulares permanentes do tipo casa
V004 | Moradores em domicílios particulares permanentes do tipo casa de vila ou em condomínio
V005 | Moradores em domicílios particulares permanentes do tipo apartamento
V006 | Moradores em domicílios particulares permanentes próprios e quitados
V007 | Moradores em domicílios particulares permanentes próprios e em aquisição
V008 | Moradores em domicílios particulares permanentes alugados
V009 | Moradores em domicílios particulares permanentes cedidos por empregador
V010 | Moradores em domicílios particulares permanentes cedidos de outra forma
V011 | Moradores em domicílios particulares permanentes com outra condição de ocupação (não são próprios, alugados, nem cedidos)
 |

### - Domicilio01_SC.csv

cod | descr
--- | ---
Cod_setor | Código do setor censitário
V050 | Domicílios particulares permanentes com 1 morador
V051 | Domicílios particulares permanentes com 2 moradores
V052 | Domicílios particulares permanentes com 3 moradores
V053 | Domicílios particulares permanentes com 4 moradores
V054 | Domicílios particulares permanentes com 5 moradores
V055 | Domicílios particulares permanentes com 6 moradores
V056 | Domicílios particulares permanentes com 7 moradores
V057 | Domicílios particulares permanentes com 8 moradores
V058 | Domicílios particulares permanentes com 9 moradores
V059 | Domicílios particulares permanentes com 10 ou mais moradores
 |

### - DomicilioRenda_SC.csv

cod | descr
--- | ---
Cod_setor | Código do setor censitário
V001 | Total de domicílios particulares improvisados
V002 | Total do rendimento nominal mensal dos domicílios particulares
V003 | Total do rendimento nominal mensal dos domicílios particulares permanentes
V004 | Total do rendimento nominal mensal dos domicílios particulares improvisados
V005 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de até 1/8 salário mínimo
V006 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1/8 a 1/4 salário mínimo
V007 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1/4 a 1/2 salário mínimo
V008 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1/2 a 1 salário mínimo
V009 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 1 a 2 salários mínimos
V010 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 2 a 3 salários mínimos
V011 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 3 a 5 salários mínimos
V012 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 5 a 10 salários mínimos
V013 | Domicílios particulares com rendimento nominal mensal domiciliar per capita de mais de 10 salários mínimos
V014 | Domicílios particulares sem rendimento nominal mensal domiciliar per capita
 |

### - A tabela de faixas estárias foi criada da seguinte maneira:

```python
Pessoa13_SC = pd.read_csv('dados/Pessoa13_SC.csv',
                          sep=';')

Pessoa13_SC.iloc[:, 23:] = Pessoa13_SC.iloc[:, 23:].apply(
    pd.to_numeric, errors='coerce').fillna(0).astype(int)

Pessoa13_SC['0a17'] = Pessoa13_SC.iloc[:, 23:53].sum(axis=1)
Pessoa13_SC['18a24'] = Pessoa13_SC.iloc[:, 53:60].sum(axis=1)
Pessoa13_SC['25a39'] = Pessoa13_SC.iloc[:, 60:75].sum(axis=1)
Pessoa13_SC['40a59'] = Pessoa13_SC.iloc[:, 75:95].sum(axis=1)
Pessoa13_SC['60mais'] = Pessoa13_SC.iloc[:, 95:136].sum(axis=1)

Pessoa13_SC = Pessoa13_SC[['Cod_setor',
                           '0a17',
                           '18a24',
                           '25a39',
                           '40a59',
                           '60mais']]
```
A próxima etapa foi criar uma tabela consolidada com todas as colunas selecionadas.

A partir dos dados selecionados foi feita a identificação dos grupo:

```python
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.cluster import KMeans

array = df.values

x = array[:, 0:45]

modelo = KMeans(n_clusters=10)
modelo.fit(x)

out = modelo.predict(x)

saida = pd.DataFrame(out)
saida['cluster'] = saida[0]
grupos = saida.groupby(["cluster"]).count()
grupos
df['cluster'] = out
```


Os dados utilizados e scripts desenvolvidos podem ser encontrados no seguinte repositòrio:
- [ml_censo_constr_civil](https://github.com/jaceguay/ml_censo_constr_civil)

Os resultados podem ser visualizados nos seguintes notebooks:

[Geometria](https://colab.research.google.com/drive/11mcmSkhl05f-CJcrfYUO-p1N8syT551d?usp=sharing)

[Censo 2010](https://colab.research.google.com/drive/1XPAxfFc50iOXS9LiV0rIXbSYYsPdLt4k?usp=sharing)

[Dados consolidados](https://colab.research.google.com/drive/1bygceqXtRjMKnGilxGEC8kYXDb7YEItV?usp=sharing)

[Mapa clusters](https://colab.research.google.com/drive/1cGEHezvPfPDvMmutx9VV3ZY51MLNI3z1)
