class Solution(object):
    def twoSum(self, numbers: list, target):
        passed_map = {}
        for i in range(len(numbers)):
            if target - numbers[i] in passed_map.keys():
                return [passed_map.get(target - numbers[i]) + 1, i + 1]
            passed_map[numbers[i]] = i


sol = Solution()
print(sol.twoSum([0, 0, 3, 4], 0))

# class Solution(object):
#     def twoSum(self, numbers: list, target):
#         map = {}
#         for i, num in enumerate(numbers):
#             # print(i, num)
#             if target - num in map:
#                 return [map[target - num] + 1, i + 1]
#             map[num] = i
