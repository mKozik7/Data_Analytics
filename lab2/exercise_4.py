import matplotlib.pyplot as plt
import numpy as np
from cmdstanpy import CmdStanModel
import scipy.stats as stats

model_tune = CmdStanModel(stan_file='code_6.stan')

F = 6
L = 6
y0 = 0

data={'y_guess':[y0],
        'theta':[(F+L)/2]}
tunes = model_tune.sample(data=data, fixed_param=True, iter_sampling=1, iter_warmup=0, chains = 1)
