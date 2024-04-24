class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapp ={}
        people = []
        for x,y in zip(names,heights):
            mapp[y] = x

        heights.sort(reverse=True)

        for height in heights:
            people.append(mapp[height])
        return people 
