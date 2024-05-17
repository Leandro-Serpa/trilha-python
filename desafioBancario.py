menu ='''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
saque = 0
transacao = []
item = 0

while True:
    opcao = input(menu)

    if opcao =="d":
        deposito=round(float(input("Digite o valor de depósito: ")),2)
        print("Depósito")
        if round(deposito, 2) > 0:
            saldo = deposito + saldo
            transacao.append(deposito)
            print(f"Saldo: R$ {saldo:1.2f}")
        else:
            print("Depósito invalido!!!")
            

    elif opcao =="s":
        saque = round(float(input("Digite valor de saque: ")),2)
        if numero_saques <= 3:
            numero_saques += 1
            if numero_saques > LIMITE_SAQUES:
                print("Ultrapassou o limite de numeros de saques")
                break
            elif saque > 500:
                print("Valor de saque ultrapassa o valor por transação.\n***Valor máximo permitido R$ 500.00***")
                break
            if round(saque, 2) <= saldo:
                saldo = round(saldo,2) - saque
                saida = saque - saque * 2
                transacao.append(saida)
                print(f'Saque autorizado! \n Saldo: {saldo:.2f}')
            else:
                print(f'Saldo insuficiente!')

            
    

    elif opcao =="e":
        print("Extrato:\n")
        for item in transacao:
            print(item)
        print(f'\n Saldo: {saldo:.2f}')

    elif opcao =="q":
        break
    else:
        print("\n Opção inválida, por favor selecione novamente a opção desejada. ")


