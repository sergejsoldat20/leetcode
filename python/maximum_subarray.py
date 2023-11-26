class Solution:
    # def maxSubArray(self, nums: list[int]) -> int:
    #     current_subarray = max_subarray = nums[0]

    #     for num in nums[1:]:
    #         current_subarray = max(num, current_subarray + num)
    #         max_subarray = max(max_subarray, current_subarray)

    #     return max_subarray

    def maxSubArray(self, nums: list[int]) -> int:

        left, right = 0, 0

        max_combination = (nums[0], nums[0])
        print(nums[0:1])
        for i in range(len(nums)):
            right = i + 1
            current_sum = sum(nums[left:right])

            if current_sum < max_combination[1]:
                left = i + 1
                continue

            if current_sum > max_combination[1]:
                max_combination = (nums[left:right], current_sum)

        return max_combination


sol = Solution()

print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
