import bioinfo_dicts as bd

def find_next_start(seq):
    '''
    returns the first ATG index
    '''
    return seq.find('ATG')

def find_first_stop(seq):
    '''
    input is a sequence starting after an ATG
    returns the inframe stop conon ORF
    '''
    stop = ['TGA','TAG','TAA']
    sequence = seq[:]
    next_codon = sequence[:3]
    sequence = sequence[3:]
    ORF = ''
    while next_codon not in stop and sequence != '':
        ORF += next_codon
        next_codon = sequence[:3]
        sequence = sequence[3:]
    if next_codon in stop:
        return ORF + next_codon
    else: return ''

def longest_orf(seq):
    '''
    find the longest ORF in seq
    '''
    longest_orf = ''
    current_index = find_next_start(seq)
    sequence = seq[:]
    while current_index != -1:
        ORF = find_first_stop(sequence[current_index:])
        sequence = sequence[3:]
        current_index = find_next_start(sequence)
        if len(ORF) > len(longest_orf):
            longest_orf = ORF
    return longest_orf

import os

filename = 'salmonella_spi1_region.fna'

def read_fasta(filename):
    '''
    read fasta file and store in a single string
    '''
    fasta = ''
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            header = f.readline()
            fasta_file = f.readlines()
            for i, line in enumerate(fasta_file):
                    fasta += line.rstrip()
    else:
        raise RuntimeError("{} does not exist".format(filename))
    return fasta

def dna2protein(orf):
    '''
    convert DNA seq to protein seq
    '''
    orf_protein = ''
    for i in list(range(int(len(orf)/3))):
        current_codon = orf[i*3:(i+1)*3]
        orf_protein += bd.codons[current_codon]
    return orf_protein
