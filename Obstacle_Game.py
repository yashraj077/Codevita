def surround(arr, N, i, j):
    index = []
    obstacles = []
    # case = ''
    while True:
        if i==0 and j==0:
            if arr[i][j+1]=="R":
                index.append([i, j+1])
            elif arr[i+1][j+1]=="R":
                index.append([i+1,j+1])
            elif arr[i+1][j]=="R":
                index.append([i+1,j])
            break
        if i==0 and j==N-1:
            if arr[i][j-1]=="S" or arr[i][j-1]=="L" or arr[i][j-1]=="W" or arr[i][j-1]=="T":
                obstacles.append(arr[i][j-1])
            elif arr[i][j-1]=="R":
                index.append([i,j-1])

            if arr[i+1][j-1]=="S" or arr[i+1][j-1]=="L" or arr[i+1][j-1]=="W" or arr[i+1][j-1]=="T":
                obstacles.append(arr[i+1][j-1])
            elif arr[i+1][j-1]=="R":
                index.append([i+1,j-1])

            if arr[i+1][j]=="S" or arr[i+1][j]=="L" or arr[i+1][j]=="W" or arr[i+1][j]=="T":
                obstacles.append(arr[i+1][j])
            elif arr[i+1][j]=="R":
                index.append([i+1,j])

            break
        if i==N-1 and j==0:
            if arr[i-1][j]=="S" or arr[i-1][j]=="L" or arr[i-1][j]=="W" or arr[i-1][j]=="T":
                obstacles.append(arr[i-1][j])
            elif arr[i-1][j]=="R":
                index.append([i-1,j])

            if arr[i-1][j+1]=="S" or arr[i-1][j+1]=="L" or arr[i-1][j+1]=="W" or arr[i-1][j+1]=="T":
                obstacles.append(arr[i-1][j+1])
            elif arr[i-1][j+1]=="R":
                index.append([i-1,j+1])

            if arr[i][j+1]=="S" or arr[i][j+1]=="L" or arr[i][j+1]=="W" or arr[i][j+1]=="T":
                obstacles.append(arr[i-1][j+1])
            elif arr[i][j+1]=="R":
                index.append([i,j+1])

            break
        if i==N-1 and j==N-1:
            index.append(arr[i-1][j])
            index.append(arr[i-1][j-1])
            index.append(arr[i][j-1])
            break
        if i==0:
            index.append(arr[i][j-1])
            index.append(arr[i+1][j-1])
            index.append(arr[i+1][j])
            index.append(arr[i+1][j+1])
            index.append(arr[i][j+1])
            break
        if i==N-1:
            index.append(arr[i][j-1])
            index.append(arr[i-1][j-1])
            index.append(arr[i-1][j])
            index.append(arr[i-1][j+1])
            index.append(arr[i][j+1])
            break
        if j==0:
            index.append(arr[i-1][j])
            index.append(arr[i-1][j+1])
            index.append(arr[i][j+1])
            index.append(arr[i+1][j+1])
            index.append(arr[i+2][j])
            break
        if j==N-1:
            index.append(arr[i-1][j])
            index.append(arr[i-1][j-1])
            index.append(arr[i][j-1])
            index.append(arr[i+1][j-1])
            index.append(arr[i+1][j])
            break
        else :
            index.append(arr[i-1][j-1])
            index.append(arr[i][j-1])
            index.append(arr[i+1][j-1])
            index.append(arr[i+1][j])
            index.append(arr[i+1][j+1])
            index.append(arr[i][j+1])
            index.append(arr[i-1][j+1])
            index.append(arr[i-1][j])
            break
    return index, obstacles
if __name__ == "__main__":
    N = 4
    # arr = [[0]*N]*N
    arr = [["A","S","L","D"], ["T","R","W","R"], ["R","M","S","R"], ["W","R","R","M"]]
    # print(*arr)
    index, obstacles = surround(arr, N, 3,0)
    print(index, obstacles)
