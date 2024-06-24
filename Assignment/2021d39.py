# 概要:
# 1. 文字列の中のアルファベット以外をスペースに置き換える
# 2. 文字列の末尾に" "を追加する
# 3. keyに" "を追加する
# 4. 検索を行う

skip = [0 for i in range(256)]

def table(key):
    key = key + " "
    keyLength = len(key)

    for k in range(256):
        skip[k] = keyLength

    for k in range(keyLength - 1):
        skip[ord(key[k])] = keyLength - 1 - k
    
    return key


def search(s, text, key):
    keyLength = len(key)

    # If not alphabetic (number, symbol, whitespace, etc.),
    # replace with a space:
    for i in range(len(text)):
        if not text[i].isalpha():
            text = text[:i] + " " + text[i + 1 :]

    text = text + " "  # Append a space to the end of the text

    currentIndex = s + keyLength - 1

    while currentIndex < len(text):
        if text[currentIndex] == key[keyLength - 1]:
            if text[currentIndex - keyLength + 1 : currentIndex + 1] == key:
                return currentIndex - keyLength + 1

        currentIndex += skip[ord(text[currentIndex])]

    return -1


text = "This is a pen. That is a pencil."
key = "pen"
key = table(key)

found_index = search(0, text, key)
while found_index != -1:
    print("{:s}".format(text[found_index:]))
    found_index = search(found_index + len(key), text, key)
