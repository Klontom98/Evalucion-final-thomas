
def get_ascii(word):
    res_ascii=[]
    for char in word:
        ascii= ord(char)
        res_ascii.append(ascii)
    return res_ascii


def get_binary(res_ascii):
     res_binario = [format(codigo_ascii, 'b') for codigo_ascii in res_ascii]
     return res_binario
 
def get_result(word):
    ascii_result = get_ascii(word)
    binary_result = get_binary(ascii_result)
    resultado_final = " "

    for i in range(len(word)):
        resultado_final +=  f"ASCII character value of'{word[i]}' is {ascii_result[i]} and the binary representation in a Byte is {binary_result[i]}.\n"
    return resultado_final