import re


def input_from_keyboard():
    """get input data from keyboard"""
    name = input('your name:')
    gender = input('you are a boy?(y/n)')
    welcome_str = 'Welcome to the matrix {prefix} {name}.'
    welcome_dic = {
        'prefix': 'Mr.' if gender == 'y' else 'Mrs',
        'name': name
    }
    # Welcome to the matrix Mr. sam.
    print('authorizing...')
    print(welcome_str.format(**welcome_dic))


def NLP_parse_data(text):
    """使用正则表达式去除标点符号和换行符"""
    text = re.sub(r'[^\w ]', ' ', text)
    lower_text = text.lower()
    # 用' '切分text，并过滤掉其中ele为null的元素，并生成单词的词频
    word_list = lower_text.split(' ')
    word_list = filter(None, word_list)

    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_cnt


if __name__ == '__main__':
    name = 'jason'
    upcase = name.replace('j', 'J')
    # name[0]: j, name[1:3]: as, ucase: Jason
    print(f"name[0]: {name[0]}, name[1:3]: {name[1:3]}, ucase: {upcase}")
    # input_from_keyboard()

    with open('/tmp/in.txt', 'r') as fin:
        text = fin.read()
    word_and_frequency = NLP_parse_data(text)
    # get all words in /tmp/out.txt file
    #     and 15
    # be 13
    # will 11
    # to 11
    # the 10
    # of 10
    # a 8
    # we 8
    # day 6
    # able 6
    with open('/tmp/out.txt', 'w') as fout:
        for word, freq in word_and_frequency:
            fout.write('{} {}\n'.format(word, freq))
