import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import IPython.display

print("\nTask1\n--------------------------------------------------------")

def dec2bin(dec_str,pad):
    return format(int(dec_str),'0'+str(pad)+'b')

img=Image.open('miki.png')
arr=np.array(img).ravel()
arr_bin=[dec2bin(d,pad='8') for d in arr]
bits=''.join(arr_bin)
img

key='0111101000001010110010000001010101111111100000000000101000110001'

PC1 = [56, 48, 40, 32, 24, 16,  8,  0, 57, 49, 41, 33, 25, 17,  9,  1, 58,
       50, 42, 34, 26, 18, 10,  2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22,
       14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 60, 52, 44, 36, 28, 20, 12,
        4, 27, 19, 11,  3]

shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

PC2=[13, 16, 10, 23,  0,  4,  2, 27, 14,  5, 20,  9, 22, 18, 11,  3,
     25, 7, 15,  6, 26, 19, 12,  1, 40, 51, 30, 36, 46, 54, 29, 39,
     50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

E = [31,  0,  1,  2,  3,  4,  3,  4,  5,  6,  7,  8,  7,  8,  9, 10, 11,
       12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22,
       23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31,  0]

SBox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

        [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],

        [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],

        [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],

        [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],

        [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],

        [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

P = [ 15,  6, 19, 20, 28, 11, 27, 16,  0, 14, 22, 25,  4, 17, 30,  9,  1,
        7, 23, 13, 31, 26,  2,  8, 18, 12, 29,  5, 21, 10,  3, 24]

IP = [57, 49, 41, 33, 25, 17,  9,  1, 59, 51, 43, 35, 27, 19, 11,  3, 61,
       53, 45, 37, 29, 21, 13,  5, 63, 55, 47, 39, 31, 23, 15,  7, 56, 48,
       40, 32, 24, 16,  8,  0, 58, 50, 42, 34, 26, 18, 10,  2, 60, 52, 44,
       36, 28, 20, 12,  4, 62, 54, 46, 38, 30, 22, 14,  6]

FP = [39,  7, 47, 15, 55, 23, 63, 31, 38,  6, 46, 14, 54, 22, 62, 30, 37,
        5, 45, 13, 53, 21, 61, 29, 36,  4, 44, 12, 52, 20, 60, 28, 35,  3,
       43, 11, 51, 19, 59, 27, 34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,
        9, 49, 17, 57, 25, 32,  0, 40,  8, 48, 16, 56, 24]

def bin2dec(bin_str):
    return int(bin_str, 2) # The int() method returns an integer object from any number or string. No parameters) returns 0
                           # (If base given) treats the string in the given base (0, 2, 8, 10, 16)

def permute(k,perm): # go through perm array get indexes and append to string elements from k array
    final = []
    for i in perm:
        final.append(k[i])
    return ''.join(final)

def shift_left(tab,n):
    final = tab[n:] + tab[:n]
    return final

def key_schedule(key): # Gets 64- bits key and returns list of 16 generated subkeys like bits string
                       # Algorithm as it is shown on schedule https://cs.if.uj.edu.pl/edu/kryptografia/Lista3.html
    final = []
    new_key = permute(key, PC1)
    left,right = new_key[:len(new_key)//2], new_key[len(new_key)//2:]
    for i in shift_table:
        left = shift_left(left, i)
        right = shift_left(right, i)

        new_key = left + right
        key = permute(new_key, PC2)
        final.append(key)
    return final

def xor(bin_str1,bin_str2):
    binary_operator = int(bin_str1,2) ^ int(bin_str2,2)
    final = format(binary_operator, '0' + str(len(bin_str1)) + 'b')
    return final

def F(right, subkey): # gets 32 bits string and 48 bits subkey string -> returns 32 bits string
    returned_permute_function = permute(right, E) # returns 48 bits string
    returned_xor_function = xor(returned_permute_function, subkey) # add subkey with xor function
    final = ''
    for i in range(0, 8): # because Sbox has 8 smaller lists
        subgroup = returned_xor_function[i*6 : (i+1)*6] # divide it into 8 groups, every with 6 bits
        binary_number = subgroup[0] + subgroup[-1] # we take first and last bits in each list -> means row's number in matrix
        first_decimal = bin2dec(binary_number) # convert to decimal number
        binary_number = subgroup[1:-1] # we take 4 bits in the middle -> means column's number in matrix
        second_decimal = bin2dec(binary_number) # convert to decimal number
        find_element = dec2bin(SBox[i][first_decimal][second_decimal], 4) # we are finding this 4 bits element
        final = final + find_element # we append all to one 32 bits string
    return permute(final, P) # and we return the result of permute function of P

def Feistel(message, subkeys, F): # message 64 bits string message , 16 subkeys bits string, F a function -> returns encoded bits string message
    for i in range(16): # 16 times
        left,right = message[:len(message)//2], message[len(message)//2:]
        returned_values = F(right, subkeys[i])
        left = xor(left, returned_values)
        if i < 15: # in last round miss this point
            left, right = right, left
        message = left + right
    return message

def DES(message, subkeys): # implementation of DES code, message is 64 bits string and 16 subkeys 48 bits string each -> returns 64 bits string after encoded
    returned_permute_function = permute(message, IP)
    returned_feistel = Feistel(returned_permute_function, subkeys, F)
    return permute(returned_feistel, FP)

img_string = ''
start = 0
end = 64
iteration_size = int(len(bits) / 64)

for _ in range(iteration_size):
    sub_bits = bits[start:end]

    encoded = DES(sub_bits, key_schedule(key))
    img_string += encoded

    start = end
    end = end + 64

def split_img(img_bin,n):
    img_split=[]
    for i in range(0, len(img_bin), n):
        img_split.append(img_bin[i:i+n])
    return img_split

img=np.array([bin2dec(b) for b in split_img(img_string,8)]).reshape(np.array(img).shape)
Image.fromarray(np.uint8(np.array(img))).show()

print("\nTask2\n--------------------------------------------------------")

iv='0011111111001100000111011100110100100101010100000111010001000110'
msg='1000110001101011011101110010100111101111101100111100001010100001011111110100000100100000111011001011000001011100110111101111110100000000100101011101110010000000110011011100000111000110011100111000010111111111011111000110001010101001101111110000010110011011'

def CBC(msg,key,iv):
    start = 0
    end = 64
    iteration_size = int(len(msg) / 64)
    final = ''

    for _ in range(iteration_size):
        sub_bits = msg[start:end]
        iv = xor(sub_bits, iv)

        encoded = DES(iv, key_schedule(key))
        iv = encoded
        final += encoded

        start = end
        end = end + 64
    return final

print(CBC(msg,key,iv)=='1111101000110001101111001100101101011001101010001101010101100111011001100111010011001011100001001111011000001111110010011110011101010000101011010011011100011110011011001011100100011100011001011101110011110001110100010111001100100010111101011111101010111000')

print("\nTask3\n--------------------------------------------------------")

def CBCde(msg,key,iv):
    start = 0
    end = 64
    iteration_size = int(len(msg) / 64)
    final = ''

    for _ in range(iteration_size):
        sub_msg = msg[start:end]

        scheduled = key_schedule(key)
        scheduled.reverse()

        encoded = DES(sub_msg, scheduled)
        xored = xor(encoded, iv)

        final += xored

        iv = sub_msg
        start = end
        end = end + 64
    return final

img_t = CBCde(img_string, key, iv)
img=np.array([bin2dec(b) for b in split_img(img_t,8)]).reshape(np.array(img).shape)
Image.fromarray(np.uint8(np.array(img))).show()

print("\nTask4\n--------------------------------------------------------")

def OFB(msg,key,iv):
    start = 0
    end = 64
    iteration_size = int(len(msg) / 64)
    final = ''

    for _ in range(iteration_size):
        p = msg[start:end]
        iv = DES(iv, key_schedule(key))

        final += xor(iv, p)

        start = end
        end = end + 64
    return final

print(OFB(msg,key,iv)=='1100001001010001100110011101011100100011010101010111010010010011100101001100010001000100011110101011011101001110000000111000111101000101101111011100001111001100110010101110100110111000111000001100110010110101111101101100101110001010111011111110101100110000')

print(OFB(OFB(msg,key,iv),key,iv)==msg)