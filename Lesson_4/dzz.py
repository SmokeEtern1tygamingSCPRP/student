result = []
def divider(a, b):
 if a < b:
    raise ValueError('Первое число должно быть больше')
 if b > 100:
    raise IndexError('Число должно быть больше')
 if b == 0:
     raise ZeroDivisionError('Нельзя делить на ноль')
 return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")

print(result)