class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, path, total):
            # Base condition
            if len(path) == k and total == n:
                result.append(path[:])
                return
            if len(path) > k or total > n:
                return  # prune invalid paths

            # Explore numbers 1 to 9
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()  # backtrack

        backtrack(1, [], 0)
        return result
        
