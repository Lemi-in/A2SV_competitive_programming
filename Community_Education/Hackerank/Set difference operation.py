if __name__ == '__main__':
    n = int(input())
    english = list(map(int, input().split()))
    m = int(input())
    french = list(map(int, input().split()))
    count = 0
    for num in english:
        if num not in french:
            count += 1
    print(count)
