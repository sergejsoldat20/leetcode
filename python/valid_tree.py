class Solution(object):
    def dfs(self, node, visited, parent, transition_function):
        if node in visited:
            return

        visited.add(node)
        print(node)
        for next in transition_function[node]:
            if next == parent:
                continue
            if next in visited:
                return False

            result = self.dfs(next, visited, node, transition_function)
            if not result:
                return False

        return True

    def validTree(self, n, edges):
       # create transition function

        transitions = {key: set() for key in range(n)}
        print(transitions)
        for transition in edges:
            if transition[0] not in transitions[transition[1]]:
                transitions[transition[1]].add(transition[0])

            if transition[1] not in transitions[transition[0]]:
                transitions[transition[0]].add(transition[1])
        print(transitions)
        visited = set()
        return self.dfs(0, visited, -1, transitions) and len(visited) == n


sol = Solution()
print(sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
