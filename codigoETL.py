import pandas as pd

# 1. Extração
# Ler o arquivo CSV
dados_vendas = pd.read_csv('/content/dados.csv')

# 2. Transformação
# Calcular o total de vendas para cada produto
dados_transformados = dados_vendas.groupby('Produto')['Valor'].sum().reset_index()

# 3. Carregamento
# Salvar os resultados em um novo arquivo CSV
dados_transformados.to_csv('dados_transformados.csv', index=False)

print("Processo de ETL concluído.")
