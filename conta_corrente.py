class ContaCorrente:
    def __init__(self, *, usuario = None, conta = None, agencia = "0001", saldo = 0, saques_diarios = 0, historico_operacao: list = []):        
        self.usuario = usuario
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.saques_diarios = saques_diarios
        self.historico_operacao = historico_operacao

    def criar_conta(*, usuario, conta):
        numero_conta = str(conta)
        nova_conta = ContaCorrente(conta=numero_conta, usuario=usuario, historico_operacao = [])
        return nova_conta