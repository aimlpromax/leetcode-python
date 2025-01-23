from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        q = deque()

        for idx, val in enumerate(nums):
            while q and nums[q[-1][1]] < nums[idx]:
                v, i = q.pop()
                result[i] = nums[idx]
            q.append((val, idx))

        for cur in nums:
            while q and nums[q[-1][1]] < cur:
                result[q[-1][1]] = cur
                q.pop()        
        return result