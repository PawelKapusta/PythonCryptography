import string
import matplotlib.pyplot as plt
import collections

alphabet=['a','ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
             'm', 'n', 'ń', 'o','ó', 'p', 'q','r', 's', 'ś', 't', 'u','v', 'w', 'x','y', 'z','ź','ż']

czestotliwosc={'a':0.0891,'ą':0.0099, 'b':0.0147, 'c':0.0396, 'ć':0.004, 'd':0.0325, 'e':0.0766, 'ę':0.0111,
            'f':0.003, 'g':0.0142, 'h':0.0108, 'i':0.0821, 'j':0.0228, 'k':0.0351, 'l':0.021, 'ł':0.0182,'m':0.028,
            'n':0.0552, 'ń':0.002, 'o':0.0775,'ó':0.0085, 'p':0.0313, 'q':0.0014, 'r':0.0469, 's':0.0432,'ś':0.0066,
            't':0.0398, 'u':0.025, 'v': 0.0004, 'w':0.0465 ,'x':0.0002,'y':0.0376, 'z':0.0564,'ź':0.0006,'ż':0.0083}

max_key=len(alphabet)

def Cezar(text, key):
    encrypted=''
    for symbol in text:
        try:
            if(symbol == symbol.upper()):
                lower = symbol.lower()
                index = alphabet.index(lower)
                index += key
                if index >= max_key:
                    index -= max_key
                elif index < 0:
                    index += max_key
                encrypted += alphabet[index].upper()
            else:
                index = alphabet.index(symbol)
                index += key
                if index >= max_key:
                    index -= max_key
                elif index < 0:
                    index += max_key
                encrypted += alphabet[index]
        except (ValueError):
            encrypted += symbol
    return encrypted

print('\n Task1:\n')
print(Cezar('Ala ma kota.',3)=='Cnc oc mqwc.')
print(Cezar('Ala ma kota.',20)=='Óżó ąó źćió.')
print(Cezar('Ala ma 2 koty.',5)=='Dod pd 2 ńsyą.')
print(Cezar('Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.',7)
                  =='Jęxkrsk eępk, vxuesc źxżj,\nGkćyńpsk ćqtxćkhćksńę!\nVxćkecźchn óyćźęqźuą eęjks hżj\nSńk ąxuhń jt ńyźsńksńę.')
print(Cezar('Cnc oc mqwc.',-3)=='Ala ma kota.')
print(Cezar('Óżó ąó źćió.',-20)=='Ala ma kota.')
print(Cezar('Dod pd 2 ńsyą.',-5)=='Ala ma 2 koty.')
print(Cezar('Jęxkrsk eępk, vxuesc źxżj,\nGkćyńpsk ćqtxćkhćksńę!\nVxćkecźchn óyćźęqźuą eęjks hżj\nSńk ąxuhń jt ńyźsńksńę.',-7)
                  =='Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.')

textToDecrypt='Hćcrek okyź hćęy? Okzpń sńóź rsńk t źt sńk vcźę, ąńkr. Okzpń vcźęofhkrż żyńqżol ącźqżręhćci, sńk ąńkr.'

print('\n Task2:\n')
for i in range(len(alphabet)):
    print(i,': ', Cezar(textToDecrypt, -i))
print("\nQuote: ", Cezar(textToDecrypt, -7), ' - Św. Augustyn, Wyznania')

print('\n Task3:\n')
plt.bar(czestotliwosc.keys(),czestotliwosc.values())
plt.show()
frequencies = {}
file=open('ksiazka1.txt', encoding="utf8")
book=file.read()
file.close()
text_from_book = ""

for x in range(len(book)):
    if book[x].isalpha():
        text_from_book = text_from_book + book[x].lower()

for char in text_from_book:
        if char in frequencies:
            frequencies[char] += 1
        elif char in alphabet:
            frequencies[char] = 1

od = collections.OrderedDict(sorted(frequencies.items()))
plt.bar(od.keys(),od.values())
plt.show()

file=open('ksiazka1.txt', encoding="utf8")
book=file.read()
file.close()

for key in range(1, 2):
    decrypted_book = Cezar(book, -4)
with open('decryptedBook1.txt', 'w', encoding='utf8') as f:
    f.write(decrypted_book)
