function lik = lda_lik(d,beta,gammas)
% lik = lda_lik(d,beta,gammas)
egamma = mnormalize(gammas,2);
lik = 0;
n = length(d);
for i = 1:n
  t = d{i};
  lik = lik + t.cnt * log (beta(t.id,:) * egamma(i,:)');
end
