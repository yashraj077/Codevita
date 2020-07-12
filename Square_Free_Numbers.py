def check_perfect_squares(num):
    sq_root = num**(0.5)
    if int(sq_root)-sq_root==0.0:
        return 0
    else:
        return 1

def find_divide(num):
    temp = []
    for i in range(1,num):
        if num%i==0:
            if check_perfect_squares(i)==1:
                temp.append(i)
    return temp

if __name__ == "__main__":
    a = int(input())
    print(find_divide(a))
    # print(ntemp)