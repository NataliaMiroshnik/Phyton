text = list(input('Введите свой текст').split())
for ind, el in enumerate(text):
    if len(text[ind]) > 10:
        el = text[ind][:10]
        print(ind, el)
    else:
        print(ind, el)