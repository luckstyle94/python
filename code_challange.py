def recomendar_plano(consumo_mensal):

    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    
    elif consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps"
    
    elif consumo_mensal > 20:
        return "Plano Premium Fibra - 300Mbps"

consumo = float(input("Informe o consumo médio mensal de dados (em GB): "))
plano_recomendado = recomendar_plano(consumo)
print(f"Plano recomendado: {plano_recomendado}")