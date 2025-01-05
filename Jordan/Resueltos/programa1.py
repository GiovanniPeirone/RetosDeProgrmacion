#nums = [2,7,11,15]
#target = 9

#nums = [3,2,4]
#target = 6

nums = [3, 3]
target = 6

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in nums:
        for j in nums:
            print("j es: ", j)
            if j + i == target and nums.index(i) != nums.index(j):
                return print([nums.index(i), nums.index(j)])
            else:
                continue

twoSum(nums, target)

#https://leetcode.com/problems/two-sum/description/

#Completado 66% Two sum
