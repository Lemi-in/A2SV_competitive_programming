class Solution:
    def numRabbits(self, answers):
        n = len(answers)
        ans = 0
        mapp = {}
        for i in range (n):
            try:
                mapp[answers[i]] += 1
            except:
                mapp[answers[i]] = 1
        for x in mapp:
            while mapp[x] >= x+1:
                print(ans, "ans at ",x)
                ans += (x+1)
                mapp[x] = mapp[x] - (x+1)
            else:
                if mapp[x] > 0:
                    ans += (x+1)
        return ans
