class Solution(object):
    def isPalindrome(self, s):

        start, end = 0, len(s) - 1

        while start < end:

            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1

            if s[start].isalnum() and not s[end].isalnum():
                end -= 1

            if not s[start].isalnum() and s[end].isalnum():
                start += 1

            if not s[start].isalnum() and not s[end].isalnum():
                start += 1
                end -= 1
        return True


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome(".,"))
