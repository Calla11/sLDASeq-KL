#! /usr/bin/env python

import os
import os.path
def getIsoLen(refFlat_Check_GeneUnionExonLenFile,refFlat_Check_MultiGeneExonSplitFile):
	print 'Begin get isoform length...'
	f_in = open(refFlat_Check_MultiGeneExonSplitFile,'r');
	targetDir = os.getcwd()
	targetDir=os.path.dirname(targetDir)
	targetDir=os.path.join(targetDir,'workfloder_B')
	isoLenFile=os.path.join(targetDir,'isoLen')
	if not os.path.exists(isoLenFile):
		 os.mkdir(isoLenFile)
	

	isoLen = {}

	for line in f_in:
		line = line.rstrip();
		line = line.split('\t');
		line4=line[4].rstrip()
		line4=line4.rstrip(',')
		ProLength = line4.split(',');
		length = ProLength[len(ProLength)-1];
		isoLen[line[1]] = length
	f_in.close();

	f_isoin = open(refFlat_Check_GeneUnionExonLenFile,'r')
	for line in f_isoin:
		line = line.rstrip();
		line = line.split('\t');
	  
	
		i = 0  
		isoNum=int(line[1])
		if isoNum>1:
			f_out = open(isoLenFile+'/'+line[0],'w');    
			while i < int(line[1]):
				if line[i+3] in isoLen:
					f_out.write(isoLen[line[i+3]] +'\n')
					i = i + 1;
		   		else:
		   			i=i+1;
		else:
			f_out = open(isoLenFile+'/'+line[0],'w');    
			f_out.write(line[2]+'\n')
					 
	   			 
	   			 
     
	 
		f_out.close()
        del isoLen
