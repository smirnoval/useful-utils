import copy
from itertools import permutations
import random
import math


def removal_excess_symbols(line):
    return [a for a in line.upper() if (ord(a) >= ord("A")) and (ord(a) <= ord("Z"))]


def get_numerical_position(line):
    q = sorted(line)
    for i in range(len(q)):
        line[line.index(q[i])] = i + 1
    return line


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def remove_repeating_symbols(line):
    result = []
    for i in line:
        if i not in result:
            result.append(i)
    return result


def trisemus(line, code_word):
    print("Phrase:", line)
    print("Code world:", code_word, '\n')
    line = removal_excess_symbols(line)
    code_word = remove_repeating_symbols(removal_excess_symbols(code_word))
    size = 5
    extra_letters = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    extra_letters.remove("J")
    missing_letters_line = size ** 2 - len(code_word)
    while missing_letters_line != 0:
        if extra_letters[0] in code_word:
            extra_letters.pop(0)
        else:
            code_word.append(extra_letters[0])
            extra_letters.pop(0)
            missing_letters_line -= 1
    check = 0
    new_alphabet, tmp = [], []
    for i in code_word:
        print(i, end='')
        tmp.append(i)
        check += 1
        if check == size:
            print(' ')
            new_alphabet.append(tmp)
            tmp = []
            check = 0

    new_alphabet = list(map(list, zip(*new_alphabet)))

    phrase = ""

    for i in line:
        for j in range(len(new_alphabet)):
            if i in new_alphabet[j]:
                k = new_alphabet[j].index(i)
                k += 1
                if k == 5:
                    k = 0
                phrase += new_alphabet[j][k]
    print('')
    print(''.join(line))
    print(phrase)


def double_square_Uitston(line):
    print("Phrase:", line, '\n')
    line = removal_excess_symbols(line)
    a, b = make_random_table(), make_random_table()
    print_tables(a, b)

    message, tmp = [], []
    check, size, ind = 0, 2, 0
    while len(line) != 0:
        if line[ind] not in tmp:
            tmp.append(line[ind])
            line.pop(ind)
        else:
            tmp.append("X")
        check += 1
        if check == size:
            message.append(tmp)
            tmp = []
            check = 0
    if len(tmp) == 1:
        tmp.append("X")
        message.append(tmp)

    encrypted = []
    for i in message:
        check = 0
        tmp = []
        a_i, a_j = -1, -1
        b_i, b_j = -1, -1
        for j in range(len(a)):
            if i[0] in a[j]:
                a_i = a[j].index(i[0])
                a_j = j
        for j in range(len(b)):
            if i[1] in b[j]:
                b_i = b[j].index(i[1])
                b_j = j
        print(a_i, a_j, b_i, b_j)
        if a_j == b_j:
            tmp.append(a[a_j][b_i])
            tmp.append(b[b_j][a_i])
            encrypted.append(tmp)
        else:
            temp = a_j
            a_j = b_j
            b_j = temp
            tmp.append(a[a_j][a_i])
            tmp.append(b[b_j][b_i])
            encrypted.append(tmp)

    for i in message:
        for j in i:
            print(j, end='')
        print('', end=' ')
    print('')
    for i in encrypted:
        for j in i:
            print(j, end='')
        print('', end=' ')
    print('')


def make_random_table():
    alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    alphabet.remove("J")
    random.shuffle(alphabet)
    check, size = 0, 5
    new_alphabet, tmp = [], []
    for i in alphabet:
        tmp.append(i)
        check += 1
        if check == size:
            new_alphabet.append(tmp)
            tmp = []
            check = 0
    return new_alphabet


def print_tables(table1, table2):
    for i in range(len(table1)):
        for j in range(len(table1)):
            print(table1[i][j], end='')
        print("  ", end='')
        for j in range(len(table2)):
            print(table2[i][j], end='')
        print('')
    print('')


def skitala(line):
    print("Phrase:", line, '\n')
    line = removal_excess_symbols(line)
    size = math.ceil(math.sqrt(len(line)))
    extra_letters = [" " for a in range(30)]
    missing_letters_line = size ** 2 - len(line)
    line += extra_letters[:missing_letters_line]
    check = 0
    for i in line:
        print(i, end='')
        check += 1
        if check == size:
            print("")
            check = 0
    print('')
    check = 0
    message, tmp = [], []
    for i in line:
        tmp.append(i)
        check += 1
        if check == size:
            message.append(tmp)
            check = 0
            tmp = []
    message = list(map(list, zip(*message)))
    for i in message:
        for j in i:
            print(j, end="")
    print('')


