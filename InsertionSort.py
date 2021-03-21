def insertion_sort(num):
    for i in range(len(num)):
        j=i
        while j>0 and num[j-1]>num[j]:
            swap(num,j-1,j)
            j-=1
    return num
def swap(num,i,j):
    temp=num[i]
    num[i]=num[j]
    num[j]=temp
num=[3,9,1010,4,1,5]
print(insertion_sort(num))