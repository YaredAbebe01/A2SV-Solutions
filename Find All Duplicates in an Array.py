class Solution:
    def findDuplicates(self, nums):
        seen = set()
        li = []
        for n in nums:
            if n in seen:
                li.append(n)
            else:
                seen.add(n)
        return li
