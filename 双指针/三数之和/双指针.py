class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):

            # i 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:
                s = nums[i] + nums[L] + nums[R]

                if s < 0:
                    L += 1

                elif s > 0:
                    R -= 1

                else:
                    ans.append([nums[i], nums[L], nums[R]])

                    L += 1
                    R -= 1

                    # L 去重
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    # R 去重
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        return ans
nums = list(map(int,input().split()))
s = Solution()
print(s.threeSum(nums))
    