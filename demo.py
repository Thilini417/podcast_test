def is_odd(number):
    return "Odd" if number % 2 == 1 else "Even"

a = [12,13,15,22,16,17]
b = []

b = [is_odd(value) for i,value in enumerate(a) if i % 2 == 0]

print(b)