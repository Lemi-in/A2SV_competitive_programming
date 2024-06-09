class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x, y = 0, len(letters)
        while x < y:
            mid = (x + y) // 2
            if ord(letters[mid]) <= ord(target):
                x = mid + 1
            else:
                y = mid
        if x < len(letters):
            return letters[x]
        else:
            return letters[0]
