import importlib

modulo = importlib.import_module("06_3551_pilha_encadeada")
PilhaEncadeada = modulo.ListaEncadeada


class FilaEncadeada:


    """Inicia o Módulo Fila Encadeada"""

    def __init__(self):
        self.fila_entrada = PilhaEncadeada()
        self.fila_saida = PilhaEncadeada()

    def esta_vazia(self):
         """Retorna True quando não há elementos armazenados.
         Complexidade O(1)"""

         return self.fila_entrada._esta_vazia() and self.fila_saida._esta_vazia()


    def enfileirar(self, item):

        """Insere o item no fim da fila
        Complexidade O(1)"""

        self.fila_entrada.push(item)

    def _transferir(self):

        """Metodo Auxiliar interno"""

        if self.fila_saida._esta_vazia():
                    while not self.fila_entrada._esta_vazia():
                        elemento = self.fila_entrada.pop()
                        self.fila_saida.push(elemento)


    def desenfileirar(self):

        """"Remove e retorna o item da frente; levanta IndexError se a fila estiver vazia.
        Complexidade O(1) amortizada (caso médio)
"""

        self._transferir()
        
        if self.fila_saida._esta_vazia():
            raise IndexError("A fila está vazia")

        return self.fila_saida.pop()

    def frente(self):

         """Retorna o item da frente sem removê-lo; levanta IndexError se a fila estiver vazia.
         Complexidade O(1) amortizada (caso médio)
"""

         self._transferir()

         if self.fila_saida._esta_vazia():
              raise IndexError("Fila Vazia")

         return self.fila_saida._topo()

    def __len__(self):

         """Retorna a quantidade de elementos da fila.
         Complexidade O(1)"""

         return len(self.fila_entrada) + len(self.fila_saida)

    def __repr__(self):
        """Representação textual legível, da frente para o fim. Complexidade O(N)"""
        return f"Frente (Saída): [{repr(self.fila_saida)}] | Fim (Entrada): [{repr(self.fila_entrada)}]"
###