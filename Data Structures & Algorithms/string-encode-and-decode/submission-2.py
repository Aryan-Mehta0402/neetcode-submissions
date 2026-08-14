class Solution:

    def encode(self, strs: List[str]) -> str:
        # length + # + str
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "$" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            lenn = int(s[i:j])
            start = j+1
            end = start + lenn
            ans.append(s[start: end])
            i = end
        return ans

