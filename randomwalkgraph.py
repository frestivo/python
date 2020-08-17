import random
import matplotlib.pyplot as plt
# adjacencies
p = {1 : [2, 4],
     2 : [1, 3, 5],
     3 : [2],
     4 : [1],
     5 : [2, 6],
     6 : [5]}
# length histogram
h = {}
i = 0
sum = 0
# input data
N = int(input('quantas experiências? '))
while True:
  startn = int(input('nó de partida? '))
  stopn = int(input('nó de chegada? '))
  if startn in p and stopn in p: break
# simulate
while i < N:
  c = 0
  n = startn
  while n != stopn:
    m = random.randint(1, len(p[n]))
    nn = p[n][m - 1]
    n = nn
    c += 1
  sum = sum + c 
  if c not in h:
    h[c] = 1
  else:
    h[c] += 1
  i += 1
#output
print ('média:', sum/N)
x = []
y = []
for i in sorted(h):
  x.append(i)
  y.append(h[i])
ymax = max(y)
pmax = y.index(ymax)
print('moda:', x[pmax], 'ocorrências:', ymax)
plt.bar(x, y)
plt.title('Histograma de comprimentos')
plt.show()
