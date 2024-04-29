from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = defaultdict(list)

    for i in range(1, n + 1):
        word = input()
        a[word].append(i)

    for _ in range(m):
        word = input()
        if word in a:
            print(" ".join(map(str, a[word])))
        else:
            print(-1)
