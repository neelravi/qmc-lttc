import numpy as np
import matplotlib.pyplot as plt

from hydrogen import e_loc

x=np.linspace(-5,5)

def make_array(a):
  y=np.array([ e_loc(a, np.array([t,0.,0.]) ) for t in x])
  return y

plt.figure(figsize=(10,5))
for a in [0.1, 0.2, 0.5, 1., 1.5, 2.]:
  y = make_array(a)
  plt.plot(x,y,label=f"a={a}")

plt.tight_layout()

plt.legend()

plt.savefig("plot_py.png")