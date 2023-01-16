
text = "Мороз и соабвлнце; день чудесный! \
        Еще абв дремлешь, друг прелестный -\
        Пора, красавица, проснись:\
        Открой сомкнуты негой взорыабв\
        Навстречу северной Авроры,\
        Звездою севера явись!"

new_text = list(filter(lambda x: 'абв' not in x, text.split()))
print(' '.join(new_text))

# from string import punctuation
# my_str = 'АБВ ылоажы фыыдлх абв? Зщышф вабвв ффлжв абВ'
# res = []

# x = 'абв'
# for c in punctuation:
#     my_str = my_str.replace(c, ' ' + c + ' ')
# data = my_str.split()
# print(data)

# for item in data:
#     if not x.lower() in item.lower():
#         res.append(item)
# res = ' '.join(res)
# for c in punctuation:
#     res = res.replace(' ' + c, c)
# print(res)
