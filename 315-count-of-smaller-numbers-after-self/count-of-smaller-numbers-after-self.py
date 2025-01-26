class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def sort(left,right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result.append(left[i])
                    small_arr[left[i][0]]+=j
                    i+=1
                else: 
                    result.append(right[j])
                    j+=1

            while i < len(left):
                    result.append(left[i])
                    small_arr[left[i][0]]+=j
                    i+=1

            while j < len(right):
                    result.append(right[j])
                    j+=1

            return result                

        def divide_n_conquer(nums):
             
             if len(nums) <= 1:
                return nums
             
             mid = len(nums) // 2
             left = divide_n_conquer(nums[:mid])
             right = divide_n_conquer(nums[mid:])

             return sort(left,right)

        small_arr = [0] * len(nums)
        divide_n_conquer(list(enumerate(nums)))
        return small_arr 