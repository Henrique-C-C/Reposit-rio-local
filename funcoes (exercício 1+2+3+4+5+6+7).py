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
###

#Quinto exercício:
def calcula_pontos_soma(lista_números_inteiros):

    j = 0
    soma_simples = 0

    while j < len(lista_números_inteiros):

        soma_simples += lista_números_inteiros[j]

        j +=1

    return soma_simples
###

#Sexto exercício:
def calcula_pontos_sequencia_baixa(faces_dados_rolados):

    pontos = 0
    p = 0

    dicionário = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    while p < len(faces_dados_rolados):
        
        dicionário[faces_dados_rolados[p]] = faces_dados_rolados[p]

        p += 1

    if dicionário[1] > 0 and dicionário[2] > 0 and dicionário[3] > 0 and dicionário[4] > 0:

        pontos = 15
    
    elif dicionário[2] > 0 and dicionário[3] > 0 and dicionário[4] > 0 and dicionário[5] > 0:

        pontos = 15

    elif dicionário[3] > 0 and dicionário[4] > 0 and dicionário[5] > 0 and dicionário[6] > 0:

        pontos = 15

    return pontos
###

#Sétimo exercício:
def calcula_pontos_sequencia_alta(facesdadosrolados):

    pontos2 = 0
    p2 = 0

    dicionário = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    while p2 < len(facesdadosrolados):
        
        dicionário[facesdadosrolados[p2]] = facesdadosrolados[p2]

        p2 += 1

    if dicionário[1] > 0 and dicionário[2] > 0 and dicionário[3] > 0 and dicionário[4] > 0 and dicionário[5] > 0:

        pontos2 = 30
    
    elif dicionário[2] > 0 and dicionário[3] > 0 and dicionário[4] > 0 and dicionário[5] > 0 and dicionário[6] > 0:

        pontos2 = 30

    return pontos2