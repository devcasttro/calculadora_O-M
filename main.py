# Taxa de variação do tempo de descarga
variacao_taxa_descarga = 5

# Dados de saída do inversor
tensao_inversor = 127
corrente_inversor = 3.937

# Dados da bateria
capacidade_bateria = 100
volt_bateria = 48

# Formulá de Cálculo
potencia_inversor = (tensao_inversor * corrente_inversor) * 1
potencia_bateria = (capacidade_bateria * volt_bateria)

tempo_descarga_hora = potencia_bateria / potencia_inversor

tempo_descarga_min = tempo_descarga_hora * 60

taxa_descarga = volt_bateria / tempo_descarga_min

# Cálcula o valor de referencia da % de variação
percentual_taxa_descarga = taxa_descarga * variacao_taxa_descarga / 100

print(f'A taxa de descarga da bateria é igual: {taxa_descarga:.3f}')

if taxa_descarga >= (0.083 - percentual_taxa_descarga):
    print('Valor considerado: BOM')

else:
    print('Valor considerado: RUIM')
