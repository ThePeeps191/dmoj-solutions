n, m = input().split()
n, m = int(n), int(m)

grid = [list(input()) for _ in range(n)]

def swap(grid, n, m):
	for row in range(n):
		for col in range(m):
			if grid[row][col] == "o" and grid[(row + 1) % m][col] == ".":
				grid[row][col], grid[(row + 1) % m][col],  = grid[(row + 1) % m][col], grid[row][col]

for _ in range(100):
	swap(grid, n, m)

grid_str = [''.join(r) for r in grid]

print("\n".join(grid_str))