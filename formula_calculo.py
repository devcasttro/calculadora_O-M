def calcular(tensao_inversor, corrente_inversor, capacidade_bateria, volt_bateria):

    # Formulá de Cálculo
    potencia_inversor = (tensao_inversor * corrente_inversor) * 1
    potencia_bateria = (capacidade_bateria * volt_bateria)

    tempo_descarga_hora = potencia_bateria / potencia_inversor

    tempo_descarga_min = tempo_descarga_hora * 60

    taxa_descarga = volt_bateria / tempo_descarga_min

    return taxa_descarga


def status(descarga):
    if descarga >= 0.083:  
       
       return 'Status: BOM'

    else:
        return 'Status: RUIM'