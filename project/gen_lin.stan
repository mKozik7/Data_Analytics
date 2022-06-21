data {
   int N;
   vector[N] points;
   real effs[N];
}

parameters {
   real alpha;
   real beta;
   real <lower=0> sigma;
}

transformed parameters {
   vector[N] mu = points*beta+alpha;
}

model {
   alpha ~ normal(600, 200);
	beta ~ normal(2, 0.5);
   sigma ~ normal(300, 50);
   effs ~ normal(mu, sigma);
}

generated quantities {
   array [N] real eff;
   vector[N] log_lik;
   array[N] real y_hat;

   for (i in 1:N) {
       eff[i] = normal_rng(mu[i], sigma);
       log_lik[i] = normal_lpdf(eff[i] | mu[i], sigma);
      y_hat[i] = normal_rng(mu[i], sigma);

   }
}