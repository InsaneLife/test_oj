# coding=utf8
# author=AaronChou
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

# (x ** 2 + y ** 2 - 1)**2 = (x * y) ** 2

# x, y = 2, 2
# print x ** 2 + y ** 2 + x * y



rate = 0.0003
size = int(1.5 * (1 / rate))
error = 0.000005
print size
x_array = [round(i * rate, 5) for i in range(-size, size)]
y_array = [round(i * rate, 5) for i in range(-size, size)]

result = []
for x in x_array:
    for y in y_array:
        eq = (x ** 2 + y ** 2 - 1) ** 3 - (x **2 *y ** 3)
        if abs(eq) < error:
            result.append([x, y])

print result.__len__()

x = [i[0] for i in result]
y = [i[1] for i in result]

f1 = plt.figure(1)
plt.subplot(211)
plt.scatter(x, y)
plt.show()
