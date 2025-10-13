class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=s.split()
        reversed_words=[i[::-1]for i in word]
        return " ".join(reversed_words)
