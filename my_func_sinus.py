import math
def func(x):
    return math.sin(x) if 0.2 <= x <= 0.9 else 1

print(func(6))
print(func(0.9))