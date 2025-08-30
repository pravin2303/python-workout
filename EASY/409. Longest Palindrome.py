class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char =set()
        length =0

        for ch in s:
            if ch in char:
                char.remove(ch)
                length +=2
            else:
                char.add(ch)
        if char:
            length +=1

        return length
