'''
convert DNA to RNA
'''

def rna(seq):
    ''' convert DNA to RNA '''
    if seq.isupper():
        return seq.replace('T','U')
    else: return seq.replace('t','u')

def revComp_RNA(seq):
    ''' convert DNA to its reverse complement as RNA '''
    seq_upper = seq.isupper()
    seq = seq[::-1]
    seq = seq.upper()

    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

    if seq_upper:
        return seq.upper()
    else: return seq
