def count_number(string):
    '''
    count the number of each base in the string as input
    return the count in dictionary
    parameters:
        -string: input sequencing? 
        -base_dict: output a dictionary which the key is the base name 
                    and the value is the number of occurrance
    '''
    base_dict = dict()
    for s in string:
        if s not in base_dict:
            base_dict[s] = 1
        else:
            base_dict[s] += 1
    return base_dict

def cal_freq(base_dict):
    '''
    calculate the frequecy of each base 
    parameter:

    '''
    print('freqs')
    total = float(sum([base_dict[b] for b in base_dict.keys()]))
    for b in base_dict.keys():
        print(b + ':' + str(base_dict[b]/total))

cal_freq(count_number('ATCTGACGCGCGCCGC'))
