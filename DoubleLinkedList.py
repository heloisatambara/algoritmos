class Empty(Exception):
    pass

class ListaDuplamenteLigada:

    ''' operações sobre uma lista duplamente ligada. '''
    # classe _Node - interna
    class _Node:
        __slots__ = '_info', '_prev', '_prox'


        def __init__ (self, info, prev, prox):
         # inicia os campos
            self._info = info
            self._prev = prev
            self._prox = prox


    # métodos de lista duplamente ligada
    def __init__ (self):
        ''' cria uma lista circular vazia.'''
        self._inicio = self._Node(None, None, None) # vazia
        self._final = self._Node(None, None, None) # vazia
        self._tamanho = 0 # tamanho da lista


    def __len__(self):
        ''' retorna o tamanho da pilha.'''
        return self._tamanho


    def is_empty(self):
        ''' retorna True se pilha vazia'''
        return self._tamanho == 0


    def adicionar_entre(self, e, anterior, sucessor):
        ''' adiciona elemento entre 2 outros.
        retorna o novo nó.'''
        novo = self._Node(e, anterior, sucessor)
        anterior._prox = novo
        sucessor._prev = novo
        self._tamanho += 1
        return novo


    def remove(self, node):
        ''' remove nó da lista e retorna seu valor.'''
        anterior = node._prev
        sucessor = node._prox
        anterior._prox = sucessor
        sucessor._prev = anterior
        self._tamanho -= 1
        val = node._info # guarda a informação
        # inative o nó
        node._prev = node._prox = node._info = None
        return val

    def Conta(LA, x):
        # devolve quantos nós da lista duplamente ligada LA com info == x.
        if LA.is_empty():
            raise Empty('Lista Vazia')
        count = 0
        p = LA._inicio
        while p != None: # roda a lista até acabar
            if p._info == x:
                count += 1 # adiciona um a cada vez que acha um x
            p = p._prox
            if p == None or p._prev._info == x and p._info != x: # para quando já passou os x: estão ordenados
                return count
            
            
        else:
            print(f'{x} não está na lista.')
            return


    def Adiciona(LA, x):
        # Adiciona novo elemento com info == x na lista duplamente ligada LA.
        # Mantém a ordem crescente.
        novo = LA._Node(x, None, None)
        if LA.is_empty():
            LA._inicio = LA._final = novo
            LA._tamanho += 1
            return
        p = LA._inicio
        if p._info >= x:
            LA._inicio = novo
            novo._prox = p
            p._prev = novo
            return
        while p._info <= x: # para quando p for menor que x, para adicionar o novo nó após p
            if p._prox == None:
                novo._prev = LA._final
                LA._final._prox = novo
                LA._final = novo
                LA._tamanho += 1
                return
            if p._prox._info > x:
                break
            p = p._prox
        
        novo._prev = p
        novo._prox = p._prox
        p._prox = novo
        LA._tamanho += 1
        

    def Remove(LA, x):
        if LA.is_empty():
            raise Empty('Lista Vazia')
        # Remove todos os elementos com info == x da lista duplamente ligada LA.
        # Estarão contíguos
        
        p = LA._inicio
        i = 0
        while True:
            if p._info == x:
                anterior = p._prev
                while p._info == x:
                    p = p._prox
                    i += 1
                    if p == None:
                        break
                posterior = p
                if anterior == None:
                    LA._inicio = posterior
                else:
                    anterior._prox = posterior
                    if posterior != None:
                        posterior._prev = anterior
                break
            p = p._prox
            if p == None:
                print(f'{x} não está na lista.')
                break
        return i
            
                    
                
    def __str__(LA):
        # Mostra os elementos da lista duplamente ligada.
        # Mostra também o anterior e o sucessor.
        if LA.is_empty():
            return 'lista vazia'
        p = LA._inicio
        print('Imprimindo a lista duplamente ligada:')
        print('\nNó    Anterior    Informação    Posterior')
        count = 1
        while p != None:
            
            if p._prev == None:
                anterior = 'None'
            else:
                anterior = p._prev._info
            if p._prox == None:
                posterior = 'None'
            else:
                posterior = p._prox._info
            print('%-5s %-11s %-13s %s' %(f'{count}', f'{anterior}', f'{p._info}', f'{posterior}'))
            p = p._prox
            count += 1
        return ''
                




if __name__ == '__main__':
    LA = ListaDuplamenteLigada()
    print('a')
    LA.Adiciona('exaurida')
    print(LA)
    LA.Adiciona('exausta')
    print(LA)
    LA.Adiciona('unhuda')
    print(LA)
    LA.Adiciona('exaurida')
    print(LA)
    LA.Adiciona('saltuda')
    print(LA.Conta('exaurida'))
    print(LA)
    LA.Remove('exaurida')
    print(LA)
