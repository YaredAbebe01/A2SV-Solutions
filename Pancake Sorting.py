class Solution:
    def pancakeSort(self, arr):
        ans = []
        n = len(arr)
        for i in range(n, 1, -1):
            j = arr.index(i)
            if j != i - 1:
                if j != 0:
                    arr[:j + 1] = reversed(arr[:j + 1])
                    ans.append(j + 1)
                arr[:i] = reversed(arr[:i])
                ans.append(i)
        return ans
