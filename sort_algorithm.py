# coding=utf8

def InsertSort(array_a, n):
    for i in range(1, n):
        temp = array_a[i]
        j = i - 1
        while temp < array_a[j] and j >= 0:
            array_a[j + 1] = array_a[j]  # 如果小于其前驱，则从后往前寻找插入位置并后移。
            j -= 1
        array_a[j + 1] = temp
    return array_a


def ShellSort(array_a, n):
    dk = n / 2
    while dk >= 1:
        for i in xrange(0, dk):
            for j in range(i + dk, n, dk):
                temp = array_a[j]
                k = j - dk
                while temp < array_a[k] and k >= 0:
                    array_a[k + dk] = array_a[k]  # 如果小于其前驱，则从后往前寻找插入位置并后移。
                    k -= dk
                array_a[k + dk] = temp
        dk = dk / 2
    return array_a


def ShellSort2(array_a, n):
    dk = n / 2
    while dk >= 1:
        for i in range(dk, n):
            temp = array_a[i]
            k = i - dk
            while temp < array_a[k] and k >= 0:
                array_a[k + dk] = array_a[k]  # 如果小于其前驱，则从后往前寻找插入位置并后移。
                k -= dk
            array_a[k + dk] = temp
        dk = dk / 2
    return array_a


def BubbleSort(array_a, n):
    for i in range(0, n - 1):
        flag = 0  # 交换标志
        for j in range(n - 1, i, -1):
            if array_a[j] < array_a[j - 1]:
                temp = array_a[j]
                array_a[j] = array_a[j - 1]
                array_a[j - 1] = temp
                flag = 1
        if flag == 0:
            return array_a  # 若此趟未发生交换，说明已经有序，返回
    return array_a


def QuickSort(array_a, low, high):
    if low < high:
        pivotpos = Partition(array_a, low, high)
        QuickSort(array_a, pivotpos + 1, high)
        QuickSort(array_a, low, pivotpos - 1)


def Partition(array_a, low, high):
    pivot = array_a[low]
    while low < high:
        while low < high and array_a[high] >= pivot:
            high -= 1
        array_a[low] = array_a[high]  # 左移比pivot小的元素
        while low < high and array_a[low] <= pivot:
            low += 1
        array_a[high] = array_a[low]  # 右移比pivot大的元素
    array_a[low] = pivot
    return low


def SelectSort(arrau_a, n):
    for i in xrange(n - 1):
        min = i
        for j in range(i + 1, n):
            if array_a[j] < array_a[min]:
                min = j
        temp = array_a[i]
        array_a[i] = array_a[min]
        array_a[min] = temp


def BuildMaxHeap(array_a, n):
    for i in range(n / 2, 0, -1):  # 从i=[n/2-1]~0，反复调整堆。
        AdjustDown(array_a, i, n - 1)


def AdjustDown(array_a, k, n):
    array_a[0] = array_a[k]
    i = 2 * k
    while (i <= n):  # 沿着k的子结点筛选
        if i < n:
            if array_a[i] < array_a[i + 1]:
                i += 1  # 取值更大的子结点
        if array_a[0] > array_a[i]:
            break
        else:
            array_a[k] = array_a[i]  # array_a[i]调整到双亲上。
            k = i
        i *= 2
        array_a[k] = array_a[0]  # 被筛选的点放入最终位置。


def HeapSort(array_a, n):
    array_a.insert(0, 0)  # 首先array_a所有元素后移，rray_a[0]不存放元素
    n = len(array_a)
    BuildMaxHeap(array_a, n)
    for i in range(n - 1, 1, -1):
        temp = array_a[i]
        array_a[i] = array_a[1]
        array_a[1] = temp  # 将最大的元素放在当前无序数组的最后
        AdjustDown(array_a, 1, i - 1)  # 把剩余的i-1整理成堆。


array_a = [1, 2, 5, 3, 4, 9, 6, 5, 4, 76, 88, 0, -1]

HeapSort(array_a, len(array_a))
print array_a
