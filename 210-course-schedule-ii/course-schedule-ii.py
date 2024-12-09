class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)

        ans=[]

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

       

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True  # Already processed; no need to visit again
            elif state == VISITING:
                return False  # Found a cycle

            states[node] = VISITING  # Mark the node as being visited

            for nei in g[node]:  # Explore all neighbors (prerequisites)
                if not dfs(nei):  # If a cycle is detected in any neighbor, return False
                    return False

            states[node] = VISITED  # Mark the node as fully processed
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):  # If a cycle is found for any course, return False
                return []
        
        return ans
        