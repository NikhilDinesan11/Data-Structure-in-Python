def merge_sort(num):
    if len(num)==1:
            return
    middle_index=len(num)//2
    left_half=num[:middle_index]
    right_half=num[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    i=0
    j=0
    k=0

    while i <len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            num[k]=left_half[i]
            i+=1
        else:
            num[k]=right_half[j]
            j+=1
        k+=1

    while i<len(left_half):
        num[k]=left_half[i]
        k=k+1
        i+=1
    while j<len(right_half):
        num[k]=right_half[j]
        k+=1
        j+=1

num= [2,5,100,-11,4,1]
merge_sort(num)
print(num)