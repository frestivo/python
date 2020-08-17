import random
import matplotlib.pyplot as plt
histo = {}
pos = 0
count = 0
# simulate
while count < 1000000:
  pos = pos + 2*random.randint(0, 1) - 1
  if pos not in histo:
    histo[pos] = 1
  else:
    histo[pos] += 1
  count += 1
# display
x = []
y = []
for i in sorted(histo):
  x.append(i)
  y.append(histo[i])
plt.plot(x, y)
plt.title('Última posição ' + str(pos))
plt.show()
