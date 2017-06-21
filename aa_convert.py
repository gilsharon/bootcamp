import bioinfo_dicts as bd

def one2three(seq):
    '''
    converts protein seq on 1 letter abbreviation to three letter abbreviation
    '''
    # convert to upper case
    seq = seq.upper()

    #convert and make sure imported AA is valid
    aa_list = []
    for AA in seq:
        if AA not in bd.aa.keys():
            raise RuntimeError('{} is not a valid AA'.format(AA))
        aa_list += [bd.aa[AA],'-']
    return "".join(aa_list[:-1])
