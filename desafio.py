menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
conta_especial = True


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Adicionados: R$ {valor:.2f}\n"

        else:
            print("Valor adicionado não pode ser menor que 0.")

    elif opcao == "2":
        valor = float(input("Valor para Saque: "))

        saque_especial = valor > saldo and conta_especial
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if saque_especial and not saldo - valor >= -1000:
            print("Operação Falhou, você excedeu o valor limite de 1000 negativos!.")

        elif excedeu_saldo and not saque_especial:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de R$500.00.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente uma opção válida...")