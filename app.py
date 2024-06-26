from usuario import Usuario
from conta_corrente import ContaCorrente
from operacao_bancaria import OperacaoBancaria

lista_usuarios : list[Usuario] = []
ultima_conta_criada = None

def verificar_existencia_usuario(cpf):
    usuario_encontrado = next((usuario for usuario in lista_usuarios if usuario.cpf == cpf), None)
    return usuario_encontrado

def menu_inicial():
    while True:
        menu = f"""

        [1] JÁ POSSUO UM USUÁRIO
        [2] CRIAR USUÁRIO
        [3] SAIR

        => """

        opcao = int(input(menu))

        if opcao == 1:
            cpf = input("Digite o seu CPF (apenas números): ")
            usuario = verificar_existencia_usuario(cpf=cpf)
            
            if usuario == None:
                print("ERROR: O CPF informado não possuí cadastro.")
            else:
                menu_usuario(usuario)

        elif opcao == 2:
            cpf = input("Digite o seu CPF (apenas números): ")
            usuario = verificar_existencia_usuario(cpf=cpf)
            
            if usuario != None:
                print("ERROR: O CPF informado já possuí cadastro.")
            
            else:
                nome = input("Digite o seu Nome: ")
                data = input("Digite sua Data de Nascimento (ano-mês-dia): ")
                endereco = input("Digite o seu Endereço: ")

                usuario = Usuario.criar_usuario(cpf=cpf, nome=nome, data_nascimento=data, endereco=endereco)
                lista_usuarios.append(usuario)

                menu_usuario(usuario)
        
        elif opcao == 3:
            print("Agradecemos por ser o nosso cliente. Volte Sempre!")
            break
        
        else:
            print("\nOperação inválida. Por favor, selecione novamente a operação desejada")

def montar_menu_usuario(contas : list[ContaCorrente]):
    numero_selecao = 1
    selecao = {}
    mensagem_menu = ""
    
    for conta in contas:
        selecao[numero_selecao] = conta
        mensagem_menu += f"        [{numero_selecao}] {conta.conta}\n"
        numero_selecao += 1

    selecao[numero_selecao] = "CRIAR CONTA"
    mensagem_menu += f"        [{numero_selecao}] CRIAR CONTA\n"
    numero_selecao += 1
    selecao[numero_selecao] = "VOLTAR"
    mensagem_menu += f"        [{numero_selecao}] VOLTAR"

    return selecao, mensagem_menu

def menu_usuario(usuario : Usuario):

    global ultima_conta_criada   

    while True:
        contas = usuario.contas
        
        selecao, mensagem_menu = montar_menu_usuario(contas)

        menu = f"""

{mensagem_menu}

        => """

        opcao = int(input(menu))

        if opcao > len(selecao):
            print("\nOperação inválida. Por favor, selecione novamente a operação desejada")

        elif selecao[opcao] == "VOLTAR":
            break

        elif selecao[opcao] == "CRIAR CONTA":
            if ultima_conta_criada == None:
                novo_numero_conta = 1
            else:
                novo_numero_conta = ultima_conta_criada + 1
            
            ultima_conta_criada = novo_numero_conta

            nova_conta = ContaCorrente.criar_conta(usuario=usuario, conta=novo_numero_conta)
            usuario.contas.append(nova_conta)

        else:
            menu_operacao(selecao[opcao])
   
def menu_operacao(conta : ContaCorrente):
    
    operacao = OperacaoBancaria(conta)
    
    while True:

        menu = f"""
        SALDO: R$ {conta.saldo:0.2f}

        [1] DEPOSITAR
        [2] SACAR
        [3] EXTRATO
        [4] VOLTAR

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

menu_inicial()