import random

#Primeiro execício:
def rolar_dados(número__de_dados):

    lista_faces_dados = []

    i = 0

    while i < número__de_dados:

        face = random.randint(1,6) 

        lista_faces_dados.append(face)

        i +=1
    
    return lista_faces_dados
###

#Segundo exercício:

def guardar_dado(lista_dados_rolados,lista_dados_estoque,índice_dado_guardar):

    lista_dados_estoque.append(lista_dados_rolados[índice_dado_guardar])

    del lista_dados_rolados[índice_dado_guardar]

    lista_próxima_jogada  = [lista_dados_rolados,lista_dados_estoque]

    return lista_próxima_jogada