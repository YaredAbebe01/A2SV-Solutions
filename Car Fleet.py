class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position:
            return 0
        cars = sorted(zip(position, speed), reverse=True)
        n = len(cars)    
        lt = 0     
        for pos, spd in cars:
            time = float(target - pos) / spd
            if time <= lt:
                n -= 1
            else:
                lt = time
        
        return n
