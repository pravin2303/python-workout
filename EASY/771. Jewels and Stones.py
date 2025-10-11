class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        #return sum(s in jewels for s in stones)
        jewels_set=set(jewels)
        count=0
        for s in stones:
            if s in jewels_set:
                count +=1
        return count
