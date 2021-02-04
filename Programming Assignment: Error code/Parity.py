from random import randrange

def unreliable_transmission(in_frame, p):
    '''
    :param in_frame: Bit string of any size up to k (input frame)
    :param p: Probability of having a bit in error (p)
    :return: Bit string of size k defined by the input bit string (output frame)
    '''
    out_frame = ''
    if isinstance(in_frame, list):
        in_frame = ''.join(in_frame)

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

def parity_gen(dataword, parity_type, size=None):
    ''' 
    :param dataword: A bit string of any size up to k (input frame) where k ≥ 9 (input frame)
    :param parity_type: Type of parity (even, odd, two-dimensional-even, two-dimensional-odd)
    :param size: Size of two-dimensional block for dataword (if two-dimensional parity bit is used)
    :return: A code word based on the type of parity
    '''
    sum = 0    

    if parity_type == 'even':
        codeword = dataword
        for bit in codeword:
            sum += int(bit)
        if sum%2 == 0: # total number of 1s is even
            codeword += '0'
        else: # total number of 1s is odd
            codeword += '1'

    elif parity_type == 'odd':
        codeword = dataword
        for bit in codeword:
            sum += int(bit)
        if sum%2 == 0: # total number of 1s is even
            codeword += '1'
        else: # total number of 1s is odd
            codeword += '0'

    elif parity_type == 'two-dimensional-even':
        codeword = []
        temp = ''
        count = 0
        for i,bit in enumerate(dataword):
            temp += bit
            count += 1
            if (i+1)%size == 0:
                for bit in temp:
                    sum += int(bit)
                if sum%2 == 0: # total number of 1s is even
                    temp += '0'
                else: # total number of 1s is odd
                    temp += '1'

                codeword.append(temp)
                sum = 0
                temp = ''
                count = 0
        
        finalTemp = ''
        for col in range(size+1):
            temp = [row[col] for row in codeword]
            for bit in temp:
                sum += int(bit)
            if sum%2 == 0: # total number of 1s is even
                # temp += '0'
                finalTemp += '0'
            else: # total number of 1s is odd
                # temp += '1'
                finalTemp += '1'
            sum = 0            
            # print(temp)

        codeword.append(finalTemp)

    elif parity_type == "two-dimensional-odd":
        codeword = []
        temp = ''
        count = 0
        for i,bit in enumerate(dataword):
            temp += bit
            count += 1
            if (i+1)%size == 0:
                for bit in temp:
                    sum += int(bit)
                if sum%2 == 0: # total number of 1s is even
                    temp += '1'
                else: # total number of 1s is odd
                    temp += '0'

                codeword.append(temp)
                sum = 0
                temp = ''
                count = 0
        finalTemp = ''
        for col in range(size+1):
            temp = [row[col] for row in codeword]
            for bit in temp:
                sum += int(bit)
            if sum%2 == 0: # total number of 1s is even
                finalTemp += '1'
            else: # total number of 1s is odd
                finalTemp += '0'
            sum = 0            

        codeword.append(finalTemp)
    return codeword

def parity_check(codeword, parity_type, size=None):
    ''' 
    :param codeword: A bit string of any size up to k (codeword).
    :param parity_type: Type of parity (even, odd, two-dimensional-even, two-dimensional-odd).
    :param size: Size of two-dimensional block for dataword (if two-dimensional parity bit is used).
    '''
    sum = 0

    if parity_type.lower() == 'even':
        for bit in codeword:
            sum += int(bit)
        if sum%2 == 0:
            return 'Valid'
        else:
            return 'Invalid'

    elif parity_type.lower() == 'odd':
        for bit in codeword:
            sum += int(bit)
        if sum%2 == 0:
            return 'Invalid'
        else:
            return 'Valid'

    elif parity_type == 'two-dimensional-even':
        temp = [codeword[i:i+size+1] for i in range(0, len(codeword), size+1)]
        # row check
        for row in temp:
            sum = 0
            for bit in row:
                sum += int(bit)
            if sum%2 != 0: # total number of 1s is odd
                return 'Invalid'
        # column check
        for col in range(size+1):
            finalTemp = [row[col] for row in temp]
            # print(finalTemp)
            sum = 0
            for bit in finalTemp:
                sum += int(bit)
            if sum%2 != 0: # total number of 1s is odd
                return 'Invalid'
        
        return 'Valid'

    elif parity_type == 'two-dimensional-odd':
        temp = [codeword[i:i+size+1] for i in range(0, len(codeword), size+1)]
        # row check
        for row in temp:
            sum = 0
            for bit in row:
                sum += int(bit)
            if sum%2 == 0: # total number of 1s is even
                return 'Invalid'
        print(temp)
        # column check
        for col in range(size+1):
            finalTemp = [row[col] for row in temp]
            sum = 0
            for bit in finalTemp:
                sum += int(bit)
            if sum%2 == 0: # total number of 1s is even
                return 'Invalid'
        
        return 'Valid' 


