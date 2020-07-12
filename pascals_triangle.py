if __name__ == "__main__":
    arr = [10,4,74,61,8,37,2,35]
    arr.sort()
    arr = arr[-6:]

    c = arr[-1]
    d = arr[-2]
    e = arr[-3]
    b = arr[-4]
    a = arr[-5]
    f = arr[-6]

    result = sum([a,4*b,6*c,4*d,e]) * sum([b,4*c,6*d,4*e,f])
    print(result)