def coordinate_polybius(line):
    print("Phrase:", line, '\n')
    line = removal_excess_symbols(line)
    alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    alphabet.remove("J")
    check, size = 0, 5
    new_alphabet, tmp = [], []
    for i in alphabet:
        print(i, end='')
        tmp.append(i)
        check += 1
        if check == size:
            print(' ')
            new_alphabet.append(tmp)
            tmp = []
            check = 0

    coordinates = []
    for i in line:
        tmp = []
        for j in range(len(new_alphabet)):
            if i in new_alphabet[j]:
                a_i = new_alphabet[j].index(i)
                a_j = j
                tmp.append(a_i)
                tmp.append(a_j)
                coordinates.append(tmp)
    print('')
    print("Old coordinates:")
    for i in coordinates:
        for j in i:
            print(j, end=' ')
        print('')
    print('')

    coordinates = list(map(list, zip(*coordinates)))
    new_coordinates = []
    for i in coordinates:
        for j in i:
            new_coordinates.append(j)

    print("New coordinates:")
    check = 0
    for i in new_coordinates:
        print(i, end=' ')
        check += 1
        if check == 2:
            print('')
            check = 0
    print('\n')

    phrase = ''
    check, size = 0, 2
    while len(new_coordinates) != 0:
        a_i, a_j = new_coordinates.pop(0), new_coordinates.pop(0)
        phrase += new_alphabet[a_j][a_i]
    print(phrase)


def polybius(line):
    print("Phrase:", line, '\n')
    line = removal_excess_symbols(line)
    alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    alphabet.remove("J")
    check, size = 0, 5
    new_alphabet, tmp = [], []
    for i in alphabet:
        print(i, end='')
        tmp.append(i)
        check += 1
        if check == size:
            print(' ')
            new_alphabet.append(tmp)
            tmp = []
            check = 0
    new_alphabet = list(map(list, zip(*new_alphabet)))

    message = ''
    for i in line:
        for j in range(len(new_alphabet)):
            if i in new_alphabet[j]:
                k = new_alphabet[j].index(i) + 1
                if k == size:
                    k = 0
                message += new_alphabet[j][k]
    print('\n' + message)


def playfair(line, code_word):
    print("Phrase:", line)
    print("Code word:", code_word, '\n')
    line, code_word = removal_excess_symbols(line), removal_excess_symbols(code_word)
    code_word = remove_repeating_symbols(code_word)
    alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    alphabet.remove("J")
    new_alphabet = code_word
    for i in alphabet:
        if i not in new_alphabet:
            new_alphabet.append(i)
    grid = []
    check, size = 0, 5
    tmp = []
    for i in new_alphabet:
        tmp.append(i)
        check += 1
        if check == size:
            grid.append(tmp)
            tmp = []
            check = 0

    for i in grid:
        for j in i:
            print(j, end='')
        print('')
    print('')

    message, tmp = [], []
    check, size, ind = 0, 2, 0
    while len(line) != 0:
        if line[ind] not in tmp:
            tmp.append(line[ind])
            line.pop(ind)
        else:
            tmp.append("X")
        check += 1
        if check == size:
            message.append(tmp)
            tmp = []
            check = 0
    if len(tmp) == 1:
        tmp.append("X")
        message.append(tmp)

    transpose_grid = list(map(list, zip(*grid)))

    encrypted = []
    for i in message:
        check = 0
        tmp = []
        for j in grid:
            if i[0] in j and i[1] in j:
                a, b = j.index(i[0]) + 1, j.index(i[1]) + 1
                if a == len(j):
                    a = 0
                elif b == len(j):
                    b = 0
                tmp.append(j[a])
                tmp.append(j[b])
                encrypted.append(tmp)
                check = 1
                break
        if check != 1:
            for j in transpose_grid:
                if i[0] in j and i[1] in j:
                    a, b = j.index(i[0]) + 1, j.index(i[1]) + 1
                    if a == len(j):
                        a = 0
                    elif b == len(j):
                        b = 0
                    tmp.append(j[a])
                    tmp.append(j[b])
                    encrypted.append(tmp)
                    check = 1
                    break
        if check != 1:
            a_i, a_j = -1, -1
            b_i, b_j = -1, -1
            for j in range(len(grid)):
                if i[0] in grid[j]:
                    a_i = j
                    a_j = grid[j].index(i[0])
                if i[1] in grid[j]:
                    b_i = j
                    b_j = grid[j].index(i[1])
            temp = a_j
            a_j = b_j
            b_j = temp
            tmp.append(grid[a_i][a_j])
            tmp.append(grid[b_i][b_j])
            encrypted.append(tmp)

    for i in message:
        for j in i:
            print(j, end='')
        print('', end=' ')
    print('')
    for i in encrypted:
        for j in i:
            print(j, end='')
        print('', end=' ')
    print('')


