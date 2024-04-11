class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l, r = 0, n - 1
        size = 0
        
        while l <= r:
            curr = people[l] + people[r]
            if curr > limit:
                size += 1
                r -= 1

            else:
                size += 1
                l += 1
                r -= 1

        return size
