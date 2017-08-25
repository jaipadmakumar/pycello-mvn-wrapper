#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Wrapper that converts arguments into maven call to run Cello from commandline')

parser.add_argument('-verilog', help='path to verilog file', required=True)
parser.add_argument('-jobID', help='specifies a job ID. This dictates the output directory name as well as file names in the directory.') 
parser.add_argument('-input_promoters', help='path to input promoters file')
parser.add_argument('-output_genes', help='path to output genes file')
parser.add_argument('-UCF', help = 'path to UCF file')

args = parser.parse_args()

print args