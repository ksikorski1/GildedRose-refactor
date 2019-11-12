import matplotlib.pyplot as plt
import numpy as np

#dane stworzone uzywajac 
#python -m radon cc -a radon_refaktoryzacja.py
#i analogicznie
#python -m radon cc -a radon_bez-refaktoryzacji.py

original = [23, 12.3, 36]
refactored = [7, 3.3, 54]

ind = np.arange(3) 
width = 0.35       
plt.bar(ind, original, width, label='original')
plt.bar(ind + width, refactored, width, label='refactored')

plt.ylabel('Ilość linii / CC score')
plt.title('Gilded Rose')

plt.xticks(ind + width / 2, ('Worst CC','Avg CC', 'SLOC'))
plt.legend(loc='best')
plt.savefig('./complexity.png')
plt.show()
