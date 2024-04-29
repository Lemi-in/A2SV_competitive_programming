if __name__ == '__main__':
    n = int(input())
    english = list(map(int, input().split()))
    m = int(input())
    french = list(map(int, input().split()))
    
    count = 0
    for num in english:
        if num in french:
            count += 1
            
    count2 = 0
    for num in english:
        if num not in french:
            count2 += 1
            
    count3 = 0
    for num in french:
        if num not in english:
            count3 += 1
            
    print( count + count2 + count3)
