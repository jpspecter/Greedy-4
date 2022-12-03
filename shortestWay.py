

class Solution:
    def shortestWay(self, source, target):
        sLen = len(source)
        tLen = len(target)
        count = 1
        sPtr = 0
        tPtr = 0
        map = {}
        for i in range(sLen):
            c = source[i]
            if c not in map:
                map[c] = []
            map[c].append(i)
        
        while (tPtr < tLen):
            tChar = target[tPtr]
            if tChar not in map:
                return -1
            
            li = map[tChar]
            k = self.binarySearch(li, sPtr)
            if k < 0:
                k = -k - 1
            
            if k == len(li):
                count += 1
                sPtr = li[0]
            else:
                sPtr = li[k]
            
            sPtr += 1
            tPtr += 1
        
        return count
    
    def binarySearch(self, li, num):
        low = 0
        high = len(li) - 1
        
        while (low < high):
            mid = (low + high) / 2
            if li[mid] == num:
                return mid
            elif li[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1