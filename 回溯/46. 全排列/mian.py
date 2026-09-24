class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        used = [False]*len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                    
                backtrack(path)

                used[i] = False
                path.pop()
            
        backtrack(path)#真正的执行函数
        return ans
nums = list(map(int,input().split()))
s = Solution()
print(s.permute(nums))

