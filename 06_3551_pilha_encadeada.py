class ListaEncadeada:

    """" Implementa Lista Encadeada"""
    


    class _No:
        """"Implementa nó de lista encadeada"""
        def __init__(self, valor, proximo = None):
            self.valor = valor
            self.proximo = proximo

    def __init__(self):
        self.primeirono = None
        self.comprimento = 0

    def __repr__(self):

        """Representação textual legível, do topo para a base.
        Complexidade o(N)"""


        no = self.primeirono
        s = ""
        while no is not None:
            
            s += f" -> {no.valor}" if s else str(no.valor)
            no = no.proximo

        return s


    def __len__(self):

        """Retorna a quantidade de elementos; exige contador mantido incrementalmente.
        complexidade O(1)"""

        return self.comprimento

    def _esta_vazia(self):

        """Retorna True quando não há elementos armazenados.
        complexidade O(1)"""

        if self.comprimento == 0:
            return True
        else:
            return False


    def _topo(self):

        """Retorna o item do topo sem removê-lo; levanta IndexError se a pilha estiver vazia.
        complexidade O(1)"""

        if self.comprimento == 0:
            raise IndexError("A pila está vazia")
        else:
            return self.primeirono.valor
    

    def pop(self):
        """Remove e retorna o item do topo; levanta IndexError se a pilha estiver vazia.
        complexidade O(1)"""

        if self.comprimento == 0:
            raise IndexError("pop from empty list")

        item = self.primeirono.valor
        self.primeirono = self.primeirono.proximo
        self.comprimento -=1 
        return item

    def push(self, valor):

        """Insere um valor no topo da pilha
        Complexidade O(1)"""

        novo_no = self._No(valor, self.primeirono)
        self.primeirono = novo_no
        self.comprimento +=1

