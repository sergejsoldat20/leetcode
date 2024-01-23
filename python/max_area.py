class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1

        max_area = 0
        while left < right:
                
            h = min(height[left], height[right])
            current_area = h * (right - left)
            max_area = max(current_area, max_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        

        print(max_area)
        return max_area

sol = Solution()
sol.maxArea([ 3, 1, 2, 4, 5])
