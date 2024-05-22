##################################################################################################################################
## STEP 1                                                                                                                       ##
##################################################################################################################################

class UsuarioTelefone:

    def __init__(self, nome, numero, plano):

        self.nome = nome
        self._numero = numero
        self._plano = plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


nome = input()
numero = input()
plano = input()

usuario = UsuarioTelefone(nome=nome, numero=numero, plano=plano)

print(usuario)

##################################################################################################################################
## STEP 2                                                                                                                       ##
##################################################################################################################################

class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo

    def verificar_saldo(self):
        if self._saldo < 10:
            return self._saldo, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >= 50:
            return self._saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return self._saldo, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        return self.plano.verificar_saldo()

nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)

##################################################################################################################################
## STEP 3                                                                                                                       ##
##################################################################################################################################

class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao_minutos):
        custo_por_minuto = 0.10
        return custo_por_minuto * duracao_minutos

    def deduzir_saldo(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao_minutos):
        custo = self.plano.custo_chamada(duracao_minutos)
        if self.plano.deduzir_saldo(custo):
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return f"Saldo insuficiente para fazer a chamada."

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Criando objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))