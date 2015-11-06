function [alpha,eta] = lda(beta,d,emmax,demmax)
global n l k gammas    qs  lambda  
% Latent Dirichlet Allocation, standard model.
% d      : data of genes
% k      : # of classes to isoform
% emmax  : # of maximum VB-EM iteration (default 100)
% demmax : # of maximum VB-EM iteration for a document (default 20)
if nargin < 2
    demmax = 20;
  if nargin < 1
      emmax = 100;
  end
end
n = length(d); 
k=size(beta,2);
l=size(beta,1);
alpha = normalize(ones(1,k));
eta = normalize(ones(1,l));
lambda = eta'*ones(1,k)+ones(l,k) * (l*7) / k;
gammas = zeros(n,k);
lambda1= zeros(l,k);
lik = 0;
plik = lik;
mnt =0;
pmnt = mnt;
tic;
fprintf(1,'number of lane      = %d\n', n);%n通道数，通道代表文档
fprintf(1,'number of exons     = %d\n', l);%l外显子个数
fprintf(1,'number of isoform   = %d\n', k);%k异构体个数

for j = 1:emmax
    fprintf(1,'iteration %d/%d..\t',j,emmax);
  % vb-estep
  for ii=1:emmax
      for i = 1:n
          [gamma,q] = vbem(d{i},beta,lambda,alpha,demmax);
          gammas(i,:) = gamma;
          qs{i} = q;
          lambda1 = accum_beta(lambda1,q,d{i});
      end
      lambda = eta'*ones(1,k)+lambda1;
      mnt = lambda1;
      if (j > 1) && converged(mnt,pmnt,1.0e-2)
          break;
      end
      pmnt=mnt;
      lambda1= zeros(l,k);
  end

  % vb-mstep
  alpha = newton_alpha(gammas);
  eta= newton_eta(lambda');
 %converge?  
  lik=lda_lik(d,lambda,gammas);
  fprintf(1,'likelihood = %g\t',lik);
  if (j > 1) && converged(lik,plik,1.0e-2)
      fprintf(1,'\nconverged.\n');
      return;
  end
  if isnan(lik)
      alpha=zeros(1,k);
      eta=zeros(1,l);
      break;
  end
  plik = lik;
  % ETA
  elapsed = toc;
  fprintf(1,'ETA:%s (%d sec/step)\r', ...
	  rtime(elapsed * (emmax / j  - 1)),round(elapsed / j));
end
fprintf(1,'\n');
end

