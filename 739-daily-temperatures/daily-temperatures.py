from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        q = deque()

        for idx, val in enumerate(temperatures):
            while q and temperatures[q[-1][1]] < temperatures[idx]:
                x,y = q.pop()
                answer[y] = idx - y 
            q.append((val, idx))
        return answer
