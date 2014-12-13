from random import shuffle, randrange
 
def make_maze(walk_limit, w=16, h=8):
	vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
	ver = [["# "] * w + ['#'] for _ in range(h)] + [[]]
	hor = [["##"] * w + ['#'] for _ in range(h + 1)]
 
	def walk(x, y):
		vis[y][x] = 1
 
		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		shuffle(d)
		for (xx, yy) in d:
			if vis[yy][xx]: continue
			if xx == x: hor[max(y, yy)][x] = "# "
			if yy == y: ver[y][max(x, xx)] = "  "
			walk(xx, yy)
 
	walk(randrange(w), randrange(h))

	grid = [[]]
	for (a, b) in zip(hor, ver):
		grid.append(''.join(a))
		grid.append(''.join(b))
		#print(''.join(a + ['\n'] + b))
	for line in grid:
		print ''.join(line)

	num = [[]]
	for line in grid:
		row = []
		for piece in line:
			if piece != '#':
				row.append(walk_limit)
			else:
				row.append(0)
		printer = ''
		for number in row:
			printer = printer + str(number)
		print printer
		num.append(row)

	return num