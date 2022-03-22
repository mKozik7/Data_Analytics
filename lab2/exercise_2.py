import pandas as pd
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

F=6
L=6

bern1 = CmdStanModel(stan_file='code_2.stan')
samp_bern1 = bern1.sample(data={'N':2, 'y':[0,1]})

bern2 = CmdStanModel(stan_file='code_3.stan')
samp_bern2 = bern2.sample(data={'N':2, 'y':[0,1]})

theta1 = samp_bern1.stan_variable('theta')
theta2 = samp_bern2.stan_variable('theta')

data = pd.DataFrame({'theta1': theta1, 'theta2': theta2})
data.plot.hist(subplots=True, bins=30)

plt.show()