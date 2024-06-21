from usuario import Usuario


class OperacaoBancaria:

    LIMITE_SAQUE_DIARIO = 3
    LIMITE_VALOR_SAQUE = 500
    
    def __init__(self, usuario : Usuario):
        self.usuario = usuario

    def deposito(self, valor):
        if valor > 0:
            self.usuario.saldo += valor
            self.usuario.historico_operacao.append(f"Deposito: R$ {valor:0.2f}")
            return True
        
        else:
            print("\nERROR NA OPERAÇÃO\n")
            print("# Valor inválido. Informe um valor acima de R$ 0.00\n\n")           
            return False
    
    def saque(self, valor):
        if ((not (0 < valor <= self.LIMITE_VALOR_SAQUE)) or (valor > self.usuario.saldo) or (self.usuario.saques_diarios >= self.LIMITE_SAQUE_DIARIO)):
                   
            mensagem_error = "\nERROR NA OPERAÇÃO\n"
            
            if (not (0 < valor <= self.LIMITE_VALOR_SAQUE)):
                mensagem_error += f"# O valor do saque deve ser maior que R$ 0.00 e obedecer o limite máximo de R$ {self.LIMITE_VALOR_SAQUE:0.2f}\n"

            if (valor > self.usuario.saldo):
                mensagem_error += "# Saldo insuficiênte\n"

            if (self.usuario.saques_diarios >= self.LIMITE_SAQUE_DIARIO):
                mensagem_error += "# Limite de saque diário alcançado. Tente realizar novamente amanhão.\n" 
            
            print(f"{mensagem_error}\n")
            return False
        
        else:
            self.usuario.saldo -= valor
            self.usuario.saques_diarios += 1
            self.usuario.historico_operacao.append(f"Saque: R$ {valor:0.2f}")            
            return True

    def extrato(self):
        print("\n################# EXTRATO ################\n")

        for operacao in self.usuario.historico_operacao:
            print(operacao)

        print(f"\nSALDO: R$ {self.usuario.saldo:0.2f}\n##########################################")