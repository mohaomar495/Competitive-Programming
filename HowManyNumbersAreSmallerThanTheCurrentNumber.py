class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in range(len(nums)):
            for x in range(len(nums)):
                if nums[x] < nums[i]:
                    arr[i] += 1
                else:
                    arr[i] += 0
        return arr
