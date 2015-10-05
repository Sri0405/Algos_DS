class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        if s =="" or s ==" ":
            return 0
        parts = s.split(" ")
        length = parts.__len__()

        while(parts[length-1]==""):
            length=length-1
        return parts[length-1].__len__()

Solution().lengthOfLastWord("a b ")