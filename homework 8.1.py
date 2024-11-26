def add_everything_up(a, b):

    try:
            sum1 = a + b
            return sum1
    except TypeError as exc:
            sum2 = str(a) + str(b)
            return sum2

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))