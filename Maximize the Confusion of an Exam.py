class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        leftt = 0
        leftf = 0
        maxt = 0
        maxf = 0
        tcount = 0
        fcount = 0
        
        for right in range(len(answerKey)):
            if answerKey[right] != 'T':
                tcount += 1
            if answerKey[right] != 'F':
                fcount += 1
                
            while tcount > k:
                if answerKey[leftt] != 'T':
                    tcount -= 1
                leftt += 1
                
            while fcount > k:
                if answerKey[leftf] != 'F':
                    fcount -= 1
                leftf += 1
                
            maxt = max(maxt, right - leftt + 1)
            maxf = max(maxf, right - leftf + 1)
        
        return max(maxt, maxf)
        
