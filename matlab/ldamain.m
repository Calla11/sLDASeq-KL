function [alpha,beta] = ldamain(emmax,demmax)
global   k
% wrapper of Latent Dirichlet Allocation, standard model.
% d      : data of gene
% k      : # of classes to isoform
% emmax  : # of maximum VB-EM iteration (default 100)
% demmax : # of maximum VB-EM iteration for a document (default 20)

if nargin < 2
  demmax = 20;
  if nargin < 1
    emmax = 100;
  end
end
fid = fopen('./refFlat/Ensemble.Gene.Info_iso.txt');
mkdir('alpha');
mkdir('eta');
mkdir('Expression_gene');
readNum = 800000;

while ~feof(fid)
  l = fgetl(fid);
  refFlat_line = textscan(l,'%s');
  Gene_length = str2num(char(refFlat_line{1}(3)));
  if (str2num(char(refFlat_line{1}(2))) > 1)
      char(refFlat_line{1}(1))
      str=pwd;
      index_dir=findstr(str,'/');
      str_temp=str(1:index_dir(end)-1); 
      a = [str_temp,'/workfloder/','ModelMultiGene_Data/',char(refFlat_line{1}(1))];
      a1 = [str_temp,'/workfloder/','ModelMultiGene_Map/',char(refFlat_line{1}(1))];
      f=fopen(a);
      f1=fopen(a1);
      if f>0&&f1>0
          al=['./alpha/',char(refFlat_line{1}(1))];
          f_alpha=fopen(al);
          if f_alpha>0
              fclose(f_alpha);
          else
              d = fmatrix(a);
              lineNo = size(d,2);
              beta = load([str_temp,'/workfloder/','ModelMultiGene_Map/',char(refFlat_line{1}(1))]);
              if size(beta,2) ~=1
                  n = length(d); 
                  count=0;
                  for i=1:n
                      count=count+sum(d{i}.cnt);
                  end
                  count;
                  if count~=0
                      k = size(beta,1);
                      [alpha,eta] = lda(beta',d,emmax,demmax);
                      if sum(alpha)==0 && sum(eta)==0
                          return;
                      end
                      dlmwrite(['./alpha/',char(refFlat_line{1}(1))],alpha/sum(alpha));
                      dlmwrite(['./eta/',char(refFlat_line{1}(1))],eta/sum(eta));
                      Expression(alpha, refFlat_line, beta, lineNo, readNum);
                  else
                      continue
                  end
              else
                  continue
              end 
          end
          fclose(f);
          fclose(f1);
      else
          continue
      end
  else
      continue;
  end
end
fclose(fid);
end

