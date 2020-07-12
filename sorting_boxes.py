def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr


if __name__ == "__main__":
    a = [20,50,30,80,70]
    ans = [20,80,30,50,70]
    k = 2
