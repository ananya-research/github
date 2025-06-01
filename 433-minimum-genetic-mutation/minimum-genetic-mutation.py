class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        start=startGene
        end=endGene

        bank_set = set(bank)
        if end not in bank_set:
            return -1

        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        genes = ['A', 'C', 'G', 'T']

        while queue:
            curr, steps = queue.popleft()
            if curr == end:
                return steps

            for i in range(8):
                for g in genes:
                    if curr[i] != g:
                        mutation = curr[:i] + g + curr[i+1:]
                        if mutation in bank_set and mutation not in visited:
                            visited.add(mutation)
                            queue.append((mutation, steps + 1))

        return -1
        