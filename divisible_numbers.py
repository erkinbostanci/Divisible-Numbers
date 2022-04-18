def div_number(number):
    divs_number = []
    for i in range(2,number):
        if number % i == 0:
            divs_number.append(i)
    return divs_number

while True:
    number = input("Enter number: ")
    if number == 'q':
        break
    number = int(number)
    print(number,"is divisible number: ",div_number(number))          