class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count5 = 0
        count10 = 0
        
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                if count5 == 0:
                    return False
                count5 -= 1
                count10 += 1
            elif bill == 20:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        
        return True
