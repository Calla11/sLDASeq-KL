f_open=open('example1.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example1','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
    
f_open=open('example2.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example2','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()

f_open=open('example3.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example3','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example4.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example4','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example5.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example5','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example6.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example6','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
f_open=open('example7.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example7','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()

f_open=open('example8.sam','r')

for line in f_open.readlines():
    line=line.rstrip();
    line=line.split("\t")
    read=line[0];
    iso=line[2];
    loc=line[3];
    f_in=open('example8','a')
    f_in.write(str(read)+'\t'+str(iso)+'\t'+str(loc)+'\n')
    f_in.close()
f_open.close()
