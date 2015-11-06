function [alpha,q] = vbem(d,beta,lambda,alpha0,emmax)
% [alpha,q] = vbem(d,beta,alpha0,[emmax])
% calculates a gene and exon posterior for a gene d.
% alpha  : Dirichlet posterior for a gene d
% q      : (L * K) matrix of word posterior over latent classes
% d      : gene data
% alpha0 : Dirichlet prior of alpha
% emmax  : maximum # of VB-EM iteration.
if nargin < 5
  emmax = 20;
end
l = length(d.id);
k = length(alpha0);
q = zeros(l,k);
nt = ones(1,k) * l / k;

pnt = nt;
for j = 1:emmax
  % vb-estep
  a = diag(exp(psi(alpha0 + nt)));
  
  b= exp((psi(lambda)-psi(ones(l,1)*sum(lambda,1))).*beta);
  c = b*a;
  sum_c=sum(c,1);
  for i4=1:k
      for j4=1:l
          if c(j4,i4)~=0
              q(j4,i4) = c(j4,i4)/sum_c(i4);
          else
              q(j4,i4) = 0;
          end
      end
  end

  % vb-mstep
  nt = d.cnt * q;

  % converge?
  if (j > 1) && converged(nt,pnt,1.0e-2)

      break;
  end
  pnt = nt;
end
alpha = alpha0 + nt;

