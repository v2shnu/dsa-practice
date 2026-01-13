def sortedSquares(nums):
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        sortednums = sorted(nums)
        return sortednums