def key_word_caesar(line, key_word, position):
    print("Phrase:", line)
    print("Code word", key_word)
    print("Shift:", position, '\n')
    line, key_word = removal_excess_symbols(line), removal_excess_symbols(key_word)
    old_alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    new_alphabet = [0 for a in range(len(old_alphabet))]
    for i in key_word:
        if position > len(new_alphabet) - 1:
            position = 0
        new_alphabet[position] = i
        position += 1
    tmp = sorted(list(set(old_alphabet) - set(key_word)))
    for i in tmp:
        if position > len(new_alphabet) - 1:
            position = 0
        new_alphabet[position] = i
        position += 1
    for i in range(len(new_alphabet)):
        print(old_alphabet[i] + '-->' + new_alphabet[i])
    print('')
    for i in line:
        print(new_alphabet[old_alphabet.index(i)], end='')
    print('')


def affine_system_caesar(line, a, b):
    print("Phrase:", line)
    print("Shift a:", a)
    print("Shift b:", b, '\n')
    line = removal_excess_symbols(line)
    old_alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    checker = NOD(a, b)
    if checker != 1:
        print("Wrong a! Must be simple for length of letters!")
        return
    new_alphabet = []
    for i in range(len(old_alphabet)):
        new_alphabet.append(chr(((a * i + b) % len(old_alphabet)) + ord("A")))
    for i in range(len(new_alphabet)):
        print(old_alphabet[i] + '-->' + new_alphabet[i])
    print('')
    for i in line:
        print(new_alphabet[old_alphabet.index(i)], end='')
    print('')


def simple_caesar(line, shift):
    print("Phrase:", line)
    print("Shift", shift, '\n')
    line = removal_excess_symbols(line)
    old_alphabet = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    new_alphabet = []
    for i in range(ord("A"), ord("Z") + 1):
        i += shift
        if i > ord("Z"):
            i = ord("A") + (i - ord("Z") - 1)
        new_alphabet.append(chr(i))
    for i in range(len(new_alphabet)):
        print(old_alphabet[i] + '-->' + new_alphabet[i])
    print('')
    for i in line:
        print(new_alphabet[old_alphabet.index(i)], end='')
    print('')


def double_transposition(line, horizontal_code, vertical_code):
    print("Phrase:", line)
    print("Horizontal code word:", horizontal_code)
    print("Vertical code word", vertical_code, '\n')
    line, horizontal_code, vertical_code = removal_excess_symbols(line), removal_excess_symbols(horizontal_code), removal_excess_symbols(vertical_code)
    number_vert, number_hor = get_numerical_position(vertical_code), get_numerical_position(horizontal_code)
    size = len(horizontal_code) * len(vertical_code)
    while size < len(line):
        horizontal_code.append(chr(random.randrange(ord("A"), ord("Z") + 1)))
        size = len(horizontal_code) * len(vertical_code)
    if size > len(line):
        extra_letters = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
        line += extra_letters[:size - len(line)]
    check = 0
    arr, tmp = [], []
    for i in range(len(line)):
        tmp.append(line[i])
        check += 1
        if check == len(horizontal_code):
            arr.append(tmp)
            tmp = []
            check = 0

    print("  ", end='')
    for i in horizontal_code:
        print(i, end='')
    print('')
    for i in range(len(arr)):
        print(vertical_code[i], end=' ')
        for j in arr[i]:
            print(j, end='')
        print(' ')
    print('-' * 30)

    tmp = [i for i in range(len(arr))]
    for i in range(len(arr)):
        tmp[number_vert[i] - 1] = arr[i]
    arr = tmp
    vertical_code = sorted(vertical_code)
    print("  ", end='')
    for i in horizontal_code:
        print(i, end='')
    print('')
    for i in range(len(arr)):
        print(vertical_code[i], end=' ')
        for j in arr[i]:
            print(j, end='')
        print(' ')
    print('-' * 30)

    for i in range(len(horizontal_code)):
        for j in range(len(vertical_code)):
            tmp[j][horizontal_code[i] - 1] = arr[j][i]
    arr = tmp
    horizontal_code = sorted(horizontal_code)
    print("  ", end='')
    for i in horizontal_code:
        print(i, end='')
    print('')
    for i in range(len(arr)):
        print(vertical_code[i], end=' ')
        for j in arr[i]:
            print(j, end='')
        print(' ')
    print('-' * 30)

    phrase = ''
    for i in arr:
        for j in i:
            phrase += j
    print("Result: ", phrase)


