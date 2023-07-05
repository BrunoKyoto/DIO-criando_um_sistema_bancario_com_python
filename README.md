# [Lab Project] Criando um Sistema Bancário com Python

###	Este projeto consiste em criar um sistema bancário simples, onde seja possível realizar depósitos, sacar e imprimir extratos.
###	Os saques, especificamente, devem respeitar o limite máximo diário de 3 retiradas, com um limite individual de R$500,00 por saque. Qualquer tentiva que esteja além desses limites deve ser negada.
###	O projeto foi bastante interessante, pois nos dá oportunidade de testar algumas estruturas, como por exemplo, condicionais aninhadas (if aninhado), laços de repetição (while), interpolação de strings, etc.
###	Foi bastante divertido e prazeroso executar este projeto.

#### Código-fonte:
```
from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
LIMITE = 500
data_atual = datetime.now()
corpo_extrato = f""
total_extrato = f"TOTAL EM CONTA: " + str(saldo)
numero_saques = 0
LIMITE_SAQUES = 2

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
        if LIMITE_SAQUES >= numero_saques:
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
        print(data_atual)
        print(f"\n-------------------EXTRATO-------------------\n")
        print("Não foram realizadas operações no período.\n" if not corpo_extrato else corpo_extrato)
        print("--------------------------------------\n")
        print(f"TOTAL EM CONTA: R${saldo:.2f}")
    elif opcao == "q":
        print("\nObrigado por utilizar nossos serviços! Tenha um bom dia!\n")
        break
```


### Potência Tech powered by iFood | Ciências de Dados com Python | Dominando o Python Para Ciência de Dados | [Lab Project] Criando um Sistema Bancário com Python