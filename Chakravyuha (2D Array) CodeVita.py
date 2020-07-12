import time
def arr2(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print(end="\n")
    # print('\n')


if __name__ == "__main__":
    t0 = time.time()
    N = int(input())
    chakra = [[0 for i in range(N)] for j in range(N)]
    powerpoints = 1 + (N**2)//11
    pos = [(0,0)]
    counter = 1
    for i in range(N//2):
        row = i
        col = i
        end_col = N-i-1
        end_row = N-i-1
        # for first row
        while(col < end_col):
            chakra[row][col] = counter
            if (counter%11 == 0):
                # powerpoints += 1
                pos.append((row,col))
            counter += 1
            col += 1

        # for last column
        while (row < end_row):
            chakra[row][col] = counter
            if (counter%11 == 0):
                # powerpoints += 1
                pos.append((row,col))
            counter += 1
            row += 1

        # for last row
        end_col = i
        end_row = i
        while (end_col < col):
            chakra[row][col] = counter
            if (counter%11 == 0):
                # powerpoints += 1
                pos.append((row,col))
            counter += 1
            col -= 1

        # for first column
        while (end_row < row):
            chakra[row][col] = counter
            if (counter%11 == 0):
                # powerpoints += 1
                pos.append((row,col))
            counter += 1
            row -= 1
    if (N%2 != 0):
        chakra[N//2][N//2] = counter
    arr2(chakra)
    print("Total Power points : ", len(pos))
    print(*pos)
    t1 = time.time()
    print("Time req to execute code : ",t1-t0)
