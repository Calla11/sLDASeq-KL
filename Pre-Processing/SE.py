#!/usr/bin/env  python
# -*- coding: utf-8 -*-
from __future__ import division  
import SE_Extract_BowtieData
import SE_Extract_CalcAbsLoc_my
import SE_static_readOnExon_oshuhua
import SE_geneExonLen
import getIsoLength
import SE_plusGene
import os
import os.path
import get_map




Sample = ['workfloder']
CatFile = ['ExtractMultiGeneData','ModelMultiGene_AbsLoc','ModelMultiGene_Data','ModelMultiGene_NormData']
lanFile=[]
for i in range(8):
	lanFile.append('Lane'+str(i+1))

def CreateRunFileName(targetDir):
	for i in range(len(Sample)):
	    targetFile = os.path.join(targetDir, 'workfloder');	 
	    BuildFile(targetFile);
	    for j in range(len(CatFile)):
	        CatlogFile = os.path.join(targetFile, CatFile[j]);
	        BuildFile(CatlogFile);
	        if j == 0 or j == 1:
	           for k in range(len(lanFile)):
	               LaneFile = os.path.join(CatlogFile, lanFile[k]);
	               BuildFile(LaneFile);
	    targetFile1 = os.path.join(targetFile, 'readInput');	 
	    BuildFile(targetFile1);

def BuildFile(targetFile):
	if os.path.exists(targetFile):                         
	       subTargetDir = targetFile;
	else: 
	        os.mkdir(targetFile)                


targetDir = os.getcwd()
targetDir=os.path.dirname(targetDir)#
TargetGeneFile='./Ensemble.Gene.Info_iso.txt'
TargetGeneExonSplitFile='./Ensemble.Exon.Split'
readFileList={}
examplefile=os.path.join(targetDir,'Example')
readFileList[0]=os.path.join(examplefile,'example1')
readFileList[1]=os.path.join(examplefile,'example2')
readFileList[2]=os.path.join(examplefile,'example3')
readFileList[3]=os.path.join(examplefile,'example4')
readFileList[4]=os.path.join(examplefile,'example5')
readFileList[5]=os.path.join(examplefile,'example6')
readFileList[6]=os.path.join(examplefile,'example7')
readFileList[7]=os.path.join(examplefile,'example8')
	 



CreateRunFileName(targetDir)
	
mapFile=os.path.join(targetDir,'workfloder')
mapFile=os.path.join(mapFile,'ModelMultiGene_Map')

if not os.path.exists(mapFile):
	 os.mkdir(mapFile)
GeneExonFile=os.path.join(targetDir,'workfloder')
GeneExonFile=os.path.join(GeneExonFile,'GeneExonFile')	 

if not os.path.exists(GeneExonFile):
	 os.mkdir(GeneExonFile)


geneMapout=mapFile
geneExonout=GeneExonFile

get_map.mapout(TargetGeneExonSplitFile,geneMapout,geneExonout)#get isoform Map

getIsoLength.getIsoLen(TargetGeneFile,TargetGeneExonSplitFile)#get isoform length

exonLen=os.path.join(targetDir,'workfloder')
exonLen=os.path.join(exonLen,'exonLen')

if not os.path.exists(exonLen):
	os.mkdir(exonLen)
ReadLen=100
exonjunfile=os.path.join(targetDir,'workfloder')
	 
exonjunfile=os.path.join(exonjunfile,'GeneExonFile')
spandExonsLen=os.path.join(targetDir,'workfloder')
	 
spandExonsLen=os.path.join(spandExonsLen,'exonLen')

SE_geneExonLen.staticGeneNewExon(TargetGeneExonSplitFile,spandExonsLen)

	
SE_plusGene.plusGeneName(TargetGeneFile,readFileList)#plus geneName,the output in:workfloder/readInput

for j in range(8):
	InputFile=os.path.join(targetDir,'workfloder')
	InputFile=os.path.join(InputFile,'readInput')
	InputFile=os.path.join(InputFile,'Lane'+str(j)+'.plusGene')
		 
	OutputPath = os.path.join(targetDir,'workfloder')
			 
	OutputPath = os.path.join(OutputPath,CatFile[0])
			 
	OutputFile = os.path.join(OutputPath,lanFile[j])
			 
	print InputFile
	print OutputFile
	SE_Extract_BowtieData.ExtractGeneBowtieData(InputFile,TargetGeneFile,OutputFile)



                    
		
for l in range(8):
    CalLocFileInPath = os.path.join(targetDir,'workfloder')
    CalLocFileInPath = os.path.join(CalLocFileInPath,CatFile[0])
    CalLocFileInPath = os.path.join(CalLocFileInPath,lanFile[l])
    CalLocFileOutPath = os.path.join(targetDir,'workfloder')
    CalLocFileOutPath = os.path.join(CalLocFileOutPath,CatFile[1])
    CalLocFileOutPath = os.path.join(CalLocFileOutPath,lanFile[l])
    print CalLocFileInPath
    print CalLocFileOutPath
    SE_Extract_CalcAbsLoc_my.CalculateAbsoluteLocation(TargetGeneFile,TargetGeneExonSplitFile,CalLocFileInPath,CalLocFileOutPath)
    	
	  
f_in = open(TargetGeneFile,'r')
for line in f_in:
	line = line.rstrip();
	line = line.split('\t');
	gene = line[0];
	isoNo = int(line[1]);
	length = int(line[2]);
	isoName = line[3:];

	for i in range(len(Sample)):                           
	   
	    for j in range(8):
	              LocInputPath = os.path.join(targetDir,'workfloder')
	              LocInputFile = os.path.join(LocInputPath,CatFile[1])
	              LocInputFile = os.path.join(LocInputFile,lanFile[j])
	              exonInputFile=os.path.join(targetDir,'workfloder')
	              exonInputFile=os.path.join(exonInputFile,'GeneExonFile')
	              exonLenFile = os.path.join(targetDir,'workfloder')
	              exonLenFile = os.path.join(exonLenFile,'exonLen')
	              DataOutputPath = os.path.join(targetDir,'workfloder')
	              DataOutputFile = os.path.join(DataOutputPath,CatFile[2])
	              NormDataOutput=os.path.join(DataOutputPath,CatFile[3])
		    #  print LocInputFile
		   #   print DataOutputFile
	              #SE_static_readOnExon.ModelMultiGeneDataScale(gene,length,isoNo,isoName,LocInputFile,exonInputFile,exonLenFile,DataOutputFile,NormDataOutput);          
		      SE_static_readOnExon_oshuhua.ModelMultiGeneDataScale(gene,length,isoNo,isoName,LocInputFile,exonInputFile,exonLenFile,DataOutputFile,NormDataOutput);
f_in.close();
	
	




