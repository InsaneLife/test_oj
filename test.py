s_in = raw_input().split(" ")
n = int(s_in[0])
k = int(s_in[1])
array1 = raw_input().split(" ")
array1 = [int(x) for x in array1]
for j in range(0, k):
    tem = array1[0]
    for i in range(0, n - 1):
        array1[i] = array1[i] + array1[i + 1]
        if array1[i] >= 100:
            array1[i] = array1[i] % 100
    array1[n - 1] = array1[n - 1] + tem
    if array1[n - 1] >= 100:
        array1[n - 1] = array1[n - 1] % 100
for each in array1:
    print each,
