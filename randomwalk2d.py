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
plt.figure(figsize=(8, 8))
plt.title('Última posição: ' + str(x[n - 1]) + ', ' + str(y[n - 1]))
plt.plot(x[0 : n//3], y[0 : n//3], 'orangered')
plt.plot(x[n//3 : 2*n//3], y[n//3 : 2*n//3], 'olivedrab')
plt.plot(x[2*n//3 : n], y[2*n//3 : n], 'skyblue')
plt.plot(0, 0, 'o', color='black')
plt.plot(x[n - 1], y[n - 1], 'o', color='black')
plt.show()
