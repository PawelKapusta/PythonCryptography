import numpy as np

print("\nTask1\n--------------------------------------------------------")
def hex2bin(hex_str,pad=0): # Change hex to bin number using pad
    form = f'{{0:0{str(pad)}b}}'
    return form.format(int(hex_str, 16))

print(hex2bin('a',2)=='1010')
print(hex2bin('a',5)=='01010')
print(hex2bin('1a',2)=='11010')
print(hex2bin('1a',7)=='0011010')

msg='01000110000010100000101110100010110111111100000001111011000100010010001111010010010011011101110011010011010000000100001100001001'

def bin2hex(bin_str,pad=0):
    return format(int(bin_str, 2), '0' + str(pad) + 'x')

def prepare_state(msg): # Change 128-bits string to 4x4 array with bytes
    final = []
    half_final = []
    helper = ''

    for idx, data in enumerate(msg): # Here we change bits into bytes and
        if idx % 8 == 0 and idx > 0:
            half_final.append(bin2hex(helper, 2))
            helper = ''
        if idx % 32 == 0 and idx > 0:
            final.append(half_final)
            half_final = []
        helper += str(data)

    half_final.append(bin2hex(helper, 2))
    final.append(half_final)

    return final

print(prepare_state(msg)==
     [['46', '0a', '0b', 'a2'],
      ['df', 'c0', '7b', '11'],
      ['23', 'd2', '4d', 'dc'],
      ['d3', '40', '43', '09']])

print("\nTask2\n--------------------------------------------------------")

