class Solution(object):

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0

        # kad jednom predjes index ne treba se vracati na njega samo nastavoto
        # od sledeceg zato sto se ocigledno ne moze krenuti od proslih ako je suma do tog indexa mannja od 0

        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            # total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1


sol = Solution()

print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
