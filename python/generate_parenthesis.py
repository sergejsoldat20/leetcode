import random


class Solution(object):
    def generateParenthesis(self, n):
        print(f"called-{n}")
        if n == 0:
            print("[]")
            return ['']
        parenthesis_list = []

        for index in range(n):
            inside = self.generateParenthesis(index)
            outside = self.generateParenthesis(n - index - 1)
            print(f"inside={inside}-outside={outside}")
            for left in inside:
                for right in outside:
                    parenthesis_list.append(f'({left}){right}')

        return parenthesis_list


def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            parentheses.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    parentheses = []
    backtrack('', 0, 0)
    return parentheses


# Example usage:
n = 3  # Generate balanced parentheses expressions with 3 pairs of parentheses
result = generate_parentheses(n)
for expr in result:
    print(expr)


# sol = Solution()
# parentheses_list = sol.generateParenthesis(3)
# print(f"Generated {len(parentheses_list)} valid combinations:")
# for p in parentheses_list:
#     print(p)
