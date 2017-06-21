
def validRepresentation(notation):
    ''' returns True if notation is valid '''
    return notation.count('(') == notation.count(')')

def dotparen_to_bp(notation):
    ''' convert dot parenthases notation to paired tuples'''
    if not validRepresentation(notation):
        return
    currentNotation = notation[:]
    currentIndex = 0
    bps = []
    while '(' in currentNotation:
        index_5 = currentNotation.find('(')
        index_3 = len(currentNotation) - currentNotation[::-1].find(')') - 1
        bps += [(index_5 + currentIndex, index_3 + currentIndex)]
        currentIndex += index_5 + 1
        currentNotation = currentNotation[index_5 + 1:index_3]
    return tuple(bps)

def denyBySterics(bps):
    ''' checks that a tuple of bps allows hairpins of 4 or more bases '''
    index_5, index_3 = bps[-1]
    if (index_3 - index_5) - 1 < 4:
        return False
    else: return True

def complementBase(base, wobble = True):
    """ return complementary base """
    if base in 'G':
        if wobble == True:
            return 'CU'
        else: return 'C'
    elif base in 'C':
        return 'G'
    elif base in 'U':
        if wobble == True:
            return 'AG'
        else: return 'A'
    elif base in 'A':
        return 'U'

def rna_ss_validator(seq, sec_structure, wobble = True):
    ''' validate secondary structure of rna'''
    indexes = []
    if validRepresentation(sec_structure) == False:
        return False, 'Not a valid representation'
    bps = list(dotparen_to_bp(sec_structure))
    if denyBySterics(bps) == False:
        return False, 'Hairpin loop shorter than 4 bases; invalid'
    for bp in bps:
        if seq[bp[1]] not in complementBase(seq[bp[0]], wobble):
            return False
    return True
