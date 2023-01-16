# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def code_char(text):
    count =0
    last_char = text[0]
    result_zip = ''
    for char in text:
        if char != last_char and char != '':
            result_zip += str(count)+last_char
            count = 1
            last_char = char
        else:
            count+=1
    result_zip += str(count)+last_char    
    return result_zip

def decode_char(text: str):
    result = ''
    number = ''
    for i in range(len(text)):
        if text[i].isnumeric():
            number += text[i]
        else:
            if number != '':
                result+=int(number)*text[i]
                number = ''
    return result 



file_input = open('input.txt','r')
code_data = file_input.readline().rstrip()
code_result = code_char(code_data)
print(f'{code_data} -> {code_result}')
decode_data = file_input.readline()
decode_result = decode_char(decode_data)
print(f'{decode_data} -> {decode_result}')
with open('output.txt','w') as output:
    output.write(code_result+'\n')
    output.write(decode_result)