print('Odszyfrowano książkę!')
print('\nBolesław Prus - "Faraon" ISBN 978-83-288-2667-0 Tom I\n')

print('\n Task4:\n')
liczb_do_lit=dict()
lit_do_liczb=dict()
for i,l in enumerate(alphabet):
    liczb_do_lit[i]=l
    lit_do_liczb[l]=i

def generate_Vignere_key(text, key):
    new_key = []
    counter = 0
    for i in range(len(text)):
        if text[i].lower() in alphabet:
            new_key.append(key[(i - counter) % len(key)])
        else:
            counter += 1
            new_key.append(text[i])
    return "".join(new_key)

def Vignere_zaszyfruj(tekst,klucz):
    key = generate_Vignere_key(tekst, klucz)
    encrypted = ""
    for i in range(len(tekst)):
        if tekst[i].lower() in alphabet:
            index = lit_do_liczb.get(tekst[i].lower()) + lit_do_liczb.get(key[i])
            new_char = liczb_do_lit.get(index % len(alphabet))
            encrypted += new_char if tekst[i].islower() else new_char.upper()
        else:
            encrypted += tekst[i]
    return encrypted

def Vignere_odszyfruj(tekst,klucz):
    key = generate_Vignere_key(tekst, klucz)
    decrypted = ""
    for i in range(len(tekst)):
        if tekst[i].lower() in alphabet:
            index = lit_do_liczb.get(tekst[i].lower()) - lit_do_liczb.get(key[i])
            new_char = liczb_do_lit.get(index % len(alphabet))
            decrypted += new_char if tekst[i].islower() else new_char.upper()
        else:
            decrypted += tekst[i]
    return decrypted

print(Vignere_zaszyfruj('Ala ma kota.','ela')=='Eva ql kśda.')
print(Vignere_zaszyfruj('Ala ma kota.','tygrys')=='Thg ćy bhqg.')
print(Vignere_zaszyfruj('Ala ma 2 koty.','indywidualistyczny')=='Iyd jw 2 ssńy.')
print(Vignere_zaszyfruj('Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.','asnyk')
                  =='Dsdbwnx myue, hdmjnó fodd,\nTrvbicżb hłfdvocprksa!\nHdvożófumh bevćaćfmę żsqbx cmq\nKse ńdmmi wą ębtevbxis.')
print(Vignere_odszyfruj('Eva ql kśda.','ela')=='Ala ma kota.')
print(Vignere_odszyfruj('Thg ćy bhqg.','tygrys')=='Ala ma kota.')
print(Vignere_odszyfruj('Iyd jw 2 ssńy.','indywidualistyczny')=='Ala ma 2 koty.')
print(Vignere_odszyfruj('Dsdbwnx myue, hdmjnó fodd,\nTrvbicżb hłfdvocprksa!\nHdvożófumh bevćaćfmę żsqbx cmq\nKse ńdmmi wą ębtevbxis.','asnyk')
                  =='Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.')

print('\n Task5:\n')

file2=open('ksiazka2.txt', encoding="utf-8")
book2=file2.read()
file2.close()
frequencies2={}
key_length = 4

text_from_book2= ""

for x in range(len(book2)):
    if book2[x].isalpha():
        text_from_book2 = text_from_book2 + book2[x].lower()

new_counter = {}
new_frequencies = {}

for n in range(0, key_length):
    new_text = ""

    for m in range(n, len(text_from_book2), key_length):
        new_text = new_text + text_from_book2[m]

    new_counter.clear()

    for x in czestotliwosc:
        new_counter[x] = new_text.count(x)

    sum_letter = 0

    for x in new_counter:
        sum_letter += new_counter[x]
    new_frequencies.clear()

    for x in new_counter.items():
        new_frequencies[x[0]] = x[1] / sum_letter

    plt.bar(new_frequencies.keys(), new_frequencies.values())
    plt.show()

for key in range(1, 2):
    decrypted_book2 = Vignere_odszyfruj(book2, 'glob')
with open('decryptedBook2.txt', 'w',encoding="utf-8") as f:
    f.write(decrypted_book2)

print('Odszyfrowano książkę!')
print('\nJuliusz Verne - Podróż naokoło świata w 80-ciu dniach\n')