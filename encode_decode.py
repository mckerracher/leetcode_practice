def encode(strs):
    result = ""
    for word in strs:
        result += str(len(word)) + "#" + word


def decode(str):
    i, result = 0, []
    while i < len(str):
        j = i
        number_length = 0
        while str[j] != '#':
            number_length += 1
            j += 1
        str_len = int(str[i:j])
        word = str[j + 1:j + 1 + str_len]
        result.append(word)
        i += str_len + 1 + number_length
    return result
