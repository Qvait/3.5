def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        if first > 0:
            if int(str_number[1]) > 0:
                number = first * get_multiplied_digits(int(str_number[1:]))
            else:
                if len(str_number) > 3:
                    number = first * get_multiplied_digits(int(str_number[2:]))
                else:
                    return number
        else:
            if len(str_number) > 2:
                number = first * get_multiplied_digits(int(str_number[2:]))
            else:
                return number
    else:
        return number
    return number

result = get_multiplied_digits(24004)
print(result)



