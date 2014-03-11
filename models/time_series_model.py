import numpy as np
from scipy import stats
import pandas
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

print sm.datasets.sunspots.NOTE

dta = sm.datasets.sunspots.load_pandas().data
dta.index = pandas.Index(sm.tsa.datetools.dates_from_range('1700','2008'))
del dta["YEAR"]

dta.plot(figsize=(12,8));
