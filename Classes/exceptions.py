try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except IndexError:
    print("error 1")

print("continuing")

try:
    x = 5
    y = x/0
    print("This won't print, either")
except ZeroDivisionError:
    print("error 2")

print("continuing again")


try:
    x = 5
    y = x/0
    print("This won't print, either")
except Exception:
    print("error 3")

print("continuing again")
