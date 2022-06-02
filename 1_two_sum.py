# https://leetcode.com/problems/two-sum/

def twoSumMethd1( nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i,j]   
  
def twoSumMethd2( nums, target):
  hashmap = {}
  for i in range (0,len(nums)):
    complement = target - nums[i]
    if complement in hashmap:
        return([i, hashmap[complement]])
    hashmap[nums[i]] = i

nums = [2,7,11,15]
target = 9

print(twoSumMethd1(nums, target))
print(twoSumMethd2(nums, target))