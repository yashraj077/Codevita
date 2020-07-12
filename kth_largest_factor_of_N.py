if __name__ == "__main__":
    a, b = map(int,input("Enter value of N, k : ").split())
    arr = []
    for i in range(1,(a+1)):
        if (a%i==0):
            arr.append(i)
    try:
        print(arr[-b])
    except:
        print(arr[0])