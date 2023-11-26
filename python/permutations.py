
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # better solution

        result = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            # print(result)
            for perm in perms:
                perm.append(n)
            result.extend(perms)

            nums.append(n)

        return result


sol = Solution()

print(sol.permute([1, 2, 3]))

# import copy
# class Solution:
#     def permute(self, nums):
#         result_list = []
#         def backtracking(numbers, current_order):
#             # print(current_order)
#             if len(current_order) == len(numbers):
#                 result_list.append(current_order)

#             for number in numbers:
#                 if number not in current_order:
#                     print(number)
#                     new_order = copy.deepcopy(current_order)
#                     new_order.append(number)
#                     backtracking(numbers, new_order)

#         # result_list = []
#         for number in nums:
#             backtracking(nums, [number])

#         return result_list
