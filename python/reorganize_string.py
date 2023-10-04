from collections import defaultdict


class Solution(object):

    def checkForAdjacent(self, word):
        for index in range(len(word) - 1):
            if word[index] == word[index + 1]:
                return False

        return True

    def reorganizeString(self, s):
        characters_showing = {k: 0 for k in set(s)}

        for symbol in s:
            characters_showing[symbol] += 1

        for key, value in characters_showing.items():
            if (value >= (len(s)/2)):
                return ""
            
        first_symbol = dict(sorted(characters_showing, key=lambda item: item[1])).pop()
        second_symbol = sorted(characters_showing, )
        




        print(characters_showing)


Solution().reorganizeString("aaba")
