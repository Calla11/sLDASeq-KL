function eta = newton_eta (lambda,maxiter,ini_eta)
% eta = newton_eta (lambda,[maxiter])
% Newton-Raphson iteration of LDA Dirichlet prior.
% lambda  : matrix of Dirichlet posteriors (M * k)
% maxiter : # of maximum iteration of Newton-Raphson

[M,K] = size(lambda);%k*l   M=k 异构体   K=l 外显子
p1=zeros(M,K);

if ~(M > 1)
  eta = lambda(1,:);
  return;
end
if nargin < 3
  ini_eta = mean(lambda) / K; % initial point
  if nargin < 2
    maxiter = 20;
  end
end

l = 0;
g = zeros(1,K);
for i=1:M
    for j=1:K
        if lambda(i,j)~=0
            p1(i,j)=psi(lambda(i,j));
        else
            p1(i,j)=0;
        end
    end
end

pg = sum(p1,1) - sum(psi(sum(lambda,2)));
eta = ini_eta;
peta = zeros(1,K);

for t = 1:maxiter
  l = l + 1;
  eta0 = sum(eta);
  g = M * (psi(eta0) - psi(eta)) + pg;
  h = - 1 ./ psi(1,eta);
  hgz = h * g' / (1 / psi(1,eta0) + sum(h));
  
  for i = 1:K
    eta(i) = eta(i) - h(i) * (g(i) - hgz) / M;
  end
  if any(eta < 0)
    eta = newton_eta(lambda,maxiter,ini_eta / 10); % try again!
    return;
  end
  
  if (l > 1) && converged(eta,peta,1.0e-4)
    break;
  end
  peta = eta;
end
