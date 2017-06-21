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
    return fasta, header

def next_block(string, blocksize):
    '''
    return the next block of 'blocksize' bases and the reminder
    of the sequence.
    '''
    return (string[:blocksize], string[blocksize:])

def gc_blocks(seq, blocksize):
    '''
    return a tuple of gc content per blocksized blocks in the seqeunce.
    if last block smaller than blocksize, its dropped
    '''
    gc_by_block = []
    reminder = seq
    while reminder != '':
        block, reminder = next_block(reminder, blocksize)
        block = block.upper()
        if len(block) == blocksize:
            gc_by_block += [(block.count('C') + block.count('G')) / len(block)]
    return tuple(gc_by_block)

def gc_map(seq, blocksize, gc_thresh):
    '''
    scans over seq, by blocksize, to check where the gc content is over
    gc_thresh
    '''
    mapped_seq = ''
    blocks = gc_blocks(seq, blocksize)
    blocks_under = []
    for i, block in enumerate(blocks):
        if block > gc_thresh:
            mapped_seq += seq[(i * blocksize):((i+1) * blocksize)].upper()
        else:
            mapped_seq += seq[(i * blocksize):((i+1) * blocksize)].lower()
            blocks_under += ['{}:{}'.format((i * blocksize),((i+1) * blocksize))]
    return mapped_seq

def output_gc_map(mapped_seq,output_filename,header):
    '''
    write mapped_seq to new filename
    '''
    if os.path.isfile(output_filename):
        raise RuntimeError("{} exists!!!".format(output_filename))
    else:
        with open(output_filename, 'w') as f:
            f.write(header)
            while mapped_seq != '':
                f.write(mapped_seq[:60] + '\n')
                mapped_seq = mapped_seq[60:]
