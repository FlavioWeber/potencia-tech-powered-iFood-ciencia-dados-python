menu = """
                =============================   
                   Menu de Opções Bancárias
                   ---- -- ------ ---------

                        [d] Depositar
                        [s] Sacar
                        [e] Extrato
                        [q] Sair

                      => """

valor = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito:")
        valor = float(input("Informe o valor a ser depositado: "))
        if valor <= 0:
            print("Digite um valor válido para o depósito!")
            continue
        else:
            saldo += float(valor)
            extrato += f"Depósito: R$ {valor:.2f} \n"
    
    elif opcao == "s":
        print("Saque:")
          
        if numero_saques >= LIMITE_SAQUES:
             print("Limite de saques excedido!")
             print("Quantidade de saques efetuados: " + str(numero_saques) )            
             continue

        else:
            valor = float(input("Informe o valor a ser sacado: "))
            if saldo < float(valor):
                print("Saldo insuficiente!")
                print("Saldo Atual: R$ " + str(float(saldo)))
                continue

            elif float(valor) <= 0:
                print("Digite um valor válido para o saque!")
                continue

            elif float(valor) > limite:
                print("Valor máximo para saque é de R$ 500,00!")
                continue 

            else:
                 numero_saques += 1
                 saldo -= float(valor)
                 extrato += f"Saque   : R$ {valor:.2f} \n"
                 
    elif opcao == "e":
        print("\n================= Extrato =================\n")
        extrato += f"\nSaldo   : R$ {saldo:.2f} \n"
        print(extrato)
        print("===========================================\n")

    elif opcao == "q":
        break
    
    else:
        print("Operacão Inválida! Favor selecionar novamente a operação desejada.")
        

