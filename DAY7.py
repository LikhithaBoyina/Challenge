class Solution():
    def search(self, nums, target):
      
        for i in nums:
            if i == target:
                return nums.index(i)
                break
        return -1

nums = list(map(int,input("Enter a list of numbers: ").split()))
target = int(input("Enter a number to be searched in the above list : "))

Sol = Solution()
print(Sol.search(nums,target))