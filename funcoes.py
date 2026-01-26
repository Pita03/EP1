import random 
def cria_pecas ():
    lista = []
    peca = [0,0]

    i = 0
    while i < 7:

        j = 0
        while j < 7:
            peca[i][j] = j
            lista.append (peca)
        
        j+=1
    i+= 1
    
    return random.shuffle (lista)
    
    

    # toda vez que chama a função ele embaralha a ordem da lista