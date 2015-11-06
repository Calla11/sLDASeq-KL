function [ geneExp ] = Expression_B( alpha, refFlat_line, beta, lineNo, readNum)
% use for computing transcript expression

alphaSampleNum = 1000;
alpha=alpha/sum(alpha);
drcalpha = drchrnd(alpha, alphaSampleNum);%生成alphaSampleNum行1列的  alpha矩阵
sampleNum = size(drcalpha);   %1000×alpha长
str=pwd;
index_dir=findstr(str,'/');
str_temp=str(1:index_dir(end)-1); 

isoLen = load([str_temp,'/workfloder_B/','isoLen/',char(refFlat_line{1}(1))]);
resultDir = [];
readNo= [str_temp,'/workfloder_B/','ModelMultiGene_Data/',char(refFlat_line{1}(1))];
readNoMatrix = fmatrix(readNo);
[iso_No, exon_no] = size(beta);
for sampleIndex = 1:sampleNum %1000次循环
    sampledrcalpha = drcalpha(sampleIndex,:);
     
    resultForEachDir = [];
    %*** use for computing denominator
    exon_no_index = 1;
    denominator = zeros(1,exon_no);

    denominator=sampledrcalpha*beta;%gene上每个exon对应的各个iso上该exon在总的比例相加  
    %*** use for computing denominator end
    isofexonNum=sum(beta,2);%异构体中外显子的个数，列相加
    exonList=zeros(1,exon_no);
    j=1;
    while j<=exon_no
        cc=1;
        exonRead=0;
        while cc<=lineNo
            exonRead=exonRead+readNoMatrix{cc}.cnt(j);%exonRead表示第j个外显子所有通道中读段的和
            cc=cc+1;
        end
        exonList(j)=exonRead;%exonList表示该gene中外显子所有通道中读段的和
        j=j+1;
    end
    if isnan(sampledrcalpha(1))%alpha（1） 若元素为NaN（非数值），在对应位置上返回逻辑1（真），否则返回逻辑0（假）
        readofgeneForNan = 0;
        kk = 1;
        while kk <= lineNo
            exon_index = 1;
            while exon_index <= exon_no
                readofgeneForNan = readofgeneForNan + readNoMatrix{kk}.cnt(exon_index);%第一个通道e上gene上所有read个数
                exon_index = exon_index+1;
            end
            kk = kk+1;
        end
        for m = 1:iso_No
            isoExp = readofgeneForNan*10^9/(isoLen(m,1)*readNum*iso_No); %readofgeneForNan为gene上所有read个数   不对XXXXXXXXXXXXXXXXXXX
            resultForEachDir = [resultForEachDir, isoExp];%记iso的表达值
        end
        
    else
        j=1;
        while j <= iso_No
            
             
                readofgene = 0;
            
                exon_index = 1;
                while exon_index <= exon_no
                    if (denominator(exon_index)==0) 
                       aa=sum(beta);
                       readofgene=readofgene+exonList(exon_index)*beta(j,exon_index)/aa(exon_index);%第j个iso上读段个数    要是没有比例则均分
                    else
                        readofgene = readofgene + exonList(exon_index)*(sampledrcalpha(j)*beta(j,exon_index)/denominator(exon_index));
                    end
                    exon_index = exon_index + 1;
                end
                
             
               allReadOfIso = sum(readofgene);
               isoExp = allReadOfIso*10^9/(isoLen(j,1)*readNum);
               if isnan(isoExp)
                  resultForEachDir = [resultForEachDir, 0];
               else
                   resultForEachDir = [resultForEachDir, isoExp];%记iso的表达值
               end
            j = j +1;
        end
    end
    resultDir = [resultDir; resultForEachDir];
end

geneExp=sum(resultDir,2);
geneExp_E=sum(geneExp)/1000;%因为循环 啦1000次
expressionFile = ['./Expression_gene_B/',char(refFlat_line{1}(1))];
fExpression = fopen(expressionFile, 'w');
dlmwrite(expressionFile, geneExp_E);
fclose(fExpression);

IsoExp=sum(resultDir,1);
IsoExp_E=IsoExp/1000;%因为循环 啦1000次
f_iso= fopen(['./','Expression_iso_B.txt'], 'a');
for i=1:iso_No
    fprintf(f_iso,'%s\t',char(refFlat_line{1}(i+3))); 
    fprintf(f_iso,'%f\n',IsoExp_E(i)); 
end
fclose(f_iso);
end

