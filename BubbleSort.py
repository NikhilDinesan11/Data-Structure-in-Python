def bubble_sort(nums):

    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                swap(nums,j,j+1)
    return nums
def swap(nums,i,j):
    temp = nums[i]
    nums[i]=nums[j]
    nums[j]=temp
a=[4,5,2,3,7]
print(bubble_sort(a))