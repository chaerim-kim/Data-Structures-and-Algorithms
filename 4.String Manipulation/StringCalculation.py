# convert string of written numbers to acc no and perform calculations
# oneminustwozeroplusthreetwo = 1-20+ 32= 13 return onethree

def stringtoNo(strParam):
    dict = {'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0',
            'plus': '+',
            'minus': '-'}

    for i,j in dict.items():
        strParam = strParam.replace(i,j)

    # perform calculation
    result = eval(strParam)

    # convert back to string
    if result <= 0:
        result = str(result).replace('-', 'negative')

    for i,j in dict.items():
        result = str(result).replace(j, i)
    return result

print(stringtoNo('oneminustwozeroplusthreetwo'))    #onethree = 13