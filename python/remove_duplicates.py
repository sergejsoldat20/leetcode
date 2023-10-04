class Solution:
    def removeDuplicates(self, nums: list) -> int:
        result = []
        for index in range(len(nums)):
            if nums[index] not in result:
                result.append(nums[index])

        return len(result)


sol = Solution()

print(sol.removeDuplicates([1, 1, 2]))
