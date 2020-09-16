# %%[markdown]
# # Arquivo receita
# Os arquivos estão formatados como Fixed Width Format.
# endereço:
# https://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj

# %%
import pandas as pd
import os

# %%
path = '/mnt/d/cnpj/2020-08/descompactados'
files = os.listdir(path)
print(files)

# %%
# ler arquivo individual
nome_arquivo = 'K3241.K03200DV.D00703.L00001'

arq_unico = open(
    f'{path}/{nome_arquivo}',
    'rb')

dados = list()

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

# %%
santa_catarina = pd.DataFrame(dados)
santa_catarina.rename(columns={
    0: 'end_cod_mun',
    1: 'cod_cnae'
}, inplace=True)

# %%
# tabela CNAEs
cnaes = pd.read_csv('tabelas/cnae.csv',
                    dtype={'cod_cnae': 'string'})

# %%
# CNAEs selecionados grupos: 41xxxxx, 42xxxxx, 43xxxxx
cnaes_ccivil = cnaes.loc[(cnaes['cod_classe']
                          .str.slice(0, 2)
                          .str.contains("41|42|43")) == True][
                              ['cod_classe', 'cod_cnae', 'nm_grupo']]

# %%
santa_catarina = santa_catarina.merge(cnaes_ccivil,
                                      left_on='cod_cnae',
                                      right_on='cod_cnae')

# %%
# tabela municípios código IBGE x código Receita
municipios_ibge = pd.read_csv('tabelas/codigo_municipios.csv',
                              sep='#',
                              dtype={'codigo_siafi': 'string'})

santa_catarina = santa_catarina.merge(municipios_ibge[['codigo_siafi',
                                                       'codigo_ibge',
                                                       'descricao']],
                                      left_on='end_cod_mun',
                                      right_on='codigo_siafi')

# %%
# pd.DataFrame(santa_catarina).to_csv(f'dados_receita_sc/{nome_arquivo}.csv',
#                                    index=False)
