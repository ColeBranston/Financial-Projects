import csv
import matplotlib.pyplot as plt
import pandas as pd
import mplcyberpunk

plt.figure(figsize=(20, 10), dpi=320)
plt.rcParams.update({'font.size': 14})
plt.style.use('cyberpunk')

spy = pd.read_csv("SPY.csv")
price = (spy['Close'].pct_change())*100
price = price.iloc[1:]

bars = []

for x in range(300):
    a = []
    bars.append(a)

counts = []
xvalue = []
count = -150

for x in price:
    bars[round(x*10+150)].append(x)
for y in bars:
    counts.append(len(y))
    xvalue.append(str(count/10))
    count+=1
plt.plot(xvalue, counts)

spy = pd.read_csv("QQQ.csv")
price = (spy['Close'].pct_change())*100
price = price.iloc[1:]

bars = []

for x in range(380):
    a = []
    bars.append(a)

counts = []
xvalue = []
count = -200

for x in price:
    bars[round(x*10+200)].append(x)
for y in bars:
    counts.append(len(y))
    xvalue.append(str(count/10))
    count+=1
plt.plot(xvalue, counts)

s = pd.DataFrame({'pct':xvalue,'count':counts})

plt.xticks(xvalue[::10])
mplcyberpunk.make_lines_glow()
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.7)
plt.title('SPY & QQQ Percentage(%) daily change since March 9th, 1999')
plt.xlabel('% daily change')
plt.ylabel('Occurences')
plt.plot(0,0,label='Source: Yahoo Finance')
plt.legend()
plt.show()
