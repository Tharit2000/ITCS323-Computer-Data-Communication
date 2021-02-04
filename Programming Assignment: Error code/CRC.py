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

def CRC_gen(dataword, CRC_type):
    ''' 
    :param dataword: Dataword of size k
    :param CRC_type: CRC-type (string e.g, CRC-8, CRC-16, CRC-32, …)
    :return: A codeword based on CRC
    '''
    codeword = dataword
    divisor = ''
    if CRC_type == 'CRC-32':
        divisor = '100000100110000010001110110110111'
    elif CRC_type == 'CRC-24':
        divisor = '1100000000101000100000001'
    elif CRC_type == 'CRC-16':
        divisor = '11000000000000101'
    elif CRC_type == 'ReCRC-16':
        divisor = '10100000000000011'
    elif CRC_type == 'CRC-8':
        divisor = '111010101'
    elif CRC_type == 'CRC-4':
        divisor = '11111'

    while len(codeword) < len(dataword) + len(divisor) - 1:
        codeword += '0'
    codeword = dataword + div(codeword,divisor)
    
    return codeword

def div(codeword, divisor):
    k = len(divisor)
    encoded = codeword[0:k]
    remainder = ''
    for i in range(k):
        if encoded[i] == divisor[i]:
            remainder += '0'
        else:
            remainder += '1'

    while k < len(codeword):
        if remainder[0] == '0':
            remainder = remainder[1:]
            remainder += codeword[k]
            k += 1
        
        encoded = remainder
        remainder = ''
        for i in range(len(divisor)):
            if encoded[0] == '0':
                div = '0' * 33
            else:
                div = divisor

            if encoded[i] == div[i]:
                remainder += '0'
            else:
                remainder += '1'

    return remainder[1:]

def CRC_check(codeword, CRC_type):
    divisor = ''
    if CRC_type == 'CRC-32':
        divisor = '100000100110000010001110110110111'
    elif CRC_type == 'CRC-24':
        divisor = '1100000000101000100000001'
    elif CRC_type == 'CRC-16':
        divisor = '11000000000000101'
    elif CRC_type == 'ReCRC-16':
        divisor = '10100000000000011'
    elif CRC_type == 'CRC-8':
        divisor = '111010101'
    elif CRC_type == 'CRC-4':
        divisor = '11111'

    if int(div(codeword, divisor)) == 0:
        return 'Valid'  
    else:
        return 'Invalid'

if __name__ == '__main__':
    CRC_types = ['CRC-4', 'CRC-8', 'ReCRC-16', 'CRC-16', 'CRC-24', 'CRC-32']
    dataword = '11001010'

    for Type in CRC_types:
        codeword = CRC_gen(dataword,Type)
        received_5 = unreliable_transmission(codeword, 0.05)
        received_10 = unreliable_transmission(codeword, 0.1)
        received_20 = unreliable_transmission(codeword, 0.2)
        validity_5 = CRC_check(received_5, Type)
        validity_10 = CRC_check(received_10, Type)
        validity_20 = CRC_check(received_20, Type)

        print('--- ' + Type + ' ---')
        print('Dataword: ' + dataword)
        print('Send: ' + codeword)
        print(f'Received (5% Error):  {received_5} ({validity_5})')
        print(f'Received (10% Error): {received_10} ({validity_10})')
        print(f'Received (20% Error): {received_20} ({validity_20})\n')  