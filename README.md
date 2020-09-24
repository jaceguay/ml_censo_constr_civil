# PÓS BIG DATA - 2019/2: Tecnologias de Desenvolvimento em Big Data

## Introdução

Classificação utilizando ML para reconhecimento de mercados da construção civil, fontes:
- dados do censo;
- receita federal.

### 1. Limpeza dados Receita

Selecionados os seguintes grupos de CNAEs em Santa Catarina:
- 41 = Construção de edifícios
- 42 = Obras de Infraestrutura
- 43 = Serviços especializados para construção

Agrupados por cidade (código cidade IBGE), contagem número de ocorrências para cada grupo.

```
santa_catarina_cnaes.csv
```

### 2. Dados IBGE

Selecionadas as seguintes tabelas:
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
    - densidade

### 3. Conjunto de dados

[NB geometria](https://colab.research.google.com/drive/11mcmSkhl05f-CJcrfYUO-p1N8syT551d?usp=sharing)

[Censo 2010](https://colab.research.google.com/drive/1XPAxfFc50iOXS9LiV0rIXbSYYsPdLt4k?usp=sharing)

[NB Dados](https://colab.research.google.com/drive/1bygceqXtRjMKnGilxGEC8kYXDb7YEItV?usp=sharing)

```
dados_selecionados_join.csv
```

### 4. Modelo ML

...

### 5. Viz

...


> # Projeto
>
> ## Definição do problema pelo cliente:
> Gostaria de expandir, investindo em regiões similares a que tenho meu empreendimento
> imobiliário atualmente, busco opções em todo o território de Santa Catarina.
>
> ## Defina sua estratégia:
> Que dados do cliente você deve coletar?
> Que dados externos você pode usar para enriquecer o estudo?
> Quais softwares vai usar? (etapas de desenvolvimento e apresentação do resultado)
>
> ## Desenvolvimento do projeto:
> Quais foram as transformações aplicadas nos dados?
> Qual algoritmo foi aplicado no projeto?
> Quantos grupos foram identificados?
>
> ## Conclusão
> Usando o conhecimento de sua região, como você avalia o resultado do seu projeto?