import random as random
from PIL import Image
import numpy as np

print("\nTask3\n--------------------------------------------------------")

img1 = Image.open('miki.png').convert('L')
img1.show()

img2 = Image.open('quest.png').convert('L')
img2.show()


def add_pic(img1, img2):
    img1_array = np.array(img1, dtype=np.uint8)
    img2_array = np.array(img2, dtype=np.uint8)
    returned_array = np.array([], dtype=np.uint8)
    temporary_array = np.array([], dtype=np.uint8)

    for i in range(len(img1_array)):
        for j in range(len(img1_array[i])):
            if img1_array[i][j] == img2_array[i][j]:
                temporary_array = np.append(temporary_array, 0)
            elif img1_array[i][j] != img2_array[i][j]:
                temporary_array = np.append(temporary_array, 255)
        returned_array = np.append(returned_array, temporary_array)
        temporary_array = np.array([], dtype=np.uint8)

    changed = returned_array.reshape(207, 200)

    returned_image = Image.fromarray(np.uint8(np.array(changed)))
    return returned_image


added_image1_and_image2 = add_pic(img1, img2)
added_image1_and_image2.save("added_image1_and_image2.png", "PNG")

random_array = np.array([], dtype=np.uint8)
array_len = 207 * 200

for i in range(array_len):
    rand = random.randrange(0, 2)
    if rand == 1:
        random_array = np.append(random_array, 255)
    elif rand == 0:
        random_array = np.append(random_array, 0)

random_changed = random_array.reshape(207, 200)

key_image = Image.fromarray(np.uint8(np.array(random_changed)))
key_image.save("key_image.png", "PNG")
key_image.show()
encrypted_image1 = add_pic(img1, key_image)
encrypted_image1.save("encrypted_image1.png", "PNG")
encrypted_image2 = add_pic(img2, key_image)
encrypted_image2.save("encrypted_image2.png", "PNG")
decrypted_image = add_pic(encrypted_image1, encrypted_image2)
decrypted_image.save("decrypted_image.png", "PNG")

print("\nTask4\n--------------------------------------------------------")

msg1_enc = '\x1e\x17\x0c\x12\x1b\x08\x0cf\x0e\x11x\x1a\x1c\x12o\x06\x18\x1f\x17\x03\x10\x01fkh\x1f\x08'
msg2_enc = '\x0b\ni\x07\x1c\x02k\x1f\x16e\x01\x0b\x07\x03\n\x15\x15\x0c\x1el\x07\x03\x03\x16\x01\x01\x02'


def add_str(msg1, msg2):
    unicode_msg1_array = []
    unicode_msg2_array = []
    added_msg1_and_msg2 = []
    returned = ""

    for i in range(0, len(msg1)):
        unicode_msg1_array.append(str(ord(msg1[i])))
        unicode_msg2_array.append(str(ord(msg2[i])))
        added_msg1_and_msg2.append(str(int(unicode_msg1_array[i]) ^ int(unicode_msg2_array[i])))
        returned += chr(int(added_msg1_and_msg2[i]))
    return returned


def add_str2(msg1, msg2, range1, range2, move):
    unicode_msg1_array = []
    unicode_msg2_array = []
    added_msg1_and_msg2 = []
    returned = ""

    for k in range(0, len(msg1)):
        unicode_msg1_array.append(str(ord(msg1[k])))

    for j in range(0, len(msg2)):
        unicode_msg2_array.append(str(ord(msg2[j])))

    for i in range(range1, range2):
        added_msg1_and_msg2.append(str(int(unicode_msg1_array[i + move]) ^ int(unicode_msg2_array[i])))
        returned += chr(int(added_msg1_and_msg2[i]))

    return returned


encrypted_sum_two_messages = add_str(msg1_enc, msg2_enc)
text = add_str2(encrypted_sum_two_messages, "MEETING A-YESTERDAY EVENING", 0, 27, 0)
text2 = add_str2(encrypted_sum_two_messages, "XX AND YYY THE AIRPORT 3 PM", 0, 27, 0)

print(text)
print(text2)
print(add_str('A', '1') == 'p')
print(add_str('A', 'A') == '\x00')
print(add_str('A', 'B') == '\x03')
print(add_str('HSUP', 'NBVH') == '\x06\x11\x03\x18')
print(add_str('131', 'FXH') == 'wky')

print("\nTask5\n--------------------------------------------------------")

file0 = open('msg0.txt', encoding="utf-8")
file1 = open('msg1.txt', encoding="utf-8")
file2 = open('msg2.txt', encoding="utf-8")
file3 = open('msg3.txt', encoding="utf-8")
file4 = open('msg4.txt', encoding="utf-8")
file5 = open('msg5.txt', encoding="utf-8")
file6 = open('msg6.txt', encoding="utf-8")
file7 = open('msg7.txt', encoding="utf-8")
file8 = open('msg8.txt', encoding="utf-8")
file9 = open('msg9.txt', encoding="utf-8")

msg0 = file0.read()
msg1 = file1.read()
msg2 = file2.read()
msg3 = file3.read()
msg4 = file4.read()
msg5 = file5.read()
msg6 = file6.read()
msg7 = file7.read()
msg8 = file8.read()
msg9 = file9.read()

file0.close()
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()

