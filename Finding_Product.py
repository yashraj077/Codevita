def n_length_combo(lst, n):

	if n == 0:
		return [[]]

	l =[]
	for i in range(0, len(lst)):

		m = lst[i]
		remLst = lst[i + 1:]

		for p in n_length_combo(remLst, n-1):
			l.append([m]+p)

	return l

def multiply(l, d):

	count = 0
	for i in l:
		mul = 1
		for j in i:
			mul = mul * j
		if (mul%d == 0):
			count += 1
	return count
if __name__ == "__main__":
	N, P, Q = map(int,input().split(","))
	l = list(map(int,input().split(",")))

	d = P*Q
	count = 0
	for i in range(2,N+1):
		count += multiply(n_length_combo(l, i), d)
	print(count)
