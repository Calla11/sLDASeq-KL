# sLDASeq-KL

##模型简介
sLDASeq-KL是利用两个条件下相同基因中异构体的比例变化，来检测差异异构体比例的模型

##如何运行sLDASeq-KL
>* 1.利用Bowtie2将读段数据比对到参考序列文件上
```shell
$ bowtie2-build -f ref_transcript.fa ref_transcript.index
$ bowtie2 -f -p 4 -k 20 --reorder --no-unal --no-mixed --no-discordant --no-hd --no-sq -x  ref_transcript.index raw_data.fasta -S align_reads.output.sam
```

* ref_transcript.fa表示异构体的参考序列文件
* ref_transcript.index表示异构体的参考序列生成的索引文件
* raw_data.fasta表示原始的读段文件
* align_reads.output.sam表示bowtie2将读段比对到参考文件上的输出文件

>* 2.将比对后的文件中有用的位置信息提取出
```shell
$ python extract_data.py
```

>* 3.将读段的位置信息转化成sLDASeq-KL模型所需要的输入格式
```shell
$ python SE.py
```

>* 4.计算出基因和异构体的表达水平，及各个基因中异构体的比例
在matlab软件中运行ldamain.m

###输出文件
* alpha文件夹存放的是模型的超参数alpha
* eta文件夹存放的是模型的超参数eta
* Expression_gene文件夹存放的是基因的表达水平
* Expression_iso.txt对应的是异构体的表达水平文件

>* 5.根据两个条件下，相同基因中异构体的比例的KL散度，进行差异异构体比例检测
在matlab软件中运行KL.m

###输出文件
* Output文件夹中sLDASeq_KL.txt则是两个条件下各个基因中异构体比例的KL散度

#实例
* 参考序列的注释文件：Homo_sapiens.GRCh37.70.cdna.all.fa.gz 下载地址：ftp://ftp.ensembl.org/pub/release-70/fasta/homo_sapiens/cdna/Homo_sapiens.GRCh37.70.cdna.all.fa.gz

>* 1.在Example路径下读段比对

```shell
$ bash bowtie2.sh
```
>* 2.在Pre-Processing路径下数据处理

```shell
$ bash pre_processing.sh
```

>* 3.在matlab路径下运行模型

使用matlab软件，先后运行ldamain.m、ldamain_B.m、KL.m

matlab路径下Output文件夹中sLDASeq_KL.txt，则是两个条件下各个基因中异构体比例的KL散度，用此来进行差异异构体比例检测。



