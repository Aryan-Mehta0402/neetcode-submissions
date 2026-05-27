class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "!" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        length = ""
        i = 0
        while i < len(s):
            if s[i] != "!" :
                length += s[i]
                print(length)
                i+=1
            else: 
                leng = int(length)
                ans.append(s[i+1: i+leng+1])
                i += leng+1
                length = ""
        return ans