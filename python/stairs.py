class Stairs:
    def __init__(self):
        self.map = dict()

    def climb_stairs(self, n: int) -> int:
        # return self.backtracking(0, n)
        return self.backtracking(n)

    def backtracking(self, n):
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n in self.map.keys():
            return self.map[n]
        counts = self.backtracking(n - 1) + self.backtracking(n - 2)
        self.map[n] = counts
        return counts

    # def backtracking(self, count, max_counts):

    #     if count > max_counts:
    #         return 0

    #     elif count == max_counts:
    #         return 1

    #     else:
    #         return self.backtracking(count + 1, max_counts) + self.backtracking(count + 2, max_counts)


sol = Stairs()
print(sol.climb_stairs(13))
