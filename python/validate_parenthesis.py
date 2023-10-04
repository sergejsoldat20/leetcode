class Solution:
    def isValid(self, s: str) -> bool:
        brackets_set = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        if len(s) % 2 == 1:
            return False
        closed_unused = []
        stack = []
        for index in range(len(s)):
            if s[index] in brackets_set.values():
                stack.append(s[index])

            else:

                closed_unused.append(s[index])
                if len(stack) > 0 and brackets_set[s[index]] == stack[-1]:
                    stack.pop()
                    closed_unused.pop()

        # print(closed_unused)
        print(len(stack))
        if len(stack) > 0 or len(closed_unused) > 0:
            return False
        return True


sol = Solution()

print(sol.isValid('[([]])'))
