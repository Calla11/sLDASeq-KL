function betas = accum_beta(betas,q,t)

betas(t.id,:) = betas(t.id,:) + diag(t.cnt) * q;
