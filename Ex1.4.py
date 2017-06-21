
def longestCommon(seq1, seq2):
    ''' find the longest common substring between seq1 and seq2 '''
    longestSeq = ''     # longest seqeunce
    if len(seq1) > len(seq2):   # the shorter sequence is the queried seq, longest is template for search
        templateSeq = seq1
        searchSeq = seq2[:]
    else:
        templateSeq = seq2
        searchSeq = seq1[:]
    for i, base in enumerate(searchSeq):
        if len(searchSeq)-i < len(longestSeq):
            break
        longest = base
        index = i
        while longest in templateSeq:
            index += 1
            if len(longest) > len(longestSeq):
                longestSeq = longest[:]
            longest = searchSeq[i:index+1]
            print(longestSeq)
    return (len(longestSeq), longestSeq)
