class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        while True:
            result = s.replace("[]", "").replace("{}", "").replace("()", "").replace(" ","")
            if result == s:
                break
            s = result
        if len(result) == 0:
            return True
        else:
            return False