def route_transposition(line, code_word):
    print("Phrase:", line)
    print("Code word:", code_word, '\n')

    line, code_word = removal_excess_symbols(line), removal_excess_symbols(code_word)
    size = math.ceil(math.sqrt(len(line)))
    extra_letters = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    missing_letters_line = size**2 - len(line)
    missing_letters_code = size - len(code_word)
    if missing_letters_code == 0:
        pass
    elif missing_letters_code < 0:
        code_word = code_word[:len(code_word) - abs(missing_letters_code)]
    else:
        code_word += extra_letters[: missing_letters_code]
    line += extra_letters[:missing_letters_line]
    check = 0
    arr, tmp = [], []
    for i in range(len(line)):
        tmp.append(line[i])
        check += 1
        if check == size:
            arr.append(tmp)
            tmp = []
            check = 0
    code_word = get_numerical_position(code_word)
    for i in range(1, size + 1):
        print(i, end='')
    print("")
    for i in arr:
        for j in i:
            print(j, end='')
        print("")
    print("")

    message = []
    for i in range(size):
        tmp = ''
        for j in range(size):
            tmp += arr[j][i]
        message.append(tmp)
    for i in message:
        print(i, end=" ")
    print('\n')
    print("*"*30)

    for i in code_word:
        print(i, end="")
    print("")
    for i in arr:
        for j in i:
            print(j, end='')
        print("")
    new_message = [i for i in range(size)]
    for i in range(len(code_word)):
        new_message[code_word[i] - 1] = message[i]
    print("")
    for i in new_message:
        print(i, end=' ')


def atbash(line):
    print("Phrase:", line, '\n')
    letters = [chr(a) for a in range(ord("A"), ord("Z") + 1)]
    rev_letters = copy.deepcopy(letters)
    rev_letters.reverse()
    for i in letters:
        print(i, end="")
    print("")
    for i in rev_letters:
        print(i, end="")
    print("")
    print("")
    line = line.upper()
    print(line)
    for i in line:
        pos = letters.index(i)
        print(rev_letters[pos], end="")


def magic_square(line, size, random_wide):
    print("Phrase:", line)
    print("Size of square:", size)
    print("Variance of values:", random_wide, '\n')

    square = make_magic_square(size, random_wide)
    print("")
    check = 0
    for i in range(len(line)):
        print(line[i], end="")
        check += 1
        if check == size:
            check = 0
            print('')
    print("")
    for i in range(len(square)):
        print(square[i], end="")
        check += 1
        if check == size:
            check = 0
            print('')
    print("")
    for i in square:
        print(line[i - 1], end="")
        check += 1
        if check == size:
            check = 0
            print('')


def make_magic_square(n, q):
    M = int(n * (n**2 + 1) / 2)
    N = n**2
    numbers = [a for a in range(1, N + 1)]
    numbers = permutations(numbers)
    list_magic_square = []
    for i in numbers:
        j = 0
        while j != N:
            if sum(i[j:j + n]) != M:
                break
            else:
                j += n
        if j == N:
            list_magic_square.append(i)
            q -= 1
            if q == 0:
                break
    return list_magic_square[random.randrange(0, len(list_magic_square))]


if __name__ == "__main__":
    atbash("SOMEWORLD")
    print('-' * 20)
    magic_square("NEWBIGSIN", 3, 20)
    print('-' * 20)
    route_transposition("Deals later days, tales ancient times", "Puskin")
    print('-' * 20)
    double_transposition("London is the capital of Great Britain and Ireland", "guitar", "pianino")
    print('-' * 20)
    simple_caesar("System password has changed", 3)
    print('-' * 20)
    affine_system_caesar("London is the capital of Great Britain", 4, 7)
    print('-' * 20)
    key_word_caesar("London is the capital of Great Britain", 'cats', 7)
    print('-' * 20)
    playfair("London is the capital of Great Britain and Ireland", "understanding")
    print('-' * 20)
    polybius("IDIOCY OFTEN LOOKS LIKE INTELLIGENCE")
    print('-' * 20)
    coordinate_polybius("SOME TEXT")
    print('-' * 20)
    skitala("IDIOCY OFTEN LOOKS LIKE INTELLIGENCE")
    print('-' * 20)
    double_square_Uitston("IDIOCY OFTEN LOOKS LIKE INTELLIGENCE")
    print('-' * 20)
    trisemus("IDIOCY OFTEN LOOKS LIKE INTELLIGENCE", "DISASTER")