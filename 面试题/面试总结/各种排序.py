
import time
import sys

sys.setrecursionlimit(1000000)
def cal_time(func):
    def waraper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('%s消耗的时间是:%s' % (func.__name__, t2-t1))
        return res
    return waraper




#### 冒泡排序
### 时间复杂度: O(n^2)  空间复杂度: O(1)
@cal_time
def Bubble_Sort(li):
    for i in range(len(li)):
        # i = 0 | i =1
        for j in range(len(li) - i - 1):  ## j = 0  j = 1
            if li[j] > li[j+1]:  ## li[0] =7 li[1] = 5 => 7>5 | li[1]=7 > li[2] = 4
                li[j], li[j+1] = li[j+1], li[j] ## li = [5,7,4,6,3,8,2,9,1] | li = [5,4,7,6,3,8,2,9,1]


### 选择排序
### 时间复杂度: O(n^2) 空间复杂度: O(1)
@cal_time
def select_sort(li):

    for i in range(len(li)-1):
        minLoc = i  # minLoc = 0
        for j in range(i+1, len(li)-1): # j = 1   j = 2

            if li[j] < li[minLoc]: ## li[1]=5 < li[0] = 7 | li[2] < li[0] => 4< 5
                li[j], li[minLoc] = li[minLoc], li[j]  ## li = [4,7,5,6,3,8,2,9,1]

### 插入排序
### 时间复杂度: O(n^2) 空间复杂度:O(1)
@cal_time
def insert_sort(li):

    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and  tmp < li[j]:
            li[j+1] = li[j]
            j = j - 1

        li[j+1] = tmp



#### 快速排序
#### 时间复杂度: O(nlgn) 空间复杂度: O(1)
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right  and li[right] > tmp:
            right = right - 1
        li[left] = li[right]
        while left < right and li[left] < tmp:
            left = left + 1
        li[right] = li[left]
    li[left] = tmp
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li, left, right):
    _quick_sort(li, left, right)


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i = i + 1
        else:
            ltmp.append(li[j])
            j = j + 1

    while i <= mid:
        ltmp.append(li[i])
        i = i + 1

    while j <= high:
        ltmp.append(li[j])
        j = j + 1

    li[low:high+1] = ltmp

### 时间复杂度: O(nlgn) 空间复杂度: O(n)
def mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2

        mergesort(li, low, mid)
        mergesort(li, mid+1, high)

        print("分解之前:", li[low:high+1])
        merge(li, low, mid, high)
        print('分解之后:', li[low:high+1])

li = [10,4,6,3,8,2,5,7]

mergesort(li, 0, len(li)-1)



# li = [7,5,4,6,3,8,2,9,1]
import random
#
# li = list(range(1,100000))
# random.shuffle(li)
#
# Bubble_Sort(li)
#
# li = list(range(1,100000))
# random.shuffle(li)
#
# insert_sort(li)

# li = list(range(1,10000000))
# random.shuffle(li)
#
# quick_sort(li, 0 , len(li)-1)
# print(li)






