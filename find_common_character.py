class Solution(object):
    def commonChars(self, words):
        if not words:
            return []
        com = Counter(words[0])
        for word in words[1:]:
            com &= Counter(word)
        ans = []
        for char, count in com.items():
            ans.extend([char] * count)
        
        return ans
