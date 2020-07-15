#!/usr/bin/env python
## This script was used to select a subset of input reads prior to the assembly
from argparse import ArgumentParser

parser = ArgumentParser(description='Merge Paired End FASTQ reads (Obs.: Input reads must be sorted before run the script)'
parser.add_argument('-i1', '--input1', metavar='', help='Input fastq file R1', required=True)
parser.add_argument('-i2', '--input2', metavar='', help='Input fastq file R2', required=True)
parser.add_argument('-o', '--output', metavar='', help='Output filename', required=True)
args = parser.parse_args()

#opening files
sub1 = open(args.i1, "r")
sub1 = sub1.readlines()
sub2 = open(args.i2, "r")
sub2 = sub2.readlines()

#output file
outname = args.o + ".fq" 
out = open(outname, "w")

for i in range(len(sub1)):
    #sub1[i] = sub1[i].strip('\n')
    #sub1[i] = sub1[i].split('\n')
    if i%4 == False:
        out.write(str(sub1[i]))
        out.write(str(sub1[i+1]))
        out.write(str(sub1[i+2]))
        out.write(str(sub1[i+3]))
        out.write(str(sub2[i]))
        out.write(str(sub2[i+1]))
        out.write(str(sub2[i+2]))
        out.write(str(sub2[i+3]))

out.close()

        

