class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min,max=-2**31,2**31-1
        if x<0:
            rev =-int(str(-x)[::-1])
        else:
            rev =int(str(x)[::-1])

        if rev < min or rev > max:
            return 0
        return rev
