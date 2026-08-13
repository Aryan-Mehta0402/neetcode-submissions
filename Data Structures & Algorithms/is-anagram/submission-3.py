class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make two hash maps and check if they are the same
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            map_s[s[i]] = 1 + map_s.get(s[i], 0) 

        for i in range(len(t)):
            map_t[t[i]] = 1 + map_t.get(t[i], 0) 

        return map_s == map_t