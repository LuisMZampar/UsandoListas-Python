#a) criar um anuncio
#b) consulta anuncio
#c) edita um anuncio

#anuncio: modelo, ano, montadora, celular, placa, valor

modelos = []
anos = [] 
montadoras = []
celulares = []
placas = [] 
valores = []

opcao = 0
while opcao != 4:
    print("1) cria anuncio")
    print("2) consulta anuncio")
    print("3) edita anuncio")
    print("4) sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        info = input("Informe o modelo: ")
        modelos.append(info)
        info = int(input("Ano de fabricacao: "))
        anos.append(info)
        info = input("Informe a montadora: ")
        montadoras.append(info)
        info = input("Celular: ")
        celulares.append(info)
        info = input("Informe a placa: ")
        placas.append(info)
        info = float(input("Valor: "))
        valores.append(info)
    elif opcao == 2:
        montadora = input("Informe a montadora: ")
        k = 1
        for i in range(len(montadoras)):
            if montadoras[i] == montadora:
                print(f'{k}) {modelos[i]} ({anos[i]}) - {montadoras[i]}')
                print(f'{valores[i]} - {celulares[i]}')
                k = k + 1
    elif opcao == 3:
        placa = input("Placa do carro: ")
        pos = placas.index(placa)
        if pos == -1:
            print("Placa não encontrada!\n")
        else:
            print("Editando o anuncio: ")    
            info = input(f"Modelo ({modelos[pos]}): ")
            if info != "":
                modelos[pos] = info
            info = input(f'Ano de fabricacao ({anos[pos]}): ')
            if info != "":
                anos[pos] = info

            info = input(f'Montadora ({montadoras[pos]}): ')
            if info != "":
                montadoras[pos] = info

            info = input(f'Valor ({valores[pos]}): ')
            if info != "":
                valores[pos] = info