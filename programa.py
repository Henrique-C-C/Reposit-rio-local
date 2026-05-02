import random
import funcoes

opções = ["1","2","3","4","0"]

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

j = 0

while j < 12:

    rerrolagens = 0
    lista_dados_guardados = []
    lista_faces_dados = []
    listacombinação = []

    i = 0

    while i < 5:

        face = random.randint(1,6) 

        lista_faces_dados.append(face)

        i +=1

    print(f"Dados rolados: {lista_faces_dados}")
    print(f"Dados guardados: {lista_dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opção = input()

    while opção not in opções:

        print("Opção inválida. Tente novamente.")
        opção = input()

    opção = int(opção)
    
    while opção != 0: 
        if opção == 1:
            
            print("Digite o índice do dado a ser guardado (0 a 4):")
            índice = int(input())
            lista_dados_guardados.append(lista_faces_dados[índice])
            del lista_faces_dados[índice]

        elif opção == 2:

            print("Digite o índice do dado a ser removido (0 a 4):")
            dado_para_remover = int(input())
            lista_faces_dados.append(lista_dados_guardados[dado_para_remover])
            del lista_dados_guardados[dado_para_remover]

        elif opção == 3 and rerrolagens < 2:
            
            rerrolagens += 1
            tamanho = len(lista_faces_dados)
            k = 0
            lista_faces_dados = []

            while k < tamanho:

                face = random.randint(1,6) 

                lista_faces_dados.append(face)

                k +=1

        elif opção == 3 and rerrolagens == 2:
            
            print("Você já usou todas as rerrolagens.")

        elif opção == 4:

            funcoes.imprime_cartela(cartela)

        print(f"Dados rolados: {lista_faces_dados}")
        print(f"Dados guardados: {lista_dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opção = input()

    if opção == 0:

        print("Digite a combinação desejada:")
        combinação = input()
        
        if combinação  in listacombinação:
            print("Essa combinação já foi utilizada.")

        if combinação not in cartela["regra_avancada"]:
            if int(combinação) not in cartela["regra_simples"]:
                print("Combinação inválida. Tente novamente.")

        listacombinação.append(combinação)


        funcoes.faz_jogada(lista_faces_dados,combinação,cartela)

        j +=1

pontuação = 0
soma_simples = 0

p = 1

while p < 7:

    soma_simples += cartela["regra_simples"][p]
    p +=1

if soma_simples >= 63:
    pontuação += 35

for regras,dicionario in cartela.items():

    for combinações,valores in dicionario.items():

        pontuação += valores

print(cartela)
print(f"Pontuação total: {pontuação}")