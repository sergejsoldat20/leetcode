class Solution(object):
    def numIslands(self, grid):

        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         print(grid[i][j])

        # we go in four directions and check if first next is zero or outside

        def find_next(grid, i, j):

            if i + 1 > len(grid) or i + 1:
                return


sol = Solution()

sol.numIslands(0)
