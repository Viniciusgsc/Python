"""
    Classe que representa uma unidade de informação
    na lista duplamente encadeada
"""
from logging import raiseExceptions


class Node:

    """ Método construtor """
    def __init__(self, data):
        self.prev = None    # Ponteiro para o nodo anterior
        self.data = data    # Dado do usuário
        self.next = None    # Ponteiro para o nodo seguinte

##################################################################

"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos)
    não estão adjacentes fisicamente uns dos outros, mas ligados
    logicamente por meio de ponteiros que indicam o anterior e
    o próximo nodo da sequência. Não tem restrição de acesso -
    inserções, exclusões e consultas podem ser realizados em
    qualquer posição da lista.
"""
class DoublyLinkedList:

    """ Método construtor """
    def __init__(self):
        self.__head = None  # Aponta para o primeiro nodo da lista
        self.__tail = None  # Aponta para o último nodo da lista
        self.__count = 0    # Mantém o número de nodos da lista

    """
        Propriedade que retorna a quantidade de itens da lista
    """
    @property
    def count(self):
        return self.__count

    """
        Propriedade que retorna se a lista está ou não vazia
    """
    @property
    def is_empty(self):
        return self.__count == 0

    """
        Método que insere um valor na posição especificada
    """
    def insert(self, pos, val):

        # Criamos um nodo que contém a informação do usuário e
        # também os ponteiros prev e next apontando para None
        inserted = Node(val)

        # 1º caso: a lista está vazia e este é o primeiro nodo a
        # ser inserido
        if self.is_empty:
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção na posição inicial (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3º caso: inserção na posição final (qualquer posição >= count)
        elif pos >= self.count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        else:
            # Encontrar o nodo atualmente na posição de inserção
            node_pos = self.__find_node(pos)
            # Encontra o nodo da posição anterior à de inserção
            before = node_pos.prev

            before.next = inserted
            inserted.prev = before
            inserted.next = node_pos
            node_pos.prev = inserted


        
        # Incrementa a contagem de itens
        self.__count += 1

    """
        Método de "atalho" para a inserção no início da lista
    """
    def insert_head(self, val):
        self.insert(0, val)
    """
        Método que remove o nodo da posição especificada
    """
    def remove(self, pos):
        # 1º caso: lista vazia ou posição fora dos limites da lista
        if self.is_empty or pos < 0 or pos > self.count - 1:
            raise Exception('ERRO: posição inválida para remoção')

        #2º caso: remoção do início da lista
        if pos==0:
            # Será removido o head da lista
            removed = self.__head
            # O novo head passa a ser o sucessor do nodo removido
            self.__head = removed.next
            # Se o novo __head for um nodo válido, ele não pode ter um antecessor 
            if self.head is not None: self.__head.prev = None
            # Em caso de remoção do único nodo restante, __tail 
            # precisa passar a valer None
            if self.count == 1: self.__tail = None
        
        #3º caso: remoção do final da lista 
            elif pos == self.count - 1:
                # Será removido o tail da lista
                removed = self.__tail
            # O novo tail passa a ser o antecessor do nodo removido
            self.__tail = removed.prev
            # Se o nobo __tail fou um nodo válido, ele não pode ter sucessor
            if self.__tail is not None: self.__tail.next = None
            # Em caso da remoção do único nodo restante, __head
            # precisa passar a valer None
            if self.count == 1: self.__head = None
        #4º caso: remoção de posição intermediária
            else:
                # Encontra o nodo a ser removido
                removed.self__find_node(pos)
                before = removed.prev # Nodo anterior
                after = removed.next # Nodo posterior
                # O nodo anterior passa a apontar á frente para o nodo after
                before.next = after
                # O nodo posterior passa a apontar para trás o nodo before
                after.prev = before
                
        # Decrementa a quantidade de itens da lista 
        self.count -= 1
        # Retorna o dado de usuário armazenado no nodo removido
        return removed.data
    """
        Função privada que encontra o nodo da posição especificada
    """
    def __find_node(self, pos):
        # 1º caso: posição 0, retorna __head
        if pos == 0:
            return self.__head
        # 2º caso, posição == count -1, retorna __tail
        elif pos == self.count - 1:
            return self.__tail
        # 3º caso: nodo intermediário
        else:
            # Se o nodo estiver na primeira metade da lista,
            # faz o percurso a partir de __head, seguindo next
            if pos < self.count // 2:
                node = self.__head
                for i in range(1, pos + 1): node = node.next

            # Senão, faz o percurso a partir de __tail, seguindo prev
            else:
                node = self.__tail
                for i in range(self.count - 2, pos - 1, -1): node = node.prev

            return node

    """
        Metodo  que permite visualizar a lista encadeada como uma string
    """

    def __str__(self):
        output =""
        node = self.__head
        for i in range(self.count):
            if output != "": output += ","
            output += f"({i}): {node.data}"
            node = node.next
            return f"[ {output} ], count: {self.count}"

###############################################################################################