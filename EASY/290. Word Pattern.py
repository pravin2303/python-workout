class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word=s.split()
        if len(pattern )!=len(word):
            return False

        c_w={}
        w_c={}
        for ch,word in zip(pattern,word):  
            if(ch in c_w and c_w[ch]!=word)or (word in w_c and w_c[word]!=ch):
                return False

            c_w[ch]=word
            w_c[word]=ch
        return True
