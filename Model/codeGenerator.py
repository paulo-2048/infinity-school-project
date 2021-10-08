from random import randint


def codeGenerator():
    code = randint(0, 9)
    for i in range(1, 8):
        codeHash = randint(0, 9)
        code = str(code) + str(codeHash)
    return code
