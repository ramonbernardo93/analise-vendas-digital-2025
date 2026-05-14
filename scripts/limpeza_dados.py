import pandas as pd

def limpar_dados_kiwify(caminho_arquivo):
    # Carregar dados
    df = pd.read_csv(caminho_arquivo)
    
    # Colunas que interessam para o negócio
    colunas_essenciais = [
        'ID da venda', 'Status', 'Produto', 'País', 'Data de Criação', 
        'Pagamento', 'Preço base do produto', 'Valor líquido', 'Taxas'
    ]
    
    # Filtrar e remover dados sensíveis (LGPD)
    # Note: Colunas como 'Cliente', 'Email', 'CPF' e 'Celular' são descartadas aqui
    df_limpo = df[colunas_essenciais].copy()
    
    # Salvar para o GitHub
    df_limpo.to_csv('vendas_limpas_julho.csv', index=False)
    print("Dados anonimizados com sucesso!")

# Execução
if __name__ == "__main__":
    limpar_dados_kiwify('ARQUIVO_CRU_KIWIFY_JULHO.csv')
