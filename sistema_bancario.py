menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """ 

saldo = 0 
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("\nDigite o valor que você deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
            
        else:
            print("Operação falhou! Digite outro valor")
        
    
    elif opcao == "2":
        valor = float(input("\nDigite o valor que você deseja sacar: "))
            
        saldo_insuficiente = valor > saldo
        limite_insuficiente = valor > limite
        exceder_saques = numero_saques >= LIMITE_SAQUES
        
        if saldo_insuficiente:
            print("Saldo Insuficiente! Digite outro valor")
        
        elif limite_insuficiente:
            print(f"Limite insuficiente! Seu limite atual é de {limite}")
            
        elif exceder_saques:
            print("Operação não concluida! O limite de saques foi excedido")
            
        elif valor > 0:
            saldo -= valor
            print(f"Sacando R$ {valor} ... ")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! Digite outro valor")
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato.strip() else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "0":
        print("\nObrigado por usar nosso banco. Volte sempre!")
        break

    else:
        print("Opção inválida, selecione novamente a operação desejada")