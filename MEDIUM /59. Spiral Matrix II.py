class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Step 1: Initialize empty n×n matrix
        matrix = [[0] * n for _ in range(n)]

        # Step 2: Define boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        # Step 3: Start filling numbers
        num = 1
        while left <= right and top <= bottom:
            # → Move right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # ↓ Move down
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # ← Move left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # ↑ Move up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix
