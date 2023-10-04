class Solution(object):

    def lengthOfLongestSubstring(self, s):
        # answer
        max_substr_len = 0

        # stores current index of character
        index_of_symbol = {}

        left = 0

        for right in range(len(s)):

            if s[right] in index_of_symbol:
                left = max(index_of_symbol[s[right]])

            max_substr_len = max(max_substr_len, right - left + 1)
            index_of_symbol[s[right]] = right + 1

        return max_substr_len


sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))


#  def lengthOfLongestSubstring(self, s):
#         # answer
#         max_substr_len = 0
#         set_of_characters = set()
#         # stores current index of character
#         index_of_symbol = {}

#         left = 0

#         for right in range(len(s)):

#             if s[right] in index_of_symbol:
#                 left = max(index_of_symbol[s[right]], left)

#             max_substr_len = max(max_substr_len, right - left + 1)
#             index_of_symbol[s[right]] = right + 1

#         return max_substr_len


# sol = Solution()

# print(sol.lengthOfLongestSubstring("abcabcbb"))
