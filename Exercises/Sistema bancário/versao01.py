menu = """
======= Menu =======
|   [1] - depósito  |
|   [2] - saque     |
|   [3] - extrato   |
|   [0] - sair      |
====================
"""

saldo = 0
limite_saque = 500
extrato = "____ Extrato ____ \n"
qtd_saques = 0
LIMITE_SAQUES_DIARIO = 3

while True:
    print(menu)
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        valor_deposito = float(input("Valor depósito: "))

        if valor_deposito < 0:
            print("Valor inválido!")
            continue

        extrato += f"+ R$ {valor_deposito:.2f}\n"
        saldo += valor_deposito

        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

    elif opcao == 2:
        valor_saque = float(input("Digite o valor do saque: "))

        excedeu_limite_diario = qtd_saques >= LIMITE_SAQUES_DIARIO
        excedeu_valor_saque = valor_saque >= limite_saque
        saldo_insuficiente = valor_saque > saldo

        if valor_saque < 0:
            print("Valor inválido!")
            continue

        elif excedeu_limite_diario:
            print(
                f"Você excedeu o limite de {LIMITE_SAQUES_DIARIO} saques diários.")
            continue

        elif excedeu_valor_saque:
            print(
                f"Não é possível realizar o saque de R$ {valor_saque:.2f}, pois ultrapassa o limite de R$ {limite_saque:.2f}.")
            continue

        elif saldo_insuficiente:
            print(f"Operação inválida, pois excede o saldo de R$ {saldo:.2f}")
            continue

        saldo -= valor_saque
        extrato += f"- R$ {valor_saque:.2f}\n"
        qtd_saques += 1

        print(
            f"Saque realizado com sucesso! O saldo atual é de R$ {saldo:.2f}")

    elif opcao == 3:
        print(extrato)
        print(f"saldo: R$ {saldo:.2f}")

    elif opcao == 0:
        break

    else:
        print("Digite uma opção válida")
