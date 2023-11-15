
def get_ascii(word):
    res_ascii=[]
    for char in word:
        ascii= ord(char)
        res_ascii.append(ascii)
    return res_ascii


def get_binary(res_ascii):
    res_binario = [bin(codigo_ascii) for codigo_ascii in res_ascii]
    return res_binario
