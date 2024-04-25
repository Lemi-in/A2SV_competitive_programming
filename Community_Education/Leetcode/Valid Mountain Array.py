class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if n < 3:
            return False
        
        first, last = 0, n - 1
        
        while first < n - 1 and arr[first] < arr[first + 1]:
            first += 1
        
        while last > 0 and arr[last] < arr[last - 1]:
            last -= 1

        if first > 0:
            if last < n - 1:
                if first == last:
                    return True
        return False
        
