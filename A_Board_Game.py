# method 1
# Iterative function to find the minimum cost to traverse from the
# first cell to last cell of a matrix
def findMinCost(cost):

	# M x N matrix
	(M, N) = (len(cost), len(cost[0]))

	# T[i][j] maintains minimum cost to reach cell (i, j) from cell (0, 0)
	T = [[0 for x in range(N)] for y in range(M)]

	# fill matrix in bottom-up manner
	for i in range(M):
		for j in range(N):
			T[i][j] = cost[i][j]

			# fill first row (there is only one way to reach any cell in the
			# first row, that is from its adjacent left cell)
			if i == 0 and j > 0:
				T[0][j] += T[0][j - 1]

			# fill first column (there is only one way to reach any cell in
			# the first column, that is from its adjacent top cell)
			elif j == 0 and i > 0:
				T[i][0] += T[i - 1][0]

			# fill rest of the matrix (there are two way to reach any
			# cell in the rest of the matrix, that is from its adjacent
			# left cell or adjacent top cell)
			elif i > 0 and j > 0:
				T[i][j] += min(T[i - 1][j], T[i][j - 1])//2

	# last cell of T stores min cost to reach destination cell
	# (M-1, N-1) from source cell (0, 0)
	return T[M - 1][N - 1]


if __name__ == '__main__':
    cost = []
    N = int(input())
    for _ in range(N):
        a = list(map(int, input().split(" ")))
        cost.append(a)
    print(findMinCost(cost))



# method 2
N = 4
matrix = [[0,3,9,6], [1,4,4,5], [8,2,5,4], [1,8,5,9]]
element = 0
def traverse(element, matrix, col, row, N):
    arr = col
    index = row
    while True:
        if index == N-1 and arr == N-1:
            break
        elif index == N-1:
            s1 = 1001
            s2 = matrix[arr + 1][index]
        elif arr == N-1:
            s2 = 1001
            s1 = matrix[arr][index+1]
        else:
            s1 = matrix[arr][index+1]
            s2 = matrix[arr+1][index]
        if s1<s2:
            element = element//2+s1
            index = index+1
        elif s1>s2:
            element = element//2+s2
            arr = arr+1
        else:
            element = element//2 + matrix[arr][index+1]
            element = min(traverse(element, matrix, arr+1, index, N), traverse(element, matrix, arr, index+1, N))
            break
    return element
print(traverse(element, matrix, 0, 0, N))
