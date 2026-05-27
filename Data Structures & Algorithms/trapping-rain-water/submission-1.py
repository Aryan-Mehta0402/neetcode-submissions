class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0]*len(height)
        max_r = [0]*len(height)

        maxl = 0
        for i in range(len(height)):
            if height[i] > maxl:
                max_l[i] = height[i]
                maxl = height[i]
            else:
                max_l[i] = maxl
        
        maxr = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > maxr:
                max_r[i] = height[i]
                maxr = height[i]
            else:
                max_r[i] = maxr
        
        area = 0

        for i in range(len(height)):
            area += max(min(max_r[i], max_l[i]) - height[i], 0)

        return area

        