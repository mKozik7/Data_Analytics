data {
	int N;
	real points[N];
}

generated quantities {
	real beta = normal_rng(1,0.1);            // wspolczynnik przy x
    real gamma = normal_rng(-0.0001, 0.0001);       //wspołczynnik pprzy 2
	real sigma = normal_rng(300, 50);          // odchylenie
	real eff[N];
	for (i in 1:N){
		eff[i] = normal_rng(points[i]*points[i]*gamma + points[i]*beta, sigma);
	}
}