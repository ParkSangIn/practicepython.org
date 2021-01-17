def check_number(l, n):
    return n in l

def binary_search(l, n):
    if len(l) % 2 == 0:
        if l[len(l)//2] == n:
            return True
        elif l[len(l)//2] > n:
            return binary_search(l[:len(l)//2],n)
        else:
            return binary_search(l[len(l)//2:],n)   

    else:
        if len(l) == 1:
            if l[0] == n:
                return True
            else:
                return False

        if l[len(l)//2] == n:
            return True
        elif l[len(l)//2] > n:
            return binary_search(l[:len(l)//2],n)
        else:
            return binary_search(l[(len(l)//2)+1:],n)

if __name__ == "__main__":
    li = [x for x in range(0,10,2)]
    print(li)

    n = int(input("Enter a number : " ))

    print("normal :")
    if check_number(li,n):
        print("{0} is in list.".format(n))
    else:
        print("{0} is not in list.".format(n))

    print("binary_search : ")
    if binary_search(li,n):
        print("{0} is in list.".format(n))
    else:
        print("{0} is not in list.".format(n))

