class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            #perform 2 sum 
            l = i + 1
            r = len(nums)-1
            while l < r:
                sum  = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else: 
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ret