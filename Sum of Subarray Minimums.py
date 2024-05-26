class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        
        left = [-1] * n
        right = [n] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans += arr[i] * (i - left[i]) * (right[i] - i)
            ans %= MOD
        
        return ans
