def longest_orf(seq):
    '''
    find the longest ORF in seq
    '''
    sub_seq = seq.upper()
    possible_ATG = []
    # find possible start sites
    while 'ATG' in sub_seq:
        if possible_ATG != []:
            last_ATG = possible_ATG[-1]+3
            possible_ATG += [sub_seq.find('ATG') + last_ATG]
            print(possible_ATG)
        else:
            possible_ATG += [sub_seq.find('ATG')]
            print(possible_ATG)
        print('***', sub_seq)
        sub_seq = sub_seq[possible_ATG[-1]+3:]
        print(sub_seq)

    return possible_ATG
