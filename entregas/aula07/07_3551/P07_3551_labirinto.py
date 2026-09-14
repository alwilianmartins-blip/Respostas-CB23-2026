import random


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

def dfs(m, n, room = " ", wall = "W", cheese = "."):

    """Cria um labirinto perfeito de modo iterativo
    Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    


    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]


    stack = [(0,0)]
    maze[0][0] = room

    while len(stack) != 0: #o laço é executado até que a pilha não esteja vazia

        x, y = stack.pop()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Norte, Sul, Oeste, Leste
        random.shuffle(directions) # Embaralha as direções para o labirinto ser aleatório

        for dx, dy in directions:
                
                nx, ny = x + dx, y+dy # move o ponto para Norte, Sul, Leste ou Oeste

                if 0 <= nx <m and 0 <= ny < n and maze[2*nx+1][2*ny+1] == wall: #verifica que os índices estão nos limites e se o ponto visitado é uma parede

                     stack.append((x,y)) #adiciona na pilha o último ponto visitado

                     stack.append((nx,ny)) #adiciona na pilha o último ponto

                     maze[2*x+1+dx][2*y+1+dy] = room

                     maze[2*nx+1][2*ny+1] = room

                     break
                

    while True:
         i = int(random.uniform(0,2*m))
         j = int(random.uniform(0,2*n))

         if maze[i][j] == room:
              maze[i][j] = cheese
              break

    return maze


def find_cheese(maze,wall = "W", cheese = ".", visitado = None, x= 1, y = 1, caminho = None):

    if caminho is None:
             caminho = []

    if visitado is None:
         visitado = set()

    if maze[x][y] == wall or (x, y) in visitado:
        return None

    visitado.add((x, y))
    caminho.append((x, y))
     
    if maze[x][y] == cheese:
            return caminho
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Norte, Sul, Oeste, Leste
    random.shuffle(directions) # Embaralha as direções para o labirinto ser aleatório

    for dx, dy in directions:
        nx, ny = x + dx, y+dy

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
             resultado =  find_cheese(maze, wall, cheese, visitado, nx, ny, caminho)

             if resultado is not None:
                  return resultado

    caminho.pop()
    return None



def mostrar_caminho(maze, caminho, marcacao = "-"):


     for item in caminho:
          x, y = item[0], item[1]

          maze[x][y] = marcacao

     print_maze(maze)



if __name__ == '__main__':
    m, n = 10, 14  # Grid size

    room = " "
    wall = "W"
    cheese = "*"
    maze = dfs(m, n, room, wall ,cheese)
    print('Maze 1')
    print_maze(maze)

    print()

    caminho = find_cheese(maze, wall, cheese)

    print("Caminho para o queijo Maze 1")

    mostrar_caminho(maze, caminho, "&")

    #Segundo Teste
    print()
    
    room2 = " "
    wall2 = "X"
    cheese2 = "9"
    maze2 = dfs(m, n, room2, wall2 ,cheese2)

    print('Maze 2')

    print_maze(maze2)
    print()

    print("Caminho 2 para o queijo \n")

    caminho2 = find_cheese(maze2, wall2, cheese2)

    mostrar_caminho(maze2, caminho2, 6)
