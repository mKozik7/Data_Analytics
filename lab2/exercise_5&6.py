import matplotlib.pyplot as plt
import arviz as az
from cmdstanpy import CmdStanModel

F=7

model_samp = CmdStanModel(stan_file='code_7.stan')
model_log_target = CmdStanModel(stan_file='code_8.stan')
model_log_target_ind = CmdStanModel(stan_file='code_9.stan')
data = {'N': F}
seed = 14071999
result_1 = model_samp.sample(data=data)
result_2 = model_log_target.sample(data=data)
result_3 = model_log_target_ind.sample(data=data)
az.plot_density([result_1,result_2,result_3])
plt.show()

model_2 = CmdStanModel(stan_file='code_10.stan')
mean_of_y = model_2.generate_quantities(data=data,
 mcmc_sample = result_3)

df = mean_of_y.generated_quantities_pd
df.plot.hist(bins=50)