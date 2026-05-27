class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) == len(t)):
            HashMap_s = {}
            HashMap_t = {}
            for i in range(len(s)):
                if s[i] not in HashMap_s:
                    HashMap_s[s[i]] = 1
                else:
                    HashMap_s[s[i]] += 1
            
            for i in range(len(s)):
                if t[i] not in HashMap_t:
                    HashMap_t[t[i]] = 1
                else:
                    HashMap_t[t[i]] += 1

            if HashMap_s == HashMap_t:
                return True
            else: 
                return False

        else:
            return False