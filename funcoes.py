import random

def rolar_dados(número__de_dados):

    lista_faces_dados = []

    i = 0

    while i < número__de_dados:

        face = random.randint(1,6) 

        lista_faces_dados.append(face)

        i +=1
    
    return lista_faces_dados