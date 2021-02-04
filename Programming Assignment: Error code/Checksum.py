from random import randrange

def unreliable_transmission(in_frame, p):
    ''' 
    :param in_frame: Bit string of any size up to k (input frame)
    :param p: Probability of having a bit in error (p)
    :return: Bit string of size k defined by the input bit string (output frame)
    '''
    out_frame = ''

    for bit in in_frame:
        randomNumber = randrange(100) + 1
        if randomNumber <= p*100:
            if bit == '0':
                out_frame += '1'
            else:
                out_frame += '0'
        else:
            out_frame += bit

    return out_frame

def Checksum_gen(dataword, word_size, num_blocks):
    ''' 
    :param dataword: Dataword of any length n (dataword)
    :param word_size: Size of each separated word (word_size)
    :param num_blicks: Number of word blocks used for one set of checksum operation (num_blocks)
    :return: A codeword based on Checksum
    '''
    codeword = dataword
    temp = [codeword[i:i+word_size] for i in range(0, len(codeword), word_size)]
    sum = '0'*word_size
    # add
    for data in temp:
        sum = bin(int(sum,2) + int(data,2))
    sum = sum[2:]
    if len(sum) > word_size:
        carry = sum[:len(sum)-word_size]
        sum = sum[len(sum)-word_size:]
        sum = bin(int(sum,2) + int(carry,2))
        sum = sum = sum[2:]
    while len(sum) < word_size:
        sum = '0' + str(sum)
    # complementing sum
    checksum = ''
    for bit in sum:
        if bit == '1':
            checksum += '0' # change 1 to 0
        else:
            checksum += '1' # change 0 to 1

    # append checksum to codeword
    codeword += checksum
    return codeword

def Checksum_check(codeword, word_size, num_blocks):
    '''
    :param codeword: codeword
    :param word_size: Size of each separated word (word_size)
    :param num_blocks: Number of word blocks used for one set of checksum operation (num_blocks)
    :return: Validity of codeword
    '''
    temp = [codeword[i:i+word_size] for i in range(0, len(codeword), word_size)]
    sum = '0'*word_size
    # add
    for data in temp:
        sum = bin(int(sum,2) + int(data,2))
    sum = sum[2:]
    if len(sum) > word_size:
        carry = sum[:len(sum)-word_size]
        sum = sum[len(sum)-word_size:]
        sum = bin(int(sum,2) + int(carry,2))
        sum = sum[2:]
    while len(sum) < word_size:
        sum = '0' + str(sum)
    # complementing sum
    complement = ''
    for bit in sum:
        if bit == '1':
            complement += '0' # change 1 to 0
        else:
            complement += '1' # change 0 to 1

    # check
    if complement == '0'*word_size:
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    dataword_input = '1010 0011 1011'
    dataword = dataword_input.replace(' ', '')
    word_size = 4
    num_blocks = 3

    checksum = Checksum_gen(dataword, word_size, num_blocks)
    checksum_received_5 = unreliable_transmission(checksum, 0.05)
    checksum_received_10 = unreliable_transmission(checksum, 0.1)
    checksum_received_20 = unreliable_transmission(checksum, 0.2)
    checksum_validity_5 = Checksum_check(checksum_received_5, word_size, num_blocks)
    checksum_validity_10 = Checksum_check(checksum_received_10, word_size, num_blocks)
    checksum_validity_20 = Checksum_check(checksum_received_20, word_size, num_blocks)

    print('--- Checksum ---')
    print('Dataword: ' + dataword_input)
    print(f'Send: {[checksum[i:i+word_size] for i in range(0, len(checksum), word_size)]}')
    print(f'Received (5% Error)  {[checksum_received_5[i:i+word_size] for i in range(0, len(checksum_received_5), word_size)]} ( {checksum_validity_5} )')
    print(f'Received (10% Error) {[checksum_received_10[i:i+word_size] for i in range(0, len(checksum_received_10), word_size)]} ( {checksum_validity_10} )')
    print(f'Received (20% Error) {[checksum_received_20[i:i+word_size] for i in range(0, len(checksum_received_20), word_size)]} ( {checksum_validity_20} )')



