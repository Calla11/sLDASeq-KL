f_open=open('example1_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example1_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
    
f_open=open('example2_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example2_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()

f_open=open('example3_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example3_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example4_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example4_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example5_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example5_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example6_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example6_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example7_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example7_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()

f_open=open('example8_B.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example8_B','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
