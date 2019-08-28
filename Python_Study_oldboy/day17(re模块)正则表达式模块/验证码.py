import random


def Authtication_code(n, alphabet=True):
    result = ''
    for i in range(0, n):
        item = str(random.randint(0, 9))
        if alphabet:
            num = str(random.randint(0, 9))
            alphabet_upper = chr(random.randint(65, 90))
            alphabet_lowwer = chr(random.randint(97, 122))
            lis = [num, alphabet_upper, alphabet_lowwer]
            item = random.choice(lis)
        result += item
    return result


print(Authtication_code(6, False))
