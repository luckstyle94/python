# Step 1
################################################

def recomendar_plano(consumo_mensal):

    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    
    elif consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps"
    
    elif consumo_mensal > 20:
        return "Plano Premium Fibra - 300Mbps"

consumo = float(input())
plano_recomendado = recomendar_plano(consumo)
print(plano_recomendado)

# Step 2
################################################

itens = []

for _ in range(3):

    item = input()

itens.append(item)

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")

# Step 3
################################################

import re


def validate_numero_telefone(phone_number):
   
    padrao_telefone = re.compile(r'\(\d{2}\)\s9\d{4}-\d{4}')
   
    if re.match(padrao_telefone, phone_number):

        return "Número de telefone válido."
    else:

        return "Número de telefone inválido."
    
phone_number = input()  

result = validate_numero_telefone(phone_number)

print(result)