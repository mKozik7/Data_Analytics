data {
  int N;
  real points[N];

}

generated quantities {
    real alpha = normal_rng(600,200);   //
    real beta = normal_rng(1,0.1);     // wspolczynnik
    real sigma = normal_rng(100,50);    // 3sigma 
    real eff[N];
    for (i in 1:N){
    eff[i] = normal_rng(points[i] * beta + alpha, sigma);  
    }
}

