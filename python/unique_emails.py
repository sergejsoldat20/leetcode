class Solution(object):
    def numUniqueEmails(self, emails):

        unique_email = set()
        for email in emails:
            local_name = email.split("@")[0].replace('.', '')
            real_local_name = ""
            for symbol in local_name:
                if symbol == '+':
                    break
                real_local_name += symbol

            unique_email.add(real_local_name + '@' + email.split("@")[1])

        print(len(unique_email))


sol = Solution()

sol.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])
