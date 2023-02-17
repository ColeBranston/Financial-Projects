from datetime import datetime
from datetime import date
import datetime
import scipy.stats
from math import log, sqrt, pi, exp
import math

def bsm(spot, strike, expiry, volatility):
    
    current = datetime.datetime.now()
    time = abs((current - expiry).days)/365
    
    start = ((log(spot/strike)+((volatility**2)/2)*time))*((volatility*math.sqrt(time)))
    end = start - volatility*math.sqrt(time)
    val =  scipy.stats.norm.cdf(start)*spot - strike*exp(time)*scipy.stats.norm.cdf(end)
    
    return val

date = datetime(2022, 8, 26, 12, 0, 0)
print(bsm(20.5,20,date,0.05))
