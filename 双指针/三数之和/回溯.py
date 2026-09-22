class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort   ()    
        ans = []
        path = []

        def backtrack(start):
            if len(path) == 3:
                if sum(path) == 0:
                    ans.append(path.copy())
                return 

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                        continue
            
                path.append(nums[i])
                backtrack(i+1)

                path.pop();

        
        backtrack(0)
        return ans