class Usuario:
    
    def __init__(self, saldo = 0, saques_diarios = 0, historico_operacao = []):
        self.saldo = saldo
        self.saques_diarios = saques_diarios
        self.historico_operacao = historico_operacao