class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # if list is empty
            return ""

        # Take the first string as starting prefix
        prefix = strs[0]

        # Compare with each other string
        for s in strs[:]:
            # While current string does not start with prefix
            while not s.startswith(prefix):
                # Shorten prefix by removing last char
                prefix = prefix[:-1]
                if prefix == "":
                    return ""   # no common prefix at all
        
        return prefix 
