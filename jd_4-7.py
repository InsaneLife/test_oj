# !/usr/bin/env python
# coding=utf-8

while 1:
    s = raw_input()
    arr = []
    max_time, min_time = 0, 1000000000
    max_num1, m1_p, max_num2, m2_p = 0, 0, 0,0
    if s != "":
        s = int(s)
        for i in xrange(s):
            x, l = [int(x) for x in raw_input().split()]
            if x + l > max_time:
                max_time = x + l
            if x + l < min_time:
                min_time = x + l
            arr.append([x, l])
        for i in range(min_time, max_time + 1):
            this_num = 0
            for each in arr:
                if i >= each[0] and i <= (each[0] + each[1]):
                    this_num += 1
            if this_num > max_num1:
                max_num1 = this_num
                m1_p = i
        for i in range(min_time, max_time + 1):
            this_num = 0
            for each in arr:
                if i >= each[0] and i <= (each[0] + each[1]) and (m1_p < each[0] or m1_p > (each[0] + each[1])):
                    this_num += 1
            if this_num > max_num2:
                max_num2 = this_num
                m2_p = i

        print max_num1, max_num2
        print m1_p, m2_p
    else:
        break
