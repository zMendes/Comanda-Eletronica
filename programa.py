import json

running = True
with open('cardapio.json') as json_data:
    cardapio = json.load(json_data)
with open('comandas.json') as f:
    comandas=(json.load(f))
while running:
    menu = input("Comanda Eletrônica\n0. Sair\n1. Imprimir cardápio\n2. Adicionar item\n3. Remover item\n4. Imprimir comanda\n-->")
    if menu!='1' and menu!='2' and menu!='3' and menu!='4' and menu!='0':
        print("Opção Inválida!!!!!!")
    if menu =='0':
        print("Até mais")
        with open('cardapio.json','w') as f:
            f.write(json.dumps(cardapio))
        with open('comandas.json','w') as f:
            f.write(json.dumps(comandas))
        running = False
    if menu =='1':
        if cardapio == {}:
            print("Não há nada aqui")
        else:
            print("O cardápio possui os itens a seguir:")
        for a,b in cardapio.items():
            print("- {0}({1:.2f}R$)".format(a,b))
    
    if menu =='2':
        escolha= input("Gostaria de adicionar ao cardápio ou à comanda? " )
        if escolha=="cardápio" or escolha=="cardapio":
            pedido=input("O que deseja adicionar ao cardápio? " )
            preco=float(input("Preço:  "))
            if preco<0:
                print("O preço não pode ser menor que zero.")
            else:
                cardapio[pedido] = preco
                print("Item adicionado")
        if escolha=="comanda":       
            comanda=input("Qual a mesa? ")
            comandas[comanda]={}
            pedido = input("Faça sua escolha: ")
            if pedido in cardapio:
                quantidade= int(input("Quantidade: "))
                if pedido in comanda:
                    comandas[comanda][pedido] +=quantidade
                else:
                    comandas[comanda][pedido] = quantidade
                print("Quantidade atual de {0}: {1}".format(pedido,comandas[comanda][pedido]))
            else:
                print("Não há este produto no cardápio.")
    if menu =='3':
        escolha=(input("Deseja remover do cardapio ou da comanda?"))
        if escolha=='comanda':
            comanda=input("De qual comanda deseja remover?")
            pedido=input("Pedido a ser removido:")
            if pedido in comandas[comanda]:
                quantidade=int(input("Quantidade a remover: "))
                if quantidade<0:
                    print("Não é possível remover quantidade não positiva")
                else:
                    if (comandas[comanda][pedido]-quantidade)>=0:
                        comandas[comanda][pedido]=comandas[comanda][pedido]-quantidade
                        print ("Quantidade atual de {0} : {1}".format(pedido,comandas[comanda][pedido]))
                    if comandas[comanda][pedido]== 0:
                        del comandas[comanda][pedido]
                    else:
                        print("ERRO. Não podem ser removidos mais itens do que haviam antes.")
                        
            else:
                print("Este item não está na comanda")
        if escolha=='cardapio' or escolha=='cardápio':
            pedido=input('Qual item deseja remover do cardápio?')
            if pedido in cardapio:
                del cardapio[pedido]
            if pedido in comandas[comanda]:
                del comandas[comanda][pedido]
            else:
                print("Item não cadastrado")
    if menu=='4':
        comanda = input("Qual comanda deseja imprimir a conta? ")
        if comanda not in comandas:
            print("Comanda Inexistente")
        else:
            total=0
            for item in comandas[comanda]:
                total += cardapio[item] * comandas[comanda][item]
                unidade= cardapio[item] * comandas[comanda][item]
                print("{0}:{1:.2f}R$".format(item,cardapio[item]))
                print("{0}:{1:.2f}R$".format(comandas[comanda][item],unidade))
            print("Valor total:{0:.2f}R$".format(total))
            print("Valor total com serviços (10%):{0:.2f}R$".format(total*1.1))
2
