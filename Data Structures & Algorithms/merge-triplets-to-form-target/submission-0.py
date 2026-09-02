class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        best = [0, 0, 0]

        for triplet in triplets:
            if (triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                continue

            best[0] = max(best[0], triplet[0])
            best[1] = max(best[1], triplet[1])
            best[2] = max(best[2], triplet[2])

        return best == target