if __name__ == '__main__':
    dataword_input = '1100010101001'
    dataword = dataword_input.replace(' ', '')

    even_parity = parity_gen(dataword, 'even')
    even_received_5 = unreliable_transmission(even_parity, 0.05)
    even_received_10 = unreliable_transmission(even_parity, 0.1)
    even_received_20 = unreliable_transmission(even_parity, 0.2)
    even_validity_5 = parity_check(even_received_5, 'even')
    even_validity_10 = parity_check(even_received_10, 'even')
    even_validity_20 = parity_check(even_received_20, 'even')
    print('--- Even ---')
    print('Dataword: ' + dataword_input)
    print('Send: ' + even_parity)
    print(f'Received (5% Error):  {even_received_5} ({even_validity_5})')
    print(f'Received (10% Error): {even_received_10} ({even_validity_10})')
    print(f'Received (20% Error): {even_received_20} ({even_validity_20})\n')

    odd_parity = parity_gen(dataword, 'odd')
    odd_received_5 = unreliable_transmission(odd_parity, 0.05)
    odd_received_10 = unreliable_transmission(odd_parity, 0.1)
    odd_received_20 = unreliable_transmission(odd_parity, 0.2)
    odd_validity_5 = parity_check(odd_received_5, 'odd')
    odd_validity_10 = parity_check(odd_received_10, 'odd')
    odd_validity_20 = parity_check(odd_received_20, 'odd')
    print('--- Odd ---')
    print('Dataword: ' + dataword_input)
    print('Send: ' + odd_parity)
    print(f'Received (5% Error):  {odd_received_5} ({odd_validity_5})')
    print(f'Received (10% Error): {odd_received_10} ({odd_validity_10})')
    print(f'Received (20% Error): {odd_received_20} ({odd_validity_20})\n')
    
    dataword_input = '1001011 1000000 1001111'
    dataword = dataword_input.replace(' ', '')
    size = 7

    even2D_parity = parity_gen(dataword, 'two-dimensional-even', size)
    even2D_received_5 = unreliable_transmission(even2D_parity, 0.05)
    even2D_received_10 = unreliable_transmission(even2D_parity, 0.1)
    even2D_received_20 = unreliable_transmission(even2D_parity, 0.2)
    even2D_validity_5 = parity_check(even2D_received_5, 'two-dimensional-even', size)
    even2D_validity_10 = parity_check(even2D_received_10, 'two-dimensional-even', size)
    even2D_validity_20 = parity_check(even2D_received_20, 'two-dimensional-even', size)
    print('--- Two Dimensional Even ---')
    print('Dataword: ' + dataword_input)
    print('Send:', even2D_parity)
    print(f'Received (5% Error):  {[even2D_received_5[i:i+size+1] for i in range(0, len(even2D_received_5), size+1)]} ({even2D_validity_5})')
    print(f'Received (10% Error): {[even2D_received_10[i:i+size+1] for i in range(0, len(even2D_received_10), size+1)]} ({even2D_validity_10})')
    print(f'Received (20% Error): {[even2D_received_20[i:i+size+1] for i in range(0, len(even2D_received_20), size+1)]} ({even2D_validity_20})\n')

    odd2D_parity = parity_gen(dataword, 'two-dimensional-odd', size)
    odd2D_received_5 = unreliable_transmission(odd2D_parity, 0.05)
    odd2D_received_10 = unreliable_transmission(odd2D_parity, 0.1)
    odd2D_received_20 = unreliable_transmission(odd2D_parity, 0.2)
    odd2D_validity_5 = parity_check(odd2D_received_5, 'two-dimensional-odd', size)
    odd2D_validity_10 = parity_check(odd2D_received_10, 'two-dimensional-odd', size)
    odd2D_validity_20 = parity_check(odd2D_received_20, 'two-dimensional-odd', size)
    print('--- Two Dimensional Odd ---')
    print('Dataword: ' + dataword_input)
    print('Send:', odd2D_parity)
    print(f'Received (5% Error):  {[odd2D_received_5[i:i+size+1] for i in range(0, len(odd2D_received_5), size+1)]} ({odd2D_validity_5})')
    print(f'Received (10% Error): {[odd2D_received_10[i:i+size+1] for i in range(0, len(odd2D_received_10), size+1)]} ({odd2D_validity_10})')
    print(f'Received (20% Error): {[odd2D_received_20[i:i+size+1] for i in range(0, len(odd2D_received_20), size+1)]} ({odd2D_validity_20})\n')