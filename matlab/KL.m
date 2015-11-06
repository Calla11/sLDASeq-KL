
fid = fopen('./refFlat/Ensemble.Gene.Info_iso.txt');
mkdir('Output');
while ~feof(fid)
    l = fgetl(fid);
    refFlat_line = textscan(l,'%s');
    char(refFlat_line{1}(1))
    a = ['./alpha/',char(refFlat_line{1}(1))];
    b = ['./alpha_B/',char(refFlat_line{1}(1))];
    fa=fopen(a);
    fb=fopen(b);
    if fa>0&&fb>0
        alpha = load(['./alpha/',char(refFlat_line{1}(1))]);
        gma = load(['./alpha_B/',char(refFlat_line{1}(1))]);
        alpha=alpha./sum(alpha);
        gma=gma./sum(gma);
        k=size(alpha,2);    
        p2=psi(alpha)-psi(sum(alpha))*ones(1,k);
        part3=gammaln(sum(alpha))-sum(gammaln(alpha))+sum((alpha-ones(1,k)).*p2);
        part4=gammaln(sum(gma))-sum(gammaln(gma))+sum((gma-ones(1,k)).*p2);
        KL2=part3-part4;
        DE = fopen(['./Output/','sLDASeq_KL.txt'], 'a');
        fprintf(DE,'%c',char(refFlat_line{1}(1)));
        fprintf(DE,'\t');
        fprintf(DE,'%f\n',KL2);
        fclose(DE);
        fclose(fa);
        fclose(fb);
    elseif fa>0
        fclose(fa);
    elseif fb>0
        fclose(fb);
    end

end
fclose(fid);
