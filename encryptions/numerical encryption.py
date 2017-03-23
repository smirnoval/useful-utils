import random


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def phi(a):
    b = a - 1
    c = 0
    while b:
        if not NOD(a, b) - 1:
            c += 1
        b -= 1
    return c


def inverse_number_by_def(a, m):
    k = 1
    b = (1 + k * m) / a
    while (not(b.is_integer())):
        k += 1
        b = (1 + k * m) / a
    return(int(b))


def inverse_number_by_euler(a, m):
    return a**(phi(m) - 1) % m


def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx


def fastPower(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = fastPower(base, exp // 2, mod)
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod


def base10toN(num,n):
    return (((num == 0) and "0") or (base10toN(num // n, n).strip("0") + "abcdefghijklmnopqrstuvwxyz"[:n][num % n]).upper())


def rsa(p, q, m):
    if is_prime(p) is False or is_prime(q) is False:
        print("Need simple numbers!")
        return
    n = p * q
    print("Find n =", n)
    phi = (p - 1) * (q - 1)
    print("Find phi = ", phi)
    e = 65537
    print("Pick e = ", e)
    d = multiplicative_inverse(e, phi)
    print("Find d = ", d)
    public = (e, n)
    private = (d, n)
    print("Public key", public)
    print("Secret key", private)
    print("Text for encryption:", m)
    cipher = encrypt(public, m)
    print("Encrypted text:", cipher)
    decipher = decrypt(private, cipher)
    print("Decrypted text:", decipher)


def encrypt(pk, plaintext):
    M, k = 0, len(plaintext) - 1
    for i in plaintext:
        M += (ord(i) - 65) * (26**k)
        k -= 1
    key, n = pk
    c = fastPower(M, key, n)
    cipher = base10toN(c, 26)
    return cipher


def decrypt(pk, ciphertext):
    M, k = 0, len(ciphertext) - 1
    for i in ciphertext:
        M += (ord(i) - 65) * (26**k)
        k -= 1
    key, n = pk
    c = fastPower(M, key, n)
    cipher = base10toN(c, 26)
    return cipher


def find_random_key_NOD_for(p):
    g = random.randrange(p + 1, 200000)
    while NOD(g, p - 1) != 1:
        g = random.randrange(p + 1, 200000)
    return g


def shamir_secret_sharing(p, m):
    print("Pick p = {0}, text for encryption = {1}".format(p, m))
    ea = find_random_key_NOD_for(p)
    print("Generate key e for A:", ea)
    da = multiplicative_inverse(ea, p - 1)
    print("Find key d for A:", da)
    eb = find_random_key_NOD_for(p)
    print("Generate key e for B:", eb)
    db = multiplicative_inverse(eb, p - 1)
    print("FInd key d for B:", db)
    M, k = 0, len(m) - 1
    for i in m:
        M += (ord(i) - 65) * (26**k)
        k -= 1
    print("Text: {0}, his numerical equivalent: {1}".format(m, M))
    c1 = fastPower(M, ea, p)
    print("Result fisrt step С1:", c1)
    c2 = fastPower(c1, eb, p)
    print("Result second step C2:", c2)
    c3 = fastPower(c2, da, p)
    print("Result third step С3:", c3)
    m = fastPower(c3, db, p)
    print("Finded value of М:", m)
    decipher = base10toN(m, 26)
    print("Decrypted text:", decipher)


def elgamal(p, m):
    g = find_random_key_NOD_for(p)
    while is_prime(g) is not True:
        g += 1
    x = find_random_key_NOD_for(p)
    while is_prime(x) is not True and x != g:
        x += 1
    print("Picked value of g={0} and x={1}".format(g, x))
    y = fastPower(g, x, p)
    print("Calculated value of y=", y)
    print("Public key: (y,g,p)=({0},{1},{2})".format(y, g, p))
    M, k = 0, len(m) - 1
    for i in m:
        M += (ord(i) - 65) * (26**k)
        k -= 1
    print("Text={0}, his numerical equivalent = {1}".format(m, M))
    k = find_random_key_NOD_for(p)
    print("FInd k=", k)
    a = fastPower(g, k, p)
    print("First part of sign a = ", a)
    b = 0
    while M != ((x * a + k * b) % (p - 1)):
        b += 1
    print("Second part of sign b = ", b)
    signature = (a, b)
    print("Sign:", signature)
    print("Check:")
    left_part = (y**a * a**b) % p
    right_part = (g**M) % p
    print("Left part = {0}, right part = {1}".format(left_part, right_part))


if __name__ == "__main__":
    print(NOD(594174, 1936921))
    print("-" * 20)
    print("Для 5", phi(5), "\nДля 20", phi(20))
    print("-" * 20)
    print("x=17^(-1)(mod7)", "x =", inverse_number_by_def(17, 7))
    print("-" * 20)
    print("x=17^(-1)(mod7)", "x =", inverse_number_by_euler(17, 7))
    rsa(36209, 54419, "LEGION")
    print("-" * 20)
    shamir_secret_sharing(45833, "DIV")
    print("-" * 20)
    elgamal(34763, "DSS")