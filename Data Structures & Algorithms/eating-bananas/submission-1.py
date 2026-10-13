class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # can calculate if k is either 1 or the max int of the array w linear time
        # brute force is checking all the possible k values from 1 to max(piles)
        # leads us to our optimal solution which is binary search
        # take max(piles) - 1 / 2, this is our middle value for binary search
        # check if koko can finish the banans in time. 
        # if not, search the second half
        # if yes, search the first half
        # store how many bananas he can eat w a variable, and take the min every time we try a new k value
        # when the loop ends, we have our k value


        bestEatingSpeed = max(piles)
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            kvalue = mid
            kEatingSpeed = 0
            # calculate how many bananas koko can eat in time

            for bananas in piles:
                kEatingSpeed += math.ceil(bananas / mid)

            # check if koko finsihed in time
            if kEatingSpeed <= h:
                # finsihed in time good job.
                right = mid - 1
                bestEatingSpeed = min(bestEatingSpeed, mid)
            else:
                # fat tubby didnt eat enough
                left = mid + 1

        return bestEatingSpeed


            

        

        