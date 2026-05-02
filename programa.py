import random
import funcoes

rerrolagens = 0
lista_dados_guardados = []
lista_faces_dados = []
opções = [1,2,3,4,0]

i = 0

while i < 5:

    face = random.randint(1,6) 

    lista_faces_dados.append(face)

    i +=1

j = 0

while j < 12:

    print(f"Dados rolados: {lista_faces_dados}")
    print(f"Dados guardados: {lista_dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opção = int(input(""))

    while opção not in opções:

        print("Opção inválida. Tente novamente.")
        print(f"Dados rolados: {lista_faces_dados}")
        print(f"Dados guardados: {lista_dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opção = int(input(""))

    if opção == 1:
        
        print("Digite o índice do dado a ser guardado (0 a 4): ")
        índice = int(input(""))
        lista_dados_guardados.append(lista_faces_dados[índice])
        del lista_faces_dados[índice]

    if opção == 2:

        print("Digite o índice do dado a ser removido (0 a 4): ")
        dado_para_remover = int(input(""))
        lista_faces_dados.append(lista_dados_guardados[dado_para_remover])
        del lista_dados_guardados[dado_para_remover]

    if opção == 3 and rerrolagens < 2:
        
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

    if opção == 4:

        print(funcoes.imprime_cartela)

    #if opção == 0:


    j +=1

        