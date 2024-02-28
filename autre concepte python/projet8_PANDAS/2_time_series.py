import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True) # << index_col='Date' >> c'est pour dire en quelque sorte que la colonne 
                                                                         # des date est celle qu'on veux utilisé en abscisse
                                                                         # << parse_dates=True >> pour dire que cette colonne (cet index) doit être
                                                                         # vue comme une date
bitcoin.head()

bitcoin['Close'].plot(figsize=(9, 6))
plt.show()

bitcoin["2019"]["close"].plot() # trace l'élévolution du bitcoin en 2019
bitcoin["2019-09"]["close"].plot() # trace l'élévolution du bitcoin en septembre 2019

bitcoin.index

bitcoin.loc['2017':'2019','Close'].plot() # trace l'élévolution du bitcoin entre 2017 et 2019
bitcoin['2017':'2019']['Close'].plot() # fait la même chose
# différents formats de dates accepté, il y en a beaucoup
#        "2019-03-20"
#        "2019/03/20"
#        "2019.03.20"
#        "2019 03 20"

#        jour mois année
#        "20-03-2019"
#        "20 March 2019"
pd.to_datetime("2019/03/20")  # pour effectuer une conversion nous même
#         on peut inclure des heures, des minutes, des secondes, des millisecondes, etc...
#        "2015-07-04 12:59"
#        "2015-07-04 12:59:59.50"





# Resample --------------------------------------------------------------------------
# permet de regrouper nos données selon une fréquence



bitcoin.loc['2019', 'Close'].resample('M').plot() # remarquons qu'il y a une erreur si l'on utilise pas les fonctions mean() , std(), min(), etc... comme ci-dessous
plt.show()

bitcoin.loc['2019', 'Close'].resample('2W').mean().plot() # evolution du bitcoin en fesant la moyenne toute les 2 semaines
plt.show()

bitcoin.loc['2019', 'Close'].resample('2W').std().plot()  # evolution du bitcoin en fesant l'écart-type toute les 2 semaines
plt.show()

plt.figure(figsize=(12, 8))
bitcoin.loc['2019', 'Close'].plot()
bitcoin.loc['2019', 'Close'].resample('M').mean().plot(label='moyenne par mois', lw=3, ls=':', alpha=0.8)
bitcoin.loc['2019', 'Close'].resample('W').mean().plot(label='moyenne par semaine', lw=2, ls='--', alpha=0.8)
plt.legend()
plt.show()




# Aggregate -------------------------------------------------------------------------

# la fonction << aggregate >> nous permet de rassembler dans un seul tableau plusieurs statistiques
# qu'on aimerait faire par dessus la fonction << resample >>
m = bitcoin['Close'].resample('W').agg(['mean', 'std', 'min', 'max'])

plt.figure(figsize=(12, 8))
m['mean']['2019'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.2, label='min-max par semaine') # pour créer en quelques sorte une zone d'incertitude entre le max et le min

plt.legend()
plt.show()


bitcoin.loc['2019', 'Close'].resample('W').agg(['mean', 'std', 'min', 'max']).plot()





# Moving Average et EWM --------------------------------------------------------------

# Moving Average
plt.figure(figsize=(12, 8))
bitcoin.loc['2019-09', 'Close'].plot()
bitcoin.loc['2019-09', 'Close'].rolling(window=7).mean().plot(label='non centre', lw=3, ls=':', alpha=0.8)
bitcoin.loc['2019-09', 'Close'].rolling(window=7, center=True).mean().plot(label='centre', lw=3, ls=':', alpha=0.8)
bitcoin.loc['2019-09', 'Close'].ewm(alpha=0.6).mean().plot(label='ewm', lw=3, ls=':', alpha=0.8)
plt.legend()
plt.show()

# Exponential Weighted Average
plt.figure(figsize=(12, 8))
bitcoin.loc['2019-09', 'Close'].plot()
for i in np.arange(0.2, 1, 0.2):
    bitcoin.loc['2019-09', 'Close'].ewm(alpha=i).mean().plot(label=f'ewm {i}', ls='--', alpha=0.8)
plt.legend()
plt.show()


# Assembler des dataset -------------------------------------------------------------- video-18:  12min 40sec !!!


# Comparaison de 2 série temporelles -------------------------------------------------

ethereum = pd.read_csv('ETH-EUR.csv', index_col='Date', parse_dates=True)
     

btc_eth = pd.merge(bitcoin, ethereum, on='Date', how='inner', suffixes=('_btc', '_eth'))
     

btc_eth[['Close_btc', 'Close_eth']]['2019-09'].plot(subplots=True, figsize=(12, 8))