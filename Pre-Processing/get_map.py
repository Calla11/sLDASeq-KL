#!/usr/bin/env  python
# -*- coding: utf-8 -*-
from __future__ import division  
#将isoform中结合区看作一个外显子  这样生成map

import os
import os.path
def mapout(InputFile,MapOutputFile,geneExonFile):
    
    
    
    print 'Begin creating mapping for every gene'
    f_in = open(InputFile)
    line = f_in.readline();
    i = 0 ;
    while(line):
		 
		
		line = line.rstrip()
		line = line.split('\t')
		gene = line[0]
		iso_no = int(line[1])
		flag=0
		isoExonList = [[]for n in range(iso_no)]
		isoBetaMatrix = [[]for n in range(iso_no)]
		if (flag==0):
			line3=line[3].rstrip()
			line3=line3.rstrip(',')
			line3=line3.split(',')            
			geneExonList = line3
			flag=1;
			for j in range(iso_no):
				line = f_in.readline()
				line = line.split('\t')
				line3=line[3]
				line3=line3.rstrip(',')
				line3=line3.split(',')
				isoExonList[j] = line3;
				 
   
			
			for j in range(len(geneExonList)):#
				for m in range(len(isoExonList)):
					if geneExonList[j] not in isoExonList[m]:
						isoBetaMatrix[m].append(0)
					else:
						isoBetaMatrix[m].append(1)
			if (iso_no>=1):
			 
                         f_out = open(MapOutputFile+'/'+ gene,'w');
                         f_exon = open(geneExonFile+'/'+gene,'w')

			 for k in range(len(geneExonList)):
			 	f_exon.write(str(geneExonList[k])+'\t')
			 for K in range(iso_no):
			 	for L in range(len(geneExonList)):
			 		f_out.write(str(isoBetaMatrix[K][L])+'\t')
				f_out.write('\n')
				
        
			
			
			
			i = i+1#
		 
			line=f_in.readline();
    f_out.close()
    f_exon.close()		
    print i;	 
    f_in.close();
	
 
 




            
