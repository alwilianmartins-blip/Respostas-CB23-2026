import random
room = " "
wall = "W"
cheese = "*"

def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

def dfs(m, n, room = " ", wall = " W", cheese = "*"):

    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]


    stack = [(0,0)]
    maze[0][0] = room

    while len(stack) != 0:

        x, y = stack.pop()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Norte, Sul, Oeste, Leste
        random.shuffle(directions) # Embaralha as direções para o labirinto ser aleatório

        for dx, dy in directions:

                nx, ny = x + dx, y+dy 

                if 0 <= nx <m and 0 <= ny < n and maze[2*nx+1][2*ny+1] == wall:

                     stack.append((x,y))

                     stack.append((nx,ny))

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


def find_cheese(maze,visitado = None, x= 1, y = 1, caminho = None):

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
             resultado =  find_cheese(maze, visitado, nx, ny, caminho)

             if resultado is not None:
                  return resultado

    caminho.pop()
    return None



def mostrar_caminho(maze, caminho):


     for item in caminho:
          x, y = item[0], item[1]

          maze[x][y] = "-"

     print_maze(maze)



if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)

    room = " "
    wall = "W"
    cheese = "*"
    maze = dfs(m, n, room, wall ,cheese)
    print('Maze 1')
    print_maze(maze)

    print()

    caminho = find_cheese(maze)

    print("Caminho para o queijo")

    mostrar_caminho(maze, caminho)

    
