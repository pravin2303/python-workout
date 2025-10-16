class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                # found a number greater than both
                return True
        return False
