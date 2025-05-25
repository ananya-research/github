class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph=defaultdict(list)

        count=0

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited=set()

        def dfs(i):
            stack=[]
            stack.append(i)
            
            while stack:
                node=stack.pop()
                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
            

        return count

        