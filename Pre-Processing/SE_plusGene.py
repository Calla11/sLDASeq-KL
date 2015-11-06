#! /usr/bin/env python

import os 
import os.path
def plusGeneName(refFlat_Check_GeneUnionExonLenFile,readFileList):
	f_isfInfor=open(refFlat_Check_GeneUnionExonLenFile,'r')
	isoList={}
	for line in f_isfInfor: 
	   line = line.rstrip();
	   line = line.split('\t');
	   gene=line[0]
	   i=0
	   while i<int(line[1]):
		     isoList[line[3+i]]=gene
		     i=i+1
	f_isfInfor.close();

	
	targetDir = os.getcwd()
	targetDir=os.path.dirname(targetDir)
	targetDir=os.path.join(targetDir,'workfloder')
	if not os.path.exists(targetDir):
		 os.mkdir(targetDir)
	readFile=os.path.join(targetDir,'readInput')
	 
	if not os.path.exists(readFile):
		 os.mkdir(readFile)
	for i in range(len(readFileList)):
		f_reads=open(readFileList[i],'r')  
		f_output = open(readFile+'/'+'Lane'+str(i)+'.plusGene','a')
		i=0;
		for line in f_reads:
		  line=line.rstrip();
		  line = line.split('\t');
		  #print line
		  
		  if len(line)==3:
			 i=i+1;
			 isfName=line[1]
			 
			 #read=line[0].split('|')
			 #read=read[2].split('.')
			 #read=read[0]+'.'+read[1]+'.1'
			 read=line[0]
			 loc=line[2]
			 if  isfName in isoList:
				 gene=isoList[isfName]
				 f_output.write(read+'\t'+isfName+'\t'+loc+'\t'+gene+'\t'+'\n')
			 
		  else:
			  pass
		f_output.close()
		f_reads.close()
 
				     