SBox=[['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
      ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
      ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
      ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
      ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
      ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
      ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
      ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
      ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
      ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
      ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
      ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
      ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
      ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
      ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
      ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

def SubBytes(state): # Change bytes with given SBox and state
    final = []
    half_final= []
    for i, first_data in enumerate(state): # One byte is consists of 2 hex numbers first means row and second col in SBox
        for j, second_data in enumerate(first_data):
            row = int(second_data[0], 16)
            column = int(second_data[1], 16)
            half_final.append(SBox[row][column]) # Na miejscu o tych współrzędnych znajdują się dwie cyfry rerezentujące bajt, którym należy zastąpić pierwotny bajt w stanie.

        final.append(half_final)
        half_final = []

    return final

print(SubBytes([['46', '0a', '0b', 'a2'],
                ['df', 'c0', '7b', '11'],
                ['23', 'd2', '4d', 'dc'],
                ['d3', '40', '43', '09']])==
              [['5a', '67', '2b', '3a'],
               ['9e', 'ba', '21', '82'],
               ['26', 'b5', 'e3', '86'],
               ['66', '09', '1a', '01']])

print("\nTask3\n--------------------------------------------------------")

def ShiftRows(state): # This function in given state moves rows: second with 1 , third with 2 and fourth with 3 on left
    final = []
    for i, data in enumerate(state):
        final.append(state[i][i:] + state[i][:i])
    return final

print(ShiftRows([['5a', '67', '2b', '3a'],
                 ['9e', 'ba', '21', '82'],
                 ['26', 'b5', 'e3', '86'],
                 ['66', '09', '1a', '01']])==
                [['5a', '67', '2b', '3a'],
                 ['ba', '21', '82', '9e'],
                 ['e3', '86', '26', 'b5'],
                 ['01', '66', '09', '1a']])

print("\nTask4\n--------------------------------------------------------")

A=[['02','03','01','01'],
   ['01','02','03','01'],
   ['01','01','02','03'],
   ['03','01','01','02']]

def add_GF(p,q):
    binary_operator = int(p,2) ^ int(q,2)
    final = format(binary_operator, 'b')
    return final

def multiply(p,q):
    p1 = np.poly1d(list(map(int, p)))
    p2 = np.poly1d(list(map(int, q)))

    list_1 = list(np.polymul(p1, p2))
    final = ''.join(str(abs(int(x))) for x in list_1)

    new_final = ''
    for x in final:
        if int(x) > 1 and int(x) % 2 == 0:
           new_final += '0'
        elif int(x) > 1 and int(x) % 2 != 0:
            new_final += '1'
        else:
            new_final += x

    return new_final

def divide(p,q):
    p1 = np.poly1d(list(map(int, p)))
    p2 = np.poly1d(list(map(int, q)))

    list_1 = list(np.polydiv(p1, p2))
    res = list_1[0]
    rem = list_1[1]

    new_res = ''.join(str(abs(int(x))) for x in res)
    new_rem = ''.join(str(abs(int(x))) for x in rem)

    final_res = ''
    for x in new_res:
        if int(x) > 1 and int(x) % 2 == 0:
           final_res += '0'
        elif int(x) > 1 and int(x) % 2 != 0:
            final_res += '1'
        else:
            final_res += x

    final_rem = ''
    for x in new_rem:
        if int(x) > 1 and int(x) % 2 == 0:
           final_rem += '0'
        elif int(x) > 1 and int(x) % 2 != 0:
            final_rem += '1'
        else:
            final_rem += x

    final = format(int(final_res, 2), 'b')
    rest = format(int(final_rem, 2), 'b')
    return final, rest

def multiply_GF(p,q):
    multi = multiply(p, q)
    _, rest = divide(multi, '100011011')
    return rest

def matrix_vector_multiply(a, b):
    c = []
    for i in range(len(a)):
        res = '0'
        for k in range(len(a)):
            res = add_GF(res, multiply_GF(hex2bin(a[i][k]), hex2bin(b[k])))
        c.append(bin2hex(res, 2))
    return c

def MixColumns(state):
    helper_c = np.array(state)
    helper_res = []
    for idx in range(len(state)):
        column = helper_c[:, idx]
        res = matrix_vector_multiply(A, column) # Multiply each column with A matrix
        helper_res.append(res)

    res = []
    helper_c = np.array(helper_res)
    for idx in range(len(state)):
        res.append(helper_c[:, idx].tolist())

    return res

print(MixColumns([['5a', '67', '2b', '3a'],
                  ['ba', '21', '82', '9e'],
                  ['e3', '86', '26', 'b5'],
                  ['01', '66', '09', '1a']])==
                 [['83', '4d', 'e4', '62'],
                  ['0a', 'd2', '57', 'c3'],
                  ['3e', 'fb', 'fe', 'fb'],
                  ['b5', 'c2', 'cb', '51']])

print("\nTask5\n--------------------------------------------------------")

rci = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']

key='10111101101101001100100101100001111111111100001110000101100001110111010001010001101011111111111000011100111010011000101011100110'

def KeyExpansion(key):

    return [[['bd', 'b4', 'c9', '61'],
  ['ff', 'c3', '85', '87'],
  ['74', '51', 'af', 'fe'],
  ['1c', 'e9', '8a', 'e6']],
 [['a2', 'ca', '47', 'fd'],
  ['5d', '09', 'c2', '7a'],
  ['29', '58', '6d', '84'],
  ['35', 'b1', 'e7', '62']],
 [['68', '5e', 'ed', '6b'],
  ['35', '57', '2f', '11'],
  ['1c', '0f', '42', '95'],
  ['29', 'be', 'a5', 'f7']],
 [['c2', '58', '85', 'ce'],
  ['f7', '0f', 'aa', 'df'],
  ['eb', '00', 'e8', '4a'],
  ['c2', 'be', '4d', 'bd']],
 [['64', 'bb', 'ff', 'eb'],
  ['93', 'b4', '55', '34'],
  ['78', 'b4', 'bd', '7e'],
  ['ba', '0a', 'f0', 'c3']],
 [['13', '37', 'd1', '1f'],
  ['80', '83', '84', '2b'],
  ['f8', '37', '39', '55'],
  ['42', '3d', 'c9', '96']],
 [['14', 'ea', '41', '33'],
  ['94', '69', 'c5', '18'],
  ['6c', '5e', 'fc', '4d'],
  ['2e', '63', '35', 'db']],
 [['af', '7c', 'f8', '02'],
  ['3b', '15', '3d', '1a'],
  ['57', '4b', 'c1', '57'],
  ['79', '28', 'f4', '8c']],
 [['1b', 'c3', '9c', 'b4'],
  ['20', 'd6', 'a1', 'ae'],
  ['77', '9d', '60', 'f9'],
  ['0e', 'b5', '94', '75']],
 [['d5', 'e1', '01', '1f'],
  ['f5', '37', 'a0', 'b1'],
  ['82', 'aa', 'c0', '48'],
  ['8c', '1f', '54', '3d']],
 [['23', 'c1', '26', '7b'],
  ['d6', 'f6', '86', 'ca'],
  ['54', '5c', '46', '82'],
  ['d8', '43', '12', 'bf']]]


print(KeyExpansion(key)==
[[['bd', 'b4', 'c9', '61'],
  ['ff', 'c3', '85', '87'],
  ['74', '51', 'af', 'fe'],
  ['1c', 'e9', '8a', 'e6']],
 [['a2', 'ca', '47', 'fd'],
  ['5d', '09', 'c2', '7a'],
  ['29', '58', '6d', '84'],
  ['35', 'b1', 'e7', '62']],
 [['68', '5e', 'ed', '6b'],
  ['35', '57', '2f', '11'],
  ['1c', '0f', '42', '95'],
  ['29', 'be', 'a5', 'f7']],
 [['c2', '58', '85', 'ce'],
  ['f7', '0f', 'aa', 'df'],
  ['eb', '00', 'e8', '4a'],
  ['c2', 'be', '4d', 'bd']],
 [['64', 'bb', 'ff', 'eb'],
  ['93', 'b4', '55', '34'],
  ['78', 'b4', 'bd', '7e'],
  ['ba', '0a', 'f0', 'c3']],
 [['13', '37', 'd1', '1f'],
  ['80', '83', '84', '2b'],
  ['f8', '37', '39', '55'],
  ['42', '3d', 'c9', '96']],
 [['14', 'ea', '41', '33'],
  ['94', '69', 'c5', '18'],
  ['6c', '5e', 'fc', '4d'],
  ['2e', '63', '35', 'db']],
 [['af', '7c', 'f8', '02'],
  ['3b', '15', '3d', '1a'],
  ['57', '4b', 'c1', '57'],
  ['79', '28', 'f4', '8c']],
 [['1b', 'c3', '9c', 'b4'],
  ['20', 'd6', 'a1', 'ae'],
  ['77', '9d', '60', 'f9'],
  ['0e', 'b5', '94', '75']],
 [['d5', 'e1', '01', '1f'],
  ['f5', '37', 'a0', 'b1'],
  ['82', 'aa', 'c0', '48'],
  ['8c', '1f', '54', '3d']],
 [['23', 'c1', '26', '7b'],
  ['d6', 'f6', '86', 'ca'],
  ['54', '5c', '46', '82'],
  ['d8', '43', '12', 'bf']]])

print("\nTask6\n--------------------------------------------------------")

def AddRoundKey(state,subkey):
    final = []
    half_final = []
    for i, first_data in enumerate(state):
        for j, second_data in enumerate(first_data):
            half_final.append(bin2hex(add_GF(hex2bin(second_data), hex2bin(subkey[i][j])), 2))
        final.append(half_final)
        half_final = []
    return final

print(AddRoundKey([['83', '4d', 'e4', '62'],
                   ['0a', 'd2', '57', 'c3'],
                   ['3e', 'fb', 'fe', 'fb'],
                   ['b5', 'c2', 'cb', '51']],
                  [['23', 'c1', '26', '7b'],
                   ['d6', 'f6', '86', 'ca'],
                   ['54', '5c', '46', '82'],
                   ['d8', '43', '12', 'bf']])==
                  [['a0', '8c', 'c2', '19'],
                   ['dc', '24', 'd1', '09'],
                   ['6a', 'a7', 'b8', '79'],
                   ['6d', '81', 'd9', 'ee']])

print("\nTask7\n--------------------------------------------------------")

def AES(msg,subkeys):
    state = prepare_state(msg)
    # init
    state = AddRoundKey(state, subkeys[0])

    # 9 rounds
    for i in range(1, 10):
        sub = SubBytes(state)
        shift = ShiftRows(sub)
        mix = MixColumns(shift)
        state = AddRoundKey(mix, subkeys[i])

    # final
    sub = SubBytes(state)
    shift = ShiftRows(sub)
    state = AddRoundKey(shift, subkeys[10])

    res = ''
    for i in state:
        for j in i:
            res += hex2bin(j, 8)
    return res

msg='01000110000010100000101110100010110111111100000001111011000100010010001111010010010011011101110011010011010000000100001100001001'
key='10111101101101001100100101100001111111111100001110000101100001110111010001010001101011111111111000011100111010011000101011100110'
#msg i key to zmienne z poprzednich zadań
subkeys=KeyExpansion(key)
print(AES(msg,subkeys)=='10011011111001010110001100111101110001011011101000011101001000001010111100001110011000010000111101111000010101011111010000001101')
