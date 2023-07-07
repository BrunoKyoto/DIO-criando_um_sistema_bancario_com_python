menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
LIMITE = 500
corpo_extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Por favor, informe o valor do depósito: "))
        print()
        if valor > 0:
            saldo += valor
            corpo_extrato += f"--Depósito: R${valor:.2f}--\n"
            print(f"O depósito de R${valor:.2f} foi realizado com sucesso!\n")

    elif opcao == "s":
        if LIMITE_SAQUES > numero_saques:
            valor = float(input("Por favor, informe o valor do saque: "))
            print()
            if valor > 0:
                if valor <= LIMITE:
                    if valor <= saldo:
                        saldo -= valor
                        corpo_extrato += f"--Saque: R${valor:.2f}--\n"
                        print(f"O saque de R${valor:.2f} foi realizado com sucesso!")
                        numero_saques += 1
                    else:
                        print("Solicitação negada: O valor do saque é superior ao valor disponível em conta!")
                else:
                    print("Solicitação negada: O valor máximo de saque deve ser R$500.00.")
        else:
            print("Desculpe, você já efetuou o número máximo de saques diários. Tente novamente amanhã. Obrigado.")

    elif opcao == "e":
        print()
        print(f"\n-------------------EXTRATO-------------------\n")
        print("Não foram realizadas operações no período.\n" if not corpo_extrato else corpo_extrato)
        print("--------------------------------------\n")
        print(f"TOTAL EM CONTA: R${saldo:.2f}")

    elif opcao == "q":
        print("\nObrigado por utilizar nossos serviços! Tenha um bom dia!\n")
        break
