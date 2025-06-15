import pandas as pd

# Caminho do arquivo
arquivo = 'Teste.xlsx'

# Ler todas as planilhas do arquivo (se quiser apenas uma, use sheet_name='NomeDaAba')
planilhas = pd.read_excel(arquivo, sheet_name=None)

# Criar um dicionário para armazenar os DataFrames tratados
planilhas_tratadas = {}

# Percorrer cada aba
for nome_aba, df in planilhas.items():
    # Aplicar a substituição em todas as células que são texto (object)
    df_tratado = df.applymap(lambda x: x.replace('_x000D_', ' ') if isinstance(x, str) else x)
    planilhas_tratadas[nome_aba] = df_tratado

# Salvar a nova planilha com as alterações
with pd.ExcelWriter('planilha_tratada.xlsx', engine='openpyxl') as writer:
    for nome_aba, df in planilhas_tratadas.items():
        df.to_excel(writer, sheet_name=nome_aba, index=False)

print("Substituição concluída e planilha salva como 'planilha_tratada.xlsx'.")
