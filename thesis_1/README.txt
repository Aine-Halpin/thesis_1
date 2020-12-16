This compressed folder contains 12 HIV fastq files.


Several programs exist, the most widely used is Trimmomatic (http://www.usadellab.org/cms/?page=trimmomatic), which is a Java based program that implements all of the above on either single-end, or paired-end FASTQ sequence libraries.

For this assignment you are going to

install the latest version of trimmomatic on your laptop/desktop

update your .bashrc file to allow the Java program to be run in any terminal

write a Python script that

accesses the FASTQ files from the test_data directory
loop over each file in the list, running trimmomatic using its default settings as reported on the package webpage for SE (single-end) reads
put the trimmed FASTQ files in a new subdirectory called trimmed_out
