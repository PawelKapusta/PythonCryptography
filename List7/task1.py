import numpy as np
import random

print("\nTask1\n--------------------------------------------------------")

g=5
p=23

a=random.randint(2, p - 1) # alicja wybiera losowy element z grupy Zp

def dec2bin(dec, pad=0):
    return format(int(dec),'0'+str(pad)+'b')

def pow_mod(x,n,m):
    p = 1
    bin_str = dec2bin(n)
    for i in bin_str:
        p = p * p % m

        if i == '1':
            p = p * x % m

    return p

A=pow_mod(g, a, p) # oblicza  A w grupie  Zp , czyli  A=g^a mod p :

b=random.randint(2, p - 1) # To samo robi Bob, wybiera losowy elemnt grupy  b  i oblicza  B=g^b :
B=pow_mod(g, b, p)

k_B=pow_mod(A, b, p) # obliczamy k_B oraz k_A
k_A=pow_mod(B, a, p)

print(k_A == k_B)

print("\nTask2\n--------------------------------------------------------")

def dec2bin(dec, pad=0):
    return format(int(dec),'0'+str(pad)+'b')

def pow_mod(x,n,m): # oblicza nam x^n mod m
    p = 1
    bin_str = dec2bin(n)
    for i in bin_str:
        p = p * p % m

        if i == '1':
            p = p * x % m

    return p

print(pow_mod(7,3,2)==1)
print(pow_mod(2,1024,7)==2)
print(pow_mod(3,10**100,7)==4)
print(pow_mod(3**99,10**100,7)==1)

print("\nTask3\n--------------------------------------------------------")

def inv(p,n): # Znajduje dla danej liczby p i n licze e ze d*e = 1 mod n
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n > 0:
        (q, p, n) = (p // n, n, p % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)

    if x0 < 0:
        return x0 + x1
    return x0

print(inv(5,7)==3)
print(inv(3,2)==1)
print(inv(5,7)==3)
print(inv(3,11)==4)

print("\nTask4\n--------------------------------------------------------")

def Fermat_test(p,k): # Dla danej liczby p sprawdza za pomocą k rund czy liczba jest pierwsza
    for _ in range(k):
        a = random.randint(2, p-2)

        if pow_mod(a, p-1, p) != 1:
            return False
    return True

print(Fermat_test(71,10)==True)
print(Fermat_test(41,10)==True)
print(Fermat_test(62,10)==False)
print(Fermat_test(84,10)==False)


def gen_p(a,b):
    rand = random.randint(a, b)
    while not Fermat_test(rand, 10):
        rand = random.randint(a, b)
    return rand

print("\nTask5\n--------------------------------------------------------")

p=24130780476900131841553779066939443255102203937160657723394451174808141403858935238883126295228560935516885174421847238379397184900972008801015315248328437

q=26660613491521684005574100352062919789979599401844483402246984186988668019447679726081352452799126206997555710356464145743285983450292024894053538317854159

def key_gen(p,q): # generuje klucze w ramach algorytmu RSA, dla podanych dużych liczb pierwszych p i q zwraca parę kluczy w postaci krotki (n, e , d), postepujemy zgodnie ze schematem w opisie zadania
    n = p * q
    euler_n = (q - 1) * (p - 1)

    e = 65537

    d = inv(e, euler_n)
    return n, e, d


print(key_gen(p,q)==(
    643341411543391711051425916925550311012265711300705520200325675109446836493100912341600261266222036750541155307483726185012838542757173209246878527615686866322037404779287199511097525538499079836420404197380885254900993985365780000028685663116338197119892656788379026665075201747282243427197060237417498419483,
    65537,
    334692241429603741219438891581498052305769251366366399304669177607406348936208181733781847015759652456012644616150535488014598320266503205353805078033123914361616918116605669461614375732022492713408743728419283824726654095683796656269600488579712785553345684168299073769307373555258299179136288438930486131753))

print("\nTask6\n--------------------------------------------------------")

n=643341411543391711051425916925550311012265711300705520200325675109446836493100912341600261266222036750541155307483726185012838542757173209246878527615686866322037404779287199511097525538499079836420404197380885254900993985365780000028685663116338197119892656788379026665075201747282243427197060237417498419483
e=208350389615113762788111263490297665109355377830736643503856528470357220208290606069461253441671763980314762012190291145414733535673548961910772961435143582756267132618995046438684186252163655289035228721360753675271711075033036291412267917936062230585687839901652792581357105686274730618278123193067279319927
d=502029145905912565237092248595126620632487653124329465045136187249992350554283419049087834111437813928483679744364041267436534897197233494007405790027156754593648940515350675746678776751088177077690779849077150675864299782170211270887279535225267271652686426692746042361641530130191025648848746210219401813175

def enc(x,e,n): # podaną liczbę x - wiadomość szyfruje za pomocą klucza publicznego (e, n)
    return pow_mod(x, e, n)
def dec(y,d,n): # podaną liczbę y - szyfrogram deszyfruje za pomoca klucza prywatnego (d, n)
    return pow_mod(y, d, n)

print(enc(17,e,n)==353230656531616665332116231509462661273082280099289165110086677972943261270362976411810450837847461343993316190457124231852161403281191913264230575248953060776390559207669288928802429515257729255854064666904850354451664771847425807841069296028397747015905377374208615536177338019721932982992946095124218548486)
print(dec(581228535329363957060482357417595500042117791982900743030228020443422357943293873902079555506233253640573184749108783275472243891683169424548126947970217999010556081853170166407244862004725833809785262442186726634369847615830487904940967188707443976155835347542897227831115870912021598488639913865347475436893,d,n)==27)
print(dec(enc(12,e,n),d,n)==12)
