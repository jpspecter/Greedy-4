#Time: O(n)
#Space: O(1)
#Program ran on leetcode successfully

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        res = self.check(tops, bottoms, tops[0])
        if res != -1:
            return res
        return self.check(tops, bottoms, bottoms[0])
    
    def check(self, tops, bottoms, num):
        tCount = 0
        bCount = 0
        for i in range(len(tops)):
            if tops[i] != num and bottoms[i] != num:
                return -1
            if tops[i] != num: 
                tCount += 1
            if bottoms[i] != num:
                bCount += 1
            
        return min(tCount, bCount)
        