class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        processorTime.sort()
        tasks.sort()
        ans = 0
        n = len(tasks)
        
        for i in range(1, len(processorTime) + 1):
            ans = max(ans, processorTime[i - 1] + tasks[n - 1])
            n -= 4    
        return ans

