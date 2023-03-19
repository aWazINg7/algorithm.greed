
def canJump(nums):
    k = 0
    i = 0
    while i < len(nums):
        if i > k:
            return False
        if i + nums[i] > k:
            k = i + nums[i]
        i += 1
    return True
    # if List[0] >= len(List) - 1:
    #     return True
    # i = 0
    # while i <= len(List):
    #     if i == len(List) - 1:
    #         return False
    #     if List[i] >= len(List) - i - 1:
    #         while len(List) - 1 > i:
    #             List.pop(len(List) - 1)
    #         return canJump(List)       #不能只是canJump(List),必须有return，否则结果不能传出，造成继续循环
    #     i += 1


List = [2, 3, 1, 1, 4]
print(canJump(List))
#class Solution:
#    def canJump(self, nums: List[int]) -> bool:
#        length = len(List) - 1
#        i = 1
#        while i <= length:
#           if List[length - i] >= i:
#                j = 0
#                while j < i:
#                    List.pop(length - j)
#                canJump(self, List)
#            else:
#                i += 1
#    return true
