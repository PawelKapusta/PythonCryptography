import numpy as np

print("\nTask1\n--------------------------------------------------------")

def add_GF(p,q):
    binary_operator = int(p,2) ^ int(q,2)
    final = format(binary_operator, 'b')
    return final

print("\nadd_GF\n")

print(add_GF('110','11')=='101')
print(add_GF('110','101')=='11')

def bin2hex(bin_str,pad):
    return format(int(bin_str, 2), '0' + str(pad) + 'x')

print("\nbin2hex\n")
print(bin2hex('1101',2)=='0d')
print(bin2hex('11010011',2)=='d3')
print(bin2hex('1111111',3)=='07f')
print(bin2hex('1',1)=='1')

print("\nTask2\n--------------------------------------------------------")

def multiply(p,q): # returns multiplication of two polynomials
    p1 = np.poly1d(list(map(int, p))) # We use numpy function to
    p2 = np.poly1d(list(map(int, q)))

    list_1 = list(np.polymul(p1, p2)) # Finds the polynomial resulting from the multiplication of the two input polynomials.
    final = ''.join(str(abs(int(x))) for x in list_1)

    new_final = ''
    for x in final: # We can get in our result polynomial with higher factor than multiplier polynomials so we have to divide it modulo
        if int(x) > 1 and int(x) % 2 == 0:
           new_final += '0'
        elif int(x) > 1 and int(x) % 2 != 0:
            new_final += '1'
        else:
            new_final += x

    return new_final

print(multiply('10','1')=='10')
print(multiply('10','10')=='100')
print(multiply('110','11')=='1010')

print("\nTask3\n--------------------------------------------------------")

def divide(p,q): # returns result of deviation two polynomials
    p1 = np.poly1d(list(map(int, p)))
    p2 = np.poly1d(list(map(int, q)))

    list_1 = list(np.polydiv(p1, p2))
    res = list_1[0]
    rem = list_1[1]

    new_res = ''.join(str(abs(int(x))) for x in res)
    new_rem = ''.join(str(abs(int(x))) for x in rem)

    final_res = ''
    for x in new_res: # We can get in our result polynomial with higher factor than multiplier polynomials so we have to divide it modulo
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

print(divide('1011','11')==('110','1'))
print(divide('1010','110')==('11','0'))
print(divide('1111','10')==('111','1'))

print("\nTask4\n--------------------------------------------------------")

def multiply_GF(p,q): # mnożymy wielomiany w ciele  GF
    multi = multiply(p, q)
    _, rest = divide(multi, '100011011') # divide with rest
    return rest # we return the rest of this polynomial

print(multiply_GF('1101','1')=='1101')
print(multiply_GF('1101','10')=='11010')
print(multiply_GF('10000000','10')=='11011')
print(multiply_GF('11100101','1010')=='10111000')

print("\nTask5\n--------------------------------------------------------")

def EEA_GF(r0,r1): # Rozszerzony Algorytm Euklidesa
    (x0, x1, y0, y1) = ('1', '0', '0', '1')
    while r1 != '0': # we are using previous functions
        res, rem = divide(r0, r1)
        (q, r0, r1) = (res, r1, rem)
        (x0, x1) = (x1, add_GF(x0, multiply_GF(q, x1))) # we are finding polynomials s and t as in s⊙p⊕t⊙q=NWD(p,q) .
        (y0, y1) = (y1, add_GF(y0, multiply_GF(q, y1)))
    return x0, y0
    pass

print(EEA_GF('11010101','10010111')==('11001', '10100'))
print(EEA_GF('11110000','11001011')==('1000000', '1010111'))


print("\nTask6\n--------------------------------------------------------")

def inverse_GF(p):
    pol, _ = EEA_GF(p, '100011011') # finding rest using x8+x4+x3+x+1 polynomial and previous function
    return pol

print(inverse_GF('11001010')=='1010011')
print(inverse_GF('1100101')=='10100110')


print("\nTask7\n--------------------------------------------------------")

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

A=[[1, 1, 1, 1, 1, 0, 0, 0],
   [0, 1, 1, 1, 1, 1, 0, 0],
   [0, 0, 1, 1, 1, 1, 1, 0],
   [0, 0, 0, 1, 1, 1, 1, 1],
   [1, 0, 0, 0, 1, 1, 1, 1],
   [1, 1, 0, 0, 0, 1, 1, 1],
   [1, 1, 1, 0, 0, 0, 1, 1],
   [1, 1, 1, 1, 0, 0, 0, 1]]

v=[0, 1, 1, 0, 0, 0, 1, 1]

def substitute(p):
    reversep = list(map(int, list(inverse_GF(p)))) # we take reverse in GF 8-bits input
    while len(reversep) < 8:
        reversep.insert(0, 0)
    q = list(np.add(np.matmul(A,reversep), v)) #Dokonujemy transformacji afinicznej za pomocą macierzy  A  oraz wektora  v
    for i in range(len(q)): # ciąg bitów  q  jest naszym wynikiem, ten ciąg właśnie znajduje się na odpowiendnim dla  p  miejscu S-Boxa.
        q[i] = q[i] % 2
    q = ''.join(str(l) for l in q)

    return bin2hex(q,2)

print(substitute('11010101')=='03')
print(substitute('01010001')=='d1')
print(substitute('11011101')=='c1')
print(substitute('11101100')=='ce')

s_box=[]
n = 8
arr = [None] * n
temp = []
def generate_binary_strings(bit_count):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')
    genbin(bit_count)
    return binary_strings

binary_strings = generate_binary_strings(8)

for i in range(len(binary_strings)):
    temp.append(substitute(binary_strings[i]))

for i in range(len(binary_strings)):
    temp[i] = substitute(binary_strings[i])

s_box = [temp[x:x+16] for x in range(0, len(temp), 16)]
print("\ns_box==SBox:")
print(s_box==SBox)