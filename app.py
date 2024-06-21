from operacao_bancaria import OperacaoBancaria
from usuario import Usuario

usuario = Usuario()
operacao = OperacaoBancaria(usuario)

while True:

    menu = f"""
    SALDO: R$ {usuario.saldo:0.2f}

    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] SAIR

    => """

    opcao = int(input(menu))

    if opcao == 1:

        opcao_validada = False

        while opcao_validada == False:
            valor = float(input("\nOBS.: Informe o valor de 0, caso deseje voltar pro menu anterior.\nInforme o valor que desejas depositar: R$ "))
            if valor == 0:
                break

            opcao_validada = operacao.deposito(valor)
                
    elif opcao == 2:
        opcao_validada = False

        while opcao_validada == False:
            valor = float(input(f"\nOBS.: Informe o valor de 0, caso deseje voltar pro menu anterior.\nInforme o valor que desejas sacar (Limite Máximo de R$ {operacao.LIMITE_VALOR_SAQUE:0.2f}): R$ "))
            if valor == 0:
                break

            opcao_validada = operacao.saque(valor)

    elif opcao == 3:
        operacao.extrato()

    elif opcao == 4:
        break
    
    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada")