N, Y = map(int, input().split())
flag = False

for x in range(N + 1):
	for y in range(N + 1 - x):
		z = N - x - y
		if 10000 * x + 5000 * y + 1000 * z == Y:
			flag = True
			break
	if flag:
		break
if flag:
	print(x, y, z)
else:
	print(-1, -1, -1)
