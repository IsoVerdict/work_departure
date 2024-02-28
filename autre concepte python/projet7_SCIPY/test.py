import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize                  # pour optimiser
from scipy import signal

from scipy.interpolate import interp1d

from scipy import fftpack                   # pour les transformés de fourier

x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x) + np.random.random(x.shape[0])*10
plt.plot(x, y)

# ETAPE 1: transformé de fourier
fourier = fftpack.fft(y)
frequences = fftpack.fftfreq(y.size)
power = np.abs(fourier)
abs_frequences = np.abs(frequences)
# plt.plot(abs_frequences, power)


# ETAPE 2: On filtre le signal
fourier[power<400] = 0  # toutes les valeurs du spètre dont l'amplitute est inférieur à 400 aurons à présent zéro pour valeur

# ETAPE 3: transformé de fourier inverse
filtered_signal = fftpack.ifft(fourier) # la methode << ifft() >> permet de faire la transformé de fourier inverse

plt.plot(x, y, lw=0.5) # on trace le signal bruillant
plt.plot(x, filtered_signal, lw=3) # on trace le signal filtrer


plt.show()