#!/usr/bin/env  python
# -*- coding: utf-8 -*-

from __future__ import division  


import os
import os.path
Sample = ['A']
readLen=100
def CalculateAbsoluteLocation(SubTargetGeneFile,TargetGeneExonSplitFile,CalLocFileInPath,CalLocFileOutPath):   
    f_ref = open(TargetGeneExonSplitFile,'r');            
    infoAll={}
    while True:
    	line=f_ref.readline();
    	if not line:
    		break;
    	else:
    		line=line.split('\t')
    		iso_no=line[1]
    		if iso_no.isdigit():
    			gene_info = [[]for i in range(3)];
                        iso_info = [[[]for j in range(3)]for i in range(int(iso_no))]
                        iso_nm_info = []
	    		gene=line[0]
	    			 
	    		split_no = line[2];
	    
		        split_index = line[3];
		        split_index = split_index.rstrip();
		        split_index = split_index.split(',')  
	       
		        split_len = line[4];
		        split_len = split_len.rstrip();
		        split_len = split_len.split(',');
	    
		        gene_info[0].append(int(split_no));
    
		        for i in range(int(split_no)):
				gene_info[1].append(int(split_index[i]));
				gene_info[2].append(int(split_len[i]));
			gene_info[2].insert(0,0)
			flag=1;
                	while flag != int(iso_no)+1:                        
				        line = f_ref.readline();
				        line = line.rstrip();
				        line = line.split('\t'); 

				        if line[0] != gene:
				            continue;
				        else:  
                 
				                iso_nm = line[1]; 
				                split_no = line[2];
		
				                split_index = line[3];
				                split_index = split_index.rstrip();
				                split_index = split_index.split(',')  
		
				                split_len = line[4];
				                split_len = split_len.rstrip();
				                split_len = split_len.split(',');
		
				                iso_nm_info.append(iso_nm);                                
				                iso_info[flag-1][0].append(int(split_no));        
				                    
				                for i in range(int(split_no)):
				                    iso_info[flag-1][1].append(int(split_index[i]));
				                    iso_info[flag-1][2].append(int(split_len[i]));
				                            
				        flag = flag + 1;    
	        	infoAll[gene]=[gene_info,iso_info,iso_nm_info]        
    f_ref.close();			

    f_info = open(SubTargetGeneFile,'r')   
    for info in f_info:
        info = info.rstrip();
        info = info.split('\t');
        gene = info[0];
        iso_no = int(info[1]);

        #if int(iso_no) ==1:              
         #  pass;
        #else:
        gene_info =infoAll[gene][0]
        iso_info = infoAll[gene][1]
        iso_nm_info = infoAll[gene][2]
                # 

         

        for sam in range(len(Sample)):              #
               if sam == 1: 
                   rep1 = 1
               else:
                   rep1 = 1
               for rep in range(rep1):
                   targetFile = os.path.join(CalLocFileInPath, gene);
            
                   if os.path.isfile(targetFile): 
                     f_gene = open(CalLocFileInPath+'/'+gene,'r');
                     f_out = open(CalLocFileOutPath+'/'+ gene,'w');

                     f_in = open(CalLocFileInPath+'/'+gene,'r');
    		     dic_read = dict()  #字典函数 dic_read ={}
           	     for line in f_in:
               		    line = line.rstrip();
              		    line = line.split('\t');
               		    readid = line[0];

               		    if readid not in dic_read:
                  	        dic_read[readid] = 1;
               		    else:
                  		dic_read[readid] = dic_read[readid] + 1;
		     f_in.close();



                     for line in f_gene:
                         line = line.rstrip();
                         line = line.split('\t');
    
                         readid = line[0];
                         loc = int(line[2]);
                         iso_na = line[1];

                         prob = line[4]
			 if readid in dic_read:
			    temp_count=dic_read[readid]
			    prob=float(prob)/temp_count




                         if iso_na in iso_nm_info:
		         
                            ind = iso_nm_info.index(iso_na);
                            exon_no = iso_info[ind][0][0];    
                            exon_ind = iso_info[ind][1];
                            exon_len=[]
                            exon_len_temp = iso_info[ind][2];
			    #print exon_len_temp

                            for i in range(len(exon_len_temp)):
                                exon_len.append((iso_info[ind][2])[i])
                            #exon_len = iso_info[ind][2];
                            exon_len.insert(0,0)
                           # print exon_len
                            #print 'loc'+str(loc)
                            abs_loc = 0;
                            relat_loc = 0;
                            relat_ind = 0;

			    exon_junc=[]
			    exon_junc_no = 2
			    exon_junc_len=[]

                            for i in range(exon_no):
                               if loc > exon_len[i] and loc<= exon_len[i+1]:
                                   relat_loc = loc - exon_len[i];
                                   relat_ind = exon_ind[i];##
				   
                                   exon_junc.append(int(relat_ind))
				   exon_junc_len.append(int(exon_len[i+1]-loc))

                                   abs_loc = gene_info[2][relat_ind-1]+relat_loc;
                                   #break;
                                   
                                      
                                   break;

                            for i in range(exon_no):
                               if loc+readLen > exon_len[i] and loc+readLen<= exon_len[i+1]:
                                   relat_loc2 = loc+readLen - exon_len[i];
                                   relat_ind2 = exon_ind[i];##

                                   abs_loc2 = gene_info[2][relat_ind2-1]+relat_loc2;
                                   #break;
                                   
                                      
                                   break;
			    #print exon_len_temp[-1]
		            if int(loc)<int(exon_len_temp[-1]): 

			       if relat_ind==relat_ind2:
                            	   f_out.write(readid+'\t'+iso_na+'\t'+str(abs_loc)+'\t'+str(relat_ind)+'\t'+str(prob)+'\n')
                               else:
				   for m in range(exon_no):
				       if exon_ind[m]>relat_ind and exon_ind[m]<relat_ind2:
					   exon_junc_no = exon_junc_no+1
					   exon_junc.append(int(exon_ind[m]))
				   	   exon_junc_len.append(int(exon_len[m+1]-exon_len[m]))
				   exon_junc.append(int(relat_ind2))
				   exon_junc_len.append(int(relat_loc2))
				   rate=[]
				   #print readid
				   #print gene
				   #print iso_na
				   #print relat_ind
				   #print relat_ind2
				   #print exon_junc_no
				   #print exon_junc_len
				   for m in range(exon_junc_no):

				       tempRate=(exon_junc_len[m]/int(readLen))*float(prob)
				       rate.append(tempRate)
				
				   for n in range(exon_junc_no):
                             	       f_out.write(readid+'\t'+iso_na+'\t'+str(abs_loc)+'\t'+str(exon_junc[n])+'\t'+str(rate[n])+'\n')
                                
              
		            else:
			       #print readid
				pass
                               				                            
                         else:
                           pass
    
                     f_gene.close();
                     f_out.close();

                   else:
                       pass;
    f_info.close()






 
