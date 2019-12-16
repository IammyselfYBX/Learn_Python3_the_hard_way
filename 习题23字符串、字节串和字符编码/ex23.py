import sys
script, encoding, errors = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, endcoding, errors):
    next_lang = line.strip()    #去掉每行结尾的 \n 
    raw_bytes = next_lang.encode(encoding, errors = errors)         # 对文字进行编码
    cooked_string = raw_bytes.decode(encoding, errors = errors)     # 对已经编码的字节串解码

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, errors)