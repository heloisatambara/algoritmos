
def Hanoi(n, torreA, torreB, torreAux, isfirst = True):
    if isfirst == True:
        global st
        stA, stB, stC = [], [], []
        st = [stA, stB, stC]
        for k in range(1, n+1):
            stA.append(k)
            stB.append(0)
            stC.append(0)
            print(f'{k}')
        else:
            stA.sort(reverse=True)
            print('A\tB\tC')

        
    if n == 1:
         # mover disco 1 da torreA para a torreB
        Movimente(1, torreA, torreB, st)
    else:
         # n - 1 discos da torreA para torreAux com torreB auxiliar
        Hanoi(n - 1, torreA, torreAux, torreB, False)
         # mover disco n da torreA para torreB
        Movimente(n, torreA, torreB, st)
         # n - 1 discos da torreAux para a torreB com torreA auxiliar
        Hanoi(n - 1, torreAux, torreB, torreA, False)
        
        
def Movimente(k, origem, destino, st):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino)
    for i in range(len(st[0])):
        if st[origem][i] == k:
            st[origem][i] = 0
    for i in range(len(st[0])):        
        if st[destino][i] == 0:
            st[destino][i] = k
            break
            
    graphMove(st)

def graphMove(l):
    for k in range(len(l[0])-1, -1, -1):
        print()
        for j in range(3):
            if l[j][k] == 0:
                print(' \t', end='')
            else:
                print(f'{l[j][k]}\t', end='')
    else:
        print('\nA\tB\tC')
    

def main():
    while True:
        n = input('Quantos discos na sua torre? obs.: 0 para o programa. ')
        try:
            n = int(n)
            if n == 0: return
            Hanoi(n, 0, 1, 2)
        except: print('Digite um número inteiro') 
    

main()
