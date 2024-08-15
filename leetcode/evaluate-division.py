from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        
        # 그래프 생성
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        # DFS 탐색
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, value in graph[start].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * value
            
            return -1.0
        
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        
        return results

# 입력 데이터
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# Solution 객체 생성 및 메서드 호출
solution = Solution()
result = solution.calcEquation(equations, values, queries)

# 결과 출력
print(result)
