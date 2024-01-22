# class Solution(object):
#     def numIslands(self, grid):
#         grid = [
#             ["1", "1", "1", "1", "0"],
#             ["1", "1", "0", "1", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "0", "0", "0"]
#         ]

#         row = len(grid)
#         col = len(grid)

#         def dfs(visited, i, j):
#             if i > len(grid) - 1 or j > len(grid[0]) - 1 or i < 0 or j < 0 or (i, j) in visited:
#                 return

#             if grid[i][j] == "0":
#                 return

#             # if (i, j) not in visited:
#             visited.add((i, j))

#             dfs(visited, i + 1, j)
#             dfs(visited, i - 1, j)
#             dfs(visited, i, j + 1)
#             dfs(visited, i, j - 1)

#         ones_set = set()
#         counter = 0

#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == "1":
#                     ones_set.add((i, j))

#         while len(ones_set) > 0:
#             i, j = ones_set.pop()
#             visited_set = set()
#             dfs(visited_set, i, j)
#             ones_set = ones_set - visited_set
#             counter += 1

#         return counter


# sol = Solution()

# print(sol.numIslands(0))
# bolje rjesenje
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        def dfs(i, j):
            if i > len(grid) or j > len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1

        return counter


sol = Solution()

print(sol.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
      "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
