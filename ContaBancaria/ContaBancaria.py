def atualiza_saldo(contas, num, valor):
    i = 0
    while i < len(contas):
        if contas[i] == num:
            contas[i + 2] = contas[i + 2] + valor
        i = i + 3


#1) abertura conta
#2) lancamento
#3) visualizacao extrato

#conta
contas = []

#lancamento
num_contas = []
valores = []

opcao = 0
while opcao != 4:
    print("1) abertura conta")
    print("2) lancamento")
    print("3) extrato")
    opcao = int(input("Opcao: "))
    if opcao == 1:
        info = int(input("Nº da conta: "))
        contas.append(info)
        info = input("Nome do cliente: ")
        contas.append(info)
        info = float(input("Saldo inicial: "))
        contas.append(info)

    elif opcao == 2:
        info = int(input("Nº da conta: "))
        num_contas.append(info)
        valor = float(input("valor: "))
        valores.append(valor)

        atualiza_saldo(contas, info, valor)

    elif opcao == 3:
        info = int(input("Nº da conta: "))
        i = 0
        while i < len(contas):
            if contas[i] == info:
                print("cliente:", contas[i+1])
                print("saldo:", contas[i+2])            
            i = i + 3

        i = 0 
        while i < len(num_contas):
            if num_contas[i] == info:
                if valores[i] < 0:
                    print("deb", valores[i])
                else:
                    print("cred", valores[i])
            i = i + 1