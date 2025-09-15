lass Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for num in nums:
            res +=[cur +[num]for cur in res]
        return res

