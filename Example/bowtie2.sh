bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example1.fa -S example1.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example2.fa -S example2.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example3.fa -S example3.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example4.fa -S example4.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example5.fa -S example5.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example6.fa -S example6.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example7.fa -S example7.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example8.fa -S example8.sam

bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example1_B.fa -S example1_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example2_B.fa -S example2_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example3_B.fa -S example3_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example4_B.fa -S example4_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example5_B.fa -S example5_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example6_B.fa -S example6_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example7_B.fa -S example7_B.sam
bowtie2 -f -p 4  -k 20 --reorder --no-unal --no-hd --no-sq -x Homo_sapiens.GRCh37.70.cdna.all.index -U example8_B.fa -S example8_B.sam

python extract_data.py

python extract_data_B.py
