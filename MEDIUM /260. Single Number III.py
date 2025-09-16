class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x =0
        for n in nums:
            x ^=n

        diff =x &(-x)
        a=b=0
        for n in nums:
            if n & diff:
                a^=n
            else:
                b^=n

        return [a,b]
