# PILHA SOBRE LISTA ENCADEADA


## push(): Complexidade O(1)
Como acessa diretamente o topo da pilha então ele adiciona um novo elemento em tempo constante

## pop(): Complexidade O(1)
Como acessa diretamente o topo da pilha e remove seu elemento, então ele realiza essa operação em tempo constante

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
Sua operação é inserir um elemento na fila, 
para isso acessa diretamente um endereço na memória da fila, logo a execução de tempo é constante

## desenfileirar(): Complexidade O(1) amortizada (caso médio) 
Numa chamada isolada, se a fila_saida estiver vazia e a fila_entrada tiver M elementos, a operação precisa transferir todos os M elementos (um pop e um push por elemento) antes de poder desenfileirar, o que custa O(M), ou seja, O(N) no pior caso.

Porém, cada elemento passa no máximo 4 vezes por uma operação de custo O(1) ao longo de toda a sua existência na fila: 1) push ao entrar em fila_entrada, 2) pop de fila_entrada na transferência, 3) push em fila_saida na transferência, e 4) pop de fila_saida ao ser desenfileirado. Como cada elemento é transferido entre as duas pilhas exatamente uma única vez durante sua existência, o custo total para N elementos é 4N, ao dividir o tempo de N operações o custo médio é O(1)

## frente(): Complexidade O(1) amortizada (caso médio) 
Semelhante à operação desenfileirar(), que tem função auxiliar _transferir(), Como cada elemento é transferido entre as duas pilhas exatamente uma única vez durante sua existência, o custo total para N elementos é 4N, ao dividir o tempo de N operações o custo médio é O(1)

## esta_vazia(): Complexidade O(1)

Como a operação verifica se o comprimento da fila é 0 ou não, a operação é executada em tempo constante

## len(): Complexidade O(1)

Essa operação verifica o valor do atributo comprimento, então essa operação é executada em tempo constante

## repr(): Complexidade O(N)

Como para representar a fila é adicionado cada elemento dela em uma string por vez, então para um tamanho N são necessários N passos, portanto a complexidade é O(N)