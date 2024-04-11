class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        arr = list(s)
        x , y = 0, n - 1
        while x < y:
            if arr[x] in vowel and arr[y] in vowel:
                arr[x] , arr[y] = arr[y] , arr[x]
                x += 1
                y -= 1
            elif arr[x] in vowel and arr[y] not in vowel:
                y -= 1
            elif arr[x] not in vowel and arr[y] in vowel:
                x += 1
            else:
                x += 1
                y -= 1
        return ''.join(arr)

