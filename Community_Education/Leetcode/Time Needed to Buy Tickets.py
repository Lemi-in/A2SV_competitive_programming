class Solution:
    def timeRequiredToBuy(self, tickets, k):
        n = len(tickets)
        q = deque([i for i in range(n)])
        time = 0
        
        while q:
            person = q.popleft()
            tickets[person] -= 1
            time += 1
            if tickets[person] > 0:
                q.append(person)
            if tickets[k] == 0:
                return time
