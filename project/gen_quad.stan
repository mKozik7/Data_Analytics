data {
	int N;
	vector[N] points;
	real effs[N];
}

parameters {
	real alpha;
	real beta;
	real gamma;
	real<lower=0> sigma;
}

transformed parameters {
	vector[N] mu = square(points)*gamma + points*beta;
}

model {
	beta ~ normal(1,0.1); 
	sigma ~ normal(300, 50);
	gamma ~ normal(-0.0001, 0.0001);
	effs ~ normal(mu, sigma);
}

generated quantities {
	real eff[N];
	vector[N] log_lik;
	for (i in 1:N){
		eff[i] = normal_rng(mu[i], sigma);
		log_lik[i] = normal_lpdf(effs[i] | mu[i], sigma);
	}
}