msg01 = add_str(msg0, msg1)
msg02 = add_str(msg0, msg2)
msg03 = add_str(msg0, msg3)
msg04 = add_str(msg0, msg4)
msg05 = add_str(msg0, msg5)
msg06 = add_str(msg0, msg6)
msg07 = add_str(msg0, msg7)
msg08 = add_str(msg0, msg8)
msg09 = add_str(msg0, msg9)
msg12 = add_str(msg1, msg2)
msg13 = add_str(msg1, msg3)
msg14 = add_str(msg1, msg4)
msg15 = add_str(msg1, msg5)
msg16 = add_str(msg1, msg6)
msg17 = add_str(msg1, msg7)
msg18 = add_str(msg1, msg8)
msg19 = add_str(msg1, msg9)
msg23 = add_str(msg2, msg3)
msg24 = add_str(msg2, msg4)
msg25 = add_str(msg2, msg5)
msg26 = add_str(msg2, msg6)
msg27 = add_str(msg2, msg7)
msg28 = add_str(msg2, msg8)
msg29 = add_str(msg2, msg9)
msg34 = add_str(msg3, msg4)
msg35 = add_str(msg3, msg5)
msg36 = add_str(msg3, msg6)
msg37 = add_str(msg3, msg7)
msg38 = add_str(msg3, msg8)
msg39 = add_str(msg3, msg9)
msg45 = add_str(msg4, msg5)
msg46 = add_str(msg4, msg6)
msg47 = add_str(msg4, msg7)
msg48 = add_str(msg4, msg8)
msg49 = add_str(msg4, msg9)
msg56 = add_str(msg5, msg6)
msg57 = add_str(msg5, msg7)
msg58 = add_str(msg5, msg8)
msg59 = add_str(msg5, msg9)
msg67 = add_str(msg6, msg7)
msg68 = add_str(msg6, msg8)
msg69 = add_str(msg6, msg9)
msg78 = add_str(msg7, msg8)
msg79 = add_str(msg7, msg9)
msg89 = add_str(msg8, msg9)

final = [round(msg01.count(chr(0)) / len(msg01), 5), round(msg02.count(chr(0)) / len(msg02), 5),
         round(msg03.count(chr(0)) / len(msg03), 5), round(msg04.count(chr(0)) / len(msg04), 5),
         round(msg05.count(chr(0)) / len(msg05), 5), round(msg06.count(chr(0)) / len(msg06), 5),
         round(msg07.count(chr(0)) / len(msg07), 5), round(msg08.count(chr(0)) / len(msg08), 5),
         round(msg09.count(chr(0)) / len(msg09), 5), round(msg12.count(chr(0)) / len(msg12), 5),
         round(msg13.count(chr(0)) / len(msg13), 5), round(msg14.count(chr(0)) / len(msg14), 5),
         round(msg15.count(chr(0)) / len(msg15), 5), round(msg16.count(chr(0)) / len(msg16), 5),
         round(msg17.count(chr(0)) / len(msg17), 5), round(msg18.count(chr(0)) / len(msg18), 5),
         round(msg19.count(chr(0)) / len(msg19), 5), round(msg23.count(chr(0)) / len(msg23), 5),
         round(msg24.count(chr(0)) / len(msg24), 5), round(msg25.count(chr(0)) / len(msg25), 5),
         round(msg26.count(chr(0)) / len(msg26), 5), round(msg27.count(chr(0)) / len(msg27), 5),
         round(msg28.count(chr(0)) / len(msg28), 5), round(msg29.count(chr(0)) / len(msg29), 5),
         round(msg34.count(chr(0)) / len(msg34), 5), round(msg35.count(chr(0)) / len(msg35), 5),
         round(msg36.count(chr(0)) / len(msg36), 5), round(msg37.count(chr(0)) / len(msg37), 5),
         round(msg38.count(chr(0)) / len(msg38), 5), round(msg39.count(chr(0)) / len(msg39), 5),
         round(msg45.count(chr(0)) / len(msg45), 5), round(msg46.count(chr(0)) / len(msg46), 5),
         round(msg47.count(chr(0)) / len(msg47), 5), round(msg48.count(chr(0)) / len(msg48), 5),
         round(msg49.count(chr(0)) / len(msg49), 5), round(msg56.count(chr(0)) / len(msg56), 5),
         round(msg57.count(chr(0)) / len(msg57), 5), round(msg58.count(chr(0)) / len(msg58), 5),
         round(msg59.count(chr(0)) / len(msg59), 5), round(msg67.count(chr(0)) / len(msg67), 5),
         round(msg68.count(chr(0)) / len(msg68), 5), round(msg69.count(chr(0)) / len(msg69), 5),
         round(msg78.count(chr(0)) / len(msg78), 5), round(msg79.count(chr(0)) / len(msg79), 5),
         round(msg89.count(chr(0)) / len(msg89), 5)]

print("Final:", final)
print("Final for msg3 and msg8: ", round(msg38.count(chr(0)) / len(msg38), 5))
print("This is the maximum, so they are coded with the same key!")
print(add_str('A', '1') == 'p')
print(add_str('A', 'A') == '\x00')
print(add_str('A', 'B') == '\x03')
print(add_str('HSUP', 'NBVH') == '\x06\x11\x03\x18')
print(add_str('131', 'FXH') == 'wky')
