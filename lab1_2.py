import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

stan_data = {
    "N":12,
    "y":[0,1,0,1,0,0,0,1,0,1,0,1]
}
model = CmdStanModel(stan_file='bern_1.stan')
sample = model.sample(stan_data)
theta = sample.stan_variable('theta')
summary = sample.summary()

quantiles5=numpy.quantile(theta,0.05)
quantiles50=numpy.quantile(theta,0.5)
quantiles95=numpy.quantile(theta,0.95)
qMean=theta.mean()

plt.figure()
plt.hist(theta, bins=50)
plt.axvline(quantiles5, color='r')
plt.axvline(quantiles50, color='g')
plt.axvline(quantiles95, color='b')
plt.axvline(qMean, color='k')
plt.show()
