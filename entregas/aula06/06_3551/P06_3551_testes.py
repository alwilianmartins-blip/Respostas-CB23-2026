
from P06_3551_fila_encadeada import FilaEncadeada
from P06_3551_pilha_encadeada import PilhaEncadeada

def unittest():

    pilha = PilhaEncadeada()

    print("\nTestes da Pilha")
    print(pilha.esta_vazia())
    print(len(pilha))
    
    pilha.push(10)
    pilha.push("Texto")
    pilha.push(True)
    pilha.push(None)
    
    print(pilha.esta_vazia())
    print(len(pilha))
    print(repr(pilha))
    
    print(pilha.topo())
    print(pilha.pop())
    print(pilha.topo())
    print(pilha.pop())
    print(pilha.pop())
    print(pilha.pop())
    print(pilha.esta_vazia())

    # Mais testes da Pilha (Intercalando tipos diferentes e push/pop repetidos)
    pilha.push(3.1415)
    pilha.push([1, 2, 3])
    pilha.push({"chave": "valor"})
    pilha.push(3.1415)
    
    print(len(pilha))
    print(repr(pilha))
    
    print(pilha.pop())
    print(pilha.topo())
    
    pilha.push("novo_topo")
    print(repr(pilha))
    print(len(pilha))
    
    print(pilha.pop())
    print(pilha.pop())
    print(pilha.pop())
    print(pilha.pop())
    print(pilha.esta_vazia())

    print("\nTestes da Fila")
    fila = FilaEncadeada()
    
    print(fila.esta_vazia())
    print(len(fila))
    
    fila.enfileirar("A")
    fila.enfileirar("B")
    fila.enfileirar("C")
    
    print(fila.esta_vazia())
    print(len(fila))
    print(repr(fila))
    
    print(fila.frente())
    print(repr(fila))
    print(fila.desenfileirar())
    print(fila.frente())
    print(fila.desenfileirar())
    
    fila.enfileirar("D")
    fila.enfileirar("E")
    
    print(repr(fila))
    print(len(fila))
    
    print(fila.desenfileirar())
    print(fila.desenfileirar())
    print(fila.desenfileirar())
    print(fila.esta_vazia())

    # Mais testes da Fila (Intercalando enfileirar e desenfileirar intensamente)
    fila.enfileirar(100)
    fila.enfileirar(200)
    
    print(fila.frente())
    print(len(fila))
    
    fila.enfileirar(300)
    print(fila.desenfileirar())
    print(repr(fila))
    
    fila.enfileirar(400)
    fila.enfileirar(500)
    print(len(fila))
    
    print(fila.desenfileirar())
    print(fila.desenfileirar())
    print(fila.frente())
    print(repr(fila))
    
    print(fila.desenfileirar())
    print(fila.desenfileirar())
    print(fila.esta_vazia())
    print(len(fila))
    
    fila.enfileirar("Último")
    print(repr(fila))
    print(fila.frente())
    print(fila.desenfileirar())
    print(fila.esta_vazia())
    print()

 
if __name__ == "__main__":
    unittest()


