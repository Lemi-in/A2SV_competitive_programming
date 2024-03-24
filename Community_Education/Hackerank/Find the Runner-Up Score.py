if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
 
    arr.sort()
    temp = arr[-1]
    for i in arr[::-1]:  
        if i != temp:
            print(i)
            break
