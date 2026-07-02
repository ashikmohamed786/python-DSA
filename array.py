# arr=[1,2,3,4,5,6,7,8,9,0]
# arr.insert(6,11)
# print(arr)
# arr[7]=12
# print(arr)
# print(sum(arr))
# str=['apple','orange','bike','bus','car','grapes','boy','girl']
# str.insert(5,'kings')
# print(str)
# str[7]='Asik'
# print(str)
# print(len(str))

# arr=[1,2,3,4,5,6]
# target=10
# left=0
# right=len(arr)-1

# while left < right:
#     total=arr[left]+arr[right]
#     if total==target:
#         print("found",arr[left],arr[right])
#         break
#     elif total<target:
#         left+=1
#     else:
#         right-=1

nums=[-1,0,1,2,-1,-4]
nums.sort()
result = []
n = len(nums)
for i in range(n - 2):
 if i > 0 and nums[i] == nums[i - 1]:
    continue
    left, right = i + 1, n - 1
while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
result