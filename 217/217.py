#Time Limit Exceeded
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        for i in nums:
            if nums.count(i) >= 2:
                return True
        return False

#Runtime: 68 ms
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        nums.sort()
        for i in range(0, len(nums)):
            if i + 1 in range(0, len(nums)) and nums[i] == nums[i + 1]:
                return True
        return False

#Runtime: 52 ms
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        nums_dict = {}
        for i in nums:
            try:
                nums_dict[i] +=1
                return True
            except:
                nums_dict[i] = 1
        return False
