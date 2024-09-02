import json



"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

"""

def analisar_faturamento(arquivo_json):
    with open('faturamento.json') as f:
        dados_faturamento = json.load(f)

    # Inicializa as variáveis
    menor_faturamento = float('inf')
    maior_faturamento = 0
    dias_acima_media = 0
    soma_faturamento = 0
    dias_com_faturamento = 0

    # Itera sobre os dados de faturamento
    for dia in dados_faturamento:
        valor_faturamento = dia["valor"]
        if valor_faturamento > 0:  # Ignora dias sem faturamento
            dias_com_faturamento += 1
            soma_faturamento += valor_faturamento
            if valor_faturamento < menor_faturamento:
                menor_faturamento = valor_faturamento
            if valor_faturamento > maior_faturamento:
                maior_faturamento = valor_faturamento

    # Calcula a média mensal
    media_mensal = soma_faturamento / dias_com_faturamento

    # Conta os dias com faturamento acima da média
    for dia in dados_faturamento:
        valor_faturamento = dia["valor"]
        if valor_faturamento > media_mensal:
            dias_acima_media += 1

    return menor_faturamento, maior_faturamento, dias_acima_media

# Exemplo de uso
arquivo_json = "faturamento.json"  # Substitua pelo nome do seu arquivo JSON
menor, maior, dias_acima = analisar_faturamento(arquivo_json)

print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")