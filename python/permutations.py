
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def backtracking(numbers: list, current_order: list):
            # print(current_order)
            if len(current_order) == len(numbers):
                return current_order

            for number in numbers:
                if number not in current_order:
                    new_order = current_order
                    new_order.append(number)
                    print(new_order)
                    print("aa")
                    print(current_order)
                    backtracking(numbers, new_order)

        result_list = []
        for number in nums:
            result_list.append(backtracking(nums, [number]))

        return result_list


sol = Solution()

print(sol.permute([1, 2, 3]))
