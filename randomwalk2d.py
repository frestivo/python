import random
import matplotlib.pyplot as plt
import numpy
#read
n = int(input('quantos movimentos?'))
x = numpy.zeros(n)
y = numpy.zeros(n)
#simulate
for i in range(1, n):
    dir = random.randint(1, 4)
    if dir == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif dir == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif dir == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
#plot
plt.title('Última posição ' + str(x[n - 1]) + ', ' + str(y[n - 1]))
plt.plot(x, y)
plt.show()
