class Solution:
    def corpFlightBookings(self, bookings, n):
        ans = [0]*n     
        for res in bookings:
            first, last, seats = res
            ans[first - 1] += seats
            if last < n:
                ans[last] -= seats        
        for i in range(1, n):
            ans[i] += ans[i - 1]
        
        return ans
