class Solution(object):

    def longestPalindromeForSingleSymbol(self, s, left, right):

        while left > 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        return left, right

    def longestPalindrome(self, s):
        # define longest palindrome
        longest_pal = ""

        # expand around center

        if len(s) % 2 == 1:
            for index in range(len(s)):
                left = index
                right = index

                left, right = self.longestPalindromeForSingleSymbol(
                    s, left, right)
                
                
                new_str = s[left:right]
                if len(new_str) > len(longest_pal):
                    longest_pal = new_str

        else:
            for index in range(len(s)):

                left = index
                right = index + 1

                left, right = self.longestPalindromeForSingleSymbol(
                    s, left, right)
                print(left, right)
                new_str = s[left:right]
                if len(new_str) > len(longest_pal):
                    longest_pal = new_str
        return longest_pal


# str_ex = "alobreee"

# print(str_ex[1:4])

sol = Solution()

print(sol.longestPalindrome("babad"))
print("babad"[0:0])
