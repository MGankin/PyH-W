from sys import exit
#Функция проверяет соответсвуют ли числа заявленной СИ
def is_base(base,number):
    number_symbols=[]
    base_symbols = []
    for n in range(base):
        base_symbols.append(str(n))
    for n in range(len(str(number))):
        a=str(number)
        number_symbols.append(a[n])
    base_symbols=map(int,base_symbols)
    number_symbols = map(int,number_symbols)
    result = set(number_symbols) - set(base_symbols)
    if len(result) == 0:
        return(True)
    else:
        return(False)
#Эта функция приводит число к десятичной СИ
def to_ten(number,base):
    decimals = None
    result = 0
    result_decimals = 0
    if float(number) - int(number) is not 0:
        decimals = number - int(number)
        number = int(number)
    decimals_divided=[]
    number_divided=[]
    for n in range(len(str(number))):
        a = str(number)
        number_divided.append(a[n])
    number_divided= [int(a) for a in number_divided]
    degree = len(number_divided)-1
    for i in reversed(number_divided):
            result += i*(base**degree)
            degree += -1
    # if decimals > 0:
    #     decimals=str(decimals)
    #     for n in range(len(str(decimals))):
    #         decimals_divided.append(decimals[n])
    #     print(decimals_divided)
    #     for n in range (-1,-1*len(decimals_divided)):
    #         for i in decimals_divided:
    #             result_decimals += i*(2**n)
    #     result += result_decimals
    return(result)
#Эта функция приводит число ко второй СИ
def to_last_base(number,base):
    number = int(number)
    residue = []
    while number > base:
        r = number % base
        residue.append(r)
        number = number // base
    r = number % base
    residue.append(r)
    reresidue = list(reversed((residue)))
    residue = ''
    for n in reresidue:
        residue += str(n)
    decimals = float(number) - int(number)
    decimals_symbols = []
    if decimals != 0:
        number = number - decimals
        while decimals != 0:
            decimals = decimals * base
            decimals_symbols.append(int(decimals))
            decimals = decimals - int(decimals)

        map(str(),decimals)
        decimals = ''.join(decimals_symbols)
        decimals = int(decimals) / (10*len(decimals))
        result = residue + decimals
        return(result)
    else:
        result = residue
        return(result)
print('Введите основание первой СИ')
base_1=int(input())
if base_1 <= 0:
        print('Основание должно быть больше нуля!')
        raise SystemExit
print('Введите первое число')
First = int(input())
print('Введите второе число')
Second = int(input())
if is_base(base_1,First) is False:
    print('Первое число не соответствует заявленной системе исчисления!')
    raise SystemExit
if is_base(base_1,Second) is False:
    print('Второе число не соответствует заявленной системе исчисления!')
    raise SystemExit
print('Введите основание второй СИ')
base_2=int(input())
if base_1 and base_2 == 10:
    print(First+Second)
elif base_2 == 10:
    print(sum)
else:
    sum = to_ten(First,base_1) + to_ten(Second,base_1)
    final = to_last_base(sum,base_2)
    print(final)
