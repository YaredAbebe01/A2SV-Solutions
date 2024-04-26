class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ke=celsius+273.15
        fa=celsius*1.80+32.00
        ans=[]
        ans.append(ke)
        ans.append(fa)
        return ans
        
