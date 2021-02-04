from random import randrange

def unreliable_transmission(in_frame, p):
    ''' 
    :param in_frame: Bit string of any size up to k (input frame)
    :param p: Probability of having a bit in error (p)
    :return: Bit string of size k defined by the input bit string (output frame)
    '''
    out_frame = ''

    error_occur = False
    for bit in in_frame:
        randomNumber = randrange(100) + 1
        if randomNumber <= p*100 and not error_occur:
            if bit == '0':
                out_frame += '1'
            else:
                out_frame += '0'
            error_occur = True
        else:
            out_frame += bit

    return out_frame

def reverse_string(s):
    return s[::-1]

def Hamming_gen(dataword): 
    '''
    :param dataword: A dataword
    :return: A codeword based on Hamming code
    '''
    # 2 ^ r >= m + r + 1 
    # Find how many R need (Redundant Bits)
    m = len(dataword) #length of data
    for i in range(m): 
        if(2**i >= m + i + 1): 
            r = i #number of parity bit
            break
    
    #insert redundant bit into data
    p1 = 0
    p2 = 1 #p1, p2 is here to point to the position 
    Ndata = '' 
  
    # If position is power of 2 then insert '0' 
    for i in range(1, m + r+1): 
        if(i == 2**p1): 
            Ndata = Ndata + '0'
            p1 += 1
        else: 
            Ndata = Ndata + dataword[-1 * p2] 
            p2 += 1
  
    # reverse the result (we calculate it backward)
    Ndata = reverse_string(Ndata)
    
    n = len(Ndata) #Total number of bit
  
    # Find parity bit
    for i in range(r): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(Ndata[-1 * j]) 
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n) 
        Ndata = Ndata[:n-(2**i)] + str(val) + Ndata[n-(2**i)+1:] 
    return Ndata
    
def Hamming_check(codeword): 
    '''
    :param codeword: codeword
    :return: Position of error (in case of a single bit error, return -1 if there is no error found)
    '''
    n = len(codeword)
    #find how many R need
    for i in range(n):
        if(2**i>n):
            r = i
            break
            
    res = 0
    
    # Find parity bits
    for i in range(r): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(codeword[-1 * j]) 
  
        # Create wrong position
        res = res + val*(10**i) 
  
    # Change binary to decimal 
    pos = int(str(res), 2)
    if pos == 0:
        return -1
    else:
        return pos

if __name__ == '__main__':
    dataword = '1001110'

    codeword = Hamming_gen(dataword)
    received_5 = unreliable_transmission(codeword, 0.05)
    received_10 = unreliable_transmission(codeword, 0.1)
    received_20 = unreliable_transmission(codeword, 0.2)
    error_pos_5 = Hamming_check(received_5)
    error_pos_10 = Hamming_check(received_10)
    error_pos_20 = Hamming_check(received_20)

    print('--- Hamming Code ---')
    print('Dataword: ' + dataword)
    print('Send: ' + codeword)
    print(f'Received (5% Error):  {received_5} (Error Position {error_pos_5})')
    print(f'Received (10% Error): {received_10} (Error Position {error_pos_10})')
    print(f'Received (20% Error): {received_20} (Error Position {error_pos_20})')
    