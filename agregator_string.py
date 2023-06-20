def my_substr(string, length):
    i = 0
    string_finish = ''
    while i <= length - 1:
        string_finish += string[i]
        i += 1
    return string_finish