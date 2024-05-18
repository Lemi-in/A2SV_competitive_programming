class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        x = sorted(point[0] for point in points)
        width = 0
        for i in range(1, len(x)):
            width = max(width, x[i] - x[i - 1])
        
        return width
