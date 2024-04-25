class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        #first we flip the image horizontally
        for row in image:
            left, right = 0, len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left] 
                left += 1
                right -= 1

        #and after fliping , we invert the fliped image
        for i in range(n):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
