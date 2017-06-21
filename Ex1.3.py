
def complementBase(base, material = 'DNA'):
    """ return complementary base """
    if base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'

def reverseComplement(seq, material = 'DNA'):
    """ return reverse complement of seq """
    revComp = ''
    for base in seq:
        revComp += complementBase(base, material)
    return revComp[::-1]

def reverseComplement_noLoop(seq, material = 'DNA'):
    ''' return reverse complement with no loops '''
    revSeq = seq[::-1]
    if material == 'DNA':
        revSeq = revSeq.replace('A','t')
        revSeq = revSeq.replace('T','A')
        revSeq = revSeq.replace('t','T')
    if material == 'RNA':
        revSeq = revSeq.replace('A','u')
        revSeq = revSeq.replace('U','A')
        revSeq = revSeq.replace('u','U')
    revSeq = revSeq.replace('G','c')
    revSeq = revSeq.replace('C','G')
    revSeq = revSeq.replace('c','C')
    return revSeq
