class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            str1 = {}
            str2 = {}
            for i in range(len(s)):
                if s[i] in str1:
                    str1[s[i]]=str1[s[i]]+1
                    continue
                str1[s[i]]=1
            for i in range(len(t)):
                if t[i] in str2:
                    str2[t[i]]=str2[t[i]]+1
                    continue
                str2[t[i]]=1
            for c in str1:
                if str1[c] != str2.get(c,0):
                    return False
            return True
        return False
