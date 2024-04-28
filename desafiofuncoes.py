import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, contas, conta_saque):

    for conta in contas:

        if conta_saque == conta["numero_conta"] and conta["conta_especial"] == "Sim":
            # if conta_saque:
            saque_especial = valor > saldo

            if saque_especial and not saldo - valor >= -1000:
                print("\n@@@ Operação falhou, você excedeu o valor limite de 1000 negativos!. @@@")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                numero_saques += 1
                print("\n=== Saque especial realizado com sucesso! ===")
            else:
                print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        elif conta_saque == conta["numero_conta"] and conta["conta_especial"] == "Não":
                 
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= limite_saques
                
                if excedeu_saldo:
                    print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

                elif excedeu_limite:
                    print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

                elif excedeu_saques:
                    print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                    numero_saques += 1
                    print("\n=== Saque realizado com sucesso! ===")

                else:
                    print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

                return saldo, extrato
            
        else:
            print("\n@@@ Operação falhou! Conta inválida. @@@")

# def filtrar_conta(conta_saque, contas):
#     for conta in contas:
#         if conta["numero_conta"] == conta_saque:
#             return conta["numero_conta"]
#     # print("\n@@@ Conta não encontrada! @@@")
#     return None
# def filtrar_conta(conta_saque, contas):
#     contas_filtradas = [conta for conta in contas if conta["numero_conta"] == conta_saque]
#     return contas_filtradas[0] if contas_filtradas else print("\n@@@ Conta não encontrada! @@@")

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta_especial = input("Conta Especial? (Sim/Não): ")
        if conta_especial == "Sim":
            print("\n=== Conta especial criada com sucesso! ===")
        else:
            print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "conta_especial": conta_especial}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Especial:\t{conta['conta_especial']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1001

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            
            conta_saque = int(input("Informe o número da sua conta para Saque: "))

            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                contas=contas,
                conta_saque=conta_saque,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            # numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
