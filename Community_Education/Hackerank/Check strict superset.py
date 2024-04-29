if __name__ == "__main__":
    A = set(map(int, input().split()))
    n = int(input())
    itIs = True
    for _ in range(n):
        subSet = set(map(int, input().split()))
        if not all(elem in A for elem in subSet) or len(A) <= len(subSet):
            itIs = False
            break
    
    print(itIs)
