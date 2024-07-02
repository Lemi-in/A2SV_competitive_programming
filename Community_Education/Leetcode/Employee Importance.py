"""
Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {}
        for ep in employees:
            mp[ep.id] = ep
        def dfs(idx):
            ep = mp[idx]
            return ep.importance + sum(dfs(sub) for sub in ep.subordinates)
        return dfs(id)
