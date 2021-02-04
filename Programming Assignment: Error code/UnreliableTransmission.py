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

if __name__ == '__main__':
    codeword = '11010101'

    print('Send: ' + codeword)
    print('--- Sent data 100 times over unreliable transmission (p = 0.05) ---')
    count_err = 0
    for i in range(100):
        received = unreliable_transmission(codeword, 0.05)
        print(f'Received #{i+1}: {received}', end = ' ')
        if(received == codeword):
            print('(No errors)')
        else:
            err = 0
            for i in range(len(codeword)):
                if(codeword[i] != received[i]):
                    err += 1
            print(f'{err} erroneous bit(s))')
            count_err += err
            perc = count_err/800*100
    print(f'Error ratio (from 800 bits sent) = {count_err}:800 ({count_err/800*100}%) where p = 0.05')

    print('\n--- Sent data 100 times over unreliable transmission (p = 0.1) ---')
    count_err = 0
    for i in range(100):
        received = unreliable_transmission(codeword, 0.1)
        print(f'Received #{i+1}: {received}', end = ' ')
        if(received == codeword):
            print('(No errors)')
        else:
            err = 0
            for i in range(len(codeword)):
                if(codeword[i] != received[i]):
                    err += 1
            print(f'{err} erroneous bit(s))')
            count_err += err
            perc = count_err/800*100
    print(f'Error ratio (from 800 bits sent) = {count_err}:800 ({count_err/800*100}%) where p = 0.1')

    print('\n--- Sent data 100 times over unreliable transmission (p = 0.2) ---')
    count_err = 0
    for i in range(100):
        received = unreliable_transmission(codeword, 0.2)
        print(f'Received #{i+1}: {received}', end = ' ')
        if(received == codeword):
            print('(No errors)')
        else:
            err = 0
            for i in range(len(codeword)):
                if(codeword[i] != received[i]):
                    err += 1
            print(f'{err} erroneous bit(s))')
            count_err += err
            perc = count_err/800*100
    print(f'Error ratio (from 800 bits sent) = {count_err}:800 ({count_err/800*100}%) where p = 0.2')

    