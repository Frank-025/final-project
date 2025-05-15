test_list = ['water', 'armadillo', 'pplllasllllasd', 'cheat']


def splice(text):
    text_len = len(text)
    if text_len % 2 > 0:
        return text[text_len - 2:text_len]
    return text[text_len // 2:text_len]


for i in test_list:
    print(splice(i))
