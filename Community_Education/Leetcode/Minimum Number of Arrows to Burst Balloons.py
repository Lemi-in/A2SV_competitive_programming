class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        print(points)
        
        arrow_pos = points[0][1] 
        arrow_count = 1 
        for i in range(1, len(points)):
            if arrow_pos >= points[i][0]:
                continue
            else:
                arrow_count += 1
                arrow_pos = points[i][1]
        
        return arrow_count
