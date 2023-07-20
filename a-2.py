N = int(input())

grid = []
for _ in range(N):
    row = input()
    grid.append(row)

outer_cells = []
for i in range(N):
    outer_cells.append((0,i))
    outer_cells.append((N-1,i))
for i in range(1,N-1):
    outer_cells.append((i,0))
    outer_cells.append((i,N-1))

shifted_grid = [[0]*N for _ in range(N)]
for i in range(len(outer_cells)):
    current_cell = outer_cells[i]
    next_cell = outer_cells[(i+1) % len(outer_cells)]
    shifted_grid[next_cell[0]][next_cell[1]] = grid[current_cell[0]][current_cell[1]]

for row in shifted_grid:
    print(''.join(row))