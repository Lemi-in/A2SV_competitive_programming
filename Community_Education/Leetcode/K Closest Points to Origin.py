class Solution:
    def kClosest(self, points, k):
        ans = []
        for point in points:
            d = ((point[0]**2) + (point[1]**2)) ** 0.5
            ans.append((point, d))

        ans.sort(key=lambda x: x[1])
        return [point for point, d in ans[:k]]
