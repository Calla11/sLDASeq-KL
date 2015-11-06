#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
import os
import os.path
 
 




def ModelMultiGeneDataScale(GeneName,GeneLen,IsoNo,IsoName,LocInputFile,ExonlistFile,ExonLenPath,DataOutput,NormDataout):
        
        ReadCout_onExon={}
        f_exon=open(ExonlistFile+'/'+GeneName,'r');
        exonlist=f_exon.readline();
        exonlist=exonlist.rstrip()
        exonlist=exonlist.split('\t')  #[1,2,3...]
        f_exon.close()
	f_exon=open(ExonLenPath+'/'+GeneName,'r')
        exonLen=f_exon.readline()
        exonLen=exonLen.rstrip()
        exonLen=exonLen.split('\t')   #[5,10,3,1...]
        f_exon.close()

	readCount = [0 for i in range(len(exonlist))]
	targetFile = os.path.join(LocInputFile, GeneName); #targetFile = ./workfloder/ModelMultiGene_AbsLoc/Lane1
        if os.path.isfile(targetFile):
          
           f_in = open(LocInputFile+'/'+ GeneName,'r');
           for line in f_in:
               line = line.rstrip();
               line = line.split('\t');
               readid = line[0];
               exonIndex = line[3];
               prob = float(line[4])
	       if exonIndex in exonlist: 
                     readCount[exonlist.index(exonIndex)]=readCount[exonlist.index(exonIndex)]+prob
	   f_in.close()

           f_out=open(DataOutput+'/'+GeneName,'a');
           for L in range(len(readCount)):
               f_out.write(str(L+1)+':'+str(readCount[L])+'\t')
           f_out.write('\n') 

	   f_out=open(NormDataout+'/'+GeneName,'a')     
           for L in range(len(readCount)):
                a=float(exonLen[L]);
                if a>0:
                   
                   #f_out.write(str(L+1)+':'+str(  (int(readCount[L])/a+0.001)*1000 )+'\t')
                   f_out.write(str(L+1)+':'+str(  ((readCount[L])/a))+'\t')#GGGGGG
		   #f_out.write(str(L+1)+':'+str(  ((readCount[L])/a+0.001))+'\t')
                
                else:
                   f_out.write(str(L+1)+':'+str(1)+'\t')
           f_out.write('\n')
	   f_out.close()
	  
