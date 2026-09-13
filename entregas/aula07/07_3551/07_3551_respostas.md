# Resposta da Questão 2


Para encontrar o queijo, foi utilizado um algoritmo 
de forma recursiva e de busca em profundidade. Essa estratégia faz com que se o algoritmo não encontrar o queijo em um caminho, ele para e retorna ao passo anterior, realizando buscas recursssivas até encontrar o queijo, caso ele não existir retorna "None".

Foi preferível usar a busca em profundidade pois a busca em largura precisaria armazenar todas as ramificações simulâneas atuais. Outrossim, já que o objetivo é achar um caminho, sem importar o tamanho, então a busca em profundidade é melhor para economizar memória.

A função "find_cheese" inicia com a matriz maze, as coordenadas iniciais x = 1 e y = 1, e os caminhos visitados e encontrados iniciam-se vazios.

Caso o caminho seja None, é atribuido a ele uma lista vazia, e para os pontos visitados, caso ele seja None atribuimos a ele um conjunto vazio. Caso a coordenada atual seja uma "Wall" ou o ponto já foi visitado, o sistem aignora. 

Usando a lista directions somamos as coordenadas atuais posições cartesianas para andar com ele para norte, sul, leste e oeste. Para cada um desses movimentos possíveis, testamos todos os casos, e se não houver "IndexError", a função chama ela mesma com a variável "resultado" para achar um novo caminho, se ele não for vazio é retornado o "resultado".

O comando "caminho.pop()" remove a coordeanada atual do caminho e a função retorna None sinalizando à chamada anterior que deve recuar e testar outra direção possível.

