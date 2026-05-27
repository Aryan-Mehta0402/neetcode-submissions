class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        con_str = ""
        for i in range(len(s)):
            if s[i] not in valid_char:
                continue
            else:
                con_str += s[i]
        con_str = con_str.lower()
        
        if con_str == con_str[::-1]:
            return True
        else:
            return False


