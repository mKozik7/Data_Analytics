import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

F= 6
L = 6

generate_quant = CmdStanModel(stan_file="code_1.stan")

samples = generate_quant.sample(data={'M':F},
                                fixed_param=True,
                                iter_sampling=1000,
                                iter_warmup=0,
                                chains=1)

fit_lambda = samples.stan_variable('lambda')
fit_l1 = samples.stan_variable('y_sim')
fit = samples.summary() 
plt.hist(fit_lambda, bins=50)
plt.title(f'Lambda')

for i in range (0,F):
    plt.figure()
    plt.title(f'y_sim {i+1}')
    plt.hist(fit_l1[:,i], bins=50)    
plt.show()

for i in range (0,F):
    plt.figure()
    plt.title(f'lambda {i+1}')
    plt.hist(fit_lambda, bins=50)