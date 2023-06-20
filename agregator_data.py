def join_numbers_from_range(start,finish):
    i = start
    string_number = ''
    while i <= finish:
        string_number += str(i)
        i += 1
    return string_number
