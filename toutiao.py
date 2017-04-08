# ss = raw_input()
ss = '[[[]]][][[[[]]]]'
result_o = []
i = 0
mark = 0
for s in ss:
    if s == '[':
        if mark == 0:
            i += 1
        else:
            result_o.append(i)
            i = 1
            mark = 0
    elif s == ']':
        mark = 1
        continue
result_o.append(i)

max_r = max(result_o)

for rr in result_o:
    for i in range(max_r, max_r - rr, -1):
        s1 = ''
        for kong in range(0, max_r - i - 1):
            s1 += ' '

        if i == max_r:
            s1 += '+'
        else:
            s1 += '|+'
        for j in xrange(i * 2 - 1):
            s1 += '-'

        if i == max_r:
            s1 += '+'
        else:
            s1 += '+|'
        print s1

    s1 = ''
    for i in xrange(max_r - 1):
        s1 += ' '
    s1 += '| |'
    print s1
    print
    print s1

    for i in range(max_r - rr+1, max_r + 1):
        s1 = ''
        for kong in range(0, max_r - i - 1):
            s1 += ' '

        if i == max_r:
            s1 += '+'
        else:
            s1 += '|+'
        for j in xrange(i * 2 - 1):
            s1 += '-'

        if i == max_r:
            s1 += '+'
        else:
            s1 += '+|'
        print s1
