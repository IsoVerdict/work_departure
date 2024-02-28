import numpy as np
import matplotlib.pyplot as plt
from pandas import *

bitcoin = read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True)
print(bitcoin.head())

plt.figure(figsize=(12, 8))
bitcoin.loc['2019', 'Close'].plot()
bitcoin.loc['2019', 'Close'].resample('M').mean().plot(label='moyenne par mois', lw=3, ls=':', alpha=0.8)
bitcoin.loc['2019', 'Close'].resample('W').mean().plot(label='moyenne par semaine', lw=2, ls='--', alpha=0.8)
plt.legend()
plt.show()