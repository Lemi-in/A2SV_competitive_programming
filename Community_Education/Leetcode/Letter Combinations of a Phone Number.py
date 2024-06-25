class Solution(object):
    def letterCombinations(self, digits):
        tel = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        if not digits: return []

        def dfs(index, path, res):
            if index == len(digits):
                res.append(path)
                return
            for letter in tel[int(digits[index])]:
                dfs(index + 1, path + letter, res)

        res = []
        dfs(0, "", res)
        return res
