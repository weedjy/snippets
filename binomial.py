q = dict()


def c(n, k):
	if n in q.keys():
		if k in q[n].keys():
			return q[n][k]
	# print("n=", n, "k=", k)
	if k == 0 or k == n:
		return 1
	elif k == 1:
		return n
	elif n == 1:
		return 1
	else:
		if n in q.keys():
			q[n][k] = c(n - 1, k - 1) + c(n - 1, k)
		else:
			q[n] = dict()
			q[n][k] = c(n - 1, k - 1) + c(n - 1, k)
		return q[n][k]

# сколькими способами можно расставить 12+12 шашек на доске 8х8 на черных клетках
print("count = ", c(32, 12)*c(20, 12))
