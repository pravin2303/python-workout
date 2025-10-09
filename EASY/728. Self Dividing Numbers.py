class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for num in range(left, right + 1):
            n = num
            divisible = True
            while n > 0:
                digit = n % 10
                if digit == 0 or num % digit != 0:
                    divisible = False
                    break
                n //= 10
            if divisible:
                result.append(num)
        return result
