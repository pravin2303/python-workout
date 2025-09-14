class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filter=''.join(ch.upper()for ch in s if ch.isalnum())
        left,right=0,len(filter)-1
        while left<right:
            if filter[left]!=filter[right]:
                return False
            left +=1
            right -=1
        return True
   
