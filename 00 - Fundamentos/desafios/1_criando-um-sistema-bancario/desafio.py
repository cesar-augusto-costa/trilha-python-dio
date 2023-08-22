menu = """
MENU:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 -  Digite uma letra: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:    + R$ {valor:.2f}\n"
            extrato += f"- Saldo:       R$ {saldo:.2f}\n"
            print("- Deposito efetuado com sucesso!")

        else:
            print("- Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("- Operação falhou! Você não tem saldo suficiente.")
            print(f"- Seu saldo é R$ {saldo:.2f}")

        elif excedeu_limite:
            print(f"- Operação falhou! O valor do saque excedeu o limite de R$ {limite:.2f}")

        elif excedeu_saques:
            print(f"- Operação falhou! Número máximo de {LIMITE_SAQUES} saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:       - R$ {valor:.2f}\n"
            extrato += f"- Saldo:       R$ {saldo:.2f}\n"
            numero_saques += 1
            print("- Saque efetuado com sucesso!")

        else:
            print("- Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("" if not extrato else "\n - HISTÓRICO \n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n- Saldo Atual: R$ {saldo:.2f}\n")
        print("=========================================")

    elif opcao == "q":
        print("- Saindo do Sistema. Volte Sempre!")
        break

    else:
        print("- Operação inválida, por favor selecione um opção válida.")
