from time import time

 # função para leitura dos arquivos
def func(arq):
    matriz = [] #declaro vetor
    texto = arq.readlines() #quebra as linhas do arquivo em vetores 
    
    for i in range(len(texto)):  # percorre os vetores
        texto[i] = texto[i].replace('\n', '')  # tira os '\n'
        matriz.append(texto[i].split(','))  # quebra nas vírgulas

     # tratando as datas
    for i in range(len(matriz)):
        matriz[i][2] = matriz[i][2].split('/')
        matriz[i][2] = matriz[i][2][::-1]
        for j in range(len(matriz[i])):
            matriz[i][2][j] = int(matriz[i][2][j])
        
    return matriz
#


 # função para definir as prioridades
def clasf(clas):
    k = clas % 10 # ultimo digito 
    j = (clas - k) % 100 // 10 # segundo
    i = (clas - k - j*10) // 100 # primeiro
    return (i-1, j-1, k-1)

               
                
#

 # sort
def classort(tab, p = (0,1,2)):
    if p[0] == 0:
        if p[1] == 1:
            def func(elem):
                return(elem[0],elem[1],elem[2])  
        elif p[1] == 2:
            def func(elem):
                return(elem[0],elem[2],elem[1])  
    elif p[0] == 1:
        if p[1] == 0:
            def func(elem):
                return(elem[1],elem[0],elem[2])  
        elif p[1] == 2:
            def func(elem):
                return(elem[1],elem[2],elem[0])  
    elif p[0] == 2:
        if p[1] == 1:
            def func(elem):
                return(elem[2],elem[1],elem[0])  
        elif p[1] == 0:
            def func(elem):
                return(elem[2],elem[0],elem[1])  
            
    tab.sort(key=func)
    return
#



'''
1 - id
2 - nome
3 - data
possibilidades: 123, 132, 213, 231, 321, 312
'''

 # bolha
def Bolha(a, p=(0,1,2)): 
    # i = 1, 2, ..., n - 1
    for i in range(1, len(a)):
    # sobe com a[i] até encontrar o lugar adequado
        j = i
        while j > 0 and a[j][p[0]] < a[j - 1][p[0]]: 
            # troca com o seu vizinho
            a[j], a[j - 1] = a[j - 1], a[j]
            # continua subindo
            j = j - 1
            
        if a[j][p[0]] == a[j - 1][p[0]]: # se o primeiro for igual
            while j > 0 and a[j][p[1]] < a[j - 1][p[1]] and a[j][p[0]] == a[j - 1][p[0]]:
                    # troca com o seu vizinho
                    a[j], a[j - 1] = a[j - 1], a[j]
                    # continua subindo
                    j = j - 1
        
            if a[j][p[1]] == a[j - 1][p[1]]: # se o segundo for igual
                    while j > 0 and a[j][p[2]] < a[j - 1][p[2]] and a[j][p[1]] == a[j - 1][p[1]]:
                        # troca com o seu vizinho
                        a[j], a[j - 1] = a[j - 1], a[j]
                        # continua subindo
                        j = j - 1
#


 # quick
def particiona(lista, inicio, fim, p):
    # Particiona a lista de lista{inicio] até lista[fim]
    i, j = inicio, fim
    # Direção - dir == 1 esquerda-direita e dir == -1 ao contrário
    dir = 1
    while i < j:
        if lista[i][p[0]] > lista[j][p[0]]:
            lista[i], lista[j] = lista[j], lista[i]
            # muda a direção
            dir = - dir
        elif lista[i][p[0]] == lista[j][p[0]]: 
            if lista[i][p[1]] > lista[j][p[1]]:
                lista[i], lista[j] = lista[j], lista[i]
                # muda a direção
                dir = - dir
            elif lista[i][p[1]] == lista[j][p[1]]:
                if lista[i][p[2]] > lista[j][p[2]]:
                    lista[i], lista[j] = lista[j], lista[i]
                    # muda a direção
                    dir = - dir
         # incrementa i ou decrementa j
        if dir == 1: i = i + 1
        else: j = j - 1
    # Devolve o índice do elemento pivô
    return i


def Quick_Sort(lista, inicio, fim, p=(0,1,2)):
    # Se a lista tem mais de um elemento, ela será
    # particionada e as duas partições serão classificadas
    # pelo mesmo método Quick Sort
    if inicio < fim:
        k = particiona(lista, inicio, fim,  p)
        Quick_Sort(lista, inicio, k - 1, p)
        Quick_Sort(lista, k + 1, fim, p)
 #



 # rodar programa
def main():
    while True:
         # Pedir o nome do arquivo de origem (‘fim’: break)
        arq = input('Nome do arquivo de origem: ')
        if arq == 'fim': break
        else: arq = open(arq, 'r')
         # Ler o arquivo de origem e colocar em TAB (já com split(‘,’) dos campos)
        TAB = func(arq)
        #print(TAB[0:20])

        while True:
            TAB0, TAB1, TAB2 = TAB[:], TAB[:], TAB[:] # TAB1 = TAB2 = TAB  (2 cópias de TAB)123
             # Pedir a ordem (número inteiro que seja permutação de 123) (‘fim’: break)
            clas = input('Ordem de classificação: ')
            if clas == 'fim': break
            else:
                clas = int(clas)
                clas = clasf(clas)
                print(clas)

             # ClassificarSort(TAB, ordem) – cronometrar e mostrar o tempo gasto
            tsort1 = time()
            classort(TAB0, clas)
            tsort2 = time()
            print('Tempo de classificação Sort() =', tsort2 - tsort1)

             # ClassificarBolha(TAB1, ordem) – cronometrar e mostrar o tempo gasto
            tbol1 = time()
            Bolha(TAB1, clas)
            tbol2 = time()
            print('Tempo de classificação Bolha =', tbol2 - tbol1 )
            #print(TAB1[0:5])
             # Comparar TAB1 com TAB para ver se classificou corretamente
            if TAB1 == TAB0: print('*** Classificação correta')
            else:
                print('*** Classificação incorreta.')
                for i in range(len(TAB1)):
                    if TAB0[i] != TAB1[i]:
                        print(TAB1[i])

             # ClassificarQuick(TAB2, ordem) – cronometrar e mostrar o tempo gasto
            tq1 = time()
            Quick_Sort(TAB2, 0, len(TAB2)-1,  clas)
            tq2 = time()
            print('Tempo de classificação do Quick =', tq2 - tq1)
            #print(TAB2[0:5])
             # Comparar TAB2 com TAB para ver se classificou corretamente
            if TAB2 == TAB0: print('*** Classificação correta')
            else: print('*** Classificação incorreta.')
#

# caminho: E:\usp\programacoes\mac\arq.txt

main()

