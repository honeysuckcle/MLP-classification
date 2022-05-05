import requests


def translate(query):
    url = 'http://fanyi.youdao.com/translate'
    data = {
        "i": query,  # 待翻译的字符串
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16081210430989",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    res = requests.post(url, data=data).json()
    return res['translateResult'][0][0]['tgt']  # 返回翻译后的结果


# 判断一句话中是否含有中文
def is_chinese(sentence):
    for ch in sentence:
        if '\u4e00' <= ch <= '\u9fff' or ch in '，。 ':
            return True
        else:
            return False


def translate_file(input, output):
    # 将description中的中文翻译后提取到新的文件里
    file_path = input
    output_file = open(output, 'w', encoding='utf-8')

    with open(file_path, 'rb') as f:
        result = f.readlines()
        count = 0
        for i in range(len(result)):
            line = result[i].decode('utf-8')
            if is_chinese(line):
                count += 1
                print(i, line)
                words = line.split('。')
                chinese = ''
                for w in words:
                    if len(w) > 0:
                        chinese += translate(w) + '.'
                output_file.write(chinese + '\n')
            else:
                line = line.replace('\r\n', '')
                output_file.write(line + '\n')
        print(count)

    output_file.close()


if __name__ == "__main__":
    # 将description中的中文翻译后提取到新的文件里
    # translate_file('../data/train_description.csv', '../data/train_description_en.csv')
    translate_file('../data/test_description.csv', '../data/test_description_en.csv')
