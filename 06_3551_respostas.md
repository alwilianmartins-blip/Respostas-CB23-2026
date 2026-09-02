# PILHA SOBRE LISTA ENCADEADA


## push(): Complexidade O(1)
Como acessa diretamente o topo da pilha então ele adiciona um novo elemento em tempo constante

## pop(): Complexidade O(1)
Como acessa diretamente o topo da pilha e remove seu elmento, então ele realiza essa operação em tempo constante

## topo(): Complexidade O(1)
Como acessa diretamente o elemento no topo da pilha, logo 
possui um tempo constante de operação

## esta_vazia(): Complexidade O(1)
Nessa operação é acessado o comprimento da lista e verifica se é 0 ou não, portanto
possui tempo constante de operação

## len(): Complexidade O(1)
Nessa operação é acessado um lugar da memória 
para verificar o comprimento, então possui tempo de execução constante

## repr(): Complexidade O(N)
Para essa operação cada elemento da 
pilha de certo tamanho N é adicionado a uma string, então
a complexidade é O(N)

# FILA CONSTRUÍDA SOBRE A PILHA

## enfileirar(item): Complexidade O(1)
Sua operação é insierir um elemento na fila, 
para isso acessa diretamente um enderço na memória da fila, logo a execução de tempo é constante

## desenfileirar(): Complexidade O(1) amortizada (caso médio) 
Como cada elemento é transferido entre as duas pilhas exatamente uma única vez durante sua existência, o custo total para N elementos é 4N, ao dividir o tempo de N operações o custo médio é O(1)

## frente(): Complexidade O(1) amortizada (caso médio) 
Semelhante à operação desenfileirar(), que tem função auxiliar _transferir(), Como cada elemento é transferido entre as duas pilhas exatamente uma única vez durante sua existência, o custo total para N elementos é 4N, ao dividir o tempo de N operações o custo médio é O(1)

## esta_vazia(): Complexidade O(1)

Como a operação verifica se o comprimento da fila é 0 ou não, a operação é executada em tempo constante

## len(): Complexidade O(1)

Essa operação verifica o valor do atributo comprimento, então essa operação é executada em tempo constante

## repr(): Complexidade O(N)

Como para representar a fila é adicionado cada elmento dela em uma string por vez, então para um Tamanho N são necessários N passos, portanto a complexidade é O(N)