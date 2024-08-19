
# This Python file uses the following encoding: utf-8

class ListNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode #None self.antNode = None

    # def getData(self):
    #     return self.data
    #
    # def setData(self, val):
    #     self.data = val
    #
    # def getNextNode(self):
    #     return self.nextNode
    #
    # def setNextNode(self, val):
    #     self.nextNode = val


# Lista Simplesmente Encadeada com Iterador
class SinglyLinkedListIterator:  # LinkedList

    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode  = firstNode
        self.iterator  = firstNode
        if firstNode:
            self.size = 1
        else:
            self.size = 0

  
    # def getSize(self):
    #     return self.size
    #
    # def get_firstNode(self):
    #     return self.firstNode
    #
    # def get_lastNode(self):
    #     return self.lastNode
    #
    # def get_iterator(self):
    #     return self.iterator
    #
    # def setSize(self, size):
    #     self.size = size


    def adiciona_inicio(self, data):


        newNode = ListNode(data,None) # treats the empty list ; trata a lista vazia
        newNode.nextNode = None

        if self.head == None: #lista vazia
            self.head = newNode
            self.tail - newNode
        else: #lista cheia 1 ou + nos
            newNode.nextNode = self.head
            self.head = newNode
        return True


    def adiciona_fim(self, data):
        """Pre condicao: Iterador definido
           Pos condicao: O data eh inserido em um Noh antes do iterador. O iterador fica sobre este Noh.
        """
        newNode = ListNode(data, None)  # treats the empty list ; trata a lista vazia
        newNode.nextNode = None

        if self.head == None: #lista vazia
            self.head = newNode
            self.tail - newNode
        else: #lista cheia 1 ou + nos
            self.tail.nextNode = newNode
            self.tail = newNode

        return True

#fazer adicionar no meio

            

            



    def elimNode(self): # elimina o elemento que está sobre o iterador e avanca o iterador para proximo Noh.
        if(self.iterator == self.firstNode): # iterador sobre o primeiro elemento
            if(self.lastNode == self.firstNode): # tem so um Noh
                self.lastNode = None # aponta para nada
                self.firstNode = None
                self.iterator = None
            else: # tem mais de um Node
                #self.firstNode = self.firstNode.nextNode # firstNode aponta para o proximo noh que passa a ser o primeiro
                self.firstNode = self.firstNode.nextNode # self.iterator.nextNode
                self.iterator.nextNode = None # isola o Noh
                self.iterator = self.firstNode # avanca para o proximo Noh
        else: # iterator pode estar sob o ultimo ou um elemento interno
            currentNode = self.firstNode  # aponta para o primeiro noh da lista
            while currentNode.nextNode != self.iterator:  # percorrer a lista e parar uma posicao antes do iterador
                currentNode = currentNode.nextNode  # avanca para o proximo noh
            if self.iterator == self.lastNode: # o iterador esta sob o ultimo:
                # por lastNode sob o penultimo elemento: percorrer a lista ate parar antes do iterador
                # para tal usar um ponteiro auxiliar currentNode
                self.lastNode = currentNode # o penultimo(currentNode) agora passa a ser o ultimo Noh
                self.iterator.nextNode = None # isola o Node
                self.iterator = None # iterador fica indefinido
                currentNode.nextNode = None # ultimo Node nao tem proximo
            else: # iterador sobre elemento intermediario
                currentNode.nextNode = self.iterator.nextNode # o noh anterior ao que sera eliminado aponta para o seguinte deste noh
                currentNode = self.iterator # guarda o Noh que vai ser eliminado
                self.iterator = self.iterator.nextNode # avanca o iterador para o proximo noh
                currentNode.nextNode = None # isola o noh
        self.size = self.size - 1 # decrementa o tamanho da lista
        return True


    def first_Node(self): # coloca o iterador sobre o primeiro Node da Lista
        self.iterator = self.firstNode
        return True


    def last_Node(self): # coloca o iterador sobre o útlimo Node da Lista
        self.iterator = self.lastNode
        return True

    def nextNode(self): # avança o iterador uma posição. para tal o iterador deve estar definido(sobre um Noh)
        if(self.iterator):
            self.iterator = self.iterator.nextNode
        return True

    # def antNode(self):

    def posNode(self, position): # coloca o iterador sobre a posição position
        """o iterador eh posto sobre o Nod da posicao que vai de 1 ate size.
           qualquer outro valor leva o iterador a ficar indefinido(None)
           Return True para posicao valida e False para iterador indefinido
        """
        if(position > 0 and position <= self.size):
            i = 1
            self.iterator = self.firstNode # poe o iterador sob o primeiro Node
            while(i < position):
                if(self.iterator.nextNode != None):
                    self.iterator = self.iterator.nextNode
                    i = i + 1
            return  True
        else:
            return False


    def isUndefinedIterator(self): # retorna verdadeiro se o iterador estiver indefinido
        if(self.iterator == None):
            return True
        else:
            return False


    def printNode(self):
        curr = self.firstNode
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


if __name__ == '__main__':

    # def printLista2(Lista):
    #     currentNode = Lista.firstNode
    #     while currentNode:
    #         print(currentNode.data)
    #         currentNode = currentNode.getNextNode()
    #         #currentNode = currentNode.nextNode


    novo_noh = ListNode(5)
    novo_noh.data = 10
    lista22 = SinglyLinkedListIterator(novo_noh)
    lista = SinglyLinkedListIterator()
    lista.addNode(10)
    lista.addNode(20)
    lista.addNode(30)
    lista.addNode(40)


    def printLista(lista):
        lista.first_Node() # por o iterador sobre o primeiro elemento
        while not lista.isUndefinedIterator():
            #print(lista.iterator.data, end=" ")
            print(lista.iterator.data)
            lista.nextNode() # avanca iterador para proximo noh
            #lista.iterator = lista.iterador.nextNode
        print('\n')


