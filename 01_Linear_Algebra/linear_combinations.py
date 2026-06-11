import numpy as np
import matplotlib.pyplot as plt 
A = np.array([2,0.02])
V = np.array([-3,0.04])
new_t =  np.add(A,V)
plt.figure(figsize=(6,6))
plt.quiver(0,0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='blue',width=0.015, label='A')
plt.quiver(0,0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='green',width=0.015, label='V')
plt.quiver(0,0, new_t[0], new_t[1], angles='xy', scale_units='xy', scale=1, color='red',width=0.015, label='new_t')
plt.xlim(-5, 5)
plt.xlim(-5, 5)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)


plt.grid(True, linestyle='--',alpha=0.6)
plt.legend(loc='upper left')
plt.title('vecteur résultant')
plt.savefig('combi.png', dpi=300, bbox_inches='tight')
plt.show()


