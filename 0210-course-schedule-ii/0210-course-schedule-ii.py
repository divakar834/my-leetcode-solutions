class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, v in prerequisites:
            g[v].append(u)

        deg = [0] * numCourses

        for u in g:
            for v in g[u]:
                deg[v] += 1

        q = deque()

        for i in range(numCourses):
            if deg[i] == 0:
                q.append(i)

        op = []

        while q:
            n = q.popleft()
            op.append(n)

            for i in g[n]:
                deg[i] -= 1

                if deg[i] == 0:
                    q.append(i)

        return op if len(op) == numCourses else []