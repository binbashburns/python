def zero_pad_number(number, length):
    numberLength = len(str(number))
    lengthMinusNumber = (length - numberLength)
    print(lengthMinusNumber * "0" + str(number))

zero_pad_number(1000, 5)