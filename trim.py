import os
# set up directory variables
seq_dir = 'test_dataset'
fastqc_dir = 'trimmed_out'
# create output directory
#os.mkdir(fastqc_dir)
print ('# created subdir: ' + fastqc_dir)


# get list of FASTQ files
file_list = os.listdir(seq_dir)
print ('# got list of files in: ' + seq_dir)
# create the command string for each sequence
# & implement it
for seq in file_list:
    command = 'java -jar /home/aine/sw/FastQC/trimmomatic-0.39.jar SE -phred33'+ "" +seq_dir+'/'+seq+ ''seq_dir + '/' + seq+ '_trimmed.fastq ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 '
    print (command)
    os.system(command)
    
# mv html & zip files out of sequence directory
# into FASTQC directory
command1 = 'mv ' + seq_dir + '/' + '*_trimmmed.fastq ' + fastqc_dir
print (command1)
os.system(command1)

print ('#done')
                                                         [ Read 27 lines ]