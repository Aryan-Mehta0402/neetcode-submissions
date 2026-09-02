class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = [0]*1001

        for i in range(len(hand)):
            count[hand[i]] += 1
        i = 0
        while i != 1001:
            if count[i] < 0:
                return False
            if count[i] == 0:
                i += 1
            else:
                for j in range(groupSize):
                    count[i+j] -= 1
        return True