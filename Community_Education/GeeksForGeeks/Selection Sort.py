class Solution: 
    def select(self, arr, i):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr, n):
        for i in range(n - 1):
            min_index = self.select(arr, i)
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
