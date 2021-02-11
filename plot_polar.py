import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
import math
import itertools
import scipy.signal
pos = 0
n = 0

main_data = []
main_data_in_rad = []
f = open('log.txt','r')
filecont = f.readlines()
for i in range(len(filecont)):
    temp = filecont[i]
    temp = temp.split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    main_data.append(temp)

main_data.sort(key = lambda x: x[0])
main_data = ([next(b) for a, b in itertools.groupby(main_data, lambda y: y[0])]) 

for i in range(len(main_data)):
    if main_data[i][0] == 179:
        break
    else:
        pos = pos+1
main_data = main_data[:pos]

for i in range(len(main_data)):
    main_data[i][0] = math.radians(main_data[i][0])

data = np.array(main_data)
x,y = data.T
filteramount = 15
while(n <= len(y)):
    avg = sum(y[n:n+filteramount])/filteramount
    for i in range(n,n+filteramount):
        y[i-1] = avg
    n = n+filteramount

fig = plt.figure()
ax = fig.add_subplot(polar=True)
c = ax.plot(x, y)
ax.set_thetamin(0)
ax.set_thetamax(180)
plt.show()