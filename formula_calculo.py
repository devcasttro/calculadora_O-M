
taxa_descarga_max = ''





def calcular(tensao_inversor, corrente_inversor, capacidade_bateria, volt_bateria):
    #Calcula a taxa de descarga máxima com base no inversor
    


    # Formulá de Cálculo
    potencia_inversor = (tensao_inversor * corrente_inversor) * 1
    potencia_bateria = (capacidade_bateria * volt_bateria)

    tempo_descarga_hora = potencia_bateria / potencia_inversor

    tempo_descarga_min = tempo_descarga_hora * 60

    taxa_descarga = volt_bateria / tempo_descarga_min

    autonomia = ((volt_bateria * 30) / 100) / (taxa_descarga * 60)

    return taxa_descarga, autonomia



def status(descarga):
    if descarga >= 0.083:  
       
       return 'Status: BOM'

    else:
        return 'Status: RUIM'
    