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
###

#Terceiro exercício:
def remover_dado(dados_rolados,dados_guardados,dado_para_remover):

    dados_rolados.append(dados_guardados[dado_para_remover])

    del dados_guardados[dado_para_remover]

    lista_proxima_jogada = [dados_rolados,dados_guardados]

    return lista_proxima_jogada
###

#Quarto exercício:
def calcula_pontos_regra_simples(lista_números_faces):

    dicionário_pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    k = 0

    while k < len(lista_números_faces):

        dicionário_pontos[lista_números_faces[k]] += lista_números_faces[k]

        k +=1

    return dicionário_pontos