class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        h = arr.index(max(arr))
        if h == 0 or h == n - 1:
            return False   
        for i in range(h):
            if arr[i] >= arr[i + 1]:
                return False      
        for i in range(h, n - 1):
            if arr[i] <= arr[i + 1]:
                return False
        
        return True

            
